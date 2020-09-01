# Muhammad Faraz Sohail


test_list = [1, 3, 5, 6, 3, 5, 6, 1]

new_list = []
temp = ''

print("The original list was:", test_list)

test_list.sort()

for num in test_list:
    if(temp == ''):
        new_list.append(num)
    else:
        if(temp == num):
            continue
        else:
            new_list.append(num)
    temp = num


print("The list after removing duplicates is:", new_list)
