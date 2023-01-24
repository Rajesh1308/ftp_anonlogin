#importing requirements

import ftplib
import socket

#anonlogin checks for anonymous login in the host provided

def anonlogin(hostname):
    try:
        #connecting with FTP

        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print("[+] FTP Anonymous login successful \n")
        ftp.quit()
    except:
        print("[-] FTP Anonymous login failed \n")

if __name__ == '__main__':
    hostname = input(">>Enter the host name : ")
    #Converting hostname to its IP address

    hostname = socket.gethostbyname(hostname)
    anonlogin(hostname)