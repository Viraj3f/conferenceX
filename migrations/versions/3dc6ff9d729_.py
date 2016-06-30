"""empty message

Revision ID: 3dc6ff9d729
Revises: 126ae6b8bd1
Create Date: 2016-06-30 10:44:01.482800

"""

# revision identifiers, used by Alembic.
revision = '3dc6ff9d729'
down_revision = '126ae6b8bd1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('HTML', sa.Column('sponsor_text', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('HTML', 'sponsor_text')
    ### end Alembic commands ###