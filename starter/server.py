from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", cupcakes=get_cupcakes("cupcakes.csv"))


@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes=get_cupcakes("cupcakes.csv"))


@app.route("/cupcake-individual/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        return render_template("individual-cupcake.html", cupcake=cupcake)
    else:
        return "Sorry! Cupcake not found."


@app.route("/orders")
def orders():
    cupcakes = get_cupcakes("orders.csv")
    cupcake_orders = set()

    for cupcake in cupcakes:
        cupcake_orders.add(
            (
                cupcake["name"],
                cupcake["price"],
                cupcakes.count(cupcake),
                sum(
                    [
                        float(cupcakes[index]["price"])
                        for index in [
                            i
                            for i, cup in enumerate(cupcakes)
                            if cup["name"] == cupcake["name"]
                        ]
                    ]
                ),
            )
        )

    return render_template("orders.html", cupcakes=cupcake_orders)


@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry! Cupcake not found."


if __name__ == "__main__":
    app.env = "development"
    app.run(debug=True, port=8000, host="localhost")
