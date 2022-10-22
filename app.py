# usage: flask run

from flask import Flask, request, send_file, render_template
import demo
import json
import random
import re

# load json files
f_plants = open('json/plants.json')
plants = json.load(f_plants)
plants = plants["plants"]

f_landforms = open('json/landforms.json')
landforms = json.load(f_landforms)

f_minerals = open('json/minerals.json')
minerals = json.load(f_minerals)

f_sea_species = open('json/sea_species.json')
sea_species = json.load(f_sea_species)

f_animals = open('json/animals.json')
animals = json.load(f_animals)

# load Flask library
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/gen')
def run_script():
    phrase = str(request.args.get('phrase'))

    if phrase is None:
        phrase = ""

    geo = random.choice(landforms)

    element = random.choice(
        ["water", "wood", "fire", "earth", "metal", "air", "wind", "sunlight", "glass", "fungus", "sponge", "laser",
         "lightning", "space", "astro", "cosmos", "lava", "smoke", "oceanic", "underwater", "deepsea", "aquatic", "ice", "snow", "frost", "gas", "fog", "mist"])

    mineral = random.choice(minerals)

    pattern = random.choice(["symmetries", "trees", "spirals", "meanders",
                            "waves", "foams", "tessellations", "cracks", "stripes"])

    plant_species = random.choice(plants)["species"]

    plant_name = random.choice(plants)["name"]

    animal_species = random.choice(["mite", "tick", "arthopod", "crustacean", "milli", "centipede", "spider", "scorpion", "pseudoscorpion", "harvestmen", "arachnid", "insect",
                                    "beetle", "butterfly", "bee", "ant", "grasshopper", "amphibian", "reptile", "frog", "toad", "salamander", "newt", "caecilian",
                                    "turtle", "tortois", "lizard", "snake", "fish", "mollusk", "shell", "cephalopod", "mammal", "primate",
                                    "bird", "parasite", "parasite host", "worm", "helminth", "plankton", "microorganism",
                                    "protozoan", "nematoad", "roundworm"])

    animal = random.choice(animals)

    sea_species1 = random.choice(sea_species)

    structure1 = random.choice(["twin city", "megacity", "megalopolis", "smart city",
                                "metro city", "garden city", "conurbation", "metropolis",
                                "municipality", "cosmopolitan city", "city state", "intermediary city",
                                "global city", "gateway city", "urban hub", "power city", "neighborhood", "town", "cityscape"])

    structure2 = random.choice(["factory", "church", "hut", "religious building",
                                "skyscraper", "palace", "pyramid", "mansion",
                                "house", "religious building", "ritual building", "shrine", "tomb", "grave", "graveyard",
                                "refuse pit", "cathedral"])

    key = "universal mystical magical place of"
    key_desc = "epic ultimate ultra elite supreme unique technological advanced futuristic next-generation archeological archetypal natural creatures living being musical architectural electrical monumental wisdom inspiration realistic imagination engineering instruments symbolism sculpture raw genius artistic energy motion emotional wild mechanical intellect"
    key_desc = key_desc.split(" ")
    random.shuffle(key_desc)
    key = key + " " + " " .join(key_desc)

    forms = [geo, element, mineral, pattern, plant_species, plant_name,
             animal_species, animal, sea_species1, structure1, structure2]
    random.shuffle(forms)

    process = "three-dimensional form 3d render painting fractal spirit"

    prompt = key + " " + " ".join(forms) + " " + phrase + " " + process

    # remove multiple spaces and remove commas
    prompt = re.sub(" +", " ", prompt).replace(",", "").lower()

    print(prompt)

    # call main func in demo.py with "prompt" arg
    demo.main({"prompt": prompt})
    return send_file("output/output.png", mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)
