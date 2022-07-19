#
# Unit Testing Utility functionality
#

from rdkit import Chem
from pathlib import Path

#takes the contents of a file and puts it in a string for processing
def fileToString(file):

    contents = ""
    with open(file) as f:
        contents = f.read()
        
    f.close()
    
    return contents
   
#converts the contetns of a file to their respective molecule
def convertToRDkit(contents, extension):
    #kekulize = False
    #Chem.doKekule = False 
    
    if (extension == ".fasta"):
        return Chem.MolFromFASTA(contents)

    if (extension == ".yaml"):
        return Chem.MolFromHELM(contents)

    if (extension == ".mol2"):
        return Chem.MolFromMol2Block(contents, False)

    if (extension == ".mol"):
        return Chem.MolFromMolBlock(contents)

    if (extension == ".pdb"):
        return Chem.MolFromPDBBlock(contents)

    if (extension == ".sma"):
        return Chem.MolFromSmarts(contents)

    if (extension == ".smi"):
        return Chem.MolFromSmiles(contents)

    if (extension == ".tpl"):
        return Chem.MolFromTPLBlock(contents)

    return None

#
# Given a path object, return the corresponding RDKit molecule object
# This simplified functionality is for testing only
#
def getRDKitMolecule(path, extension):
    content = fileToString(path)
    return convertToRDkit(content, extension)
    
def createParser(arguments):
  if arguments == None:
    return None

  from argparse import ArgumentParser
  parser = ArgumentParser(description='eMolFrag2')
  parser.add_argument("-i",
  type=str,
  help='Set the input path')
  
  parser.add_argument("-o",
  type=str,
  help='Set the output path')
  
  parser.add_argument("-m",
  type=int, choices=range(0,3),
  help='Set the execution type')
  
  parser.add_argument("-c",
  type=int, choices=range(0,3),
  help='Set the output type')

  args = parser.parse_args(arguments)
  
  return args
  
#
#
# Printing to console ; can modify later to dump stream to other locations
#
# 
def emit(level, s):
    print("  " * level + s)
    
def emitError(level, s):
    print("  " * level + "Error:", s)

def emitWarning(level, s):
    print("  " * level + "Warning:", s)