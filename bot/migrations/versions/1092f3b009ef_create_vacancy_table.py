"""create vacancy table

Revision ID: 1092f3b009ef
Revises: e8cf06ef45f8
Create Date: 2024-02-22 08:23:53.696257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1092f3b009ef'
down_revision: Union[str, None] = 'e8cf06ef45f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'vacancy',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('user_id', sa.Integer, index=True),
        sa.Column('company_name', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('location', sa.String),
        sa.Column('salary', sa.Float(precision=2)),
        sa.Column('contacts', sa.String),
        sa.Column('image_path', sa.String)
    )


def downgrade() -> None:
    op.drop_table('vacancy')
