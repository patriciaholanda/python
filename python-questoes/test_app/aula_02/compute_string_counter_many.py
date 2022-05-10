from src.gen_functions import string_counter_many
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-li', '--list',
                    default=['Emanuel', 'Diogo', 'Silvia', 'Andre', 'Antonio', 'Diogo', 'Silvia', 'Laura', 'Lu', 'Lu', 'Lu'],
                    help='search list')
    args = vars(ap.parse_args())

    list = np.array(args['list'])
    result = string_counter_many(list)
    print('Frequency of occurrence: ', result)

if __name__ == '__main__':
    main()