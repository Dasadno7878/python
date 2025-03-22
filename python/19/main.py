import one
import two
import three

def main():
    # 1. Считываем данные
    x, h, N = data_io.read_input()
    
    # 2. Обрабатываем (вычисляем y и S)
    y = data_processing.compute_y(x)
    S = data_processing.compute_sum(x, h, N)

    # 3. Выводим результаты
    data_io.print_result("Значение y", y)
    data_io.print_result("Сумма S", S)



main()
