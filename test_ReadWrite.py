import pytest
import sys
import ReadWrite


def test___init__():
    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite.ReadWrite()

    # Check if the inputFilePath is taken from the command line arguments.
    assert ReadWrite_instance.inputFilePath == sys.argv[1]

# def test_WriteToOutput():
#     # Setup.
#     inputFilePath = "input.nfa"
#     outputFilePath = "output.dfa"

#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

#     # Call the method to be tested.
#     ReadWrite_instance.WriteToOutput(outputFilePath)
