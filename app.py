# Universal Prompt Formula
# usage:
# /gen?phrase=[string]

from flask import Flask, request, send_file, render_template
import demo
import json
import random
import re

# load json files
l_plants = json.load(open('json/plants.json'))["plants"]
l_landforms = json.load(open('json/landforms.json'))
l_minerals = json.load(open('json/minerals.json'))
l_rocks = json.load(open('json/rocks.json'))
l_sea_species = json.load(open('json/sea_species.json'))
l_animals = json.load(open('json/animals.json'))
l_time = json.load(open('json/time.json'))
l_elements1 = json.load(open('json/elements1.json'))
l_elements2 = json.load(open('json/elements2.json'))
l_patterns = json.load(open('json/patterns.json'))
l_animal_species = json.load(open('json/animal_species.json'))
l_structure1 = json.load(open('json/buildings_community.json'))
l_structure2 = json.load(open('json/buildings_single.json'))

# load Flask library
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/gen')
def run_script():
    phrase = str(request.args.get('phrase'))

    time = random.choice(l_time)
    land = random.choice(l_landforms)
    geo = random.choice(l_rocks)
    element1 = random.choice(l_elements1)
    element2 = random.choice(l_elements2)
    mineral = random.choice(l_minerals)
    pattern = random.choice(l_patterns)
    plant_species = random.choice(l_plants)["species"]
    plant_name = random.choice(l_plants)["name"]
    animal_species = random.choice(l_animal_species)
    animal = random.choice(l_animals)
    structure1 = random.choice(l_structure1)
    structure2 = random.choice(l_structure2)

    # 1 in 8 chance of sea species
    if random.randint(1, 8) == 8:
        sea_species = random.choice(l_sea_species)
    else:
        sea_species = ""

    # build prompt formula
    key = "universal mystical magical place of "
    key_desc = "epic ultimate ultra elite supreme unique technological mythological advanced futuristic archaeological archetypal seasonal natural creatures living being musical architectural electrical monumental color wisdom inspiration realistic imagination engineering instruments symbolism sculpture genius artistic energy motion emotional wild mechanical intellectual"
    key_desc = key_desc.split(" ")
    random.shuffle(key_desc)

    key = key + " ".join(key_desc)

    # forms
    forms = [land, geo, time, element1, element2, mineral, pattern, plant_species, plant_name,
             sea_species, animal_species, animal, structure1, structure2]
    random.shuffle(forms)

    # process
    process = "three-dimensional form 3d render painting fractal spirit"

    # build prompt
    if phrase == "":
        # formula = description + forms + process
        prompt = key + " " + " ".join(forms) + " " + process
    else:
        # phrase only
        prompt = phrase

    # remove multiple spaces and commas
    prompt = re.sub(" +", " ", prompt)
    prompt = re.sub(",+", ",", prompt)

    print(prompt)

    # call main func in demo.py with "prompt" arg
    demo.main({"prompt": prompt})
    return send_file("output/output.png", mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
