# Minecraft-3ds-Image-Flip
- Flips skins from Java Edition to be used on Minecraft 3DS. Extremely simple CLI that "just works".

# Features:
- Flips normal *.png Images From Java to MC-3DS.
- Can Flip Compiled *.3dst Files. ***Both X & Y Only Axis ATM***.
- Change Color of Compiled *.3dst Files. ***See [CLI/CLU Usage](https://github.com/Cracko298/Minecraft-3ds-Image-Flip/#cliclu-usage) for additional information***.

# Usage:
### CLI/CLU Usage:
```
### Utility Commands:
> .\m3dsflip help

### 3DST Commands:
> .\m3dsflip 3dstflip <image_path>
> .\m3dsflip -c -invert <image_path>
> .\m3dsflip -c -green <image_path>

### PNG Commands:
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

### Image/Video Gallery:
<p>
    <img width="256" height="256" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/3ae3fe61-8fac-4302-8096-9f5dd22d1fc5" alt="Inverted Notch Skin">
    <img width="320" height="320" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/ba035930-8454-4fe8-867f-35a6b0782d9d" alt="Normal Notch Skin">
    <img width="256" height="256" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/d3f24862-d815-4181-88fd-23064dd219d7" alt="Green Hue Notch Skin">
</p>

<embed>https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/500cb648-111f-4c9f-a80b-c91ab71216a8</embed>
