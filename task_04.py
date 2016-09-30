#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" task 4 """

def process_data (data)
    """ function to return total sum of data and the average

    Args:
        data: A list or tuple of numbers

    Returns:
        Tuple: contains sum and average of data

    example:
        >>> process_data([1, 2, 3])
            (6, 2, 0)
    """
    mysum = 0

    for mynum in data:
        mysum += mynum
    myavg = (mysum / float(len(data)))
    return (mysum, myavg)
