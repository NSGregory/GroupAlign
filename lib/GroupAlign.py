"""Part of the GroupAlign script library"""
# TODO: In progress
# TODO: determine structure

import os
import re
import sys

from name import Name #TODO: test name module
from gui import selectFile
from data_reader import dataReader #TODO: test data_reader module
from groups import assignGroups #TODO: test groups module
from excel_generator import excelGenerator #TODO: test excel_generator module
from display_data import displayData #TODO: write display_data module
from Options import Options


class GroupAlign:

    def __init__(self, options):
        self.options = options
        #not sure what this line represents at this point
        #self.process = Process()

    def processData(self):
        if self.options.batch:
            #for batch processing of an entire directory
            cwd = os.getcwd()
            files = os.listdir()
            txtRe = re.compile('GA_(.*)\.(xls|xlsx)',re.I)

        elif self.options.filename:
            #for command line processing of a single file
            files = [self.options.filename]
            txtRe = re.compile('(.*)\.(xls|xlsx)',re.I)

        else:
            #defaults to GUI if no command line arguments are given
            files = [selectFile.byGui()]
            txtRe = re.compile('(.*)\.(xls|xlsx)', re.I)

        print(files)
        for file in files:
            print(file)
            try:
                match = txtRe.match(file) #simple filetype check and funnels if statments into single pathway
            except:
                print(f"#{file} is not a supported filetype")
            if match:

                # result is a collection of pandas dataframes of the source excel sheet
                # dataFrames are organized into a dict if multiple sheets are found
                data = dataReader(file)

                # result is a dict of best result; dict of dicts if multiple viable results
                groups = assignGroups(data)

                #creates the excel sheet output
                out_filename = Name.outputFile(file)
                excelWkst = excelGenerator(groups)
                excelWkst.add(groups.assignments)
                excelWkst.save(out_filename)

                #visualize the data if desired
                if self.options.graph:
                    graph = displayData(groups)
                    graph.scatter_from_group()


if __name__ == '__main__':
    # more legible feedback using the rich library
    from rich.traceback import install
    install(show_locals=True)

    # main function
    options = Options()
    opts = options.parse(sys.argv[1:])
    assigner = GroupAlign(opts)
    assigner.processData()

