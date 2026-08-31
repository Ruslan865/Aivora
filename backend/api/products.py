from flask import Blueprint, request, jsonify
from database import db
from models.product import Product

products_bp = Blueprint("products", __name__, url_prefix="/api/products")


# GET /api/products
# Bütün aktiv məhsulları göstərir
@products_bp.route("", methods=["GET"])
def get_products():
    products = Product.query.filter_by(status="active").all()

    return jsonify({
        "count": len(products),
        "products": [product.to_dict() for product in products]
    }), 200


# GET /api/products/<id>
# Konkret məhsulu göstərir
@products_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify({
        "product": product.to_dict()
    }), 200


# GET /api/products/search?q=...
# Məhsul axtarışı
@products_bp.route("/search", methods=["GET"])
def search_products():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify({
            "error": "Search query is required"
        }), 400

    products = Product.query.filter(
        Product.status == "active",
        Product.title.ilike(f"%{query}%")
    ).all()

    return jsonify({
        "count": len(products),
        "query": query,
        "products": [product.to_dict() for product in products]
    }), 200


# GET /api/products/supplier/<supplier_id>
# Müəyyən supplier-in məhsulları
@products_bp.route("/supplier/<int:supplier_id>", methods=["GET"])
def get_supplier_products(supplier_id):
    products = Product.query.filter_by(
        supplier_id=supplier_id,
        status="active"
    ).all()

    return jsonify({
        "count": len(products),
        "supplier_id": supplier_id,
        "products": [product.to_dict() for product in products]
    }), 200
