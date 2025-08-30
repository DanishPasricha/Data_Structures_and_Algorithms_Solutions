class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(board):
            arr = []
            for i in board:
                if i == ".": continue
                if i in arr: return False  
                else: arr.append(i)   
            return True

        board2 = []
        board3 = []
        
        for i in range(9):
            temp = []
            for j in range(9):
                temp.append(board[j][i])
            board2.append(temp)
            
        for x in [0,3,6]:
            for k in [0,3,6]:
                temp = []
                for i in range(x,x+3):
                    for j in range(k,k+3):
                        temp.append(board[i][j])
                board3.append(temp)

# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
# [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]

        for i in board: #simple row check
            if check(i)==False:
                return False
        for i in board2: #simple column check
            if check(i)==False:
                return False
        for i in board3: #simple sub check
            if check(i)==False:
                return False

        return True
