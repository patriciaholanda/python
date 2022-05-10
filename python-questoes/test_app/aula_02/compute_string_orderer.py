from src.gen_functions import string_orderer
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-li', '--list',
                    default=['Emanuel', 'Ricardo', 'Silvia', 'Andre', 'Antonio', 'Diogo', 'Laura', 'Lu'],
                    help='list to order')
    ap.add_argument('-asc', '--ascending',
                    default=True,
                    help='type of ordering: True (ascending) | False (descending)')
    args = vars(ap.parse_args())

    list = np.array(args['list'])
    asc = args['ascending']
    result = string_orderer(list, asc)
    print('Ordered strings: ', result)

if __name__ == '__main__':
    main()