# Your Happy Place Demo v0.1.0

The first public downloadable demo release of **Your Happy Place** by **Kadabra Games**.

## Available platforms

- Windows 64-bit (IL2CPP, Vulkan)
- Linux x86-64 (IL2CPP, Vulkan)
- macOS Universal (Mono, Metal)

## Installation and launch

**Extract the complete archive before launching the game.** Do not run the game from inside an archive or move its executable away from the accompanying Unity data and runtime files.

### Windows

1. Download `YourHappyPlace-Windows.zip`.
2. Select **Extract All**.
3. Open the extracted `YourHappyPlace_Windows_Vulkan_IL2CPP` folder.
4. Run `YourHappyPlace.exe`.

### Linux

1. Download `YourHappyPlace-Linux.zip`.
2. Extract the complete ZIP.
3. Open the extracted `YourHappyPlace_Linux_Vulkan_IL2CPP` directory.
4. If necessary, run `chmod +x YourHappyPlace.x86_64`.
5. Run `./YourHappyPlace.x86_64`.

### macOS

1. Download `YourHappyPlace-macOS.zip`.
2. Extract the complete ZIP.
3. Open the extracted `YourHappyPlace_macOS_Metal_Mono` folder.
4. Open `YourHappyPlace.app`.

The macOS build uses Mono because macOS IL2CPP compilation requires a macOS host with Xcode. It uses Metal exclusively.

## Security notices

These demo builds are unsigned. Windows SmartScreen or macOS Gatekeeper may display a warning when the game is opened for the first time. Confirm that the archive came from this official repository before allowing it to run.

## File integrity

`SHA256SUMS.txt` is included with this release so every downloaded archive can be verified using SHA-256.
