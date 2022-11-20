with open("test.txt","w") as f:
    f.write("test string")

"""
with open("test.txt","r") as f:
    print(f.read())
    """
with open("test.txt","r") as f:
    for line in f:
        print(line)