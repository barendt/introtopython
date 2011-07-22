#!/usr/bin/env python

"""We need the SeqIO module from within the Bio (Biopython) module.
Modules can have modules inside of them.

"""
try:
    from Bio import SeqIO
except ImportError:
    print "Sorry, you need Biopython to run this."
    import sys
    sys.exit(1)

fasta_file = "NBMycotube-83332.init.fa"

for sequence in SeqIO.parse(open(fasta_file, "rb"), "fasta"):
    print str(sequence.seq)
