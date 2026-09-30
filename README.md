# Your Happy Place

Official downloadable demo builds for **Your Happy Place**, developed by **Kadabra Games**.

Download the latest demo from the repository's [Releases](https://github.com/redgargoyle/YourHappyPlace-Releases/releases/latest) page.

## Available platforms

- Windows 64-bit (IL2CPP, Vulkan)
- Linux x86-64 (IL2CPP, Vulkan)
- macOS Universal (Mono, Metal)

## Installation

Download the archive for your operating system and **extract the complete archive before launching**. The game will not work correctly if its executable is separated from the accompanying Unity data and runtime files.

- **Windows:** Extract the ZIP, open the extracted folder, and run `YourHappyPlace.exe`.
- **Linux:** Download [YourHappyPlace-Linux.tar.gz](https://github.com/redgargoyle/YourHappyPlace-Releases/releases/download/v0.1.0/YourHappyPlace-Linux.tar.gz), extract it to your Home folder, open the extracted folder, and double-click `YourHappyPlace.x86_64`. The executable and included launcher already have permission to run.
- **macOS:** Extract the ZIP, then open `YourHappyPlace.app`.

These demo builds are currently unsigned. Windows SmartScreen or macOS Gatekeeper may display a warning. Verify that the archive came from this official repository before choosing to open it.

The macOS build uses Mono because Unity requires a macOS host with Xcode to produce macOS IL2CPP builds. Metal is the only configured graphics API for macOS.

SHA-256 checksums are supplied in `SHA256SUMS.txt`. The repaired Linux tarball has its own `YourHappyPlace-Linux.tar.gz.sha256` checksum. The old Linux ZIP is retained, but the tarball is recommended.

Official website: [kadabra.games](https://kadabra.games)
