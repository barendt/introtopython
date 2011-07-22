#!/usr/bin/env python

"""Write out a FASTA file.

Writing is more complicated and requires a few things from Bio.

Biopython's writing method expects to be given a list of SeqRecord objects and
it will write them to a file. Each SeqRecord object contains a Seq object that
has the actual sequence (and what type of sequence it is) as well as an id.

"""

try:
    from Bio import SeqIO
    from Bio.Seq import Seq
    from Bio.SeqRecord import SeqRecord
    from Bio.Alphabet import generic_rna
except ImportError:
    print "Sorry, you need Biopython to run this."
    import sys
    sys.exit(1)

sequences = [
    "ACGGCG",
    "ACGCGT",
    "CCCCGC",
    ]

list_to_write = list()
count = 1
for sequence in sequences:
    # since we are writing RNA, replace T with U (though Bio doesn't care)
    sequence = sequence.replace("T", "U")

    new_sequence = SeqRecord(Seq(sequence, generic_rna), id=str(count))
    list_to_write.append(new_sequence)
    count += 1

with open("my_first_fasta.fasta", "wb") as f:
    SeqIO.write(list_to_write, f, "fasta")
