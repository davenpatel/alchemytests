"""create personnel branch

Revision ID: 2879dd74ac18
Revises:
Create Date: 2026-06-19 07:59:51.755831

"""

from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = "2879dd74ac18"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = ("personnel",)
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
