RawInput = input('Введите последовательность чисел через пробел: ')
int_array = [int(i) for i in RawInput.split (' ') if i.isdigit()]
 
while True:
     try:
         num = int(input('Введите число: '))
         if num < 0 or num > 999:
             raise Exception
         break
     except ValueError:
         print('Введите вероное число')
     except Exception:
         print('В не диапазон')
 
int_array.append(num)
list.sort(int_array)
def binary_search(int_array, num, left, right):
     if left > right:
         return False
     middle = (right + left) // 2
     if int_array[middle] == num:
         return middle
     elif num < int_array[middle]:
         return binary_search(int_array, num, left, middle - 1)
     else:
         return binary_search(int_array, num, middle + 1, right)
         
print(binary_search(int_array, num, 0, len(int_array)-1))
