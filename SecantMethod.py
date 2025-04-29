def f(x):
    return x**3 - x - 2  # Example function

def secant_method(x0, x1, tolerance=1e-6, max_iterations=100):
    print("Iter\t x_n-1\t\t x_n\t\t x_n+1\t\t f(x_n+1)\t Error")
    for iteration in range(1, max_iterations+1):
        if abs(f(x1) - f(x0)) < 1e-12:
            print("Denominator too small.")
            return None
        
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))  # Secant formula
        error = abs(x2 - x1)
        
        print(f"{iteration}\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {f(x2):.6f}\t {error:.6f}")
        
        if error < tolerance:
            return x2
        
        x0, x1 = x1, x2

    print("Did not converge.")
    return None

# Example usage
root = secant_method(1, 2)
if root is not None:
    print(f"\nRoot found by Secant Method: {root:.6f}")
