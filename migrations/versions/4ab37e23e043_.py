"""empty message

Revision ID: 4ab37e23e043
Revises: cf431fc6abd0
Create Date: 2019-04-20 23:46:06.843443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ab37e23e043'
down_revision = 'cf431fc6abd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer_information', 'created_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_information', sa.Column('created_on', sa.VARCHAR(length=12), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
