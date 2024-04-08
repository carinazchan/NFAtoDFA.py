import pytest
import sys
import io
import ReadWrite
from unittest.mock import patch


def test___init__():
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWriteInstance = ReadWrite.ReadWrite(["script", "test"])

        # Check if the inputFilePath is taken from the command line arguments.
        assert ReadWriteInstance.inputFilePath == "test"


def test_CheckCommandLine():
    # Test if the CheckCommandLine method returns None when the correct amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWriteInstance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert ReadWriteInstance.CheckCommandLine() == None

    # Test if the CheckCommandLine method returns an error message when the incorrect amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1", "argument2"]):
        # Create an instance of ReadWrite.
        ReadWriteInstance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert (
            ReadWriteInstance.CheckCommandLine()
            == "Need two arguments: YourScript.py InputFile.txt"
        )


def test_GetLine():
    # Create a mock file contents.
    mockFileContents = """
    {1} {2}	{3}
    a	b
    {1}
    {1}
    BEGIN
    {1}, EPS = {3}
    {1}, b = {2}
    {2}, a = {3}
    {2}, b = {3}
    {2}, a = {2}
    {3}, a = {1}
    END
    """

    # Create a mock file object.
    mockFile = io.StringIO(mockFileContents)

    # Create an instance of ReadWrite.
    ReadWriteInstance = ReadWrite.ReadWrite(sys.argv)

    # Check if the GetLine method returns the correct values.
    assert ReadWriteInstance.GetLine(mockFile) == (
        ["1", "2", "3"]["a", "b"]["1"]["1"][
            "{1}, EPS = {3}",
            "{1}, b = {2}",
            "{2}, a = {3}",
            "{2}, b = {3}",
            "{2}, a = {2}",
            "{3}, a = {1}",
        ]
    )
