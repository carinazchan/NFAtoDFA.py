# Main.py

import sys
import ReadWrite


def main():
    ReadWriteInstance = ReadWrite.ReadWrite()
    ReadWriteInstance.CheckCommandLine()
    print(ReadWriteInstance.inputFilePath)
    ReadWriteInstance.GetLine()
    print("hello")

if __name__ == "__main__":
    main()
