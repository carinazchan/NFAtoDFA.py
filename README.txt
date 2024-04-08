README

Instructions for Running the Program:
- Make sure all necessary .py files are in one folder.
- In Terminal, cd to the correct directory (the folder containing all your .py files for this project).
- Run in the terminal: python3 Main.py input.nfa

Linter & Unit Tests:
- Linter and unit tests run automatically when making a pull request on GitHub.

Unit Test Coverage Report:
- After commit and push, make a pull request (continue to preview pull request).
- Let the linter and unit tests run in GitHub.
- Click on "Details" for the row with Unit Tests.
- Click on drop down arrow for "Upload pytest test results".
- Click on the URL after "Artifact download URL: " to download the URL for the unit test covereage report.
- A file named, "Coverage.zip" should be in your Downloads.
- Unzip it (double click on it).
- Go to the Coverage folder that appears from the unzip.
- Double click on, "index.html". Takes you to a website with the coverage of the unit tests.
- NOTE: The only coverage that matters is for the files named, "test_[insert file name to be tested].py". Disregard other covereage stats.


Sources:
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://www.askpython.com/python/examples/fixed-takes-0-positional-arguments-but-1-was-given
- https://youtu.be/mzlH8lp4ISA?si=Dm0MQbNj-wggFp1s
