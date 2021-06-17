import os, getpass

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

    ssid = input("\n SSID : ")               #  Wifi Network Name
    pswd = getpass.getpass("\n PSWD : ")     #  Wifi Network Password
    
   

getParams()

mkFiles(ssid, pswd)

#os.system('cp wpa_supplicant.conf ssh /Volumes/boot or /path/to/sd card boot')

