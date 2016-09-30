#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" task 5"""

def flip_keys (to_flip):
    """ reverse the order of the inner sequence
    Args:
        to_flip (list): list that has nested, immutable sequence inside

    Returns:
        list: the original list with its inner elements reversed

    Example:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
        """
    num = 0
    for seq in to_flip:
        seq[::-1]
        num += 1
        return to_flip
    
