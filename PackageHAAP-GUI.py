#!/usr/bin/python
import os, sys
import zipfile
import datetime

GTmodules = ["Config.ini", "GUImain.py", 
            "./source/ControlDiag.py",
            "./source/ControlEmail.py",
            "./source/ControlEngine.py",
            "./source/ControlLED.py",
            "./source/ControlTCP.py",
            "./source/ControlAPI.py",
            "./source/ControlJSON.py",
            "./source/ControlSwitch.py",
            "./source/ControlName.py",
            "./source/DisplayConfigPanel.py",
            "./source/DisplayDiagPanel.py",
            "./source/DisplayDashboard.py",
            "./source/DisplayHaapPanel.py",
            "./source/DisplayMenubar.py",
            "./source/ParseEngineVPD.py",
            "./source/ParseINIfile.py",
            "./source/ZipUtility.py",
            "./data/API.dat",
            "./data/default.dat"
            ]

zippath = './z_package/'
if not os.path.exists(zippath): os.makedirs(zippath)

zip_file_name = zippath + datetime.datetime.now().strftime('HaapGUI%Y%m%d%H%M%S'+'.zip')
zip = zipfile.ZipFile(zip_file_name, 'w')

for f in GTmodules:
    print f
    zip.write(f)
    
#
CODES =[]
codepath = './mcode/'

for dirpath, dirs, files in os.walk(codepath):
    for filename in files:
        if filename[-3:] != "bin": continue
        CODES.append(codepath+filename)

#for f in CODES:
#    print f
#    zip.write(f)
    
zip.close()
