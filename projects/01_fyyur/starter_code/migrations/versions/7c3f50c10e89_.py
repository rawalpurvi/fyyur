"""empty message

Revision ID: 7c3f50c10e89
Revises: 77c2c371b146
Create Date: 2020-12-27 13:13:30.200794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c3f50c10e89'
down_revision = '77c2c371b146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show_details', sa.Column('show_id', sa.Integer(), nullable=False, primary_key=True))
    op.drop_column('show_details', 'id')
    

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('show_details', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('show_details', 'show_id')
    # ### end Alembic commands ###
