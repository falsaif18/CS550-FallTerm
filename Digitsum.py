def digits(n):
	if n < 10:
		return n
	else:
		return digits(n//10) + n%10

print(digits(15677))
print(digits(17947489928398))