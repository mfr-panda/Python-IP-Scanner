#!/usr/bin/python

infos ='''
  
######################################################

		  --- OPTIONS et USAGE ---

  python scan-ip.py [options] 
  options : -h, -i, -t, -o, -n

  Exemples :
          python scan-ip.py --help

          python scan-ip.py -i 192.168.1-1-254

------------------------------------------------------
                Panda - FabLac                     
######################################################
'''
# ==================================================== 
# usage des options
usage = "usage: %prog [options] "

# ====================================================

# Importation des Modules
import os
import multiprocessing
import time
import optparse
import platform


# Ping
class PingScan:
 def __init__(self, target, thread, output, timeout):
  self.start_time=time.time()
  self.collect_ip=multiprocessing.Queue()
  self.target=target
  self.thread=thread
  self.output=output
  self.timeout=timeout
  self.set_os_command()
  #self.checkping()
  self.multi_scan()

  # Sauvegarde Output
 def save_output(self):
  f=open(self.output,'a')
  for i in self.collect_ip:
   f.write(i+'\n')
  f.close()
  return

 # Multi_processing
 def multi_scan(self):
  proces=[]
  for ip in self.target:
   k=len(multiprocessing.active_children())
   if k==self.thread:
    time.sleep(3)
    self.thread=self.thread+30
   mythread=multiprocessing.Process(target=self.checkping, args=(ip,))
   mythread.start()
   proces.append(mythread)

  for mythread in proces:
   mythread.join()
  self.endtime=time.time()
  self.affichage_resultats()
  return

 # Affichage
 def affichage_resultats(self):
  sauvegarde_ip=[]
  x=1
  while x==1:
   try:
    sauvegarde_ip.append(self.collect_ip.get_nowait())
   except:
    x=x+1
  self.collect_ip=sauvegarde_ip

  print "\n"*3,"#"*80
  print "[+] Demarrage Scan \t\t:\t",time.ctime(self.start_time)
  print "[+] Fin du Scan  \t\t:\t",time.ctime(self.endtime)
  print "[+] Duree Totale du scan \t:\t",self.endtime-self.start_time
  print "[+] Nombre Adresses IP Actives\t:\t",len(self.collect_ip)
  if self.output:
   self.save_output()
  return

 # Selection de commande selon OS
 def set_os_command(self):
  oper = platform.system()
  if (oper=="Windows"):
   ping = "ping -n {} {}"
  elif (oper== "Linux"):
   ping= "ping -c {} {}"
  else :
   ping= "ping -c {} {}"
  self.commad=ping
  return

 # Status IP
 def checkping(self, ip):
  ping=self.commad
  recv=os.popen(ping.format(self.timeout, ip)).read()
  recv=recv.upper()
  if recv.count('TTL'):
   print "[+]\t {} \t==> IP Active ".format(ip)
   self.collect_ip.put(ip)
  return


# Extraction plage IP
def extraction(plage):
 storeplage=[]
 if plage:
  # Verification plage IP
  if "-" in plage and "," not in plage:
   x1,x2=plage.split('-')
   storeplage=range(int(x1),int(x2))
  elif "," in plage and "-" not in plage:
   storeplage=plage.split(',')
  elif "," in plage and "-" in plage:
   x2=[]
   for i in plage.split(','):
    if '-' in i:
     y1,y2=i.split('-')
     x2=x2+range(int(y1),int(y2))
    else:
     x2.append(i)
   storeplage=x2
  else:
   storeplage.append(plage)
 else:
  pass
 return storeplage

# Extraction adresse IP
def IP_extractor(ip):
 storeobj=[]
 ip=ip.split('.')
 x1=extraction(ip[0])
 x2=extraction(ip[1])
 x3=extraction(ip[2])
 x4=extraction(ip[3])
 for i1 in x1:
  for i2 in x2:
   for i3 in x3:
    for i4 in x4:
     storeobj.append("{}.{}.{}.{}".format(i1,i2,i3,i4))
 return storeobj

def main():
 CYELLOW = '\033[33m'
 CEND = '\033[0m'
 print(CYELLOW + infos + CEND)
 parser=optparse.OptionParser(usage=usage)
 parser.add_option('-i','--ip',type='string',dest='ip',help="Specifie une adresse ou la plage IP", default=None)
 parser.add_option('-t',"--thread",type='string', dest="thread", help="Specifie le nombre de threads pour le scan ", default='100')
 parser.add_option('-o',"--output",type='string', dest="output", help="Specifie le nom et le chemin pour le fichier de sortie .txt", default="logs_scan_ip.txt")
 parser.add_option('-n','--timeout',type='string', dest="timeout", help="Specifie le nombre de tentatives par IP",default='1')
 (options, args)= parser.parse_args()
 if not options.ip:
  print "[+] Indiquez une plage IP, ex: scan-ip.py -i 192:168:1:1-254 "
  exit(0)
 target=options.ip
 thread=options.thread
 output=options.output
 timeout=options.timeout
 target=IP_extractor(target)
 PingScan(target,thread,output,timeout)
 return


if __name__ == '__main__':
 main()
