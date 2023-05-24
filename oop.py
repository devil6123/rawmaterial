# ##############classes in python============
import csv


class Item:
    all = []
    pay_rate = 0.6
    # constructor is automatically called as sooon as instance is being created

    def __init__(self, name: str, quantity: int, price: int):

        # using for validation
        assert price >= 0, f"peice must be greater than or eqaul to zero"
        assert quantity >= 0, f"quantity must be greater than or equal to zero"
        assert len(name) >= 5, f"name must have atleast 5 characters"

        self.name = name
        self.quantity = quantity
        self.price = price
        # actions to execute
        Item.all.append(self)

    def apply_dicount(self):
        self.price = self.price*self.pay_rate

    def calculate_item_price(self):  # methods (inside a class)
        return self.quantity*self.price

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                quantity=float(item.get("quantity")),
                price=float(item.get("price"))
            )

    @staticmethod
    def is_integer(num): 
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            False

    def __repr__(self) -> str:  # string representation of an object
        return f"Item('{self.name}','{self.quantity}','{self.price}')"


Item.instantiate_from_csv()
print(Item.all)


# for instance in Item.all:
#     print(instance.name)


# print(Item.__dict__)  # it returns all the attributes belonging to class level
# print(item1.__dict__) # it return all the attributes belong to the instance level


# # print(f"item name is {item1.name} and tatal price is {item1.calculate_item_price()}")
# # print(f"item name is {item2.name} and tatal price is {item2.calculate_item_price()}")


# class Data:
#     def __init__(self,name,number) :
#         self.name=name
#         self.number=number
#     def print_data(self):
#         print(f"hello my name is {self.name}  and my number is {self.number}")

# data=Data("babar",1234567)
# data.print_data()


# weight converter programm

weight=float(input("Enter your weitght"))
unit=input(("kilograms or pounds (K or L)"))

if unit=="K":
    weight=weight*2.205
    unit="Lbs"
elif unit=="L":
    weight=weight/2.205
    unit="Kgs"
else:
    print(f"{unit} unit is noe valid")

print(f"your new weight is {weight}{unit}")
