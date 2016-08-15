"""empty message

Revision ID: 9a01232a22cc
Revises: 0d25e6904746
Create Date: 2016-06-10 09:41:32.125958

"""

# revision identifiers, used by Alembic.
revision = '9a01232a22cc'
down_revision = '008dae41b45e'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sponsor_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'sponsors', sa.Column('description', sa.String(), nullable=True))
    op.add_column(u'sponsors', sa.Column('sponsor_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sponsors', 'sponsor_type', ['sponsor_type_id'], ['id'])
    op.add_column(u'tracks', sa.Column('location', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'tracks', 'location')
    op.drop_constraint(None, 'sponsors', type_='foreignkey')
    op.drop_column(u'sponsors', 'sponsor_type_id')
    op.drop_column(u'sponsors', 'description')
    op.drop_table('sponsor_type')
    ### end Alembic commands ###