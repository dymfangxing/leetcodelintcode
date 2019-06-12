#coding=utf-8
"""
其实就是彩虹排序
"""
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        #pass colors array, 
        #color region: color_from, color_to, 
        #to-be ordered region: index_from, index_to
        self.quickSort(colors, 1, k, 0, len(colors) - 1)

    def quickSort(self, colors, color_from, color_to, index_from, index_to):
        if color_from == color_to or index_from == index_to:
            return

        current_color = (color_from + color_to)//2
        left, right = index_from, index_to

        while left <= right:
            while left <= right and colors[left] <= current_color:
                left += 1
            while left <= right and colors[right] > current_color:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
        
        self.quickSort(colors, color_from, current_color, index_from, right)
        self.quickSort(colors, current_color + 1, color_to, left, index_to)

    #solu 2: pure quick select. only loop k times. easier to understand ...
    def sortColors2(self, colors, k):
        # write your code here
        if colors is None or k is None:
            return -1

        if len(colors) == 0 or k == 0:
            return []

        for i in range(1, k + 1):
            self.quickSelect(colors, 0, len(colors) - 1, i)

        return colors

    def quickSelect(self, colors, start, end, target):
        while start <= end:
            while start <= end and colors[start] <= target:
                start += 1
            while start <= end and colors[end] > target:
                end -= 1
            if start <= end:
                colors[start], colors[end] = colors[end], colors[start]
                start += 1
                end -= 1

#solu 3
"""
这种算法的思想类似与quickSort与mergeSort结合，quickSort的思想在于partition进行分割，
mergeSort的思想在于直接取中间（这里表现为取中间大小的数），分为左右两个相等长度的部分。

区别在于partition的判定条件变为了中间大小的元素而不是中间位置的元素，因此等号的取值可以只去一边也不会有影响。

rainbowSort实现的是将colors数组的索引范围start到end位置排序，排序的大小范围是colorFrom到coloTo.

即：每次把 < midColor的数放到左边；> midColor的数放到右边
然后 [start,left]就是都 < midColor的数;
[right, end]就是都 > midColor的数
"""
class Solution:
    def sortColors2(self, colors, k):
        if colors is None or k is None or k < 0:
            return -1

        if len(colors) == 0:
            return []
        
        start, end = 0, len(colors) - 1

        self.rainbowSort(colors, start, end, 1, k)

    def rainbowSort(self, colors, start, end, colorFrom, colorTo):
        if colorFrom == colorTo:
            return

        if start >= end:
            return

        midColor = (colorFrom + colorTo)//2
        left,right = start, end

        while left <= right:
            while left <= right and colors[left] <= midColor:
                left += 1
            while left <= right and colors[right] > midColor:
                right -= 1
            if left <= right:
                colors[left],  colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbowSort(colors, start, left, colorFrom, midColor)
        self.rainbowSort(colors, right, end, midColor + 1, colorTo)

#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = Solution()
    #print(solu.middleNode(a, b, n))
    colors = [3, 2, 2, 1, 4]
    k = 4
    solu.sortColors2(colors, k)
    print(colors)

