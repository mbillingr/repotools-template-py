""" This is a module
"""

class Number(object):
    """ This is a class
    """
    def __init__(self, nr=0):
        self.nr = nr

    def __repr__(self):
        return 'Number({})'.format(self.nr)

    def add(self, nr):
        self.nr += nr

    def mul(self, nr):
        self.nr *= nr
