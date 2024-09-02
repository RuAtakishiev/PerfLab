n, m = map(int, input().split())

circular_array = list()
numerical_path = list()


def get_first_number(circular_array: list) -> int:
    if circular_array:
        return circular_array[-1]
    
    else:
        return 1


def get_circular_array(n: int, first_number: int, circular_array: list) -> list:
    global numerical_path

    if not circular_array or first_number != 1:
        numerical_path.append(first_number)
        step = first_number

        for _ in range(m):
            circular_array.append(step)
            
            if n > step:
                step += 1
            
            else:
                step = 1            
        
        return get_circular_array(n, get_first_number(circular_array), circular_array)

    else:
        return circular_array


if n > 0 and m > 0:
    get_circular_array(n, get_first_number(circular_array), circular_array)

    print(''.join(map(str, numerical_path)))

else:
    print(0)

