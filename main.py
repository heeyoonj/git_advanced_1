from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
"""
Determines if a number is even and return an even list.
Args:
int_list: A list of integer.
Returns:
A list of even integers.
"""
# TODO: Implement even_list
	return [num for num in int_list if num % 2 == 0]

# Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
"""
Computes the sum of the squares of all even numbers in a lis
Args:
even_int_list: A list of even integers.
Returns:
The sum of the squares of all even numbers in the list.
"""
# TODO: Implement sum_of_squares_of_even
	return sum(num ** 2 for num in even_int_list if num % 2 == 0)

# Main function
def main():
	input_list = list(map(int, input("Input: ").strip().split()))
	even_numbers = even_list(input_list)
	sum_squares_even = sum_of_squares_of_even(even_numbers)
	print(f"Output: {sum_squares_even}")

# Boilerplate code
if __name__ == "__main__":
main()
