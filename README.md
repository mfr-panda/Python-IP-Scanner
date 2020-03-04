# Python-IP-Scanner
Scan Network Ip adresses with python

--------  scan-ip.py  ---------

--- OPTIONS et UTILISATION ---


  python scan-ip.py [options] 

  -i IP, --ip=IP
                        Specifie la l'adresse IP ou la plage IP
  -t THREAD, --thread=THREAD
                        Specifie le nombre de threads pour le scan (defaut;100)
  -o OUTPUT, --output=OUTPUT
                        Specifie le chemin pour le fichier de sortie .txt (defaut:log_scan_ip.txt)
  -n TIMEOUT, --timeout=TIMEOUT
                        Specifie le nombre de requetes par IP (defaut:1)

  EXEMPLES :

  -afficher Aide : python scan-ip.py --help

  -scan plage IP: python scan-ip.py -i 192:168:1:1-254

------------------------------------------------------         
######################################################
