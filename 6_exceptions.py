#!/usr/bin/env python

iupac_nucleotides = {
    "A": "A",
    "C": "C",
    "G": "G",
    "T": "T",
    "R": "AG",
    "Y": "CT",
    "S": "GC",
    "W": "AT",
    "K": "GT",
    "M": "AC",
    "B": "CGT",
    "D": "AGT",
    "H": "ACT",
    "V": "ACG",
    "N": "ACGT",
}

# accessing a key not in a dict will throw an exception and exit your program
#print iupac_nucleotides["Z"]

# you could test ahead of time...
if "Z" in iupac_nucleotides:
    print iupac_nucleotides["Z"]

# but it is often easier to ask forgiveness than permission...
try:
    print iupac_nucleotides["Z"]
except KeyError:
    print "Sorry, Z isn't in this dict."

""" that thing above is "trying" to do something. If it gets an exception called
KeyError, it does the thing inside the except. If it gets a different exception it still fails.

"""

try:
    print 1 / 0
except KeyError:
    print "division by 0 gives a different exception"

# You can also handle an exception (any exception) regardless of what type it is
try:
    print 1 / 0
except:
    print "Something is wrong."
