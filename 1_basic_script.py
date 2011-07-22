#!/usr/bin/env python
# ^That line tells the computer how to interpret this file

# Anything starting with a '#' is a comment. Long comments 
# go inside triple-quotes.

""" 'import' tells python to load module we will need. Modules can
have all sorts of things - functions, data, settings, objects.

"""
import sys


def main():
    """Print something and return.

    """
    print "Hello, world!"

    # returning 0 indicates success.
    return 0

# these next two lines indicate what should be done if this file is executed
if __name__ == "__main__":
    sys.exit(main())
