"""create upload table

Revision ID: 2695cb77cdf2
Revises: 
Create Date: 2022-12-06 23:46:09.000000

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2695cb77cdf2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "upload",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(64), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("file", sa.String(255), nullable=False),
    )


def downgrade():
    op.drop_table("upload")
