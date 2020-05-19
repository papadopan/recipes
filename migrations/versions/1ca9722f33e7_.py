"""empty message

Revision ID: 1ca9722f33e7
Revises: df9c1c09d634
Create Date: 2020-05-16 21:35:24.453790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ca9722f33e7'
down_revision = 'df9c1c09d634'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Recipe_category_id_fkey', 'Recipe', type_='foreignkey')
    op.drop_column('Recipe', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Recipe_category_id_fkey', 'Recipe', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###