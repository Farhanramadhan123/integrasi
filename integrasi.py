import numpy as np

def f(x):
    return 4 / (1 + x**2)

def trapezoid_integration(a, b, N):
    # Step size
    h = (b - a) / N
    
    # Calculate the sum of the function values
    sum_f = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        sum_f += f(a + i * h)
    
    # Calculate the integral
    integral = h * sum_f
    return integral

# Define the limits of integration
a = 0
b = 1

# Test the implementation for various values of N
Ns = [10, 100, 1000, 10000]

for N in Ns:
    integral_value = trapezoid_integration(a, b, N)
    print(f"Untuk N = {N}: Nilai integral = {integral_value}")
