from src.gen_functions import distance
import argparse
import numpy as np

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-x', '--x',
                    default=3,
                    help='first coordinate')
    ap.add_argument('-y', '--y',
                    default=1,
                    help='second coordinate')
    args = vars(ap.parse_args())

    x = np.array(args['x'])
    y = np.array(args['y'])
    result = distance(x, y)
    print('Distance: ', result)

if __name__ == '__main__':
    main()
