"""empty message

Revision ID: 99b56dec4c9c
Revises: bdbdb786bf4a
Create Date: 2023-05-26 18:40:27.444861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99b56dec4c9c'
down_revision = 'bdbdb786bf4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('calle', sa.String(length=120), nullable=False),
    sa.Column('numero', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('calle')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('address')
    # ### end Alembic commands ###
