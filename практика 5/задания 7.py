def calculate_fuet_cost():
    "Рассчитывает расход топлива и его стоимость."

distance = float(input("Какие расстояние (км)?"))
fuel_consumption = float(input("Сколько литров на 100 км?"))
fuel_price = float(input("Сколько стоит литр топлива?"))

total_liters = distance * (fuel_consumption / 100)
total_cost = total_liters * fuel_price

print(f"Расход топлива: {total_liters:.2f} л")
print(f"Стоимоть поездки: {total_cost:.2f} руб")

calculate_fuet_cost()
