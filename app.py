# app.py
from flask import Flask
from routes.musicas_routes import musicas_bp

app = Flask(__name__)
app.register_blueprint(musicas_bp)

if __name__ == "__main__":
    app.run(debug=True)
