import subprocess

# script locations (the only thing that should need editing
# for readability group by folders when execute order does not matter
script_locations = [  
  "init.sh", # init.sh SHOULD ALWAYS be the first script to run
  
  "install/yay-installer.sh",
]

#####################################################
# anything below this below should not need editing #
#####################################################





def execute_scripts(script_paths):
    for script in script_paths:
        try:
            result = subprocess.run(["bash", script], check=True, text=True, capture_output=True) #run
            print(f"Output of {script}:\n{result.stdout}") #print output

                        ### start of error handling ###
        except subprocess.CalledProcessError as e:
            print(f"Script failed: Error occurred while running {script}:\n{e.stderr}")
          
        except FileNotFoundError:
            print(f"Not found: Script file {script} not found.")
          
        except Exception as e:
            print(f"Unexpected Error: An unexpected error occurred: {e}")
                        ### end of error handling ###

execute_scripts(script_locations)

print("end of subprocess.py")
