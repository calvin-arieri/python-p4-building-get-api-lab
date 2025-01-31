"""adding created at

Revision ID: 82f352573937
Revises: d6929bb913ac
Create Date: 2023-06-24 14:39:12.107621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82f352573937'
down_revision = 'd6929bb913ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('bakery_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_baked_goods_bakery_id_bakeries'), 'bakeries', ['bakery_id'], ['id'])

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_baked_goods_bakery_id_bakeries'), type_='foreignkey')
        batch_op.drop_column('bakery_id')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
