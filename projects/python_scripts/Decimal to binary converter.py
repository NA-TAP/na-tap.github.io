def get_powers_of_2(number):
    powers = []
    power = 1
    while power <= number:
        powers.insert(0, power)
        power *= 2
    return powers

def subtract_list(number, list):
    new_list = []
    i = 0
    while number > 0 and i < len(list):
        new_number = list[i]
        if new_number <= number:
            new_list.append(1)
            number -= new_number    
        else:  
            new_list.append(0)
        i += 1
    return new_list

number = int(input("Enter a number: "))
list = get_powers_of_2(number)
ans = subtract_list(number, list)
5
print('List or string mode?')
mode = input('l or s').upper()
if mode == 'L':
    print(ans)
else:
    print(''.join(map(str, ans)))
