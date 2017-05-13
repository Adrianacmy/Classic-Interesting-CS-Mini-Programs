# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    # Write your code here
    for row in A:
        if len(row) != len(A):
            return False

    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i][j] != -A[j][i]:
                return False
    return True


# Test Cases:
print(antisymmetric([[0, 1, 2],
               [-1, 0, 3],
               [-2, -3, 0]]))

print(antisymmetric([[1, 2, 5],
               [0, 1, -9],
               [0, 0, 1]]))

