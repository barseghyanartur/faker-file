import json
from decimal import Decimal
from typing import Optional, Union

from . import db

__all__ = ("Upload",)


class Upload(AbstractProduct):
    """Product model."""

    __tablename__ = "upload"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    description = db.Column(db.Integer())
    price_with_tax = db.Column(db.Unicode(6400))
    file = db.File()

    def __str__(self) -> str:
        return f"{self.name}"
