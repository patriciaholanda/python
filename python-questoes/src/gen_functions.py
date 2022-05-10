from math import dist
import numpy as np
import collections

def distance(x, y):
    """
    Question 01
    Calculates the Euclidean distance of two points
    input:
    x = first number integer type
    y = second number integer type
    return:
    The Euclidean distance of two points
    """
    d = np.sqrt(np.sum(np.square(x-y)))
    return d


def distance_many(x, list):
    """
    Question 02
    Calculates the Euclidean distance of many points into a array to find the nearest point of X.
    input:
    x = coordinate - integer type
    list = array containing n coordinates
    return:
    Nearest point of X
    """
    neighbor = 0
    for y in list:
        dist = distance(x, y)
        if(dist > neighbor):
            neighbor = dist
    return neighbor


def string_orderer(list, asc):
    """
    Question 03
    Sort a string list
    input:
    list = array containing n strings
    asc = boolean condition that indicates whether the ordering is ascending or descending : True | False
    return:
    List of strings ordered based on the number of elements in each string
    """
    list = sorted(list, key=len)
    if asc != True:
        list.sort(reverse=True)
    return list


def string_counter(list, string):
    """
    Question 04
    Determines number of repetitions of a specific string inside a string list.
    input:
    list = array containing n strings
    string = string that will have its frequency calculated
    return:
    Number of repetitions of a specific string inside a string list
    """
    counter = np.count_nonzero(list == string)
    return counter


def string_counter_many(list):
    """
    Question 05
    Determines the number of occurrences of all strings in a string list.
    input:
    list = array containing n strings
    return:
    Number of occurrences of all strings in a string list.
    """
    list.sort()
    return(collections.Counter(list))