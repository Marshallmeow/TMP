## Абстрактная фабрика

```
from abc import ABC, abstractmethod

class Legs(ABC):
 def __init__(self, object: str):
  self._object = object

 @abstractmethod
 def create(self): pass


class Cap(ABC):
 def __init__(self, object: str):
  self._object = object

 @abstractmethod
 def create(self): pass


class ModernLegs(Legs):
 def __init__(self):
  super().__init__("Викторианский")

 def create(self):
  print(f'Создана основа для кресла: {self._object}')


class ModernCap(Cap):
 def __init__(self):
  super().__init__("Викторианский")

 def create(self):
  print(f'Создана обивка кресла: {self._object}')


class VenLegs(Legs):
 def __init__(self):
  super().__init__("Лофт")

 def create(self):
  print(f'Создана основа для кресла: {self._object}')


class VenCap(Cap):
 def __init__(self):
  super().__init__("Лофт")

 def create(self):
  print(f'Создана обивка кресла: {self._object}')


class GuiAbstractTable(ABC):
 @abstractmethod
 def getLegs(self) -> Legs: pass

 @abstractmethod
 def getCap(self) -> Cap: pass


class ModernGuiFactory(GuiAbstractTable):
 def getLegs(self) -> Legs:
  return ModernLegs()

 def getCap(self) -> Cap:
  return ModernCap()


class VenGuiFactory(GuiAbstractTable):
 def getLegs(self) -> Legs:
  return VenLegs()

 def getCap(self) -> Cap:
  return VenCap()


class Application:
 def __init__(self, table: GuiAbstractTable):
  self._gui_table = table

 def create_gui(self):
  legs = self._gui_table.getLegs()
  cap = self._gui_table.getCap()
  legs.create()
  cap.create()

def create_factory(objectname: str) -> GuiAbstractTable:
 tabled = {
  "Викторианский": ModernGuiFactory,
  "Лофт": VenGuiFactory
 }
 return tabled[objectname]()


objectname = "Викторианский"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()

objectname = "Лофт"
cr = create_factory(objectname)
app = Application(cr)
app.create_gui()
```
## Строитель 

```
from abc import ABC, abstractmethod

class Product:
 dough = ["дрожжевое", "слоёное"]
 meat = ['курица', 'колбаса']
 top = ['сыр', 'оливки', 'помидорки', 'огурчики']
 souse = ["томатный", "песто"]

class pizza:
 def __init__(self, name):
  self.name = name
  self.meat = None
  self.topping = []
  self.souse = None
  self.dough = None
 def printer(self):
  print(f'название:{self.name}\n' \
        f'мясо:{self.meat}\n' \
        f'начинка:{[it for it in self.topping]}\n' \
        f'соус:{self.souse}\n' \
        f'тесто:{self.dough}\n')

class Builder(ABC):
 @abstractmethod
 def add_souce(self) -> None: pass
 @abstractmethod
 def add_meat(self) -> None: pass
 @abstractmethod
 def add_topping(self) -> None: pass
 @abstractmethod
 def prepare_dough(self) -> None: pass
 @abstractmethod
 def get_piz(self) -> pizza: pass

class Director:
 def __init__(self):
  self.builder = None
 def set_builder(self, builder: Builder):
  self.builder = builder
 def make_piz(self):
  if not self.builder:
   raise ValueError("Builder didn't set")
  self.builder.add_souce()
  self.builder.add_meat()
  self.builder.add_topping()
  self.builder.prepare_dough()

class HomePiz(Builder):
 def __init__(self):
  self.piz = pizza("Домашняя")
 def add_souce(self) -> None:
  self.piz.souse = Product.souse[0]
 def add_meat(self) -> None:
  self.piz.meat = Product.meat[1]
 def add_topping(self) -> None:
  self.piz.topping.append(Product.top[0])
  self.piz.topping.append(Product.top[1])
  self.piz.topping.append(Product.top[2])
  self.piz.topping.append(Product.top[3])
 def prepare_dough(self) -> None:
  self.piz.dough = Product.dough[0]
 def get_piz(self) -> pizza:
  return self.piz

class PestoPiz(Builder):
 def __init__(self):
  self.piz = pizza("Песто с курицей")
 def add_souce(self) -> None:
  self.piz.souse = Product.souse[1]
 def add_meat(self) -> None:
  self.piz.meat = Product.meat[0]
 def add_topping(self) -> None:
  self.piz.topping.append(Product.top[0])
  self.piz.topping.append(Product.top[1])
 def prepare_dough(self) -> None:
  self.piz.dough = Product.dough[1]
 def get_piz(self) -> pizza:
  return self.piz

director = Director()
print("Домашняя-1, Песто с курицей-2")
a=int(input())
if a==1:
 builder = HomePiz()
else:
 builder = PestoPiz()
director.set_builder(builder)
director.make_piz()
pizza = builder.get_piz()
pizza.printer()
```

## Адаптер 

```
class intTime:
 def geti(self):
  return 12345678

class strTime:
 def gets(self):
  return "87654321"

class Adapter(intTime,strTime):
 def get1(self):
  return str(self.geti())
 def get2(self):
  return int(self.gets())


work = Adapter()
intwork=intTime()
strwork=strTime()
print("результат:" + work.get1())
print(work.get2()+intwork.geti())
```

## Посредник

```
from abc import ABC, abstractmethod

class User():
 def __init__(self, med, name, st):
    self.mediator = med
    self.name = name
    self.statusmember = st

 @abstractmethod
 def send(self, msg):
  pass

 @abstractmethod
 def sendA(self, msg):
  pass

 @abstractmethod
 def sendO(self, msg):
  pass

 @abstractmethod
 def receive(self, msg):
  pass

class ChatMediator:
 def __init__(self):
  self.users = []
 def add_user(self, user):
  self.users.append(user)
 def send_message(self, msg, user):
  for u in self.users:
   if u != user:
    u.receive(msg)
 def send_messageA(self,msg,user):
  for u in self.users:
   if u != user and u.statusmember == "Administration":
    u.receive(msg)
 def send_messageO(self,msg,user):
  for u in self.users:
   if u != user and u.statusmember == "Other":
    u.receive(msg)

class ConcreteUser(User):
 def send(self, msg):
  print(self.name + ": отправил сообщение: " + msg)
  self.mediator.send_message(msg, self)
 def sendA(self, msg):
  print(self.name + ": отправил администрации: " + msg)
  self.mediator.send_messageA(msg, self)
 def sendO(self, msg):
  print(self.name + ": отправил штатным сотрудникам: " + msg)
  self.mediator.send_messageO(msg, self)
 def receive(self, msg):
  print(self.name + ": получено сообщение: " + msg)

def printl():
 print("-" * 50)

mediator = ChatMediator()
user1 = ConcreteUser(mediator, "Олег", "Administration")
user2 = ConcreteUser(mediator, "Маруся", "Administration")
user3 = ConcreteUser(mediator, "Даша", "Other")
user4 = ConcreteUser(mediator, "Глаша", "Other")
user5 = ConcreteUser(mediator, "Иван", "Other")

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)
mediator.add_user(user4)
mediator.add_user(user5)

user1.send("Привет всем")
printl()

user1.sendA("Привет Администрация")
printl()

user1.sendO("Привет ОбычныеСотрудники")
printl()

```