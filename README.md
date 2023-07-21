# Minecraft-3ds-Image-Flip
- Flips skins from Java Edition to be used on Minecraft 3DS. Extremely simple CLI that "just works".

# Features:
- Flips normal *.png Images From Java to MC-3DS.
- Can Flip Compiled *.3dst Files. ***Only on both X & Y Axis ATM***.

# Usage:
### CLI/CLU Usage:
```
> .\m3dsflip help

> .\m3dsflip 3dstflip <image_path>
> .\m3dsflip -c -invert <image_path>
> .\m3dsflip -c -green <image_path>

> .\m3dsflip yflip <image_path>
> .\m3dsflip xflip <image_path>
```
### Help Message:
```
> .\m3dsflip <mode> <command> <image_path>
```
```
> .\m3dsflip     =  Call Executable
> <mode>         =  -c (Color Mode)
> <image_path>   =  Path to Image ('xflip' and 'yflip' only support *.png).
> <command>      =  Commands Such as "yflip" or "3dstflip"
```
## Building:
```
> pyinstaller -F --onefile "m3dsflip.py" --icon="favicon.ico"
```
## Source Usage:
```
python m3dsflip.py <mode> <command> <image_path>
```

# Download:
- **Compiled Download Avaliable [Here](https://github.com/Cracko298/Minecraft-3ds-Image-Flip/releases/download/v0.3.0/m3dsflip.exe).**

### Video Demonstration:
<embed>https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/500cb648-111f-4c9f-a80b-c91ab71216a8</embed>
