import ftplib
import socket

def anonlogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print("[+] FTP Anonymous login successful \n")
        ftp.quit()
    except:
        print("[-] FTP Anonymous login failed \n")

if __name__ == '__main__':
    hostname = input(">>Enter the host name : ")
    hostname = socket.gethostbyname(hostname)
    anonlogin(hostname)