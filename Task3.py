# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
lst = list(map(int, input("Enter the numbers through backspace:\n").split()))
unique_list = []
for i in lst:
    if i not in unique_list:
     unique_list.append(i)
print(f'The list of non-repeating elements in the original sequence: {unique_list}')
