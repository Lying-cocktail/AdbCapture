import sys
import os
import time 
from reportlab.platypus import SimpleDocTemplate, Image
from reportlab.lib.styles import getSampleStyleSheet
import numpy
import subprocess

def screencap2(outf):
    out=subprocess.Popen('adb shell screencap -p',stdout=subprocess.PIPE)  
    out=out.stdout.read().replace(b'\r\n', b'\n')  
    with open(outf,"wb") as f:
        f.write(out)    

PAGCOUNT=300 

os.mkdir("work")

for i in range(0,PAGCOUNT):
    #cmd = "adb shell screencap -p > work/%04d.png"  %(i)
    #os.system(cmd)
    screencap2("work/%04d.png" % (i))
    cmd = "adb shell input tap 1050 1084"
    os.system(cmd)
sys.exit(0)
