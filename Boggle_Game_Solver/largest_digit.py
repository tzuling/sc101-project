"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	n = abs(n)
	divisor = 10
	n_max = 0

	return find_largest_digit_helper(n, divisor, n_max)


def find_largest_digit_helper(n, divisor, n_digit_max):
	if n == 0:
		return n_digit_max
	else:
		tmp = n % divisor
		n = n // divisor
		if n_digit_max < tmp:
			n_digit_max = tmp

		return find_largest_digit_helper(n, divisor, n_digit_max)


if __name__ == '__main__':
	main()
