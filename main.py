#! /usr/bin/env python3.9

""" Sorts baseline data into predefined groups so that differences in mean and standard deviation are minimized.
    It is originally designed for scientific purposes when a group is measured at baseline and again after an
    intervention, with the goal of making the baseline measures as similar as possible between groups."""


#builtin imports
import sys
#third party imports

#custom
from lib import GroupAlign
from lib import Options

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = Options()
    opts, args = options.parse(sys.argv[1:])

    groups = GroupAlign(options)
    groups.processData()




