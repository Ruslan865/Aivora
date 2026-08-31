from flask import Blueprint, request, jsonify

from database import db
from models.product import Product
from models.supplier import Supplier


products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/api/products"
)


@products_bp.route("", methods=["POST"])
def create_product():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = [
        "supplier_id",
        "title",
        "price"
    ]

    for field in required_fields:
        if data.get(field) is None:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    supplier = Supplier.query.get(data["supplier_id"])

    if not supplier:
        return jsonify({
            "error": "Supplier not found"
        }), 404

    product = Product(
        supplier_id=data["supplier_id"],
        title=data["title"],
        description=data.get("description"),
        price=data["price"],
        currency=data.get("currency", "USD"),
        stock=data.get("stock", 0),
        shipping_cost=data.get("shipping_cost", 0),
        shipping_countries=data.get("shipping_countries"),
        processing_time_days=data.get(
            "processing_time_days"
        ),
        tracking_available=data.get(
            "tracking_available",
            False
        ),
        image_url=data.get("image_url"),
        status="active"
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product created successfully",
        "product": product.to_dict()
    }), 201


@products_bp.route("", methods=["GET"])
def get_products():
    products = Product.query.filter_by(
        status="active"
    ).order_by(
        Product.created_at.desc()
    ).all()

    return jsonify({
        "count": len(products),
        "products": [
            product.to_dict()
            for product in products
        ]
    })
