import platform

def is_linux():
    return platform.system() == 'Linux'

def is_arch():
    return True #FIX ME
  
def is_plasma(): 
    bool_installed = True #FIX ME
    bool_running = True #FIX ME
    return bool_installed and bool_running

def is_compatible():
  return (is_linux() and is_arch() and is_plasma())

print(is_compatible())
