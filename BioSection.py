def f(x):
    return x**3 - x - 2  # Example function

def bisection_method(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)\t\t Error")
    c_old = a  # For error calculation

    for iteration in range(1, max_iterations+1):
        c = (a + b) / 2  # Bisection formula
        error = abs(c - c_old)
        
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
        
        if abs(f(c)) < tolerance or error < tolerance:
            return c
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        
        c_old = c

    print("Did not converge.")
    return None

# Example usage
root = bisection_method(1, 2)
if root is not None:
    print(f"\nRoot found by Bisection Method: {root:.6f}")
