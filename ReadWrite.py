import sys

"""
Reads from an input file and writes to an output file.
"""


class ReadWrite:

    # Constructor for the ReadWrite class.
    def __init__(self, sysArgv=sys.argv):
        self.inputFilePath = sysArgv[
            1
        ]  # Second argument is the file path (python3 doesn't count as an argument).

    # Checks the command line arguments to see if the correct amount of arguments are passed.
    def CheckCommandLine(self):
        # sys.argv: A list of command-line arguments passed to a Python script. Script name is the first element (sys.argv[0]).
        if len(sys.argv) != 2:  # If the length of the command line arguments is != 2
            return "Need two arguments: YourScript.py InputFile.txt"
        else:
            return

    def GetLine(self):
        with open(self.inputFilePath, "r") as file:
            # Iterate through each line in the file.
            fileLines = file.read().split("\n")

            # Read Q: line[0].
            Q = fileLines[0].replace("{", "").replace("}", "").split("\t")

            # Read Sigma: lines[1].
            sigma = fileLines[1].split("\t")

            # Read q0: lines[2].
            q0 = fileLines[2].replace("{", "").replace("}", "").split("\t")

            # Read F: lines[3].
            F = fileLines[3].replace("{", "").replace("}", "").split("\t")

            # Read transitions: lines[4:]. Reads from line 4 to the end of the file.
            delta = []  # List of transitions.
            for deltaLine in fileLines[4:]:
                if deltaLine == "BEGIN" or deltaLine == "":
                    continue
                elif deltaLine == "END":
                    break
                else:
                    delta.append(deltaLine)

        print(Q, sigma, q0, F, delta)

        returnList = [Q, sigma, q0, F, delta]

        return returnList
