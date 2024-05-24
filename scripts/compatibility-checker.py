import platform

def is_linux():
    return platform.system() == 'Linux'

def is_arch():
    return True #FIX ME
  
def is_plasma():
    bool_installed = True
    bool_running = True
    return bool_installed and bool_running #FIX ME

def is_compatible():
  return (is_linux() and is_arch() and is_plasma()

print(is_compatible())
