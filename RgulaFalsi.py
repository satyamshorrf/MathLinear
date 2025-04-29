def f(x):
    return x**3 - x - 2  # Example function

def regula_falsi(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        print("Invalid interval. f(a) and f(b) must have opposite signs.")
        return None

    print("Iter\t a\t\t b\t\t x\t\t f(x)\t\t Error")
    x_old = a  # To calculate error

    for iteration in range(1, max_iterations+1):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))  # Regula Falsi formula
        error = abs(x - x_old)
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {x:.6f}\t {f(x):.6f}\t {error:.6f}")

        if abs(f(x)) < tolerance:
            return x
        
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x
        
        x_old = x
    
    print("Did not converge.")
    return None

# Example usage
root = regula_falsi(1, 2)
if root is not None:
    print(f"\nRoot found by Regula Falsi Method: {root:.6f}")
