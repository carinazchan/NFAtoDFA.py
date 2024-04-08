import pytest
import sys
import ReadWrite
from unittest.mock import patch


def test___init__():
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the inputFilePath is taken from the command line arguments.
        assert ReadWrite_instance.inputFilePath == sys.argv[1]


def test_CheckCommandLine():
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert ReadWrite_instance.CheckCommandLine() == None

    with patch.object(sys, "argv", ["test.py", "argument1", "argument2"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert (
            ReadWrite_instance.CheckCommandLine()
            == "Need two arguments: YourScript.py InputFile.txt"
        )
