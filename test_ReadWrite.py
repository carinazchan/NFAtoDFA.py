import pytest
import sys
import ReadWrite


@pytest.fixture
def mock_sys_argv(monkeypatch):
    # Mock sys.argv to contain the desired file path.
    monkeypatch.setattr(sys, 'argv', ['script_name.py', 'dummy.txt'])

def test___init__():
    # Call the constructor for ReadWrite.
    read_write_instance = ReadWrite.ReadWrite()

    # Check if the inputFilePath attribute is set correctly.
    assert read_write_instance.inputFilePath == 'dummy.txt'

def test_CheckCommandLine_correct_args(capsys):
    # Create an instance of ReadWrite.
    read_write_instance = ReadWrite.ReadWrite()

    # Call CheckCommandLine.
    read_write_instance.CheckCommandLine()

    # Check if the program did not exit (i.e., correct number of arguments).
    out, _ = capsys.readouterr()  # Capture stdout.
    assert out == ''  # No output should be printed.

def test_CheckCommandLine_incorrect_args(capsys):
    # Modify sys.argv to contain only the script name without any file path.
    sys.argv = ['script_name.py']

    # Create an instance of ReadWrite.
    read_write_instance = ReadWrite.ReadWrite()

    # Call CheckCommandLine.
    with pytest.raises(SystemExit) as e:
        read_write_instance.CheckCommandLine()

    # Check if the program exited with the expected error message.
    out, _ = capsys.readouterr()  # Capture stdout.
    assert str(e.value) == '1'  # Check the exit status code.
    assert out == 'Need two arguments: YourScript.py InputFile.txt\n'  # Check the error message.

def test_GetLine(read_write_instance, monkeypatch):
    # Define the contents of the mocked file.
    file_contents = """
        {1}	{2}	{3}
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

    # Mock the open function to return a file-like object with predefined contents.
    def mock_open_func(filename, mode):
        return StringIO(file_contents)

    monkeypatch.setattr('builtins.open', mock_open_func)

    # Call the GetLine method.
    result = read_write_instance.GetLine()

    # Define the expected result.
    expected = (
        ['1', '2', '3'],
        ['a', 'b'],
        ['1'],
        ['1'],
        ['{1}, EPS = {3}', '{1}, b = {2}', '{2}, a = {3}', '{2}, b = {3}', '{2}, a = {2}', '{3}, a = {1}']
    )

    # Check if the result matches the expected value.
    assert result == expected


# def test___init__():
#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite.ReadWrite()

#     # Check if the inputFilePath is taken from the command line arguments.
#     assert ReadWrite_instance.inputFilePath == sys.argv[1]

# def test_WriteToOutput():
#     # Setup.
#     inputFilePath = "input.nfa"
#     outputFilePath = "output.dfa"

#     # Create an instance of ReadWrite.
#     ReadWrite_instance = ReadWrite(inputFilePath, outputFilePath)

#     # Call the method to be tested.
#     ReadWrite_instance.WriteToOutput(outputFilePath)
