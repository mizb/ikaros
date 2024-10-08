"""update multithread

Revision ID: ae24eb9602af
Revises: 98e01c6ecbdc
Create Date: 2024-09-06 21:25:23.629679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae24eb9602af'
down_revision = '98e01c6ecbdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scrapingconfigs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('threads_num', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('scrapingconfigs', schema=None) as batch_op:
        batch_op.drop_column('threads_num')

    # ### end Alembic commands ###
