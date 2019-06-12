DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    """
    Hint: find word in matrix, then compare it with the word in
    dict to see if it exists
    """

    def wordSearchII(self, board, words):
        # write your code here
        if not board:
            return []

        #reduce time complexity
        word_set = set(words)
        prefix_set = set()

        #hint: create a prefix set, so if prefix does not match,
        #do not have to try the rest of it
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])
        
        #hint: use set to remove duplicates
        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                self.searching(
                    board,
                    i,
                    j,
                    c,
                    word_set,
                    prefix_set,
                    set([(i, j)]),
                    results
                )

        return list(results)

    def searching(self, board, x, y, word, word_set, prefix_set, visited, results):
        if word not in prefix_set:
            return

        if word in word_set:
            results.add(word)

        for delta_x, delta_y in DIRECTIONS:
            x_ = x + delta_x
            y_ = y + delta_y

            if (x_, y_) in visited:
                continue

            if not self.isValid(board, x_, y_):
                continue

            visited.add((x_, y_))
            self.searching(
                board,
                x_,
                y_,
                word + board[x_][y_],
                word_set,
                prefix_set,
                visited,
                results 
            )
            visited.remove((x_, y_))



    def isValid(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])

if __name__ == '__main__':
    solu = Solution()
    board = [ ['d', 'o', 'a', 'f'],
               ['a', 'g', 'a', 'i'],
               ['d', 'c', 'a', 'n']
             ]

    words = ["dog", "dad", "dgdg", "can", "again"]

    result = solu.wordSearchII(board, words)
    print("result is: ", result)