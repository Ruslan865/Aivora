from datetime import datetime

from database import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id"),
        nullable=False
    )

    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)

    price = db.Column(db.Float, nullable=False)
    currency = db.Column(
        db.String(10),
        default="USD",
        nullable=False
    )

    stock = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    shipping_cost = db.Column(
        db.Float,
        default=0
    )

    shipping_countries = db.Column(db.Text)

    processing_time_days = db.Column(db.Integer)

    tracking_available = db.Column(
        db.Boolean,
        default=False
    )

    image_url = db.Column(db.String(500))

    ai_score = db.Column(db.Float)

    status = db.Column(
        db.String(50),
        default="active",
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "currency": self.currency,
            "stock": self.stock,
            "shipping_cost": self.shipping_cost,
            "shipping_countries": self.shipping_countries,
            "processing_time_days": self.processing_time_days,
            "tracking_available": self.tracking_available,
            "image_url": self.image_url,
            "ai_score": self.ai_score,
            "status": self.status,
            "created_at": self.created_at.isoformat()
            if self.created_at else None
        }
