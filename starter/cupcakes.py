class Cupcake:
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling

    def add_sprinkles(self, *args):
        self.sprinkles = []

        for arg in args:
            self.sprinkles.append(arg)


my_favorite_cupcake = Cupcake(
    "Banana Chocolate Cupcake",
    4.99,
    "Banana",
    "Chocolate Buttercream",
    "Melted Chocolate",
)

my_favorite_cupcake.frosting = "Chocolate"
my_favorite_cupcake.filling = "Chocolate"
my_favorite_cupcake.name = "Triple Chocolate"

print(my_favorite_cupcake.frosting)
print(my_favorite_cupcake.filling)
print(my_favorite_cupcake.name)

my_favorite_cupcake.add_sprinkles(
    "Banana", "Chocolate Marshmallow", "Mocha", "Strawberry"
)

print(my_favorite_cupcake.sprinkles)
