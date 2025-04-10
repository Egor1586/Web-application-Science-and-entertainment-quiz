"""empty message

Revision ID: 0a2d7e47a44b
Revises: a0b18bfb206f
Create Date: 2025-04-08 21:50:53.659539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a2d7e47a44b'
down_revision = 'a0b18bfb206f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###
