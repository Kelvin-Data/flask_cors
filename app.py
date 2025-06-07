from flask import Flask, jsonify, render_template
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Allow CORS only for your Netlify frontend
    CORS(app, resources={
        r"/api/*": {
            "origins": ["https://flask-cors.netlify.app"]
        }
    })

    @app.route('/api')
    def api():
        return jsonify({'data': 'Hello World'})

    return app
    
app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
