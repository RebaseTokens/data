import subprocess


def loopApp():
   
    loop = 1
    while loop == 1:
        print ("Two Checker")
        try:
            process = subprocess.call(['python3', '/home/admin/Desktop/data/daotwo.py'])
        except Exception as errore:
            print (errore)
            continue         
            
loopApp()
