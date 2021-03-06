"""add about-me and last_seen fields to Users table

Revision ID: 292f124d43a9
Revises: 66dac566a7b1
Create Date: 2020-04-06 21:37:55.554218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '292f124d43a9'
down_revision = '66dac566a7b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
