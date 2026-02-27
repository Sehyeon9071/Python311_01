with open("hello.txt", "r") as file:
    line = None
    while line != "":
        line = file.readline()
        print(line.strip("\n"))
