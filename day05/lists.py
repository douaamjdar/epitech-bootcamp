#task1.1
the_list = [1, 2, 3, 4, 5]
print (the_list[0])

#task1.2
print (the_list[-1])

#task1.3
the_list.append(42)
the_list.append("forty-two")
print(the_list)

#task1.4
print (the_list)
for element in the_list:
  print(element)

#task1.5
the_list.pop(-1)
print(the_list)

#task1.6
the_list.insert(0,0)
print(the_list)

#task1.7
print(the_list[1:4])

#task1.8
reversed_list = the_list.copy()
reversed_list.reverse()
print(reversed_list)

#task1.9
for number in range(11, 21):
  the_list.append(number)
print(the_list)

#task1.10
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)
print(my_first_list)

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]
print(my_first_list)

#task1.11
numbers = [1, 2, 3, 4, 5]
result = 1 
for number in numbers:
  result = result * number
print(result)

#task1.12
print([x + 10 for x in [3, 2, 6, 7, 1, 4]])

#task1.13
numbers = [8, 3, 12, 5, 1]
print(min(numbers))
print(max(numbers))

#task1.14
numbers.sort(reverse=True)
print(numbers)

#task1.15
print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

#task1.16
def rm_duplicates(elements):
    return list(set(elements))
print(rm_duplicates([1, 1, 1, 1, 2, 2, 2, 2, 2]))
print(rm_duplicates([42, '42', 42.0, 21+21, 42*10/10]))
