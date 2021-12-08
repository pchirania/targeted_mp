"""
Python script to first get a list of protein IDs that correspond to specific GH families from the input list of annotations
Next use the IDs to get those sequences from the input MAG protein fasta files and output as a new fasta file. The sequences that do not belong to the GH family are output in the background fasta file.

Created by Payal Chirania - March 2020
"""
import sys
from Bio import SeqIO
import os


#input file with CAZyme annotations <hard coded here, can be user-input>
file1= "newParsedResult-dbcan_ofAll1401MAGs.txt" 

#input file with all the protein sequences from MAGs in Fasta format <hard coded here, can be user-input>
allSeqFiles = "allMAGSCombined_Clustered.fasta"

#GHs with most annotations across all MAGs or any list of GHs as needed <hard coded here, can be user-input>
ghList = ["GH13", "GH2", "GH3", "GH43", "GH23"]  

idDict ={}

#assigning empty list for each GH in the dictionary:
for ghFam in ghList:
    idDict[ghFam] = []

#getting list of protein Ids for specific GH families
with open(file1,"r") as parsedDbResultFile:
    for line in parsedDbResultFile:
        #print(line)
        if line.startswith("Gene"):
            continue
        else:
            line2 = line.rstrip("\n").split("\t")
            geneId = line2[0]
            domain = line2[1]
            if domain in ghList:
                if len(idDict[domain])==0:
                    idDict[domain] = [geneId]
                else:
                    idDict[domain].append(geneId)
                
#print(idDict)

#getting the sequences for specific GH families' protein IDs and writing in Fasta file
for ghFam2, ghFamIdList in idDict.items():
    #print(ghFam2)
    #print(ghFamIdList)
    
    ghFile = ghFam2 + "_AnDig_Clustered"+ ".fasta"
    print(ghFile)
    ghFileBkgd = ghFam2 + "_AnDig_Clustered"+ "-background.fasta"
    print(ghFileBkgd)

    out_handle = open(ghFile, "w")
    out_handle2 = open(ghFileBkgd, "w")
    
    for rec in SeqIO.parse(allSeqFiles, "fasta"):
        if rec.id in ghFamIdList:
            print(rec.id)
            SeqIO.write(rec, out_handle, "fasta")
        else:
            SeqIO.write(rec, out_handle2, "fasta")

out_handle.close()
out_handle2.close()
