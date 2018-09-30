# i3-wm Quake Any Window

**WIP!**

## Features
* Quake mode for any window
* Toggle mode
* Sticky top
* While toggled follow you in any workspace
* Hides on '-1' workspace
* Set quake height

## Example usage
* Quickly toggle a special VsCode/md-editor instance to drop some lines in your cheatSheet repository.

## Intstall
* Clone and drop anywhere (why not in the i3 config file?)
* `sudo chmod a+x ./i3QAW.py`
* Set a keybind in your i3 config file and specify the window class (you can use [xprop](https://www.archlinux.org/packages/extra/x86_64/xorg-xprop/) shell command to help you) you wish to quake
    * `bindsym $alt+w exec "/home/username/.config/i3/i3QAW.py WindowClass"`

## Usage
* Pick the window of the same classe name as the one you specified in your keybind (i3 confi) and float it
  * (float shortcut in (i3 config) example: `bindsym $mod+Shift+space floating toggle`)
* repeat at will.

## Roadmap
* Alpha setting
* Full multi-screen multi-rez support (currently some issues on multi-rez)
* Auto startup an instance of binded quake windows at startup, float them and hide them

* Suggestions or inputs are welcome. Enjoy!
