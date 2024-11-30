from Flask import *
import urllib.parse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
