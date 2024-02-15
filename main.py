from flask import Flask, request, jsonify
import csv
import random

flower_data = []
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        flower_data.append(row)

app = Flask(__name__)

@app.route("/")
def home():
    return "home"
    
@app.route("/get-flower")
def get_all_flower():
    return jsonify(flower_data), 200

@app.route("/get-flower/random")
def get_one_random_flower():
    return jsonify(random.choice(flower_data)), 200

@app.route("/get-flower/random=<int:number_of_random>")
def get_n_random_flower(number_of_random):
    if number_of_random <= len(flower_data):
        return jsonify(random.sample(flower_data, number_of_random)), 200
    else:
        return jsonify({"error": "sample too large"}), 404

@app.route("/get-flower/id=<int:flower_id>")
def get_flower_by_id(flower_id):
    if flower_id < len(flower_data):
        return jsonify(flower_data[flower_id]), 200
    else:
        return jsonify({"error": "Not found"}), 404
    
@app.route("/get-flower/flower=<string:flower_name>")
def get_flower_by_name(flower_name):
    return_list = []
    for flower in flower_data:
        if flower_name.lower() in flower['flower_name'] :
            return_list.append(flower)
    if return_list:
        return jsonify(return_list), 200
    else:
        return jsonify({"error": "Not found"}), 404
    
@app.route("/get-flower/meaning=<flower_meaning>")
def get_flower_by_meaning(flower_meaning):
    return_list = []
    for flower in flower_data:
        if flower_meaning.lower() in flower['meaning']:
            return_list.append(flower)
    if return_list:
        return jsonify(return_list), 200
    else:
        return jsonify({"error": "Not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)
