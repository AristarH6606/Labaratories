class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        if new_radius > 0:
            self.radius = new_radius
        else:
            return 'Ошибка: радиус не может быть отрицательным'

circle = Circle(3.0)
print(f'Изначальный радиус: {circle.get_radius()}')
circle.set_radius(1.5)
print(f'Новый радиус: {circle.get_radius()}')