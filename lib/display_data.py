"""For visualizing pandas dataframes
   This instance is for the GroupAlign script.  Will use settings from GroupAlign to make a series of subplots
   of each of the values of interest after the samples have been assigned to groups."""

#TODO: address conflict between tkinter and matplotlib - currently plt.show() redraws the askopenfilename window

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.use("gtk3cairo")

class displayData:

    def __init__(self, data):
        self.data = data
    def scatter_from_group(self):
        """Assumes that the input is a group object from the group module, potentially with multiple entries"""
        graph_data = self.data.df_assignment_merge
        columns_to_graph = self.data.graph
        for set in graph_data.keys():
            df = graph_data[set]
            if "Assignments_new" in df.columns:
                df.rename(columns={"Assignments_new": "Assignments"}, inplace=True)
            sns.set_theme(style="ticks", color_codes=True)
            num_columns = 3
            num_rows = (len(columns_to_graph)/num_columns).__ceil__() #rows*columns must be >= number of subplots
            fig, axes = plt.subplots(num_rows,
                                     num_columns,
                                     figsize=(15, 8),
                                     sharey=False) #syntax note: (2,3) is 2 rows with 3 columns
                                                   # sharey = share y axis range
            fig.suptitle(set)


            x_place = 0
            y_place = 0
            ax_i = 0 #iterating through axes
            for subplot in columns_to_graph:

                if df[subplot].max() < 1:
                    range = 1 #to cover percentages
                else:
                    range = (df[subplot].max()*1.2).__ceil__() #make the upper limit on y axis slightly larger than max value
                if num_rows > 1:
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
                    # set x axis to be diagonal
                    plt.setp(plot.get_xticklabels(), rotation=15)

                    #alternative to the doubling of entire graphing section
                    #if num_rows is <1 then an error will emerge if there is a y coordinate within subplots
                    #still needs to be tested
                    #if num_rows > 1:
                    #    places = [y_place, x_place]
                    #else:
                    #    places = [x_place]
                    # ax=axes[*places]  #the * before a variable tells python to unpack it as arguments, must be iterable


                else:
                    plot = sns.boxplot(x="Assignments",
                                       ax=axes[x_place],
                                y=subplot,
                                #kind="box",
                                data=df)
                    plot = sns.stripplot(x="Assignments",
                                  y=subplot,
                                  ax=axes[x_place],
                                  alpha=0.7,
                                  jitter=0.2,
                                  color='k',
                                  data=df)
                    #plot.set(title=subplot)   #can't just plot all columns because each dataset will have some non-numeric columns
                    plt.setp(plot.get_xticklabels(), rotation=15)
                    plot.set_ylim(0,range)
                    # set x axis to be diagonal



                x_place += 1
                if x_place > (num_columns-1):
                    y_place += 1
                    x_place = 0

        plt.show()






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
    excelWkst.save(out_filename)
    #base = importr("base")
    #anticlust = importr("anticlust")
