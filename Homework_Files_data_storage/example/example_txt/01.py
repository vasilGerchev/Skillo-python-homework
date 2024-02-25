with open('test.txt', 'r') as f:
    f_content = f.read()
    print(f_content)

with open('test.txt', 'a+') as f:
    f.write("This is a example for file adding")


