# Task 1
# number = input("Enter a 4-digit number: ")
# reversed_number = ""
#
# for digit in number:
#     reversed_number = digit + reversed_number
#
# print("Reversed number:", reversed_number)

# Task 2
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3
#
# print("The largest number is:", largest)

# Task 3
# my_tuple = tuple(map(int, input("Enter elements of the tuple separated by spaces: ").split()))
# search_number = int(input("Enter the number to search for: "))
#
# if search_number in my_tuple:
#     index = my_tuple.index(search_number)
#     print(f"The number {search_number} is found at index {index}.")
# else:
#     print(f"The number {search_number} is not found in the tuple.")

# Task 4
# def dups(lst):
#     duplicates = []
#     for item in lst:
#         if lst.count(item) > 1 and item not in duplicates:
#             duplicates.append(item)
#     return duplicates
#
# num_elements = int(input("Enter the number of elements in the list: "))
# lst = [input(f"Enter element {i+1}: ") for i in range(num_elements)]
#
# duplicates = dups(lst)
# print("Duplicate elements are:", duplicates)

# Task 5
def cumulative_product(lst):
    cum_product = []
    product = 1
    for num in lst:
        product *= num
        cum_product.append(product)
    return cum_product

numbers = [1, 2, 3, 4]
result = cumulative_product(numbers)
print("Cumulative product:", result)


#task 3 again
# Function to search for a number in a tuple
# def search_number_in_tuple(tup, number):
#     for index in range(len(tup)):
#         if tup[index] == number:
#             return index
#     return -1  # Return -1 if the number is not found

# Main program (simplified)
# tup = (10, 20, 30, 40, 50)  # Example tuple
# num_to_search = int(input("Enter the number to search: "))
#
# index = search_number_in_tuple(tup, num_to_search)
#
# if index != -1:
#     print(f"The number {num_to_search} is found at index {index}.")
# else:
#     print(f"The number {num_to_search} is not found in the tuple.")


#task 4
# Function to find the count of duplicate elements in a list
# def dups(input_list):
#     duplicates_count = 0
#     checked = []
#     for i in input_list:
#         if input_list.count(i) > 1 and i not in checked:
#             duplicates_count += 1
#             checked.append(i)
#     return duplicates_count
#
# # Program to use the function
# n = int(input("Enter the number of elements in the list: "))
# elements = []
# for _ in range(n):
#     elements.append(int(input(f"Enter element {_ + 1}: ")))
#
# duplicate_count = dups(elements)
# print(f"{duplicate_count} elements have been duplicated in the list.")
