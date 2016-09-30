#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" lists and tuples"""

import data

BALLETS = data.BALLETS

del BALLETS[1] = 'Swan Lake'

BALLETS.append('herman schmerman')

BALLETS.extend(['don quixote', 'sylvia'])
