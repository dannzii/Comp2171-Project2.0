"""empty message

Revision ID: 43e87b9284d4
Revises: 11d61b24f875
Create Date: 2019-04-21 00:55:21.836240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e87b9284d4'
down_revision = '11d61b24f875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_information', sa.Column('title', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer_information', 'title')
    # ### end Alembic commands ###