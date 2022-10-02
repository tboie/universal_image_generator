# usage: flask run

from flask import Flask
from flask import request
from flask import send_file
from flask import render_template
import demo
import json
import random
import re

f_plants = open('json/plants.json')
plants = json.load(f_plants)
plants = plants["plants"]

f_landforms = open('json/landforms.json')
landforms = json.load(f_landforms)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/gen')
def run_script():
    phrase = str(request.args.get('phrase'))

    if phrase is None:
        phrase = "black"

    geo = random.choice(landforms)
    element = random.choice(
        ["water", "wood", "fire", "earth", "metal", "air", "wind", "sunlight", "glass", "fungus", "sponge",
         "energy", "lightning", "space", "astro", "cosmos", "lava", "smoke", "oceanic", "underwater", "deepsea", "aquatic"])
    pattern = random.choice(["symmetries", "trees", "spirals", "meanders",
                            "waves", "foams", "tessellations", "cracks", "stripes"])
    plant_species = random.choice(plants)["species"]
    key = " universal fractal spirit"

    phrase = phrase + " " + element + " " + \
        pattern + " " + geo + " " + plant_species + key

    phrase = re.sub(" +", " ", phrase).replace(",", "").lower()

    print(phrase)

    # call main func in demo.py with "prompt" arg
    demo.main({"prompt": phrase})
    return send_file("output/output.png", mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
