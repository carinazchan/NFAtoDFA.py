# main.py

import sys
import ReadWrite
from epsilon_closure import epsilon_closure

def main():
    ReadWriteInstance = ReadWrite.ReadWrite()
    ReadWriteInstance.CheckCommandLine()
    lines = ReadWriteInstance.GetLine()

    # Extract transitions from the lines
    transitions = lines[4]

    # Example usage of epsilon_closure
    initial_state = lines[2][0]  # Example initial state
    closure = epsilon_closure(transitions, initial_state)
    print(f"Epsilon closure of {initial_state}: {closure}")

if __name__ == "__main__":
    main()
