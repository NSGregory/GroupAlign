#TODO: switch from mtrap to GroupAlign based on needs

from argparse import ArgumentParser

class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'GroupAlign'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-b', '--batch', default=False, dest='batch', action='store_true', help='Batch Process all files in directory')
        self.parser.add_argument('-f', '--filename', default=None, dest='filename', action='store', help='File to be processed')
        self.parser.add_argument('-g', '--graph', default=False, dest='graph', action='store_true', help='Graph the viable groups')

    def parse(self, args = None):
        return self.parser.parse_args(args)

#testing
if __name__ == '__main__':
    import sys
    opt = Options()
    opts = opt.parse(sys.argv[1:])
    print(opts.batch)
    print(opts.filename)