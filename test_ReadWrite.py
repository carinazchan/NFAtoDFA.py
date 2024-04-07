import pytest
from ReadWrite import ReadWrite


def test___init__():
    # Setup.
    inputFilePath = "input.nfa"
    outputFilePath = "output.dfa"

    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

    # Call the method to be tested.
    ReadWrite_instance.__init__(inputFilePath, outputFilePath)


def test_WriteToOutput():
    # Setup.
    inputFilePath = "input.nfa"
    outputFilePath = "output.dfa"

    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

    # Call the method to be tested.
    ReadWrite_instance.WriteToOutput(outputFilePath)


def test_CheckCommandLine():
    # Setup.
    inputFilePath = "input.nfa"
    outputFilePath = "output.dfa"

    # Create an instance of ReadWrite.
    ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

    # Call the method to be tested.
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        ReadWrite_instance.CheckCommandLine()

    # pytest_wrapped_e is an instance of pytest.raises which acts as a context manager that catches exceptions.
    assert (
        pytest_wrapped_e.type == SystemExit
    )  # Check if the exception type is SystemExit.
    assert pytest_wrapped_e.value.code == 1  # Check if the exception code is 1.
