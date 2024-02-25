file_name = "test.txt"

with open(file_name, 'a+') as file:
    file.write("Hello, World!\n")
    file.write("This is a simple example of file adding.\n")
    print(file.read())

print("Will read the file")
# File is automatically closed when the 'with' block exits

with open(file_name, 'r') as file:
    contents = file.read()
    print("File Contents:\n", contents)