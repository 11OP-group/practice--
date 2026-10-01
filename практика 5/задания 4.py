def calculate_rectangle_area(width, height):
    "Вычисляет площадь прямоугольник."
    return width * height

def calculate_circle_area(radius):
    "Вычислят площадь круга."
    return 3.14 * radius ** 2

width = float(input("Введите ширину прямоугольника:"))
height = float(input("Введите высоту прямоугольника:"))

rectangle_area = calculate_rectangle_area(width, height)
print(f"Площадь прямоугольника:{rectangle_area:.2f}")

radius = float(input("Введите радиус круга:"))
circle_area = calculate_circle_area(radius)
print(f"Площадь круга:{circle_area:.2f}")