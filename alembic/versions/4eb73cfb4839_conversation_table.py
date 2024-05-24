"""Conversation table

Revision ID: 4eb73cfb4839
Revises: 8943f71b2f3b
Create Date: 2024-05-24 21:37:03.526303+00:00

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4eb73cfb4839"
down_revision: Union[str, None] = "8943f71b2f3b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "conversation",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("user.id"), nullable=False),
        sa.Column(
            "campaign_id", sa.Integer(), sa.ForeignKey("campaign.id"), nullable=False
        ),
        sa.Column("source", sa.String(length=32), nullable=False),
        sa.Column("message", sa.String(length=255), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
    )
    op.create_index(
        "ix_conversation_user_id",
        "conversation",
        ["user_id", "campaign_id"],
        unique=True,
    )


def downgrade() -> None:
    op.drop_index("ix_conversation_user_id", table_name="conversation")
    op.drop_table("conversation")
