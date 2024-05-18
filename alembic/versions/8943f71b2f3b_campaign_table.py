"""Campaign Table

Revision ID: 8943f71b2f3b
Revises: 500f3c78e940
Create Date: 2024-05-18 16:38:06.105596+00:00

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8943f71b2f3b"
down_revision: Union[str, None] = "500f3c78e940"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "campaign",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("start_date", sa.DateTime(), nullable=False),
        sa.Column("end_date", sa.DateTime(), nullable=False),
    )
    op.create_table(
        "campaign_user",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=False),
        sa.Column(
            "campaign_id", sa.Integer(), sa.ForeignKey("campaign.id"), nullable=False
        ),
    )
    op.create_index(
        "ix_campaign_campaign_user",
        "campaign_user",
        ["user_id", "campaign_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_campaign_campaign_user", table_name="campaign_user")
    op.drop_table("campaign_user")
    op.drop_table("campaign")
