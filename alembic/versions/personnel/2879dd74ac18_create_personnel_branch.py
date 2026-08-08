"""create personnel branch

Revision ID: 2879dd74ac18
Revises:
Create Date: 2026-06-19 07:59:51.755831

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "2879dd74ac18"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = ("personnel",)
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
