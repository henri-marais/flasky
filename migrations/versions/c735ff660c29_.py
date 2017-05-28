"""empty message

Revision ID: c735ff660c29
Revises: 38c4e85512a9
Create Date: 2017-05-28 09:55:13.102076

"""

# revision identifiers, used by Alembic.
revision = 'c735ff660c29'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
