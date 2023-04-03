import random

# 1 haneli 5 random sayılar
numbers = [random.randint(1,9) for i in range(5)]

# 2 haneli on'un katları olan sayı
numbers2 = [random.randint(1,9)*10 for i in range(1)]
numbers=numbers+numbers2

# Hedef sayıyı 
target_number = random.randint(100, 999)

# Tüm işlemler için fonksiyon 
def calculate(numbers, target_number):
    operators = ['+', '-', '*', '/']
    results = []
    for i in range(5):
        for j in range(5):
            if i != j:
                for k in range(4):
                    if k == 3 and numbers[j] == 0:
                        continue
                    expression = str(numbers[i]) + operators[k] + str(numbers[j])
                    try:
                        result = eval(expression)
                        if result == target_number:
                            return target_number, expression
                        results.append((result, expression))
                    except ZeroDivisionError:
                        continue
    for i in range(len(results)):
        for j in range(i, len(results)):
            if i != j:
                for k in range(4):
                    if k == 3 and results[j][0] == 0:
                        continue
                    expression = results[i][1] + operators[k] + results[j][1]
                    try:
                        result = eval(expression)
                        if result == target_number:
                            return target_number, expression
                        results.append((result, expression))
                    except ZeroDivisionError:
                        continue
    closest_result = min(results, key=lambda x: abs(x[0]-target_number))
    return closest_result[0], closest_result[1]

# Sonuçları hesaplamak
result, expression = calculate(numbers, target_number)

# Sonuçları yazdırmak
print("rastgele sayılar: ", numbers)
print("hedef: ", target_number)
print("işlem: ", expression)
print("sonuç: ", result)
