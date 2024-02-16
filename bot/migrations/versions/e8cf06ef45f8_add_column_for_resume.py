"""add column for resume

Revision ID: e8cf06ef45f8
Revises: f2fddb7aa289
Create Date: 2024-02-16 16:46:30.414438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8cf06ef45f8'
down_revision: Union[str, None] = 'f2fddb7aa289'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('resume', sa.Column("image_path", sa.String))


def downgrade() -> None:
    op.drop_column('resume', 'image_path')
