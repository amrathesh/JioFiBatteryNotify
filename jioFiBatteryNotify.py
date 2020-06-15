
import requests 
from bs4 import BeautifulSoup 
import urllib.request
import time
from win10toast import ToastNotifier

    
def notify(notifyval):
     toastobj = ToastNotifier()
     toastobj.show_toast("JioFi Battery Monitor","Battery has reached "+str(notifyval)+" %")  

def connect(host):
        try:
            urllib.request.urlopen(host) 
            return True
        except:
            return False

def exitcall():
      print("\n")
      print("Exiting JioFi Battery Notifier".center(100, '-'))
      time.sleep(2)
      exit(0)

if __name__ == "__main__":
     print("JioFi Battery Notifier".center(100, '-'))
     while True:
          try:
               URL = "http://jiofi.local.html/"
               if(connect(URL)):
                    print("[INFO] Connected with JioFi ...")
                    notifyAt = int(input("[*] When you want to get notified : "))
                    print("[OK] You will be notified once battery drains to ",notifyAt," %\n",sep='')
                    break
               else:
                    print("[INFO]Please connect to JioFi and Try Again")
                    input("[*]Press Enter After connecting to continue ")
                    time.sleep(1)
          except ValueError:
               print("[ERR]Please enter when u want to get notified!")
               continue
          except KeyboardInterrupt:
               exitcall()

     while True:
          try: 
               
               r = requests.get(URL) 
               soup = BeautifulSoup(r.content, 'html5lib') 
               batterySample = str(soup.find_all(id="batterylevel"))
               batteryVal = int(batterySample[47:49])
               if(batteryVal <= notifyAt):
                    for i in range(3):
                         notify(batteryVal)
                         time.sleep(1)
                    print("[INFO] Notified")
                    notifyAt = int(input("[*] When you want to get notified : "))
                    print("[OK] You will be notified once battery drains to ",notifyAt," %\n",sep='')
                    
               else:
                         print("Battery Percentage : ",batteryVal," %",sep ='',end="\r")
                         time.sleep(10)
                         print(" "*28,end="\r")
                         time.sleep(1)
                    
          except:
               exitcall()
               


