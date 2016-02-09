#!/usr/bin/python

import ftplib
import argparse

parser = argparse.ArgumentParser(description="Check FTP sites for ANON login.")
parser.add_argument('-f', '--file', type=file)
args = parser.parse_args()


def ftplogin(hostname):
    for word in args.file.read().split():    
        try: 
            ftp = ftplib.FTP(word,timeout=3)
            ftp.login('anonymous', 'none@sun.com')
            print '\n[*] ' + str(word) + ' FTP Anonymous Logon Succeeded.'
            ftp.quit()
            ftp.close()
        except Exception, ftplib.all_errors:
            print '\n[-] ' + str(word) + ' FTP Anonymous Logon Failed.'         

ftplogin(args.file)

