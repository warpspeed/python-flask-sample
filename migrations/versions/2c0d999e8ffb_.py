"""empty message

Revision ID: 2c0d999e8ffb
Revises: None
Create Date: 2015-06-18 13:36:37.239101

"""

# revision identifiers, used by Alembic.
revision = '2c0d999e8ffb'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('is_complete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    ### end Alembic commands ###