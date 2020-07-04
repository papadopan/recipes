"""empty message

Revision ID: a96424263c6a
Revises: 4fc2e0283e70
Create Date: 2020-07-03 23:16:20.456969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a96424263c6a'
down_revision = '4fc2e0283e70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Recipe_cook_id_fkey', 'Recipe', type_='foreignkey')
    op.drop_column('Recipe', 'cook_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('cook_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('Recipe_cook_id_fkey', 'Recipe', 'cook', ['cook_id'], ['id'])
    # ### end Alembic commands ###