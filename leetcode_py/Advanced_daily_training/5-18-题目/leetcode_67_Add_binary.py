#coding=utf-8

"""
hint: two pointers points to a and b
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not a or not b:
            return -1
        
        add = 0
        result = []
        result1 = []
        
        sizeA = len(a) - 1
        sizeB = len(b) - 1
        
        for i in range(max(sizeA, sizeB), -1, -1):
            if sizeA >= 0:
                bitA = int(a[sizeA])
                sizeA -= 1
            else:
                bitA = 0
                
            if sizeB >= 0:
                bitB = int(b[sizeB])
                sizeB -= 1
            else:
                bitB = 0

            if bitA + bitB + add == 0:
                result.append(0)
                add = 0
            elif bitA + bitB + add == 1:
                result.append(1)
                add = 0  
            elif bitA + bitB + add == 2:
                result.append(0)
                add = 1
            elif bitA + bitB + add == 3:
                result.append(1)
                add = 1
                
        if add == 1:
            result.append(1)
            
        result1 = result[::-1]
        
        str1 = ''.join(str(e) for e in result1)
        
        return str1

            
            
            
            

            
            
            
            