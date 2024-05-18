"""create unique constraint on user.phone

Revision ID: 500f3c78e940
Revises: feab36c7c633
Create Date: 2024-05-18 00:53:20.525226+00:00

"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "500f3c78e940"
down_revision: Union[str, None] = "feab36c7c633"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(op.f("uq_user_phone"), "user", ["phone"])


def downgrade() -> None:
    op.drop_constraint(op.f("uq_user_phone"), "user", type_="unique")
