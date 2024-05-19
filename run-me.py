import runpy

scripts_to_run = [  'scripts/my-script.py',
          
                    'shellrc-append/append-to-bashrc.py',
                    'scripts/utility/source-bashrc.py',
]

def run(path):
  runpy.run_path(path)

for script in scripts_to_run:
  run(script)
