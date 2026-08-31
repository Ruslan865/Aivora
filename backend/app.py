from flask import Flask, jsonify

from database import db
from models.supplier import Supplier
from models.product import Product
from models.order import Order
from api.suppliers import suppliers_bp


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///aivora.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(suppliers_bp)


@app.route("/")
def home():
    return jsonify({
        "name": "Aivora",
        "status": "online",
        "message": "Aivora AI Marketplace backend is running."
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "database": "connected"
    })


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
