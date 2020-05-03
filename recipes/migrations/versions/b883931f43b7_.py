"""empty message

Revision ID: b883931f43b7
Revises: f13c21c56050
Create Date: 2020-05-03 13:56:21.264381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b883931f43b7'
down_revision = 'f13c21c56050'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Recipe', sa.Column('image_file', sa.LargeBinary(), nullable=True))
    op.add_column('Recipe', sa.Column('image_name', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Recipe', 'image_name')
    op.drop_column('Recipe', 'image_file')
    # ### end Alembic commands ###
