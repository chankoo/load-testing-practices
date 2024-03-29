"""Initial migration

Revision ID: 9fcb39f31c80
Revises: 
Create Date: 2023-12-30 05:23:51.732819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fcb39f31c80'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_url',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('short_id', sa.CHAR(length=6), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_short_url_short_id'), 'short_url', ['short_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_short_url_short_id'), table_name='short_url')
    op.drop_table('short_url')
    # ### end Alembic commands ###
