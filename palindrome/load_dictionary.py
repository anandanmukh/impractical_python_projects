"""Loads a text file"""

import sys
from tempfile import TemporaryFile

def load(file):
    """Open a text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split("\n")
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt

    except IOError as e:
        print(f"{e}\n Error Opening {file}. Terminating  Program.")
        file = sys.stderr
    sys.ext(1)