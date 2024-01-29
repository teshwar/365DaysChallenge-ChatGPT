"""
    Day 28: Design Patterns (Part 2)
        Continue exploring design patterns, focusing on patterns like Strategy, Command, and Template Method.

--------------------------------------------------------------------------------------------------------------------        

    Strategy Design Pattern:
        PaymentStrategy is an interface defining the strategy (payment method).
        CreditCardPayment and PayPalPayment are concrete implementations of the payment strategy.

    Command Design Pattern:
        Command is an interface defining a command.
        LightOnCommand is a concrete command that turns on a light.

    Template Method Design Pattern:
        AbstractClass is an abstract class defining a template method with steps.
        ConcreteClass is a concrete implementation providing specific steps in the template method.
"""

# Strategy Design Pattern
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with credit card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount} with PayPal")

# Command Design Pattern
class Command:
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class Light:
    def turn_on(self):
        print("Light is ON")

# Template Method Design Pattern
class AbstractClass:
    def template_method(self):
        self.step_one()
        self.step_two()

    def step_one(self):
        pass

    def step_two(self):
        pass

class ConcreteClass(AbstractClass):
    def step_one(self):
        print("Step one in ConcreteClass")

    def step_two(self):
        print("Step two in ConcreteClass")

if __name__ == "__main__":
    # Strategy
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    credit_card_payment.pay(100)
    paypal_payment.pay(50)

    # Command
    light = Light()
    light_on_command = LightOnCommand(light)
    light_on_command.execute()

    # Template Method
    concrete_instance = ConcreteClass()
    concrete_instance.template_method()

