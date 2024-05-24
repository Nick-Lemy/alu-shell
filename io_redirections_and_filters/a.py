import os
import stat

def create_bash_script():
    # Ask the user for the file name
    file_name = input("Enter the file name: ")
    
    # Ask the user for the second line content
    second_line = input("Enter the content for the second line: ")
    
    # Create and write to the file
    with open(file_name, 'w') as file:
        file.write("#!/bin/bash\n")
        file.write(second_line + "\n")
    
    # Add execute permissions to the file
    os.chmod(file_name, os.stat(file_name).st_mode | stat.S_IXUSR)
    
    print(f"File '{file_name}' has been created and made executable in the current working directory.")

# Run the function
create_bash_script()
