"""Part of the GroupAlign script library"""
# TODO: In progress
# TODO: determine structure

import os
import re

from name import Name #TODO: test name module
from gui import selectFile
from data_reader import dataReader #TODO: test data_reader module
from groups import assignGroups #TODO: test groups module
from excel_generator import excelGenerator #TODO: test excel_generator module
from display_data import displayData #TODO: write display_data module


class GroupAlign:

    def __init__(self, options):
        self.options = options
        self.process = Process()

    def processData(self):
        if self.options.batch:
            #for batch processing of an entire directory
            cwd = os.getcwd()
            files = os.listdir()
            txtRe = re.compile('GA_(.*)\.(xls|xlsx)',re.I)

        elif self.options.filename:
            #for command line processing of a single file
            files = self.options.filename
            txtRe = re.compile('(.*)\.(xls|xlsx)',re.I)

        else:
            #defaults to GUI if no command line arguments are given
            files = selectFile.byGui()
            txtRe = re.compile('(.*)\.(xls|xlsx)', re.I)

        )
        for file in files:
            try:
                match = txtRe.match(file) #simple filetype check and funnels if statments into single pathway
            except:
                print(f"#{file} is not a supported filetype")
            if match:

                data = dataReader(file) #result is a collection of pandas dataframes of the source excel sheet
                                        #dataFrames are organized into a dict if multiple sheets are found
                                            #TODO: decide if "groups" should be dict vs. pd dataFrame
                groups = assignGroups(data) #result is a dict of best result; list of dicts if multiple viable results
                out_filename = Name.outputFile(file)
                excelWkst = excelGenerator(file)
                excelWkst.add(groups.assignments)
                excelWkst.save(out_filename)
                if self.options.graph:
                    graph = displayData(groups)
                    graph.scatter_from_group()



