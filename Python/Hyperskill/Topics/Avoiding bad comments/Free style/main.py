import os

file_name = input("Please write the name of the file to work with:\n")

if os.path.exists(file_name):
    with open(file_name) as file:
        content = file.read()  # Store content read by file to variable 

    new_content = process(content) 

    with open(f'{file_name}_processed.txt', 'w') as new_file:  # Creates a new file for the processed content
        new_file.write(new_content)

    print("All done!")

else:
    print("The file you entered does not exist!")
