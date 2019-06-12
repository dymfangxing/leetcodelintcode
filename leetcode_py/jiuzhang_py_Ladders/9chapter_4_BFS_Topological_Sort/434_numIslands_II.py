#coding=utf-8

"""
Hint: Union Find: 并集查找:

https://stomachache007.wordpress.com/2017/10/23/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95%E9%AB%98%E7%BA%A7%E7%8F%AD%E7%AC%94%E8%AE%B02-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8A/

1）把operators里每个点及其neighbors的father都置为这个点（union）
2）在union过程中，当本来属于不同father的点接壤时，把他们并成一个点
"""


#Definition for a point.

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        results = []
        island = set()
        self.size = 0
        self.father = {}
        for i, operator in enumerate(operators):
            print("$$$$$$$$$$$$$$$$$$$$$$$$$:  ", i)
            print("current adding island is: ", operator.x, operator.y)

            x, y = operator.x, operator.y
            """
            防止重复添加小岛：operators里有相同元素
            """
            if (x, y) in island:
                results.append(self.size)
                continue
            
            island.add((x, y))
            self.father[(x, y)] = (x, y)
            self.size += 1
            for delta_x, delta_y in DIRECTIONS:
                x_ = x + delta_x
                y_ = y + delta_y
                if (x_, y_) in island:
                    self.union((x_, y_), (x, y))
                print("in this loop: ", i)
                print("father islands is: ", self.father)
            print("after: ", i)
            print("father is: ", self.father)

            results.append(self.size)
            
        return results

    def union(self, point_a, point_b):
        """
        合并a，b两点：就是说把x,y 和x_delta和y_delta的father都置为x，y
        """
        root_a = self.find(point_a)
        root_b = self.find(point_b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size -= 1
        
    def find(self, point):
        """
        找到这个point的father，father’s father 。。。全部置为point
        """
        path = []
        while point != self.father[point]:
            path.append(point)
            point = self.father[point]
        
        for p in path:
            self.father[p] = point
            
        return point

if __name__ == '__main__':
    n = 4
    m = 5
    p1 = Point(1,1)
    p2 = Point(0,1)
    p3 = Point(3,3)
    p4 = Point(3,4)
    A = [p1, p2, p3, p4]

    result = Solution().numIslands2(n, m, A)

    print("After processing, result is: ", result)
