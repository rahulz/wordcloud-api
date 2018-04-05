import base64
from io import StringIO, BytesIO

from flask import Flask, send_file, json
from flask import request
from flask_cors import CORS

from utils import wordcloud

app = Flask(__name__)

CORS(app)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/get_cloud/<format>', methods=['POST'])
def get_cloud(format):
    if request.method == "POST":
        text = request.json['text']
        cloud = wordcloud(text)
        img = BytesIO()
        cloud.savefig(img, dpi=300, format="svg")
        img.seek(0)
        r = {'img': "data:image/svg+xml;base64," + base64.b64encode(img.read()).decode("utf-8")}
        return json.dumps(r)
    else:
        return ""


if __name__ == '__main__':
    app.run(debug=True)
