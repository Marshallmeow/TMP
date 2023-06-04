from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def do_work(self, x, y):
        pass

class Adder(BaseStrategy):
    def do_work(self, x, y):
        return x + y

class Minus(BaseStrategy):
    def do_work(self, x, y):
        return x - y

class Multiplicator(BaseStrategy):
    def do_work(self, x, y):
        return x * y

class Division(BaseStrategy):
    def do_work(self, x, y):
        return x / y

class Calculator:
    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print('Result is', self.strategy.do_work(x, y))

calc = Calculator()
calc.set_strategy(Adder())
calc.calculate(10, 20)
calc.set_strategy(Minus())
calc.calculate(10, 20)
calc.set_strategy(Multiplicator())
calc.calculate(10, 20)
calc.set_strategy(Division())
calc.calculate(10, 20)