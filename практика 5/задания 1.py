def claculate_tax() :
    "Рассчитывает подоходный налог и сумму дохода после его вычета."

income = float(input("Введите годовой доход : "))
tax_rate = 0.13
tax = income * tax_rate
net_income = income - tax

print(f"Общая сумма дохода: {income:,.2f} руб.")
print(f"Сумма рассчитанного налога: {tax:,.2f}руб.")
print(f"Сумма на руки после вычате налога: {net_income:,.2f}руб.")

claculate_tax()