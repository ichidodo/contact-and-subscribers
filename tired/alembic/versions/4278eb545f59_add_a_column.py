"""Add a column

Revision ID: 4278eb545f59
Revises: d90a385ade53
Create Date: 2022-04-18 14:43:56.134791

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '4278eb545f59'
down_revision = 'd90a385ade53'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass



def upgrade():
    op.add_column('everybody', sa.Column('Email', sa.Unicode(200)))
    op.add_column('everybody',sa.Column('Password', sa.Unicode(200)))
    op.add_column('everybody', sa.Column('Blocked', sa.Boolean))
    op.add_column('everybody', sa.Column('Email_Verified', sa.Boolean))
    op.add_column('everybody',sa.Column('Created_At',sa.DateTime, default=datetime.datetime.now))
    op.add_column('everybody',sa.Column('Updated_At',sa.DateTime, default=datetime.datetime.now) )




def downgrade():
    op.drop_column('everybody','Email')
    op.drop_column('everybody', 'Password')
    op.drop_column('everybody', 'Blocked')
    op.drop_column('everybody', 'Email_Verified')
    op.drop_column('everybody', 'Created_At',datetime)
    op.drop_column('everybody', 'Updated_At',datetime)