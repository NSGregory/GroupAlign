"""For visualizing pandas dataframes
   This instance is for the GroupAlign script.  Will use settings from GroupAlign to make a series of subplots
   of each of the values of interest after the samples have been assigned to groups."""

import seaborn as sns
import matplotlib.pyplot as plt

class displayData:

    def __init__(self, data):
        self.data = data
    def scatter_from_group(self):
        """Assumes that the input is a group object from the group module, potentially with multiple entries"""
        graph_data = self.data.df_assignment_merge
        columns_to_graph = self.data.graph
        for set in graph_data.keys():
            df = graph_data[set]
            sns.set_theme(style="ticks", color_codes=True)
            num_columns = 3
            num_rows = (len(columns_to_graph)/num_columns).__ceil__() #rows*columns must be >= number of subplots
            fig, axes = plt.subplots(num_rows,
                                     num_columns,
                                     figsize=(15, 8),
                                     sharey=False) #syntax note: (2,3) is 2 rows with 3 columns
            fig.suptitle(set)
            x_place = 0
            y_place = 0
            ax_i = 0 #iterating through axes
            for subplot in columns_to_graph:

                if df[subplot].max() < 1:
                    range = 1 #to cover percentages
                else:
                    range = (df[subplot].max()*1.2).__ceil__() #make the upper limit on y axis slightly larger than max value

                plot = sns.boxplot(x="Assignments",
                                   ax=axes[y_place, x_place],
                            y=subplot,
                            #kind="box",
                            data=df)
                plot = sns.stripplot(x="Assignments",
                              y=subplot,
                              ax=axes[y_place, x_place],
                              alpha=0.7,
                              jitter=0.2,
                              color='k',
                              data=df)
                #plot.set(title=subplot)   #can't just plot all columns because each dataset will have some non-numeric columns
                plot.set_ylim(0,range)

                x_place += 1
                if x_place > (num_columns-1):
                    y_place += 1
                    x_place = 0






if __name__ == '__main__':
    from data_reader import dataReader
    from gui import selectFile
    from groups import assignGroups
    from name import Name
    from excel_generator import excelGenerator

    file = selectFile.byGui()
    data = dataReader(file)
    groups = assignGroups(data)
    graph = displayData(groups)
    graph.scatter_from_group()
    out_filename = Name.outputFile(file)
    excelWkst = excelGenerator(groups)
    #excelWkst.save(out_filename)
    #base = importr("base")
    #anticlust = importr("anticlust")
