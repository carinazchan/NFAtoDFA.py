import sys

"""
Reads from an input file and writes to an output file.
"""


class ReadWrite:
    """
    Constructor for the ReadWrite class.
    """

    def __init__(self, inputFilePath, outputFilePath):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath

    """
    Checks the command line arguments to see if the correct amount of arguments are passed.
    """

    def CheckCommandLine(self):
        # sys.argv: A list of command-line arguments passed to a Python script. Script name is the first element (sys.argv[0])
        if len(sys.argv) != 2:  # If the length of the command line arguments is != 2
            print("Need two arguments: YourScript.py InputFile.txt")
        sys.exit(1)  # Exit the program

    # def SetInputFilePath(self):
    #     self.inputFilePath = sys.argv[1] #Second argument is the file path

    # def GetLine(self):
    #     with open(self.inputFilePath, 'r') as file: #Open the file in read mode ('r')
    #         #Iterate through each line in the file
    #         lines = file.read().split('\n')
    #         # Read Q: lines[0]
    #         Q = lines[0].replace('{', '').replace('}', '').split('\t')
    #         print("this is Q")
    #         print(Q)
    #         # Read Sigma: lines[1]
    #         sigma = lines[1].split('\t')
    #         print(sigma)
    #         # Read q0: lines[2]
    #         q0 = lines[2].replace('{', '').replace('}', '').split('\t')
    #         print(q0)
    #         # Read F: lines[3]
    #         F = lines[3].replace('{', '').replace('}', '').split('\t')
    #         print(F)
    #         # Read transitions: lines[4:]
    #         delta = []
    #         for line in lines[4:]:
    #             if (line == "BEGIN" or line == ""):
    #                 continue
    #             elif (line == "END"):
    #                 break
    #             delta.append(line)
    #         print(delta)
    #             #print(line.strip())  # Example: Print each line after removing leading and trailing whitespaces
    #     return (Q, sigma, q0, F, delta)

    """
    Writes to the output file.
    """

    def WriteToOutput(self, outputFilePath):
        # Open the file in write mode
        with open(outputFilePath, "w") as file:
            # Write content to the file
            file.write("Hello, this is a sample text.\n")
            file.write("Writing to a text file in Python is easy!")

        file.close()

        print(f"File '{outputFilePath}' has been created and written to.")
