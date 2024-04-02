# GroupAlign

In development.

Use case: Assigning samples to groups so that baselines match

Pulls data from excel spreadsheet and then uses the anticlust R package to assign samples into groups.  Requires installation both R and the anticlust R package separate from the python script.

Will graph user assigned features of the samples so that the assigment can be visually evaluated.

display_data.py essentially performs all the intended functions of this project

You will need to set the file path to your R package in the groups.py script.  For example:
os.environ['R_HOME'] = '/Library/Frameworks/R.framework/Resources'
