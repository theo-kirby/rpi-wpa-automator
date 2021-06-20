import os, getpass
import sys, getopt

cc = ''
ssid = ''
pswd = ''
usage = '\n Usage : wpa_helper.py -n <Network Name> -p <Network Password> -c <Country Code>\n'
    
def mkFiles(s,p,c):
        
    os.system('touch wpa_supplicant.conf ssh')
    
    wpa = '''
country='''+c+'''
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
    global cc

    #ssid = input("\n SSID : ")               #  Wifi Network Name
    #pswd = getpass.getpass("\n PSWD : ")     #  Wifi Network Password
    
  
  
def main(argv):
    
   try:
      opts, args = getopt.getopt(argv,"n:p:c:",["nname=","npass=", "ccode="])
      
   except getopt.GetoptError:
      print(usage)
      sys.exit(2)
      
   options = len(opts)
   
   for opt, arg in opts:
       
      if opt == '-h':
         print(usage)
         sys.exit()
         
      elif opt in ("-n", "--Network Name"):
          global ssid
          ssid = arg
         
      elif opt in ("-p", "--Network Password"):
          global pswd
          pswd = arg
          
      elif opt in ("-c", "--Country Code"):
          global cc
          cc = arg
          
   if options == 0:
      print(usage)

  
if __name__ == "__main__":
    
    main(sys.argv[1:])
    getParams()
    mkFiles(ssid, pswd, cc)
    
    #os.system('cp wpa_supplicant.conf ssh /Volumes/boot')

