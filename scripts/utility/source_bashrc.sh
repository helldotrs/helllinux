import subprocess

def run_source_bashrc():
    # Run the command
    subprocess.run(['bash', '-c', 'source ~/.bashrc'])

# Example usage
if __name__ == "__main__":
    run_source_bashrc()
