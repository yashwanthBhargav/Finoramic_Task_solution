class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        if len(A)== 9:
            ans=1
            c=0
            for i in range(9):
                if len(A[i])==9:
                    c=c+1
            if c == 9:
                for i in range(9):
                    arrx=[]
                    arry=[]
                    for j in range(9):
                        if A[i][j] not in arrx:
                            if A[i][j] != ".":
                                arrx.append(A[i][j])
                        else:
                            ans= 0
                        if A[j][i] not in arry:
                            if A[j][i] !=".":
                                arry.append(A[j][i])
                        else:
                            ans= 0
                        if i%3==0 and j%3==0:
                            arr=[]
                            for p in range(3):
                                for q in range(3):
                                    if A[i+p][j+q] not in arr:
                                        if A[i+p][j+q] !=".":
                                            arr.append(A[i+p][j+q])
                                    else:
                                        ans= 0
            else:
                ans=0
        else:
            ans=0
        return ans
