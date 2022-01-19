"""
Python script to compare the input peptidome (of a target GH family) with the respective input background (non-target GH) peptidome and output the peptides 
that are unique to the target GH peptidome. Here, trypsin was used for digestion of proteins to peptides before input into the script. The script also filters the input target peptidome to include only peptides with 6-25 amino acids (per targeted proteomic recommendations)
before the comparison with the background peptidome. The script also maintains the link of target peptides to the proteins they are derived from.

Created by Payal Chirania - April 2020
"""

import sys
from Bio import SeqIO
import glob
import os

#input fasta file containing the background peptidome (i.e., peptidome derived from non-target-GH proteins). The format is protein followed by the peptides it produces.
bkgdPeptidome = sys.argv[1]

#input fasta file containing the target protein family peptidome (i.e., peptidome derived from target-GH family proteins). The format is protein followed by the peptides it produces.
targetPeptidome = sys.argv[2]

#assigning empty list or dictionary for storing the input and output peptidomes:
targetDict = {}
bkgdPepList= []
uqTargetDict = {}

#output file name as user input  - comma separated .csv file	
outputFile = sys.argv[3]

print(bkgdPeptidome+"\t"+targetPeptidome+"\t"+outputFile)

#parsing through the input target peptidome and storing peptides with 6-25 amino acids them as a dictionary with their protein Ids as the key to keep the peptide to protein link.
with open(targetPeptidome,"r") as targetPep:
    for line in targetPep:
        #print(line)
        if line.startswith(">"):
            #print(line)
            proteinName = line.rstrip("\n").split(" ")[0][1:]
            targetDict[proteinName] = []
        else:
            line2 = line.rstrip("\n")
            if("M" in line2 or "C" in line2):
                continue
            elif(len(line2) >=6 and len(line2)<=25):
                targetDict[proteinName].append(line2)
            #print(line2)
print("reading target peptidome done.")         

#parsing through the input background peptidome and storing the peptides as a list.
with open(bkgdPeptidome,"r") as bkgdPep:
    for line in bkgdPep:
        #print(line)
        if line.startswith(">"):
            continue
        else:
            line2 = line.rstrip("\n")
            bkgdPepList.append(line2)
            #print(line2)          

print("reading background peptidome done.") 

#comparing the target and background peptidomes and storing the peptides unique to the target peptidome ("unique targte peptidome") in a separate dictionary
for protId, pepList in targetDict.items():
    #print(set(pepList))
    uqPepList = list(set(pepList) - set(bkgdPepList))
    if len(uqPepList) != 0:
        uqTargetDict[protId] = uqPepList
    #print(uqTargetDict[protId])
    
#print(uqTargetDict)
print("Got uq-peptidome from the target against background.") 

#counting the peptides and proteins in the unique target peptidome
protCnt=0
pepCnt =0

for k, val in uqTargetDict.items():
    protCnt +=1 
    print(k, val)
    for v in val:
        pepCnt +=1
        
print("Count of peptides unique to target list:")         
print(pepCnt)
print("Count of proteins that unique peptides belong to:")   
print(protCnt)

#saving the unique target peptidome in the output file (here .csv was used). The output consists of two columns- column 1 contains the peptide and column 2 contains the protein the peptide comes from. 
print("Starting output in a new file....")   
with open(outputFile,"w") as outfile:
    outLine = "Peptide,Protein\n"
    outfile.write(outLine)    
    for pId, pepL in uqTargetDict.items():
        for pep in pepL:
            outLine = pep + "," + pId + "\n"
            outfile.write(outLine)
            
print("Output finished. :)")   

