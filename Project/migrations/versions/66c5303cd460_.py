"""empty message

Revision ID: 66c5303cd460
Revises: 5f82a8a53398
Create Date: 2025-04-08 21:50:04.691355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66c5303cd460'
down_revision = '5f82a8a53398'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=True))
        batch_op.drop_column('mail')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mail', sa.VARCHAR(length=50), nullable=True))
        batch_op.drop_column('email')

    # ### end Alembic commands ###
