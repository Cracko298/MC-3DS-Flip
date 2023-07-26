# Minecraft-3ds-Image-Flip
- Flips skins (and more) from Java Edition to be used on Minecraft 3DS. Extremely simple CLI that "just works".

# Features:
- Flips normal *.png Images From Java to MC-3DS.
- Can Flip Compiled *.3dst Files. ***Both X & Y Only Axis ATM***.
- Change Color of Compiled *.3DST Files. ***See [CLI/CLU Usage](https://github.com/Cracko298/Minecraft-3ds-Image-Flip/#cliclu-usage) for additional information***.
- Grab MetaData of File using the **-g** flag.

# Usage:
### CLI/CLU Usage:
```
#  Utility Commands:
> .\m3dsflip help

#  3DST Commands:
> .\m3dsflip 3dstflip <image_path>
> .\m3dsflip -c -invert <image_path>
> .\m3dsflip -c -green <image_path>
> .\m3dsflip -c -orange <image_path>
> .\m3dsflip -c -red <image_path>
> .\m3dsflip -c -blue <image_path>
> .\m3dsflip -g -meta <image_path>

#  PNG Commands:
> .\m3dsflip yflip <image_path>
> .\m3dsflip xflip <image_path>
> .\m3dsflip -g -head <image_path>
> .\m3dsflip -g -body <image_path>
> .\m3dsflip -g -larm <image_path>
> .\m3dsflip -g -rarm <image_path>
> .\m3dsflip -g -lleg <image_path>
> .\m3dsflip -g -rleg <image_path>
```
### Command Explanation:
```
> .\m3dsflip <flag> <command/args> <image_path>
```
```
> .\m3dsflip     =  Call Executable
> <flag>         =  -c (Color Flag), -g (Grab Flag).
> <command>      =  Commands Such as "yflip" or "3dstflip" (or Args Such as "-invert" or "-orange").
> <image_path>   =  Image Path (If path has "speaces" within it, surround it in quotes. An Example: "C:\Windows\Users\batch user384\skin.png").
```
## Building:
```
> pyinstaller -F --strip --exclude-module numpy --exclude-module opencv --exclude-module cv2 --onefile "m3dsflip.py" --icon="favicon.ico"
```
## Source Usage:
```
python m3dsflip.py <flag> <command> <image_path>
```
## Notice:
- If you decide to change the color/hue of your *.3DST Skin.
- **I am not responsible for any data that might become corrupted, or if the output is not the desired result.**
- Blurry Images on this GitHub page do NOT reflect the quality (enlarged so you can see them).
- These Skin Hue Changes do **NOT** work on all skins. Make sure your *.3DST Skin is a compatible size: ***16.0kb***.


# Download:
- **Compiled Download Avaliable [Here](https://github.com/Cracko298/Minecraft-3ds-Image-Flip/releases/download/v0.4.0/m3dsflip.exe).**

## Road-Map (Updates/Patches):
```
1. finish the "-g" flag (Whicy will support grabbing multiple body parts of both Images). *(High Priority | 55% Way There).

2. A "-r" flag will be added flag to replace body parts with of Compiled .3DST Skins. *(Second Priority)

3. Proper Flipping of Compiled .3DST Skins. *(High Priority)

4. Converting Between .PNG and Compiled .3DST Skins. *(Last Priority)
```

# Image Gallery:
<p>
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/3ae3fe61-8fac-4302-8096-9f5dd22d1fc5" alt="Inverted Notch Skin">
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/ba035930-8454-4fe8-867f-35a6b0782d9d" alt="Normal Notch Skin">
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/d3f24862-d815-4181-88fd-23064dd219d7" alt="Green Hue Notch Skin">
</p>

<p>
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/7cbf415d-d17a-4788-9ec5-5c0b3ee40da8" alt="Red Hue Notch Skin">
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/c68fd63c-dd4f-4e46-869b-8b5b263b9a99" alt="Orange Hue Notch Skin">
    <img width="273" height="273" src="https://github.com/Cracko298/Minecraft-3ds-Image-Flip/assets/78656905/c6e15678-b661-45a2-9646-65c6694e0a59" alt="Blue Hue Notch Skin"> 
</p>
