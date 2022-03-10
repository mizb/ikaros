"""update site sources

Revision ID: e76363a21cbe
Revises: 6749dee88757
Create Date: 2022-02-22 09:34:12.817637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e76363a21cbe'
down_revision = '6749dee88757'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('site_sources', sa.String(), nullable=True))
        batch_op.drop_column('website_priority')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_priority', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('site_sources')

    # ### end Alembic commands ###