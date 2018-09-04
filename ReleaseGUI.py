#!/usr/bin/env python
import os, sys
import zipfile
import datetime

GTmodules = ["Config.ini", "GUImain.py", 
            "./source/ControlDiag.py",
            "./source/ControlEmail.py",
            "./source/ControlEngine.py",
            "./source/ControlLED.py",
            "./source/ControlTCP.py",
            "./source/DisplayConfigPanel.py",
            "./source/DisplayDashboard.py",
            "./source/DisplayHaapPanel.py",
            "./source/DisplayMenubar.py",
            "./source/ParseEngineVPD.py",
            "./source/ParseINIfile.py",
            "./source/ZipUtility.py",
            "./data/default.dat"
            ]
Vendors =   ["opzoon",
            "SilverShine",
            "UDsafe"
            ]
#
# Modify Company and Product name


#
# Modify Options (main and ini files)


#
# Modify Others

zippath = './zipfile/'
if not os.path.exists(zippath): os.makedirs(zippath)

zip_file_name = zippath + datetime.datetime.now().strftime('HaapGUI%Y%m%d%H%M%S'+'.zip')
zip = zipfile.ZipFile(zip_file_name, 'w')

for f in GTmodules:
    print f
    zip.write(f)
    
zip.close()
