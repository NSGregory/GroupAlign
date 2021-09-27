"""Module for taking data from an excel sheet and processing it into useful pandas dataFrames"""

import pandas as pd
import csv

class dataReader:

    def __init__(self, filename):
        self.filename = filename
        self.settings_tab = "GA_settings"
        self.parameters = self.get_xls_parameters()
        self.datasets = self.get_datasets()

    #todo: populate as needed

    def get_xls_parameters(self):
        """Looks for the options tab in an excel file and uses it to decide how to handle the file"""
        # this block converts easy to use excel format for the end user
        # into a pivoted dataFrame that can be referenced by the column title
        settings_tab = pd.read_excel(self.filename, self.settings_tab)
        pivoted_format = settings_tab.pivot(index=None, values="Value", columns="Options")
        re_indexed = pivoted_format.apply(lambda x: pd.Series(x.dropna().values))

        # for loop here converts the dataFrame columns into a pure dict
        # which simplifies the values being used later
        parameters = {}
        for key in re_indexed.keys():
            parameters[key] = re_indexed[key][0]
        return parameters

    def get_datasets(self):
        """Builds a dict of dataFrames to be passed on later for analysis"""
        datasets = {}
        for wkst in self.parameters["Data_tabs"].split(","):
            try:
                datasets[wkst.strip()] = pd.read_excel(self.filename, wkst.strip())
            except:
                print(f"Data tab '{wkst}' listed in settings was not found in worksheet")
        return datasets






if __name__ =='__main__':
    from gui import selectFile
    file = selectFile.byGui()
    data = dataReader(file)




