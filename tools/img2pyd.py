#!/usr/bin/env python3

import argparse
import struct
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import sys



s_prior_header = """
________=0x00
_______X=0x01
______X_=0x02
______XX=0x03
_____X__=0x04
_____X_X=0x05
_____XX_=0x06
_____XXX=0x07
____X___=0x08
____X__X=0x09
____X_X_=0x0A
____X_XX=0x0B
____XX__=0x0C
____XX_X=0x0D
____XXX_=0x0E
____XXXX=0x0F
___X____=0x10
___X___X=0x11
___X__X_=0x12
___X__XX=0x13
___X_X__=0x14
___X_X_X=0x15
___X_XX_=0x16
___X_XXX=0x17
___XX___=0x18
___XX__X=0x19
___XX_X_=0x1A
___XX_XX=0x1B
___XXX__=0x1C
___XXX_X=0x1D
___XXXX_=0x1E
___XXXXX=0x1F
__X_____=0x20
__X____X=0x21
__X___X_=0x22
__X___XX=0x23
__X__X__=0x24
__X__X_X=0x25
__X__XX_=0x26
__X__XXX=0x27
__X_X___=0x28
__X_X__X=0x29
__X_X_X_=0x2A
__X_X_XX=0x2B
__X_XX__=0x2C
__X_XX_X=0x2D
__X_XXX_=0x2E
__X_XXXX=0x2F
__XX____=0x30
__XX___X=0x31
__XX__X_=0x32
__XX__XX=0x33
__XX_X__=0x34
__XX_X_X=0x35
__XX_XX_=0x36
__XX_XXX=0x37
__XXX___=0x38
__XXX__X=0x39
__XXX_X_=0x3A
__XXX_XX=0x3B
__XXXX__=0x3C
__XXXX_X=0x3D
__XXXXX_=0x3E
__XXXXXX=0x3F
_X______=0x40
_X_____X=0x41
_X____X_=0x42
_X____XX=0x43
_X___X__=0x44
_X___X_X=0x45
_X___XX_=0x46
_X___XXX=0x47
_X__X___=0x48
_X__X__X=0x49
_X__X_X_=0x4A
_X__X_XX=0x4B
_X__XX__=0x4C
_X__XX_X=0x4D
_X__XXX_=0x4E
_X__XXXX=0x4F
_X_X____=0x50
_X_X___X=0x51
_X_X__X_=0x52
_X_X__XX=0x53
_X_X_X__=0x54
_X_X_X_X=0x55
_X_X_XX_=0x56
_X_X_XXX=0x57
_X_XX___=0x58
_X_XX__X=0x59
_X_XX_X_=0x5A
_X_XX_XX=0x5B
_X_XXX__=0x5C
_X_XXX_X=0x5D
_X_XXXX_=0x5E
_X_XXXXX=0x5F
_XX_____=0x60
_XX____X=0x61
_XX___X_=0x62
_XX___XX=0x63
_XX__X__=0x64
_XX__X_X=0x65
_XX__XX_=0x66
_XX__XXX=0x67
_XX_X___=0x68
_XX_X__X=0x69
_XX_X_X_=0x6A
_XX_X_XX=0x6B
_XX_XX__=0x6C
_XX_XX_X=0x6D
_XX_XXX_=0x6E
_XX_XXXX=0x6F
_XXX____=0x70
_XXX___X=0x71
_XXX__X_=0x72
_XXX__XX=0x73
_XXX_X__=0x74
_XXX_X_X=0x75
_XXX_XX_=0x76
_XXX_XXX=0x77
_XXXX___=0x78
_XXXX__X=0x79
_XXXX_X_=0x7A
_XXXX_XX=0x7B
_XXXXX__=0x7C
_XXXXX_X=0x7D
_XXXXXX_=0x7E
_XXXXXXX=0x7F
X_______=0x80
X______X=0x81
X_____X_=0x82
X_____XX=0x83
X____X__=0x84
X____X_X=0x85
X____XX_=0x86
X____XXX=0x87
X___X___=0x88
X___X__X=0x89
X___X_X_=0x8A
X___X_XX=0x8B
X___XX__=0x8C
X___XX_X=0x8D
X___XXX_=0x8E
X___XXXX=0x8F
X__X____=0x90
X__X___X=0x91
X__X__X_=0x92
X__X__XX=0x93
X__X_X__=0x94
X__X_X_X=0x95
X__X_XX_=0x96
X__X_XXX=0x97
X__XX___=0x98
X__XX__X=0x99
X__XX_X_=0x9A
X__XX_XX=0x9B
X__XXX__=0x9C
X__XXX_X=0x9D
X__XXXX_=0x9E
X__XXXXX=0x9F
X_X_____=0xA0
X_X____X=0xA1
X_X___X_=0xA2
X_X___XX=0xA3
X_X__X__=0xA4
X_X__X_X=0xA5
X_X__XX_=0xA6
X_X__XXX=0xA7
X_X_X___=0xA8
X_X_X__X=0xA9
X_X_X_X_=0xAA
X_X_X_XX=0xAB
X_X_XX__=0xAC
X_X_XX_X=0xAD
X_X_XXX_=0xAE
X_X_XXXX=0xAF
X_XX____=0xB0
X_XX___X=0xB1
X_XX__X_=0xB2
X_XX__XX=0xB3
X_XX_X__=0xB4
X_XX_X_X=0xB5
X_XX_XX_=0xB6
X_XX_XXX=0xB7
X_XXX___=0xB8
X_XXX__X=0xB9
X_XXX_X_=0xBA
X_XXX_XX=0xBB
X_XXXX__=0xBC
X_XXXX_X=0xBD
X_XXXXX_=0xBE
X_XXXXXX=0xBF
XX______=0xC0
XX_____X=0xC1
XX____X_=0xC2
XX____XX=0xC3
XX___X__=0xC4
XX___X_X=0xC5
XX___XX_=0xC6
XX___XXX=0xC7
XX__X___=0xC8
XX__X__X=0xC9
XX__X_X_=0xCA
XX__X_XX=0xCB
XX__XX__=0xCC
XX__XX_X=0xCD
XX__XXX_=0xCE
XX__XXXX=0xCF
XX_X____=0xD0
XX_X___X=0xD1
XX_X__X_=0xD2
XX_X__XX=0xD3
XX_X_X__=0xD4
XX_X_X_X=0xD5
XX_X_XX_=0xD6
XX_X_XXX=0xD7
XX_XX___=0xD8
XX_XX__X=0xD9
XX_XX_X_=0xDA
XX_XX_XX=0xDB
XX_XXX__=0xDC
XX_XXX_X=0xDD
XX_XXXX_=0xDE
XX_XXXXX=0xDF
XXX_____=0xE0
XXX____X=0xE1
XXX___X_=0xE2
XXX___XX=0xE3
XXX__X__=0xE4
XXX__X_X=0xE5
XXX__XX_=0xE6
XXX__XXX=0xE7
XXX_X___=0xE8
XXX_X__X=0xE9
XXX_X_X_=0xEA
XXX_X_XX=0xEB
XXX_XX__=0xEC
XXX_XX_X=0xED
XXX_XXX_=0xEE
XXX_XXXX=0xEF
XXXX____=0xF0
XXXX___X=0xF1
XXXX__X_=0xF2
XXXX__XX=0xF3
XXXX_X__=0xF4
XXXX_X_X=0xF5
XXXX_XX_=0xF6
XXXX_XXX=0xF7
XXXXX___=0xF8
XXXXX__X=0xF9
XXXXX_X_=0xFA
XXXXX_XX=0xFB
XXXXXX__=0xFC
XXXXXX_X=0xFD
XXXXXXX_=0xFE
XXXXXXXX=0xFF

fontdata = [
    #  #05 OFF
    0x05, 0x18, 0x10, 0x00,
    ________, ________,
    ____XXXX, XXXX____,
    __XX____, ____XX__,
    _X___XX_, ______X_,
    _X__X__X, ______X_,
    X__X____, X______X,
    X__X____, X______X,
    _X__X__X, ______X_,
    _X___XX_, ______X_,
    __XX____, ____XX__,
    ____XXXX, XXXX____,
    ________, ________,    
    #  #06 ON
    0x06, 0x18, 0x10, 0x00,
    ________, ________,
    ____XXXX, XXXX____,
    __XX____, ____XX__,
    _X______, _XX___X_,
    _X______, XXXX__X_,
    X______X, XXXXX__X,
    X______X, XXXXX__X,
    _X______, XXXX__X_,
    _X______, _XX___X_,
    __XX____, ____XX__,
    ____XXXX, XXXX____,
    ________, ________,   
    #  #07 Full
    0x07, 0x18, 0x08, 0x00,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    XXXXXXXX, ________,
    #  #08 Fill
    0x08, 0x18, 0x08, 0x00,
    _XXXXXXX, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _X_____X, ________,
    _XXXXXXX, ________,
    #  #09 Tab
    0x09, 0x18, 0x0C, 0x00,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    #  #32 Tab
    0x20, 0x18, 0x04, 0x00,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,
    ________, ________,

"""

def writestring(file, ss):
    "Write string data to file"
    file.write(bytes(ss, encoding="ASCII",errors = "ignore"))

def Txt_Fromimg(font_name, priname, out_size:int, ckvale:int):
    print(f"Process:{font_name}")
    if (priname == "__") :
        priname = ""
    py_file = "fcdata.py"
    txt_file = "txts" + "/" + priname + str(f"{Path(font_name).stem}.txt")
    out_file = "src" + "/" + priname + str(f"{Path(font_name).stem}.h")
    bmp_file = "imgs" + "/" + priname + str(f"{Path(font_name).stem}.bmp")
    if (Path(bmp_file).exists()):
        img = Image.open(bmp_file)
        pixels = img.load()
        ckv = 0xff * 3 * ckvale // 100
        h_s = out_size // 2
        s_w = out_size * 4
        s_h = out_size * 4

        with open(py_file, "wb") as f:
            writestring(f, s_prior_header)
            for y in range(16):
                for x in range(16):
                    ssx = 16
                    smax = 0
                    chrno = y*16+x
                    if ((chrno > 32) and (chrno < 127)) or ((chrno > 160) and (chrno < 256)):
                        for dy in range (out_size):
                            for dx in range(16):
                                pt = pixels[x * s_w + out_size * 2 + h_s - 1 + dx, y * s_h + out_size * 2 + h_s + dy]
                                if ((pt[0] + pt[1] + pt[2]) >= ckv):
                                    ssx = dx if (ssx > dx) else ssx
                                    smax = dx if (smax < dx) else smax
                        chrwd = smax - ssx + 1
                        #width
                        chrwd = max(chrwd, 0)
                        if (chrwd > 0):
                            chrwd = chrwd + 1
                        if (chrwd == 0):
                            ssx = 0
                        #write head
                        writestring(f,"    # ")
                        if chrno >= 0x20:
                            f.write(struct.pack("B",chrno))
                        writestring(f," #" + "%d"%chrno + " width " + "%d"%chrwd+"\n")
                        writestring(f,"    # Option: fixed,fixed(outheight*2),width,xoffset \n")
                        writestring(f,"    0x%02x"%chrno + ", 0x%02x"%(out_size*2)+ ", 0x%02x"%chrwd + ", 0x%02x,\n"%(ssx))

                        #x * s_w + out_size * 2 + h_s - 1
                        #y * s_h + out_size * 2 + h_s

                        for dy in range (out_size):
                            writestring(f,"    ")
                            for dx in range(16):
                                if (dx == 8):
                                    writestring(f,", ")
                                pt = pixels[x * s_w + out_size * 2 + h_s - 1 + dx, y * s_h + out_size * 2 + h_s + dy]
                                writestring(f,"X" if ((pt[0] + pt[1] + pt[2]) >= ckv) else "_")
                            writestring(f,",\n")
            writestring(f, "    ]")
        import os
        py_file = "fcdata.py"
        os.system("copy /Y fcdata.py \"" + txt_file + "\"")
        os.system("python3 fontcreate.py \"" + out_file + "\"")
        #print(d)
        #run it


def process_onefile(filename, fontdef):
    fontdef.setdefault(filename, {})
    fdef = fontdef[filename]
    fdef.setdefault("fontsize", "12")  #
    fdef.setdefault("fixedsize", "12") #
    fdef.setdefault("resize", "12")
    fdef.setdefault("xoffset", "0")
    fdef.setdefault("yoffset", "0")
    fdef.setdefault("check", "75")
    fdef.setdefault("_a_", "_")
    Txt_Fromimg(filename, fdef["_a_"] + "_", int(fdef["fixedsize"]), int(fdef["check"]))  #ogn font image


def main():
    import json
    jsonfile = "fonts/fonts.json"
    if Path(jsonfile).exists():
        with open(jsonfile,'r') as load_f:
            try:
                fontdef = json.load(load_f)
                #print("Rom define file loaded")
                load_f.close()
            except: 
                print("Fonts define file load failed")
                fontdef = {}
                load_f.close()
    else :
        fontdef = {};

    if (len(sys.argv) > 1):
        process_onefile(sys.argv[1], fontdef)
    else:
        for key in fontdef:
            process_onefile(key, fontdef)
        
if __name__ == "__main__":
    main()