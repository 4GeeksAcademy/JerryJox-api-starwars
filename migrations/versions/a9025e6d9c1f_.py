"""empty message

Revision ID: a9025e6d9c1f
Revises: da678c47244a
Create Date: 2023-05-29 18:27:01.978889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9025e6d9c1f'
down_revision = 'da678c47244a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cha__favs', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_cha_favs'])

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_character'])

    with op.batch_alter_table('collaboration', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_collab'])

    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_films'])

    with op.batch_alter_table('pla__favs', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_pla_favs'])

    with op.batch_alter_table('shi__favs', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_shi_favs'])

    with op.batch_alter_table('starship', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_starship'])

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id_user'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('starship', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('shi__favs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('pla__favs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('film', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('collaboration', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('character', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('cha__favs', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###