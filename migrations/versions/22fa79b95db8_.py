"""empty message

Revision ID: 22fa79b95db8
Revises: 027474d76a2d
Create Date: 2022-11-28 17:35:33.293786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22fa79b95db8'
down_revision = '027474d76a2d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=sa.INTEGER(),
               type_=sa.Text(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contacts', schema=None) as batch_op:
        batch_op.alter_column('telephone',
               existing_type=sa.Text(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###