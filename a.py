
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


squares = [x**2 for x in range(start, end + 1)]


even_squares = [num for num in squares if num % 2 == 0]
odd_squares = [num for num in squares if num % 2 != 0]
print("Square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
