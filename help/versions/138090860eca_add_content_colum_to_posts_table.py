"""add content colum to posts table

Revision ID: 138090860eca
Revises: def0c2ae024f
Create Date: 2021-12-13 12:32:30.903683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '138090860eca'
down_revision = 'def0c2ae024f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
