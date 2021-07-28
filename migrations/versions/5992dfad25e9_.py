"""empty message

Revision ID: 5992dfad25e9
Revises: 3a373e361543
Create Date: 2021-07-28 15:59:16.782493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5992dfad25e9'
down_revision = '3a373e361543'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('photo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=False),
    sa.Column('filename', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('temp',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('slug', sa.String(length=32), nullable=False),
    sa.Column('maxtemp', sa.Integer(), nullable=False),
    sa.Column('mintemp', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temp')
    op.drop_table('photo')
    # ### end Alembic commands ###