from __future__ import print_function
from io import StringIO
import sys

## 1.c Coding: Printing "Hello Queeny!" on termimal
# github@LongIslandWithoutIceTea
# Your task:
# implement the print_on_terminal function below
# feel free to try modifying other things in this code

def print_on_terminal():
    ## TODO:
    # write your print function here
    # Hint: you only need one line of code to do this,
    #       don't for get to indent the line using tab

    print('Hello Queeny!')

    return


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout


if __name__ == "__main__":
    with Capturing() as output:
        print_on_terminal()
    print("Desired output:")
    print('Hello Queeny!\n')
    if not output:
        print('')
        print('Your output is empty!')
    elif output[0] == 'Hello Queeny!':
        print('Your output:')
        print(output[0] + '\n')
        print('Congratulation! You\'ve just created your first Python program~')
    else:
        print('Your output:')
        print(output[0] + '\n')
        print('The string you printed is not correct, please try again!')