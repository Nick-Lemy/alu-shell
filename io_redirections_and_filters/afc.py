#!/bin/bash
import os

def create_bash_script():
	file_name = input("Enter the file name: ")
	second_line = input("Enter the content for the second line: ")
	with open(file_name, 'w') as file:
		file.write("#!/bin/bash\n")
		file.write(second_line + "\n")
	print(f"File '{file_name}' has been created in the current working directory.")

# Run the function
create_bash_script()
