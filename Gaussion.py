def gaussian_elimination(a, b):
    n = len(b)
    
    # Forward Elimination
    for i in range(n):
        # Make the diagonal element 1, swap rows if needed
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("Matrix is singular!")
        
        for j in range(i+1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= ratio * a[i][k]
            b[j] -= ratio * b[i]
    
    # Back Substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        sum_ax = sum(a[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - sum_ax) / a[i][i]
    
    return x

# Example Usage
a = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]
b = [8, -11, -3]

solution = gaussian_elimination(a, b)
print("\nSolution using Gaussian Elimination:")
for i, val in enumerate(solution):
    print(f"x{i+1} = {val:.6f}")
