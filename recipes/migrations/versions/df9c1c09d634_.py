"""empty message

Revision ID: df9c1c09d634
Revises: 8c767813f419
Create Date: 2020-05-16 21:20:05.464315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df9c1c09d634'
down_revision = '8c767813f419'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Recipe', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Recipe', type_='foreignkey')
    op.drop_column('Recipe', 'category_id')
    # ### end Alembic commands ###
