from src.gen_functions import string_counter
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-li', '--list',
                    default=['Emanuel', 'Diogo', 'Silvia', 'Andre', 'Antonio', 'Diogo', 'Laura', 'Lu'],
                    help='search list')
    ap.add_argument('-s', '--searched_string',
                    default='Diogo',
                    help='string that will be searched in the list')
    args = vars(ap.parse_args())

    list = np.array(args['list'])
    s = args['searched_string']
    result = string_counter(list, s)
    print('Frequency of occurrence: ', result)

if __name__ == '__main__':
    main()