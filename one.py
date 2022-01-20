import subprocess


def loopApp():
   
    loop = 1
    while loop == 1:
        print ("Main Checker")
        try:
            process = subprocess.call(['python3', '/home/admin/Desktop/data/daomain.py'])
        except Exception as errore:
            print (errore)
            continue         
            
loopApp()
