# Python-IP-Scanner
*Scan and Log Network IP adresses with python*

--------  scan-ip.py  ---------

--- OPTIONS et UTILISATION ---

# Usage:
    python scan-ip.py [options] 
                        
                       
|IP     |-i |--ip     | Specifie la l'adresse IP ou la plage IP                                    |
|THREAD |-t |--thread | Specifie le nombre de threads pour le scan (defaut:100)                    |
|OUTPUT |-o |--output | Specifie le chemin pour le fichier de sortie .txt (defaut:log_scan_ip.txt) |
|TIMEOUT|-n |--timeout|Specifie le nombre de requetes par IP (defaut:1)                            |


  EXEMPLES :

 # -afficher Aide :
    python scan-ip.py --help

 # -scan plage IP: 
    python scan-ip.py -i 192:168:1:1-254

------------------------------------------------------         
######################################################
