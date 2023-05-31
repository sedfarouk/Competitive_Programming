# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_earnings(shoe_sizes, customers):
    earnings = 0
    for customer in customers:
        size, price = customer
        if size in shoe_sizes:
            earnings += price
            shoe_sizes.remove(size)
    return earnings

num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

customers = []
for _ in range(num_customers):
    customer = tuple(map(int, input().split()))
    customers.append(customer)

earnings = calculate_earnings(shoe_sizes, customers)
print(earnings)
