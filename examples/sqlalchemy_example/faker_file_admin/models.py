from . import db

__all__ = ("Upload",)


class Upload(db.Model):
    """Upload model."""

    __tablename__ = "upload"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64), unique=True)
    description = db.Column(db.Integer(), nullable=True)
    file = db.Column(db.Unicode(255))

    def __str__(self) -> str:
        return f"{self.name}"
