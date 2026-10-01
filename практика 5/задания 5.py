amount = int(input("Введите сумму для снятия:"))

count_5000 = amount // 5000
amount = amount % 5000

count_2000 = amount // 2000
amount = amount % 2000

count_1000 = amount // 1000
amount = amount % 1000

count_500 = amount // 500
amount = amount % 500

count_200 = amount // 200
amount = amount % 200

count_100 = amount // 100
amount = amount % 100

print(f"5000:{count_5000}")
print(f"2000:{count_2000}")
print(f"1000:{count_1000}")
print(f'500:{count_500}')
print(f"200:{count_200}")
print(f"100:{count_100}")