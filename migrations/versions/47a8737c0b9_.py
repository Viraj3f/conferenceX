"""empty message

Revision ID: 47a8737c0b9
Revises: 4560804bcbd
Create Date: 2016-07-18 09:36:24.956909

"""

# revision identifiers, used by Alembic.
revision = '47a8737c0b9'
down_revision = '4560804bcbd'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('HTML', sa.Column('payment_msg', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('HTML', 'payment_msg')
    ### end Alembic commands ###
