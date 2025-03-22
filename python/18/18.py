import math

def poly_add(p, q):
    
    max_len = max(len(p), len(q))
    p_extended = p + [0]*(max_len - len(p))
    q_extended = q + [0]*(max_len - len(q))
    return [p_extended[i] + q_extended[i] for i in range(max_len)]

def poly_derivative(p):
    
    if len(p) <= 1:
        return [0]
    return [(i+1)*p[i+1] for i in range(len(p)-1)]

def poly_mult_x(p):
    
    return [0] + p

def get_polynomial(n, cache={}):
   
    if n in cache:
        return cache[n]
    
    if n == 0:
        cache[0] = [1]      
        return cache[0]
    elif n == 1:
        cache[1] = [0, 1]   
        return cache[1]
    else:
        Pn_minus_1 = get_polynomial(n-1, cache)
        xPn_minus_1 = poly_mult_x(Pn_minus_1)
        dPn_minus_1 = poly_derivative(Pn_minus_1)
        cache[n] = poly_add(xPn_minus_1, dPn_minus_1)
        return cache[n]

def poly_eval(p, x):
  
    result = 0
    power_of_x = 1
    for coeff in p:
        result += coeff * power_of_x
        power_of_x *= x
    return result

def nth_derivative_f(n, x):
   
    Pn = get_polynomial(n)
    return math.exp(x**2 / 2) * poly_eval(Pn, x)

def main():
    n = int(input("Введите порядок производной (n): "))
    x_val = float(input("Введите значение x: "))
    result = nth_derivative_f(n, x_val)
    print(f"{n}-я производная в точке x = {x_val} равна {result}")


main()
