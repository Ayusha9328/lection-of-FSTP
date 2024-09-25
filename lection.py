""" class Human:
    name = None
    age = None

human1 = Human() #это экземпляр класса (или объект)
print(human1.name, human1.age) # README (строка 84-86)

human2 = Human()
human2.name = "Ayusha"
human2.age = 30
print(human2.name, human2.age) """

class Human:
    def __init__(self, name: str, age: int) -> None: # см. пунткт 88-91
        self.name = name
        self.age = age

human1 = Human("Ayusha", 30)
print(human1.name, human1.age)

human2 = Human("Anastasia", 32)
print(human2.name, human2.age)
        