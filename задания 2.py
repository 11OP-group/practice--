my_list = [1, 2, 3]
print(my_list)
my_list[0] = 100
print(my_list)

my_tuple = (1, 2, 3)
print(my_tuple)
my_list[0] = 100
print(my_tuple) # картредж не изменился потомучто tuple нельзя изменить после создания

my_string = "cat"
print(my_string)
my_string[0] = 'b'
print(my_string) # происходит ошибка из за того что my_string = "cat" отсутствуют круглые или квадратные скобки что делает my_string = "cat" не списком а скорее переменной