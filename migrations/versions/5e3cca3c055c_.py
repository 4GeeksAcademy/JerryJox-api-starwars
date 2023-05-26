"""empty message

Revision ID: 5e3cca3c055c
Revises: 99b56dec4c9c
Create Date: 2023-05-26 18:53:48.372966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e3cca3c055c'
down_revision = '99b56dec4c9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id_films', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('characters', sa.String(length=120), nullable=False),
    sa.Column('starships', sa.String(length=120), nullable=False),
    sa.Column('planets', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id_films'),
    sa.UniqueConstraint('characters'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('planets'),
    sa.UniqueConstraint('starships')
    )
    op.drop_table('user')
    op.drop_table('address')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('calle', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('numero', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='address_pkey'),
    sa.UniqueConstraint('calle', name='address_calle_key')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('films')
    # ### end Alembic commands ###