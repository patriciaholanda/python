from src.gen_functions import distance_many
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-x', '--x',
                    default=3,
                    help='first coordinate')
    ap.add_argument('-l', '--list',
                    default=[2, 8, 9, 12],
                    help='coordinates list')
    args = vars(ap.parse_args())

    x = args['x']
    list = np.array(args['list'])
    result = distance_many(x, list)
    print('Distance: ', result)

if __name__ == '__main__':
    main()