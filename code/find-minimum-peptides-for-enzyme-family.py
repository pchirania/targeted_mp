"""
Python script to find the least number of common unique peptides between proteins belonging to an enzymatic group such as a GH family
Each peptide will capture some new proteins if not all

Created by Payal Chirania March 2020, modified in April 2020
"""
import sys
import os


#input file name - it is a csv file with 2 columns - first with peptides and second with protein in matches each match in one row.
inputFilename = sys.argv[1]

#output file name 1 - tab delimited .txt file
outputFilename =sys.argv[2]

#output file name 2  - tab delimited .txt file	
outputFilename2 =sys.argv[3]

#output file name 3  - tab delimited .txt file	
outputFilename3 =sys.argv[4]

def getDict(fileName):
    dictFromFile = {}
    with open(fileName,"r") as inputFile:
        for line in inputFile:
            if line.startswith("Peptide"):
                continue
            else:
                line2 = line.rstrip().split(",")
                pepId = line2[0]
                protId = line2[1]
                if pepId in dictFromFile.keys():
                    if protId not in dictFromFile[pepId]:
                        dictFromFile[pepId].append(protId)
                    # this was added to remove duplicate additions of same protein to a peptide key
                else:
                    dictFromFile[pepId] = [protId]                
            
    return dictFromFile

def pepWithMaxVal (dict1):
    maxVal=0
    maxPep = ""
    for key,value in dict1.items():
        cnt = len(dict1[key])
        if maxVal < cnt:    #here considering only one peptide if 2 or more have same count of peptides
            maxVal = cnt
            maxPep = key
    return [maxPep, maxVal]


def reducePepToProtDict(pepToProtDict, selecPep):
    dict2 = {}
    for key, value in pepToProtDict.items():
        newDictValue = list(set(pepToProtDict[key]) - set(pepToProtDict[selecPep]))
        if newDictValue:
            dict2[key] = newDictValue
        #print (pepToProtDict[startPep])
        #print (dict2[key])
    #print (dict2)
    return dict2

pepToProtDictOrig = getDict(inputFilename)
pepList = []
iterDict = pepToProtDictOrig
#print (iterDict)
pepListWithCntDict ={} # count of new proteins captured by the peptide

while(iterDict): 
    
    startPepList = pepWithMaxVal(iterDict)
    startpep = startPepList[0]
    startpepProtCnt = startPepList[1]
    if startpepProtCnt ==0:
        print("in exit")
        break
    pepList.append(startpep)
    pepListWithCntDict[startpep] = startpepProtCnt
    iterDict = reducePepToProtDict(iterDict, startpep)
    #print(len(iterDict))
    
print(pepList)
print(len(pepList))


#output of peptide sequences in file
with open(outputFilename,"w") as outputFile:
    outputFile.write("Peptide\tNo.Of-New-ProteinsCovered\n")
    
    for pep,protCnt in pepListWithCntDict.items() :
        newEntry= pep+"\t"+str(protCnt) + "\n"
        outputFile.write(newEntry)
        
#output of the dictionary (pep to protein) in a file
with open(outputFilename2,"w") as outputFile2:
    outputFile2.write("Peptide\tProtein-Accessions(All)\n")
    for pep,protList2 in pepToProtDictOrig.items():
        if pep in pepList:
            for protein1 in protList2:
                linePrint = pep + "\t" + protein1 + "\n"
                #print(linePrint)
                outputFile2.write(linePrint)

print(len(pepListWithCntDict))  

with open(outputFilename3,"w") as outputFile3:
    outputFile3.write("Peptide\tNo.Of-Total-ProteinsCovered\n")
    
    for pep2,protCnt2 in pepToProtDictOrig.items() :
        if pep2 in pepList:
            newEntry2= pep2+"\t"+str(len(protCnt2)) + "\n"
            outputFile3.write(newEntry2)

