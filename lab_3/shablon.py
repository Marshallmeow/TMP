from abc import ABC, abstractmethod

class Algorithm(ABC):
    def template_method(self):
        self.make_food()
        self.first_step()
        self.second_step()
        self.third_step()
        self.done_food()
        self.printer()

    def make_food(self):
        print("Приготовить фастфуд")

    @abstractmethod
    def first_step(self):
        pass

    @abstractmethod
    def second_step(self):
        pass
    @abstractmethod
    def third_step(self):
        pass

    def done_food(self):
        print("Фастфуд готов!")

    def printer(self):
        n=50
        print("*" * n) 

class part:
    def doublebulk(self):
        print("Положить две булки")
    def onebulk(self):
        print("Положить одну булку")
    def meat(self):
        print("Положить мясную котлету")
    def vegetables(self):
        print("Положить листья салата")
    def sasuage(self):
        print("Положить сосиску")
    def ketchunes(self):
        print("Добавить майонез и кетчуп")
    def kolbasa(self):
        print("Положить колбасу")
class burger(Algorithm):
    def first_step(self):
        make = part()
        make.doublebulk()
    def second_step(self):
        make = part()
        make.vegetables
    def third_step(self):
        make = part()
        make.meat()
    def done_food(self):
        print("Бургер готов!")
class hotdog(Algorithm):
    def first_step(self):
        make = part()
        make.doublebulk()
    def second_step(self):
        make = part()
        make.ketchunes()
    def third_step(self):
        make = part()
        make.sasuage()
    def done_food(self):
        print("Хот-дог готов!")
class buter(Algorithm):
    def first_step(self):
        make = part()
        make.onebulk()
    def second_step(self):
        make = part()
        make.ketchunes
    def third_step(self):
        make = part()
        make.kolbasa()
    def done_food(self):
        print("Бутерброд готов!")

print ("Make a burger")
burg = burger()
burg.template_method()


print ("Make a hot dog")
hot = hotdog()
hot.template_method()

print ("Make a buter")
but = buter()
but.template_method()

