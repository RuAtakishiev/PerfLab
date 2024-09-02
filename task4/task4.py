import re, os


def get_lacking_steps(numbers: list, min_value: int, max_value: int) -> int:
    if min_value != max_value:
        min_value_count = 0
        max_value_count = 0

        for number in numbers:
            if number == min_value:
                min_value_count += 1
            
            else:
                max_value_count += 1

        if min_value_count < max_value_count:
            return min_value_count
        
        else:
            return max_value_count
    
    else:
        return 0


def get_count_steps(numbers: int, count: int, flag: bool) -> int:
    min_value = min(numbers)
    max_value = max(numbers)

    if max_value - min_value > 1:
        if flag:
            number_index = numbers.index(min_value)
            numbers[number_index] += 1

            flag = False

        else:
            number_index = numbers.index(max_value)
            numbers[number_index] -= 1

            flag = True

        count += 1
        
        return get_count_steps(numbers, count, flag)

    else:
        lacking_steps = get_lacking_steps(numbers, min_value, max_value)

        count += lacking_steps
        return count

file_name = input()

if os.path.exists(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

        numbers = re.findall(r'\d+', content)
    
    if numbers:
        numbers = [int(i) for i in numbers]
        flag = True
        count = 0

        print(get_count_steps(numbers, count, flag))

    else:
        print("Содержимое файла не валидное")

else: 
    print("Файл не найден")
