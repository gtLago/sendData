import os, time
import paramiko
import bz2
import csv
import datetime

def envioCentral(fileName):
    try:      
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port=port, username=username, password=password)
        sftp = ssh.open_sftp()
        remotepath = '/home/lago/lago2018/UVGSUR/'+ fileName +''
        localpath = '/home/lagouvg/data/'+ fileName +''
        sftp.put(localpath, remotepath)
        sftp.close()
        ssh.close()
    except Exception, e:
        print str(e)

path_to_watch = "/home/lagouvg/data/"
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (1)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: 
    print ("Added: ", ", ".join (added))
    envioCentral(added[0])
  if removed: print("Removed: ", ", ".join (removed))
  before = after