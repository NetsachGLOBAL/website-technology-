from flask import Flask, request, jsonify, render_template
import builtwith
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_technologies():
    data = request.get_json()
    url = data['url']

    # Ensure the URL starts with HTTP or HTTPS
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        technologies = builtwith.parse(url)
        return jsonify({'technologies': technologies})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
