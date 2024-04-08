import pytest
import sys
import io
import ReadWrite
from unittest.mock import patch


def test___init__():
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the inputFilePath is taken from the command line arguments.
        assert ReadWrite_instance.inputFilePath == sys.argv[1]


def test_CheckCommandLine():
    # Test if the CheckCommandLine method returns None when the correct amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert ReadWrite_instance.CheckCommandLine() == None

    # Test if the CheckCommandLine method returns an error message when the incorrect amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1", "argument2"]):
        # Create an instance of ReadWrite.
        ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert (
            ReadWrite_instance.CheckCommandLine()
            == "Need two arguments: YourScript.py InputFile.txt"
        )


def test_GetLine():
    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite.ReadWrite(sys.argv)

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
    mock_file = io.StringIO(mockFileContents)

    assert ReadWrite_instance.GetLine(mock_file) == (
        ["1", "2", "3"]["a", "b"]["1"]["1"][
            "{1}, EPS = {3}",
            "{1}, b = {2}",
            "{2}, a = {3}",
            "{2}, b = {3}",
            "{2}, a = {2}",
            "{3}, a = {1}",
        ]
    )
