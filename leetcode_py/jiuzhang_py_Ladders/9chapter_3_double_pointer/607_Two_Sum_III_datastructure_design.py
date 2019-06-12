#use double pointer.
#we could use Hash Map too.
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    A = []

    def add(self, number):
        # write your code here
        if number is None:
            return -1

        self.A.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        if len(self.A) == 0:
            return False

        self.A.sort()

        start, end = 0, len(self.A) - 1

        while start + 1 < end:
            temp_sum = self.A[start] + self.A[end]

            if temp_sum == value:
                return True
            elif temp_sum < value:
                start += 1
            else:
                end -= 1

        if self.A[start] + self.A[end] != value:
            return False
        else:
            return True


#Calculate the (a^n) % b where a, b and n are all 32bit positive integers.
if __name__ == '__main__':
    #print(strStr("a", "a"))
    solu = TwoSum()
    #print(solu.middleNode(a, b, n))
    solu.add(1)
    solu.add(3)
    solu.add(5)
    print(solu.find(4))
    print(solu.find(7))

