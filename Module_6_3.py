from random import randint


class Animal:                                           # Создаем родительский класс Animal.
    live = True                                         # Создаем атрибут live класса Animal.
    sound = None                                        # Создаем атрибут sound класса Animal.
    _DEGREE_OF_DANGER = 0                               # Создаем атрибут _DEGREE_OF_DANGER класса Animal.

    def __init__(self, speed: int):                     # Создаем конструктор класса Animal, который принмает значение скорости (speed).
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx: int, dy: int, dz: int):          # Также конструктор принимает значение координат нахождения. Т.е. создаем метод перемещения животного в пространстве.
        if self._cords[2] + dz * self.speed < 0:        # Где ставим условие, что если животное помещено глубоко в пространстве,
            print("It's too deep, I can't dive :(")     # то выводим соответствующее предложение о невозможности перемещения животного на экране.
        else:                                           # В иных случаях мы обновляем координаты по осям X, Y, Z.
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):                                # Добавляем метод текущих координат животного.
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}") # С помощью которого получаем координаты животного на экран в тот или иной момент времени.

    def attack(self):                                   # Также создаем метод определения атаки животного.
        if self._DEGREE_OF_DANGER < 5:                  # В данном случае определяем, что если отсутствует определенная степень опасности, то ставим ограничение по условию задачи
            print("Sorry, I'm peaceful :)")             # и выводим на экран соответствующую надпись.
        else:                                           # В иных случаях (степени) опасности, выводим информацию об опасности на экран.
            self._DEGREE_OF_DANGER >= 5
            print("Be careful, I'm attacking you 0_0")

    def speak(self):                                    # Создаем метод возможности воспроизведения каких-либо звуков.
        print(self.sound)                               # С последующим выводом на экран.

class Bird(Animal):                                     # Создаем дочерний класс Bird к родительскому классу Animal.
    beak = True                                         # Где добавляем необходимый атрибут (наличие клюва) по условиям задачи.

    def lay_egg(self):                                  # и добавляем метод вывода информации на экран о количестве яиц в кладке птицы.
        print(f"Here are(is) {randint(1, 4)} egggs for you") # С использованием метода randint можем задать определенный динапазон для количества яиц в кладке.

class AquaticAnimal(Animal):                            # Создаем дочерний класс AquaticAnimal к родительскому классу Animal.
    _DEGREE_OF_DANGER = 3                               # Где добавляем атрибут опасности данного вида животных.
                                                        # Это говорит нам, что происходит переопределение атрибута для данного вида животных.
    def dive_in(self, dz: int):                         # Добавляем метод для погружения животного в воду.
        self._cords[2] -= int(abs(dz) * (self.speed / 2)) # Если животное умеет погружаться в воду, то происходит изменение по оси Z.

class PoisonousAnimal(Animal):                          # Создаем дочерний класс PoisonousAnimal к родительскому классу Animal.
    _DEGREE_OF_DANGER = 8                               # Где добавляем атрибут опасности данного вида животных.
                                                        # Это говорит нам, что происходит переопределение атрибута для данного вида животных.
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):   # Создаем подкласс Duckbill к дочерним классам.
    sound = "Click-click-click"                         # В котором рассматриваем возможность воспроизведения звука.

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()