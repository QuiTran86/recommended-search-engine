from flask import Flask

from backend.api import netflix_blueprint
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])
app.register_blueprint(netflix_blueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=4000, debug=True)
