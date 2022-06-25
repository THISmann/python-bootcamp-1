"""empty message

Revision ID: 1fbe4b8340de
Revises: 
Create Date: 2022-06-25 11:11:58.417777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbe4b8340de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('my_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_my_model_details'), 'my_model', ['details'], unique=False)
    op.create_table('rode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_rode_name'), 'rode', ['name'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('executant', sa.String(length=64), nullable=True),
    sa.Column('date_end', sa.String(length=64), nullable=True),
    sa.Column('data_start', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_author'), 'task', ['author'], unique=False)
    op.create_index(op.f('ix_task_data_start'), 'task', ['data_start'], unique=False)
    op.create_index(op.f('ix_task_date_end'), 'task', ['date_end'], unique=False)
    op.create_index(op.f('ix_task_description'), 'task', ['description'], unique=False)
    op.create_index(op.f('ix_task_executant'), 'task', ['executant'], unique=False)
    op.create_index(op.f('ix_task_status'), 'task', ['status'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=64), nullable=True),
    sa.Column('status_session', sa.String(length=64), nullable=True),
    sa.Column('role', sa.String(length=64), nullable=True),
    sa.Column('task', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['task.id'], ),
    sa.ForeignKeyConstraint(['task'], ['task.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)
    op.create_index(op.f('ix_user_role'), 'user', ['role'], unique=False)
    op.create_index(op.f('ix_user_status_session'), 'user', ['status_session'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_status_session'), table_name='user')
    op.drop_index(op.f('ix_user_role'), table_name='user')
    op.drop_index(op.f('ix_user_password'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_task_status'), table_name='task')
    op.drop_index(op.f('ix_task_executant'), table_name='task')
    op.drop_index(op.f('ix_task_description'), table_name='task')
    op.drop_index(op.f('ix_task_date_end'), table_name='task')
    op.drop_index(op.f('ix_task_data_start'), table_name='task')
    op.drop_index(op.f('ix_task_author'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_rode_name'), table_name='rode')
    op.drop_table('rode')
    op.drop_index(op.f('ix_my_model_details'), table_name='my_model')
    op.drop_table('my_model')
    # ### end Alembic commands ###
