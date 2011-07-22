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


# By default, looping over a dict gives you keys
for code in iupac_nucleotides:
    print code

# You can test to see if a key is in a dict
if "N" in iupac_nucleotides:
    print iupac_nucleotides["N"]


# You can make it work over values
for value in iupac_nucleotides.values():
    print value

if "ACGT" in iupac_nucleotides.values():
    print "It's there."


# You can also get both at once
for code, value in iupac_nucleotides.iteritems():
    print "{0}: {1}".format(code, value)


somelist = [1, 2, 3, 4, 5]

# adding a new thing to a list
somelist.append(6)

# list comprehensions are a way to build up a new list
newlist = [i * 2 for i in somelist]
print newlist

# this is the same as
newlist = list()
for i in somelist:
    newlist.append(i * 2)
print newlist



