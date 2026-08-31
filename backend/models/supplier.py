from flask import Blueprint, request, jsonify

from database import db
from models.supplier import Supplier


suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/api/suppliers"
)


@suppliers_bp.route("", methods=["POST"])
def create_supplier():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    required_fields = [
        "country",
        "email"
    ]

    for field in required_fields:
        if not data.get(field):
            return jsonify({
                "error": f"{field} is required"
            }), 400

    supplier_type = data.get(
        "supplier_type",
        "company"
    )

    allowed_types = [
        "company",
        "individual_seller",
        "sole_proprietor"
    ]

    if supplier_type not in allowed_types:
        return jsonify({
            "error": "Invalid supplier_type",
            "allowed_types": allowed_types
        }), 400

    # Company üçün company_name tələb olunur.
    # Individual seller və sole proprietor üçün isə
    # contact_name və ya company_name istifadə oluna bilər.
    company_name = data.get("company_name")

    if supplier_type == "company" and not company_name:
        return jsonify({
            "error": "company_name is required for company supplier"
        }), 400

    if not company_name:
        company_name = data.get("contact_name")

    if not company_name:
        return jsonify({
            "error": "company_name or contact_name is required"
        }), 400

    existing_supplier = Supplier.query.filter_by(
        email=data["email"]
    ).first()

    if existing_supplier:
        return jsonify({
            "error": "Supplier with this email already exists"
        }), 409

    supplier = Supplier(
        supplier_type=supplier_type,

        company_name=company_name,
        country=data["country"],
        email=data["email"],
        contact_name=data.get("contact_name"),
        phone=data.get("phone"),
        website=data.get("website"),

        registration_number=data.get(
            "registration_number"
        ),
        tax_id=data.get(
            "tax_id"
        ),
        legal_address=data.get(
            "legal_address"
        ),
        business_name=data.get(
            "business_name"
        ),

        verification_status=data.get(
            "verification_status",
            "pending"
        ),

        tracking_available=data.get(
            "tracking_available",
            False
        ),

        processing_time_days=data.get(
            "processing_time_days"
        ),

        ai_score=data.get(
            "ai_score"
        )
    )

    db.session.add(supplier)
    db.session.commit()

    return jsonify({
        "message": "Supplier created successfully",
        "supplier": supplier.to_dict()
    }), 201


@suppliers_bp.route("", methods=["GET"])
def get_suppliers():
    suppliers = Supplier.query.order_by(
        Supplier.created_at.desc()
    ).all()

    return jsonify({
        "count": len(suppliers),
        "suppliers": [
            supplier.to_dict()
            for supplier in suppliers
        ]
    })
