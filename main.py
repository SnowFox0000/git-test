def main(n):
	balance = 0
	l = 1000 - 55
	for i in range(l):
		balance += n
		n += 2

	print(balance)

if __name__ == "__main__":
	n = 126
	main(n)
