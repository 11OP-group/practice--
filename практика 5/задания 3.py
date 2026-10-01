def convert_usd_to_rub(amount_usd):
    "Конвертирует сумму из долларов в рубли."

    rate = 95.50
    return  amount_usd * rate

amount = float(input("Введите сумму в долларах :"))
result = convert_usd_to_rub(amount)
print(f"Сумма в рублях: {result:.2f}руб.")


