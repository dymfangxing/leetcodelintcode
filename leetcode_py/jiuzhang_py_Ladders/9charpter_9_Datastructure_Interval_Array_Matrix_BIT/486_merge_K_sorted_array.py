import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if not arrays:
            return
        """
        size = sum(len(arr) for arr in arrays)
        if size == 0:
            return []
        """
        heap = []
        results = []

        for index, array in enumerate(arrays):
            if len(array) == 0:
                continue

            heapq.heappush(heap, (array[0], index, 0))

        while len(heap) > 0:
            val, x, x_index = heapq.heappop(heap)
            results.append(val)

            if x_index + 1 < len(arrays[x]):
                heapq.heappush(heap, (arrays[x][x_index + 1], \
                               x, x_index + 1))

        return results