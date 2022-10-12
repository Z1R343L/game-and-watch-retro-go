#!/usr/bin/env python3
import os
import sys
import hashlib
import xml.dom.minidom

def getGameControls(collection,sha1):
    controls = 65535
    for software in collection.getElementsByTagName("software"):
        system = software.getElementsByTagName('system')[0]
        for dump in software.getElementsByTagName('dump'):
            for rom in dump.getElementsByTagName('rom'):
                hash = rom.getElementsByTagName('hash')[0].childNodes[0].data
                if (hash == sha1string):
                    if (rom.getElementsByTagName('controls')):
                        controls = rom.getElementsByTagName('controls')[0].childNodes[0].data
                    if (software.getElementsByTagName('controls')):
                        controls = software.getElementsByTagName('controls')[0].childNodes[0].data
                    return controls
            for megarom in dump.getElementsByTagName('megarom'):
                hash = megarom.getElementsByTagName('hash')[0].childNodes[0].data
                if sha1string == hash:
                    if (megarom.getElementsByTagName('controls')):
                        controls = megarom.getElementsByTagName('controls')[0].childNodes[0].data
                        return controls
                    if (software.getElementsByTagName('controls')):
                        controls = software.getElementsByTagName('controls')[0].childNodes[0].data
                        return controls
            for disk in dump.getElementsByTagName('disk'):
                hash = disk.getElementsByTagName('hash')[0].childNodes[0].data
                if sha1string == hash:
                    if (disk.getElementsByTagName('controls')):
                        controls = disk.getElementsByTagName('controls')[0].childNodes[0].data
                        return controls
                    if (software.getElementsByTagName('controls')):
                        controls = software.getElementsByTagName('controls')[0].childNodes[0].data
                        return controls
    return controls

BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

n = len(sys.argv)

if n < 2:
    print("Usage :\nrfindBlueMsxControls.py database.xml file.rom \n")
    sys.exit(0)

# Open file
#print("Opening "+sys.argv[2])
sha1 = hashlib.sha1()

with open(sys.argv[2], 'rb') as f:
    while True:
        if data := f.read(BUF_SIZE):
            sha1.update(data)

        else:
            break
sha1string = sha1.hexdigest()

DOMTree = xml.dom.minidom.parse(sys.argv[1])
collection = DOMTree.documentElement

print(getGameControls(collection,sha1string))
sys.exit(0)
