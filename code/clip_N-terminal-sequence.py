"""
This Python script removes the first X number (as entered in arguments by the user) of amino acids from the protein sequence.
Created by Payal Chirania - March 2020
"""

import sys
from Bio import SeqIO
import glob
import os
import re

#input target fasta file
protSeqFile = sys.argv[1]

#length to remove, we are using 24aa
removalLen = int(sys.argv[2])

#output file name. I have been adding -first24aaAndDigSite to the target file name to get the output file name
outputFile = sys.argv[3]

print(removalLen) # prints the number of amino acids to be removed form the N-terminal of the input sequences

out_handle = open(outputFile,"w")

for rec in SeqIO.parse(protSeqFile,"fasta"):
        
        #firstK_loc = re.search("[KR][^P]", str(rec.seq))
        #print(firstK_loc.start())
        
        #removing first X number of amino acids - removing 24aa - so if the 25th is K or R then it would stay
        rec.seq = rec.seq[removalLen:]
        
        
        #removing amino acids till the next digestion site including the K or R if needed
        newDigest_loc = re.search("[KR][^P]", str(rec.seq))
        #print(newDigest_loc.start())
        #rec.seq = rec.seq[(newDigest_loc.start()+1):]
        
        SeqIO.write(rec, out_handle, "fasta")   


out_handle.close()