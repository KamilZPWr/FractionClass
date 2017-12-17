# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 10:28:28 2017

@author: Kamil
"""

import fraction as f

f1 = f.Fraction(2,4)
f1.printFraction

f2 = f.Fraction(-4,5)
f1.printFraction

print('suma: ',f1 + f2)
print('roznica: ',f1 - f2)
print('ilozyn: ',f1*f2)
print('iloraz: ',f1/f2)
print(f1.compare(f2))