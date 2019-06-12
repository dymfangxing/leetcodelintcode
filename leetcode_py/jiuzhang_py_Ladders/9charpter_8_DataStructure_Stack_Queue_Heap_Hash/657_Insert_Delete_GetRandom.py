#coding=utf-8
"""
Hint:

1) 用一个dict和一个arr分别存数的index和val
2）主要是remove要O(1)：找到要remove的数，跟最后那个数对换，然后pop最后那个数
"""

"""
solu 1: 5_30_solu
"""
import random
import math

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.arr = []
        self.hashdict = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        """
        dict is used to store val's index
        """
        if val not in self.hashdict:
            self.arr.append(val)
            index = len(self.arr) - 1
            self.hashdict[val] = index
            return True
        return False

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.hashdict:
            return False
            
        """
        condition 1: val is the last num
        """
        """
        condition 2: val is not the last num, swap it with the last num 
                     and update arr and dict
        """
        if val == self.arr[-1]:
            self.arr.pop()
            del self.hashdict[val]
        else:
            index = self.hashdict[val]
            self.arr[index], self.arr[-1] = self.arr[-1], self.arr[index]
            self.hashdict[self.arr[index]] = index
            del self.hashdict[self.arr[-1]]
            self.arr.pop()
            
        return True
            

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        if len(self.arr) == 0:
            return False
        random_index = math.floor(random.uniform(0, 1) * len(self.arr))//1
        return self.arr[random_index]

"""
solu 2: 1st solu
"""
class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.dic = {}
        self.arr = []

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.dic:
            return False

        self.arr.append(val)
        index = len(self.arr) - 1
        self.dic[val] = index
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.dic:
            return False

        if val == self.arr[-1]:
            last = self.arr.pop()
            del self.dic[last]
            return True

        """
        把要删除的元素和最后一个元素互换，然后pop最后那个
        """
        #This is the situation where you should replace the val with last element of arr
        #Put arr's last element to this element's position, pop the last one
        arr_index = self.dic[val]
        last = self.arr.pop()
        if len(self.arr) > 0:
            self.arr[arr_index] = last

        #Remove that element in dict, update last element's new index in arr
        del self.dic[val]
        if len(self.arr) > 0:
            self.dic[last] = arr_index
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        index = math.floor(random.uniform(0, 1) * (len(self.arr))) // 1
        return self.arr[index]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
