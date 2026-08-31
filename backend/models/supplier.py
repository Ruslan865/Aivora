from datetime import datetime

from database import db


class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(200), nullable=False, unique=True)
    contact_name = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    website = db.Column(db.String(300))

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
            "company_name": self.company_name,
            "country": self.country,
            "email": self.email,
            "contact_name": self.contact_name,
            "phone": self.phone,
            "website": self.website,
            "verification_status": self.verification_status,
            "tracking_available": self.tracking_available,
            "processing_time_days": self.processing_time_days,
            "ai_score": self.ai_score,
            "created_at": self.created_at.isoformat()
            if self.created_at else None
        }
