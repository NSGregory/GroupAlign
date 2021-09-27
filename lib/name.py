""" Module for naming files from varied inputs """

from pathlib import Path

class Name:
    """Simple module for renaming output files based on a filepath input."""
    prefix = "GA_"
    def __init__(self):
        #TODO: Don't think we need any inits at this time but placeholding for now
        self.prefix = "GA_complete_"

    def file(self,filename):
        #TODO: Is this OS dependent? Windows OS may use \ for pathnames
        #TODO: candidate for pruning
        return filename.split('/')[-1]

    def outputFile(filename, prefix=prefix):
        """This is meant to be compatible across different OS"""
        path = Path(filename)
        #path.name includes the suffix
        #using stem gives name without suffix
        #allows the name to be elsewhere in the title
        return prefix + path.stem





if __name__ =='__main__':
    filename = Name.outputFile("test.py", "This_file_is_done")
    print(filename)
    filename = Name.outputFile("usr/this/is/a/simple/exercise.pdf")
    print(filename)