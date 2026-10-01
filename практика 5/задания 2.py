def claculate_bmi():
    "Рассчитывает индекс массы тела по весу и росту."

weight , height = map(float , input("Введите вес и рост :").split())
bmi = weight / (height * height)
print(f"Ваш ИМТ : {bmi:.1f}")

claculate_bmi()