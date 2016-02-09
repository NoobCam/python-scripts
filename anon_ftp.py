#!/usr/bin/python

import ftplib
import argparse

def main(hostname):
    parser = argparse.ArgumentParser(description="Check FTP sites for ANON login.")
    parser.add_argument('-f', '--file', type=file)
    args = parser.parse_args()

	for word in args.file.read().split():
            ftp = ftplib.FTP(word)
            ftp.login('anonymous', 'none@sun.com')
            print '\n[*] ' + str(word) + ' FTP Anonymous Logon Succeeded.'
            ftp.quit()
            return True
        
        except Exception, e:
            print '\n[-] ' + str(word) + ' FTP Anymous Logon Failed.'
            return False
main(host)


