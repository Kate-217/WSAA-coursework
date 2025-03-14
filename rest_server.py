from flask import Flask, url_for, request, redirect, abort, render_template


app = Flask(__name__, static_url_path='', static_folder='staticpages')


#@app.route("/")  # Maps the root URL to the home() function
#def home():
#    return "Welcome to my website!"

# About
#@app.route("/about")  
#def about():
#    return render_template("about.html")


# t-shirts 
tshirt_prices = {
    "yellow": 20,
    "blue": 22,
    "red": 23
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected_color =None
    price = None
    
    if request.method == "POST":
        selected_color = request.form.get("color")
        price = tshirt_prices.get(selected_color, "Unknown")

    return render_template("index.html", selected_color=selected_color, price=price)



if __name__ == "__main__":
    app.run(debug=True)


