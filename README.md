# targeted_mp
Custom scripts and out data for an in silico targeted metaproteomics study on Anaerobic Digester microbiomes.

__About the Project:


**Details about the scripts within the "code" folder:

1. Script - "get-target-background-sequences.py"

This script takes a protein FASTA file and a list of protein IDs as inputs and outputs two FASTA files - one containing the protein sequences corresponding to the IDs in the input list, and the other one containing protein sequences that do not match protein ID in the input protein ID list.

In the study, this script was utilized to generate target and background protein sequences for each target GH family. The input was protein sequences from all the MAGs and a list of protein IDs belonging to a target GH family across all the MAGs. 

2. Script - "clip_N-terminal-sequence.py"

This script takes a protein FASTA file as input and removes the first X (provided as input by user) amino acids from the N-terminal of every protein sequence in the input FASTA file. The script then outputs a FASTA file containing the trimmed protein sequences.

In the study, this script was utilized to clip first 24 N-terminal amino acids from all the protein sequences of a target GH family before the sequences were digested in silico by trypsin. This was done to prevent inclusion of potential signal peptides (which get cleaved off during protein maturation) in the list of final peptides for monitoring a GH family.


5. Script - "find-minimum-peptides-for-enzyme-family.py"


