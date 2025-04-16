class DivisibleBy3And5:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def find_numbers(self):
        result = [x for x in range(self.n + 1, self.k) if x % 3 == 0 and x % 5 == 0]
        return result

# Пример использования
n = 10
k = 50
finder = DivisibleBy3And5(n, k)  # Создаем объект класса
print(finder.find_numbers())  # Вызываем метод для поиска чисел