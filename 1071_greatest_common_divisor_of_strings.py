from typing import List
from functools import *
from math import *
from test_harness.harness import harness_run
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
   
        if ( str1 + str2 ) != ( str2 + str1 ):
		
            # if str1 and str2 has no common factor, then reject			
            return ''

        else:
		
            # if str1 =\= str2, then str1[:length_by_gcd] is the answer
			
            length_by_gcd = gcd( len(str1), len(str2) )
            return str1[:length_by_gcd]

            
                
        