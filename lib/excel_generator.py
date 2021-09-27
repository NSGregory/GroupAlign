"""Turns out the to_excel function of dataframes solves most of the issues here making this a small class.
   If the original file has multiple tabs being analyzed, the output file will include each of those tabs as separate
   output tabs.
    """
import pandas as pd
class excelGenerator:

    def __init__(self, group):
        self.group = group

    def add(self, assignments):
        pass

    def save(self, filename):
        """Assumes group is a pandas dataframe"""
        writer = pd.ExcelWriter(filename+".xlsx")
        for tab in self.group.df_assignment_merge.keys():
            self.group.df_assignment_merge[tab].to_excel(writer,tab)

        writer.save()

        #df.to_excel("filename.xlsx")





if __name__ == '__main__':
    from data_reader import dataReader
    from gui import selectFile
    from groups import assignGroups
    from name import Name

    file = selectFile.byGui()
    data = dataReader(file)
    groups = assignGroups(data)
    out_filename = Name.outputFile(file)
    excelWkst = excelGenerator(groups)
    #excelWkst.save(out_filename)
    #base = importr("base")
    #anticlust = importr("anticlust")