"""Make some things non-nullable in the deck table

Revision ID: 2eb59605e7b
Revises: 354eb71928d
Create Date: 2015-11-06 17:43:38.025874

"""

# revision identifiers, used by Alembic.
revision = '2eb59605e7b'
down_revision = '354eb71928d'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tb_deck', 'first_used',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('tb_deck', 'last_used',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('tb_deck', 'link',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
    op.alter_column('tb_deck', 'times_used',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tb_deck', 'times_used',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_deck', 'link',
               existing_type=mysql.VARCHAR(length=256),
               nullable=True)
    op.alter_column('tb_deck', 'last_used',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('tb_deck', 'first_used',
               existing_type=mysql.DATETIME(),
               nullable=True)
    ### end Alembic commands ###