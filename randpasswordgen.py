import random

def readFile(fileName):
    file = open(fileName, "r")
    cmd = file.read()
    file.close()
    return cmd

def writeFile(fileName, string):
    file = open(fileName, "w")
    file.write(string)
    file.close()

def randomPassword(length=10) -> str:
    validchars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIGJLMNOPQRSTUVWXYZ!-_"
    password = ""
    if length <= 0:
        length = 10
    for i in range(length):
        password += validchars[random.randint(0,len(validchars)-1)]
    return password

if __name__ == "__main__":
    print("Service Started!")
    writeFile("generatecommand.txt","") # Creating file for reading / deleting previous session data.
    print("generatecommand.txt Initialized!")
    print("Ready for input!")
    while True:
        password = ""
        command = readFile("generatecommand.txt")
        if command != "":
            try:
                password = randomPassword(int(command))
            except:
                if command != "":
                    password = randomPassword()
        if password != "":
            writeFile("generatecommand.txt","") # Clearing the command
            writeFile("passwordgenerated.txt",password) # Writing password to output.
            print("Password Generated!")