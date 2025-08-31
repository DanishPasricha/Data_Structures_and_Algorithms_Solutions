class Solution(object):
    def solveSudoku(self,board):
        R = [set() for _ in range(9)]  # Track numbers used in each ROW
        C = [set() for _ in range(9)]  # Track numbers used in each COLUMN  
        B = [set() for _ in range(9)]  # Track numbers used in each 3x3 BLOCK
        E = []                         # Store all EMPTY cell positions

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    E.append((r,c))  # Remember this empty spot
                else: #if element is not empty
                    ch=board[r][c] #update in R,C,B lists
                    R[r].add(ch) #add to row no.
                    C[c].add(ch) #add to col no.
                    B[(r//3)*3+(c//3)].add(ch) #add to block no

        
        def f(k):  # k is the index in our empty cells list E
            if k == len(E):
                return 1  # Solved! All empty cells filled
            
            r, c = E[k]           # Get current empty cell position
            b = (r//3)*3+(c//3)   # Calculate which block it's in
            
            for ch in "123456789":
                # The magic check: Is this number available?
                if ch not in R[r] and ch not in C[c] and ch not in B[b]:
                    # Place the number and update our tracking
                    board[r][c] = ch
                    R[r].add(ch)
                    C[c].add(ch) 
                    B[b].add(ch)
                    
                    # Recurse to next empty cell (hun dekh f(k) di value ja ta 1 hovegi ja ta 0, 
                    # je 1 hoyi ehda matlab apni destination yaani ke saare empty cells fill hogye, eda matlabh apna es point te 
                    # aah decision sahi aa taahi agge te saare decisions sahi hoke sahi result de rahe taa taa 1 return krde 
                    #  te je f(k+1) false hunda yaani ke 0 return krda ehda matlabh eh current decision galat aa ta fer backttack krde 
                    # undo everything at this point )
                    if f(k+1):
                        return 1
                    
                    # Backtrack: undo everything
                    board[r][c] = "."
                    R[r].remove(ch)
                    C[c].remove(ch)
                    B[b].remove(ch)
            
            return 0  # No valid number found
        f(0)
