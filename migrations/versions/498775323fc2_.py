"""empty message

Revision ID: 498775323fc2
Revises: f7dfce29f25b
Create Date: 2021-08-08 16:57:50.002391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '498775323fc2'
down_revision = 'f7dfce29f25b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###