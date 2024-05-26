import platform
import subprocess

def is_linux():
    return platform.system() == 'Linux'

def is_arch():
    return True #FIX ME
  
def is_plasma(): 
    
    bool_running = True #FIX ME

    bool_plasma6_installed = "plasmashell 6" in (subprocess.run("plasmashell --version", shell=True))
    bool_installed = bool_plasma5_installed
    
    return bool_installed and bool_running

def is_compatible():
  return (is_linux() and is_arch() and is_plasma())

print(is_compatible())
