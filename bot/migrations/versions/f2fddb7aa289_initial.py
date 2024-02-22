"""initial

Revision ID: f2fddb7aa289
Revises: 
Create Date: 2024-02-10 14:03:58.410283

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2fddb7aa289'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'resume',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('skills', sa.String),
        sa.Column('experience', sa.String),
        sa.Column('education', sa.String)
    )


def downgrade() -> None:
    op.drop_table("resume")
