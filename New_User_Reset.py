# Script to reset user info
import time
import subprocess

start = time.time()

def reset_User_status ():
    # Accesses the file with user status in it
    with open ("NewUserCheck.bat", 'w') as f:
        f.write ('0')

    print ("Done")

reset_User_status()

end = time.time()
print ("\n" + str (end-start) )