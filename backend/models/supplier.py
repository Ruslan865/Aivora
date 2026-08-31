from datetime import datetime

from database import db


class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)

    supplier_type = db.Column(
        db.String(50),
        nullable=False,
        default="company"
    )

    company_name = db.Column(db.String(200))
    country = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(200), nullable=False, unique=True)
    contact_name = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(300))

    registration_number = db.Column(db.String(100))
    tax_id = db.Column(db.String(100))
    legal_address = db.Column(db.String(500))
    business_name = db.Column(db.String(200))

    verification_status = db.Column(
        db.String(50),
        default="pending",
        nullable=False
    )

    tracking_available = db.Column(
        db.Boolean,
        default=False
    )

    processing_time_days = db.Column(db.Integer)

    ai_score = db.Column(db.Float)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_type": self.supplier_type,
            "company_name": self.company_name,
            "business_name": self.business_name,
            "country": self.country,
            "email": self.email,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "website": self.website,
            "registration_number": self.registration_number,
            "tax_id": self.tax_id,
            "legal_address": self.legal_address,
            "verification_status": self.verification_status,
            "tracking_available": self.tracking_available,
            "processing_time_days": self.processing_time_days,
            "ai_score": self.ai_score,
            "created_at": (
                self.created_at.isoformat()
                if self.created_at else None
            )
        }
