"""create everybody table

Revision ID: d90a385ade53
Revises: 
Create Date: 2022-04-18 13:53:08.520233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd90a385ade53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass



def create_everybody_table() -> None:
    op.create_table('everybody',
    sa.Column('id', sa.Integer,primary_key = True),
    sa.Column('First_Name', sa.Unicode(50)),
    sa.Column('Last_Name', sa.Unicode(200)),
    sa.Column('Telephone_Number', sa.Integer, primary_key=True)),




def upgrade() -> None:
    create_everybody_table()
def downgrade() -> None:
    op.drop_table('everybody')