#!/usr/bin/env python3
"""Create a complete, executable Linux tarball without changing game bytes."""
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import tarfile
import zipfile
from datetime import datetime, timezone

EXPECTED_SOURCE = '872f66222f580dd8763f13f6fa049658c94710a80aa00f7a39134b3d018a3741'
ROOT = 'YourHappyPlace_Linux_Vulkan_IL2CPP'
PLAYER = ROOT + '/YourHappyPlace.x86_64'
REPAIR_TIME = int(datetime(2026, 9, 30, tzinfo=timezone.utc).timestamp())

def digest(stream):
    value = hashlib.sha256()
    while block := stream.read(4 * 1024 * 1024):
        value.update(block)
    return value.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    with args.source.open('rb') as stream:
        if digest(stream) != EXPECTED_SOURCE:
            raise SystemExit('Source archive differs from the verified v0.1.0 release.')
    manifest = {}
    with zipfile.ZipFile(args.source) as source:
        if source.read(PLAYER)[:4] != b'\x7fELF':
            raise SystemExit('Expected Linux ELF player is missing.')
        with tarfile.open(args.output, 'w:gz', compresslevel=6) as target:
            for item in source.infolist():
                path = PurePosixPath(item.filename)
                if path.is_absolute() or '..' in path.parts or path.parts[0] != ROOT:
                    raise SystemExit('Unsafe or unexpected archive path: ' + item.filename)
                if ((item.external_attr >> 16) & 0o170000) == 0o120000:
                    raise SystemExit('Unexpected symlink: ' + item.filename)
                entry = tarfile.TarInfo(item.filename.rstrip('/'))
                entry.mtime = REPAIR_TIME
                entry.mode = 0o755 if item.is_dir() or item.filename == PLAYER else 0o644
                if item.is_dir():
                    entry.type = tarfile.DIRTYPE
                    target.addfile(entry)
                else:
                    entry.size = item.file_size
                    with source.open(item) as stream:
                        manifest[item.filename] = digest(stream)
                    with source.open(item) as stream:
                        target.addfile(entry, stream)
            extras = {
                'Play Your Happy Place.sh': '#!/bin/sh\nset -eu\ncd -- "$(dirname -- "$0")"\nexec ./YourHappyPlace.x86_64 "$@"\n',
                'START HERE.txt': 'YOUR HAPPY PLACE — LINUX DEMO v0.1.0\n\nExtract this entire .tar.gz archive to your Home folder.\nOpen the extracted folder and double-click YourHappyPlace.x86_64.\nIf your file manager asks, choose Run. No chmod step is needed.\n\nYou may also run "Play Your Happy Place.sh" from a terminal.\nKeep the executable, Data folder and runtime libraries together.\nThis packaging repair preserves every original game file byte for byte.\n',
            }
            for name, text in extras.items():
                data = text.encode('utf-8')
                entry = tarfile.TarInfo(ROOT + '/' + name)
                entry.mtime = REPAIR_TIME
                entry.mode = 0o755 if name.endswith('.sh') else 0o644
                entry.size = len(data)
                target.addfile(entry, io.BytesIO(data))
                manifest[entry.name] = hashlib.sha256(data).hexdigest()
    verified = {}
    with tarfile.open(args.output, 'r:gz') as archive:
        for item in archive.getmembers():
            if item.isfile():
                verified[item.name] = digest(archive.extractfile(item))
        assert archive.getmember(PLAYER).mode == 0o755
        assert archive.getmember(ROOT + '/Play Your Happy Place.sh').mode == 0o755
    assert verified == manifest, 'Round-trip content hash mismatch'
    with args.output.open('rb') as stream:
        output_hash = digest(stream)
    report = {'gameVersion': '0.1.0', 'sourceSha256': EXPECTED_SOURCE,
              'archive': args.output.name, 'sha256': output_hash,
              'bytes': args.output.stat().st_size, 'allOriginalFileBytesPreserved': True,
              'executableMode': '0755', 'membersSha256': verified}
    args.output.with_suffix(args.output.suffix + '.verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: value for key, value in report.items() if key != 'membersSha256'}, indent=2))

if __name__ == '__main__':
    main()
