import util
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify_img', methods= ['GET', 'POST'])
def classify_img():
    image_data = request.form.get('image_data')

    response = jsonify(util.Classify_img(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python flaskserver for world leaders Image Classification")
    util.load_saved_artifacts()
    app.run(port = 3000, debug=True)
