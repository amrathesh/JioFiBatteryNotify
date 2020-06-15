import subprocess
import time


#installs required modules using pip
print("Installing dependencies for JioFi Battery Notifier....")
dep = ['requests','bs4','win10toast']

try:
    for i in dep:
       subprocess.call(['pip', 'install',i])

    print("All dependencies were succefully installed.... ")
    time.sleep(2)
    print("Exiting....")
except :
    print("Can't install modules check whether pip is installed")
    time.sleep(1)
    exit(0)

exit(0)
