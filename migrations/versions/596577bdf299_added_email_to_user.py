"""added email to user

Revision ID: 596577bdf299
Revises: 890896fb43ce
Create Date: 2023-01-20 09:43:18.570292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '596577bdf299'
down_revision = '890896fb43ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=50), nullable=True))
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
