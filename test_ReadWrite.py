import pytest
import sys
import ReadWrite
from unittest.mock import Mock


@pytest.fixture
def mock_argv():
    return ['test.py', 'input_file.txt']

def test_readwrite_constructor(mock_argv, monkeypatch):
    monkeypatch.setattr(sys, 'argv', mock_argv)
    rw = ReadWrite()
    assert rw.inputFilePath == 'input_file.txt'


# def test___init__(mock_args):
#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite.ReadWrite()
#     print("hello")

#     # Check if the inputFilePath is taken from the command line arguments.
#     assert ReadWrite_instance.inputFilePath == mock_args.argv[1]


# def test_WriteToOutput():
#     # Setup.
#     inputFilePath = "input.nfa"
#     outputFilePath = "output.dfa"

#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

#     # Call the method to be tested.
#     ReadWrite_instance.WriteToOutput(outputFilePath)
