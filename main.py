import os, time
import shutil
import stat
import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    # Code of your program here
    # Provide the new path here
    ro_mask = 0o777 ^ (stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)

    if os.path.isfile('C:/$WINDOWS.~BT/Sources/appraiserres.dll'): 
        shutil.copy2('Sources/appraiserres.dll', 'C:/$WINDOWS.~BT/Sources/appraiserres.dll') # target filename is /dst/dir/file.ext
        os.chdir('C:/$WINDOWS.~BT/Sources')
        os.chmod('appraiserres.dll', ro_mask)
        print ("File exist")
        time.sleep(3) #30s
    else:
        # os.mkdir('C:/$WINDOWS.~BT')
        # os.mkdir('C:/$WINDOWS.~BT/Sources/')
        # os.chdir('C:/$WINDOWS.~BT/Sources') 
        print ("File not exist")
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    time.sleep(3) #30s
    print ("Admin! Rerun")
        # Provide the new path here
    ro_mask = 0o777 ^ (stat.S_IWRITE | stat.S_IWGRP | stat.S_IWOTH)

    if os.path.isfile('C:/$WINDOWS.~BT/Sources/appraiserres.dll'): 
        shutil.copy2('Sources/appraiserres.dll', 'C:/$WINDOWS.~BT/Sources/appraiserres.dll') # target filename is /dst/dir/file.ext
        os.chdir('C:/$WINDOWS.~BT/Sources')
        os.chmod('appraiserres.dll', ro_mask)
        print ("File exist")
        time.sleep(3) #30s
    else:
        print ("File not exist")


