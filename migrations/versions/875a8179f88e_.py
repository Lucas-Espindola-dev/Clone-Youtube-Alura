"""empty message

Revision ID: 875a8179f88e
Revises: 4b97a9e3ee2a
Create Date: 2023-08-05 10:27:03.424355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '875a8179f88e'
down_revision = '4b97a9e3ee2a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
