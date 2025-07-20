import turtle
t = turtle

# radius = t.numinput('Требуются данные', 'Введите радиус окружности от 10 - 200', default=50, minval=10, maxval=200)
# t.circle(radius)


name = t.numinput('Требуются данные', 'Имя')
print(name)
t.write(name)


turtle.done()