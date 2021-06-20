import os, getpass
import sys, getopt

ssid = ''
pswd = ''
    
def mkFiles(s,p):
        
    os.system('touch wpa_supplicant.conf ssh')
    
    wpa = '''
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid='''+"\""+s+"\""+'''
scan_ssid=1
psk='''+"\""+p+"\""+'''
key_mgmt=WPA-PSK
}'''

    f = open('w.txt', 'w')
    f.write(wpa)
    f.close()

    command = 'cat <<EOF  w.txt > wpa_supplicant.conf'  
    os.system(command)

def getParams():

    global ssid
    global pswd

    #ssid = input("\n SSID : ")               #  Wifi Network Name
    #pswd = getpass.getpass("\n PSWD : ")     #  Wifi Network Password
    
  
  
def main(argv):
       
   try:
      opts, args = getopt.getopt(argv,"n:p:",["nname=","npass="])
      
   except getopt.GetoptError:
      print('wpa_helper.py -n <Network Name> -p <Network Password>')
      sys.exit(2)
      
   for opt, arg in opts:
       
      if opt == '-h':
         print('wpa_helper.py -n <Network Name> -p <Network Password>')
         sys.exit()
         
      elif opt in ("-n", "--Network Name"):
          global ssid
          ssid = arg
         
      elif opt in ("-p", "--Network Password"):
        global pswd
        pswd = arg
         
if __name__ == "__main__":
    
    main(sys.argv[1:])
    getParams()
    mkFiles(ssid, pswd)
    
#os.system('cp wpa_supplicant.conf ssh /Volumes/boot')

