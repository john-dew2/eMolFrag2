import sys
from pathlib import Path
from eMolFrag2.unittests import utilities
from eMolFrag2.src.input import AcquireMolecules, AcquireFiles, Configuration, Options

usr_dir = Path.cwd()
dataPath = usr_dir.joinpath("eMolFrag2/unittests/data/db-files")
mol2 = dataPath.joinpath("mol2")
smi = dataPath.joinpath("smi")
sdf = dataPath.joinpath("sdf")
pdb = dataPath.joinpath("pdb")
mol = dataPath.joinpath("mol")

def runAcquireMoleculesTests():
    
    testPaths = [mol2, smi, pdb, mol]
    #Tests if mol2 and smi are taken
    for filePath in testPaths:
        arguments = f"!python -m eMolFrag2.src.eMolFrag -i {filePath} -o output/"
        files = getListofFiles(arguments)
        runAcquireMolecules(files, len(files))
        
    #Will recognize the files as bad
    runAcquireMolecules(getListofFiles(f"!python -m eMolFrag2.src.eMolFrag -i {sdf} -o output/"), 0)

def getListofFiles(args):
    initializer = Options.Options()
    initializer = Configuration.readConfigurationInput(initializer, args)
    return AcquireFiles.acquireMoleculeFiles(initializer)

def runAcquireMolecules(files, expec):
    retFiles = AcquireMolecules.acquireMolecules(files)
    assert len(retFiles) == expec

#
#
# Unit test initiation functionality
#
#
def runtest1(func):

    try:
       func()
       return True

    except:
       return False


def runtest(test_name, test_func, successful, failed):
    if runtest1(test_func):
        successful.append(test_name)
    else:
        failed.append(test_name)

def runtests():
    printlevel = 1
    utilities.emit(printlevel, f"Executing {__name__} unit tests.")
    
    #
    # Define all tests as a Dictionary: {str-name, <function-to-execute>}
    #
    tests = {"acquireMolecules": runAcquireMoleculesTests}

    #
    # Run
    #
    successful = []
    failed = []
    for test_name, test_func in tests.items():
        runtest(test_name, test_func, successful, failed)

    # 
    # Report
    #
    if not failed:        
        utilities.emit(printlevel, f'{__name__} unit tests are successful.')

    else:
        for test in failed:
            utilities.emit(printlevel+1, f'Failed {test}.')

if __name__ == "__main__":
    runtests()