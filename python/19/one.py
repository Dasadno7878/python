def read_input():
    
    x = float(input("Введите x: "))
    h = float(input("Введите h: "))
    N = int(input("Введите N (целое число): "))
    return x, h, N

def print_result(name, value):
  
    print(f"{name}: {value}")
