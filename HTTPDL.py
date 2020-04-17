#!/usr/bin/python

import urllib
print("Begin download")

urllib.urlretrieve("https://github.com/vim/vim-win32-installer/releases/download/v8.2.0534/gvim_8.2.0534_x86.exe", "viminstaller.exe")

print("Completed")