"""empty message

Revision ID: 51ea7266551
Revises: 27cdae2d8b6
Create Date: 2016-06-30 05:10:28.696689

"""

# revision identifiers, used by Alembic.
revision = '51ea7266551'
down_revision = '27cdae2d8b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sponsor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('website', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('HTML', sa.Column('sponsor_text', sa.Text(), nullable=True))
    op.add_column('HTML', sa.Column('sponsor_url', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('HTML', 'sponsor_url')
    op.drop_column('HTML', 'sponsor_text')
    op.drop_table('sponsor')
    ### end Alembic commands ###
