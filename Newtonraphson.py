def f(x):
    return x**3 - x - 2  # Example function

def f_prime(x):
    return 3*x**2 - 1  # Derivative

def newton_raphson(x0, tolerance=1e-6, max_iterations=100):
    print("Iter\t x_n\t\t f(x_n)\t\t Error")
    for iteration in range(1, max_iterations+1):
        fx = f(x0)
        fpx = f_prime(x0)
        
        if abs(fpx) < 1e-12:
            print("Zero derivative. No solution found.")
            return None
        
        x1 = x0 - fx / fpx  # Newton-Raphson formula
        error = abs(x1 - x0)
        
        print(f"{iteration}\t {x0:.6f}\t {fx:.6f}\t {error:.6f}")
        
        if error < tolerance:
            return x1
        
        x0 = x1

    print("Did not converge.")
    return None

# Example usage
root = newton_raphson(1.5)
if root is not None:
    print(f"\nRoot found by Newton-Raphson Method: {root:.6f}")
