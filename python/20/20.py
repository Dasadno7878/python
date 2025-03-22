class LongString:
    def __init__(self, s1="", s2="", s3="", s4=""):
        self.parts = [s1, s2, s3, s4]
    
    def read_long_string(self):
        print("Введите 4 части длинной строки:")
        for i in range(4):
            self.parts[i] = input(f"Часть {i+1}: ")
    
    def print_long_string(self):
        
        print(" | ".join(self.parts))
    
    def concat(self, other):
        
        return LongString(
            self.parts[0] + other.parts[0],
            self.parts[1] + other.parts[1],
            self.parts[2] + other.parts[2],
            self.parts[3] + other.parts[3]
        )
    
    def trim(self):
        
        self.parts = [part.strip() for part in self.parts]
    
    def find_substring(self, substring):
        
        joined = "".join(self.parts)
        return joined.count(substring)


def sort_long_strings(long_strings):
    
    long_strings.sort(key=lambda ls: "".join(ls.parts))


def count_substring_in_list(long_strings, substring):
    
    total_count = 0
    for ls in long_strings:
        total_count += ls.find_substring(substring)
    return total_count


def main():
    # Создадим список из нескольких LongString
    n = int(input("Сколько длинных строк ввести? "))
    arr = []
    for _ in range(n):
        ls = LongString()
        ls.read_long_string()
        ls.trim()  
        arr.append(ls)
    
   
    print("\nИсходные длинные строки:")
    for ls in arr:
        ls.print_long_string()
    sort_long_strings(arr)
    print("\nПосле сортировки:")
    for ls in arr:
        ls.print_long_string()
    substr = input("\nВведите подстроку для поиска: ")
    total = count_substring_in_list(arr, substr)
    print(f"Подстрока '{substr}' встречается во всех длинных строках суммарно {total} раз.")
    
    # Пример конкатенации первых двух элементов (если их минимум два)
    if len(arr) >= 2:
        concat_result = arr[0].concat(arr[1])
        print("\nПример конкатенации первой и второй строки:")
        concat_result.print_long_string()



main()
