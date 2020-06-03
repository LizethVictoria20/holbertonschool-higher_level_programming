#!/usr/bin/python3
'''[Project about inheritance]
'''


class MyList(list):
    '''[Class MyList]
    '''
    def print_sorted(self):
        '''[function that prints the list]
        '''
        print(sorted(self))
