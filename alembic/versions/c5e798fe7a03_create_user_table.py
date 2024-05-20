"""Create user table

Revision ID: c5e798fe7a03
Revises:
Create Date: 2024-05-14 20:13:14.287004+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c5e798fe7a03"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("fname", sa.String(length=64), nullable=False),
        sa.Column("lname", sa.String(length=64), nullable=True),
        sa.Column("phone", sa.String(length=11), nullable=False),
    )
    op.create_index(op.f("ix_user_phone"), "user", ["phone"], unique=True)


def downgrade() -> None:
    op.drop_index(op.f("ix_user_phone"), table_name="user")
    op.drop_table("user")
