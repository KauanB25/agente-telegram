"""tabela de historico de chat

Revision ID: 05c82d02b05d
Revises: e21be2965988
Create Date: 2026-03-18 20:43:59.400260

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision: str = '05c82d02b05d'
down_revision: Union[str, Sequence[str], None] = 'e21be2965988'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users_history',
    sa.Column('id', sa.Integer(), sa.Identity(always=True), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False, unique=True),
    sa.Column('history', JSONB(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['id_user'], ['users_telegram.id_telegram'], ),
    sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users_history')
