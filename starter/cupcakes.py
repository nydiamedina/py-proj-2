class Cupcake:
    size = "regular"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for arg in args:
            self.sprinkles.append(arg)

    def calculate_price(self, quantity):
        return quantity * self.price


class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []


if __name__ == '__main__':
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

    my_favorite_mini_cupcake = Mini(
        "Mini Banana Chocolate Cupcake",
        2.49,
        "Banana",
        "Chocolate Buttercream"
    )

    print(my_favorite_mini_cupcake.name)
    print(my_favorite_mini_cupcake.price)
    print(my_favorite_mini_cupcake.size)
