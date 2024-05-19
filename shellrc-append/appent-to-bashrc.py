import os

# Function to read and append the content of a file to ~/.bashrc
def append_to_bashrc(file_path, bashrc_path):
    with open(file_path, 'r') as file:
        content = file.read()
    with open(bashrc_path, 'a') as bashrc:
        bashrc.write(content + '\n')

# Main function
def main():
    home_dir = os.path.expanduser("~")
    bashrc_path = os.path.join(home_dir, '.bashrc')
    append_dir = os.getcwd()  # Assuming the .append files are in the current working directory

    # Append prefix.append
    prefix_path = os.path.join(append_dir, 'prefix.append')
    if os.path.exists(prefix_path):
        append_to_bashrc(prefix_path, bashrc_path)

    # Append all other .append files except postfix.append
    for file_name in os.listdir(append_dir):
        if file_name.endswith('.append') and file_name not in ['prefix.append', 'postfix.append']:
            file_path = os.path.join(append_dir, file_name)
            append_to_bashrc(file_path, bashrc_path)

    # Append postfix.append
    postfix_path = os.path.join(append_dir, 'postfix.append')
    if os.path.exists(postfix_path):
        append_to_bashrc(postfix_path, bashrc_path)

if __name__ == "__main__":
    main()
