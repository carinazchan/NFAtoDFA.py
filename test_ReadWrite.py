import pytest
import sys
import ReadWrite
from unittest.mock import patch, mock_open
from epsilon_closure import epsilon_closure  # Import the epsilon_closure function


def test___init__():
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        readWriteInstance = ReadWrite.ReadWrite(["script", "test"])

        # Check if the inputFilePath is taken from the command line arguments.
        assert readWriteInstance.inputFilePath == "test"


def test_CheckCommandLine():
    # Test if the CheckCommandLine method returns None when the correct amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1"]):
        # Create an instance of ReadWrite.
        readWriteInstance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert readWriteInstance.CheckCommandLine() == None

    # Test if the CheckCommandLine method returns an error message when the incorrect amount of arguments are passed.
    with patch.object(sys, "argv", ["test.py", "argument1", "argument2"]):
        # Create an instance of ReadWrite.
        readWriteInstance = ReadWrite.ReadWrite(sys.argv)

        # Check if the CheckCommandLine method returns None.
        assert (
            readWriteInstance.CheckCommandLine()
            == "Need two arguments: YourScript.py InputFile.txt"
        )


def test_GetLine():
    # Create a mock file contents.
    mockFileContents = """{1}\t{2}\t{3}
a\tb
{1}
{1}
BEGIN
{1}, EPS = {3}
{1}, b = {2}
{2}, a = {3}
{2}, b = {3}
{2}, a = {2}
{3}, a = {1}
END"""

    # Create an instance of ReadWrite.
    readWriteInstance = ReadWrite.ReadWrite(sys.argv)

    with patch("builtins.open", mock_open(read_data=mockFileContents)):
        # Check if the GetLine method returns the correct values.
        assert readWriteInstance.GetLine() == [
            ["1", "2", "3"],
            ["a", "b"],
            ["1"],
            ["1"],
            [
                "{1}, EPS = {3}",
                "{1}, b = {2}",
                "{2}, a = {3}",
                "{2}, b = {3}",
                "{2}, a = {2}",
                "{3}, a = {1}",
            ],
        ]


# New test for the epsilon_closure function
def test_epsilon_closure():
    transitions = [
        "{1}, EPS = {3}",
        "{1}, b = {2}",
        "{2}, a = {3}",
        "{2}, b = {3}",
        "{2}, a = {2}",
        "{3}, a = {1}"
    ]

    # Check epsilon closure for state 1
    assert epsilon_closure(transitions, "1") == {"1", "3"}

    # Check epsilon closure for state 2
    assert epsilon_closure(transitions, "2") == {"2"}

    # Check epsilon closure for state 3
    assert epsilon_closure(transitions, "3") == {"3"}
