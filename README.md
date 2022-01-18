# targeted_mp
Custom scripts and out data for an in silico targeted metaproteomics study on Anaerobic Digester microbiomes.

__Project:

The work is part of a study titled “In-silico evaluation of a targeted metaproteomics strategy for broad screening of cellulolytic enzyme capacities in anaerobic microbiome bioreactors,” by Manuel I. Villalobos Solis, Payal Chirania, and Robert L. Hettich.

We have conducted a detailed in-silico examination of the potential of mass spectrometry-based targeted metaproteomics as a means of fast, sensitive, and extensive cellulolytic enzymatic measurements on anaerobic digestion microbiomes. We performed an in-silico selection and evaluation of groups of tryptic peptides from five important GH families derived from a dataset of 1401 metagenome-assembled genomes in anaerobic digesters. We selected groups of shared peptides among proteins within a GH family while at the same time being unique compared to all other background proteins. In particular, we were able to identify a tractable unique set of peptides that were sufficient to monitor the range of GH families. The unique peptides selected for groups of GHs were found to be sufficient for distinguishing enzyme specificity or microbial taxonomy. In total, these in-silico results suggest that targeted metaproteomics could be a valuable approach for estimating molecular level enzymatic capabilities and responses of microbial communities to different substrates or conditions, which is a critical need in either building or utilizing constructed communities or defined cultures for bio-production.



__Details about the scripts within the "code" folder:

__1. Script - "get-target-background-sequences.py"
		
This script takes a protein FASTA file and a list of protein IDs as inputs and outputs two FASTA files - one containing the protein sequences corresponding to the IDs in the input list, and the other one containing protein sequences that do not match protein ID in the input protein ID list.

In the study, this script was utilized to generate target and background protein sequences for each target GH family. The input was protein sequences from all the MAGs and a list of protein IDs belonging to a target GH family across all the MAGs. 



__2. Script - "clip_N-terminal-sequence.py"

This script takes a protein FASTA file as input and removes the first X (provided as input by user) amino acids from the N-terminal of every protein sequence in the input FASTA file. The script then outputs a FASTA file containing the trimmed protein sequences.

In the study, this script was utilized to clip first 24 N-terminal amino acids from all the protein sequences of a target GH family before the sequences were digested in silico by trypsin. This was done to prevent inclusion of potential signal peptides (which get cleaved off during protein maturation) in the list of final peptides for monitoring a GH family.



__3. Script - "find-minimum-peptides-for-enzyme-family.py"
				
This script takes an input comma separated (.csv) file containing two columns- first column with peptide sequences and the second column with the protein ID it matches in a row. This script then parses through this file to identify the minimum number of peptides (in column 1) that can represent all the proteins in the column 2.
				In this study, this script was used to identify the final list of peptides to monitor all the proteins from a target GH family within the constructed microbiome of 1401 MAGs. The input was the list of peptides unique to specific GH family proteins compared to the background of all other non-target protein sequences.

