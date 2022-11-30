from abc import ABC, abstractmethod
from pprint import pprint
import csv


class Cupcake(ABC):
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

    @abstractmethod
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

    def calculate_price(self, quantity):
        return quantity * self.price


class Regular(Cupcake):
    size = "regular"

    def calculate_price(self, quantity):
        return quantity * self.price


class Large(Cupcake):
    size = "large"

    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def calculate_price(self, quantity):
        return quantity * self.price


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = [
            "size",
            "name",
            "price",
            "flavor",
            "frosting",
            "sprinkles",
            "filling",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow(
                    {
                        "size": cupcake.size,
                        "name": cupcake.name,
                        "price": cupcake.price,
                        "flavor": cupcake.flavor,
                        "frosting": cupcake.frosting,
                        "filling": cupcake.filling,
                        "sprinkles": cupcake.sprinkles,
                    }
                )
            else:
                writer.writerow(
                    {
                        "size": cupcake.size,
                        "name": cupcake.name,
                        "price": cupcake.price,
                        "flavor": cupcake.flavor,
                        "frosting": cupcake.frosting,
                        "sprinkles": cupcake.sprinkles,
                    }
                )


def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = [
            "size",
            "name",
            "price",
            "flavor",
            "frosting",
            "sprinkles",
            "filling",
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if hasattr(cupcake, "filling"):
            writer.writerow(
                {
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "filling": cupcake.filling,
                    "sprinkles": cupcake.sprinkles,
                }
            )
        else:
            writer.writerow(
                {
                    "size": cupcake.size,
                    "name": cupcake.name,
                    "price": cupcake.price,
                    "flavor": cupcake.flavor,
                    "frosting": cupcake.frosting,
                    "sprinkles": cupcake.sprinkles,
                }
            )


if __name__ == "__main__":
    regular_cupcake = Regular(
        "Banana Chocolate Cupcake",
        4.99,
        "Banana",
        "Chocolate Buttercream",
        "Melted Chocolate",
    )

    regular_cupcake.add_sprinkles(
        "Banana", "Chocolate Marshmallow", "Mocha", "Strawberry"
    )

    mini_cupcake = Mini(
        "Mini Lemon Chocolate Cupcake", 2.49, "Lemon", "Chocolate Buttercream"
    )

    mini_cupcake.add_sprinkles("Lemon", "Orange", "Lime")

    large_cupcake = Large(
        "Large Banana Chocolate Cupcake",
        6.99,
        "Banana",
        "Chocolate Buttercream",
        "Caramel",
    )

    large_cupcake.add_sprinkles(
        "White Chocolate", "Peanut Butter", "Cookie", "Chocolate"
    )

    cupcake_list = [regular_cupcake, mini_cupcake, large_cupcake]

    write_new_csv("sample.csv", cupcake_list)
    read_csv("sample.csv")
