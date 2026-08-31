from datetime import datetime

from database import db


class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)

    order_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id"),
        nullable=False
    )

    buyer_name = db.Column(
        db.String(200),
        nullable=False
    )

    buyer_email = db.Column(
        db.String(200),
        nullable=False
    )

    buyer_country = db.Column(
        db.String(100),
        nullable=False
    )

    shipping_address = db.Column(
        db.Text,
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        default=1,
        nullable=False
    )

    total_amount = db.Column(
        db.Float,
        nullable=False
    )

    currency = db.Column(
        db.String(10),
        default="USD",
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="pending",
        nullable=False
    )

    tracking_number = db.Column(
        db.String(200)
    )

    tracking_url = db.Column(
        db.String(500)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    def to_dict(self):
        return {
            "id": self.id,
            "order_number": self.order_number,
            "product_id": self.product_id,
            "supplier_id": self.supplier_id,
            "buyer_name": self.buyer_name,
            "buyer_email": self.buyer_email,
            "buyer_country": self.buyer_country,
            "quantity": self.quantity,
            "total_amount": self.total_amount,
            "currency": self.currency,
            "status": self.status,
            "tracking_number": self.tracking_number,
            "tracking_url": self.tracking_url,
            "created_at": self.created_at.isoformat()
            if self.created_at else None,
            "updated_at": self.updated_at.isoformat()
            if self.updated_at else None
        }
