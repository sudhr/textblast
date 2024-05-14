"""Add converstion table

Revision ID: feab36c7c633
Revises: c5e798fe7a03
Create Date: 2024-05-14 20:17:01.437243+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "feab36c7c633"
down_revision: Union[str, None] = "c5e798fe7a03"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "converstion",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=False),
        sa.Column("source", sa.String(length=32), nullable=False),
        sa.Column("message", sa.String(length=255), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
    )
    op.create_index(
        op.f("ix_converstion_user_id"), "converstion", ["user_id"], unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f("ix_converstion_user_id"), table_name="converstion")
    op.drop_table("converstion")
