import base64
import sys
import os


shellcode = b''

def enterShellCodeFile(filename):
    global shellcode

    if os.path.isfile(filename):
        f = open(filename,'rb')
        binary_code = f.read()
        f.close()
        shellcode = base64.b64encode(binary_code);

    else:
        print("File not found Error")


def main():
    print("Welcome to Malware Generator")

    file_name = input("Enter the path of your file: ")
    enterShellCodeFile(file_name)

    print(shellcode)


if __name__=="__main__":
    main()
