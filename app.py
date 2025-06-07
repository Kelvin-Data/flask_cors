from flask import Flask, jsonify, render_template
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/api')
    def api():
        return jsonify({'data': 'Hello World'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
