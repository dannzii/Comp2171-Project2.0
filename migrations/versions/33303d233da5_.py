"""empty message

Revision ID: 33303d233da5
Revises: 0b77f29b8791
Create Date: 2019-04-23 00:45:10.938467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33303d233da5'
down_revision = '0b77f29b8791'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointment', sa.Column('appointmentdate', sa.String(length=120), nullable=True))
    op.drop_column('appointment', 'appointment_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointment', sa.Column('appointment_date', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_column('appointment', 'appointmentdate')
    # ### end Alembic commands ###
