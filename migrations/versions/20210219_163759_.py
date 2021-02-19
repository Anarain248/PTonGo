"""all tables migrated 

Revision ID: 0b7a66e319c3
Revises:
Create Date: 2021-02-19 16:37:59.128606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b7a66e319c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('exercisetype', sa.String(length=100), nullable=False),
    sa.Column('reps', sa.String(length=100), nullable=False),
    sa.Column('primarymuscle', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('exercisetype'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('primarymuscle'),
    sa.UniqueConstraint('reps')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('primarymacro', sa.String(length=500), nullable=False),
    sa.Column('totalmacros', sa.String(length=100), nullable=False),
    sa.Column('totalcalories', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('primarymacro'),
    sa.UniqueConstraint('totalcalories'),
    sa.UniqueConstraint('totalmacros')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('foods')
    op.drop_table('exercises')
    # ### end Alembic commands ###