"""added tables for configuration gui

Revision ID: version_0_3
Revises: 96ff8f93ef32
Create Date: 2020-06-08 23:04:34.555492

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'version_0_3'
down_revision = '96ff8f93ef32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_name', sa.String(length=256), nullable=False),
    sa.Column('hostname', sa.String(length=256), nullable=True),
    sa.Column('min_activity_duration', sa.Integer(), nullable=True),
    sa.Column('max_active_ping_delay', sa.Integer(), nullable=True),
    sa.Column('sample_size', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('process_name_pattern', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(length=256), nullable=True),
    sa.Column('first_name', sa.String(length=256), nullable=True),
    sa.Column('last_name', sa.String(length=256), nullable=True),
    sa.Column('locale', sa.String(length=5), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ruleset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('context_label', sa.String(length=256), nullable=True),
    sa.Column('context', sa.String(length=256), nullable=True),
    sa.Column('context_details', sa.String(length=256), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('min_time_of_day', sa.Time(), nullable=True),
    sa.Column('max_time_of_day', sa.Time(), nullable=True),
    sa.Column('max_time_per_day', sa.Integer(), nullable=True),
    sa.Column('max_activity_duration', sa.Integer(), nullable=True),
    sa.Column('min_break', sa.Integer(), nullable=True),
    sa.Column('free_play', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user2device',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('percent', sa.Integer(), nullable=True),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('device_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # op.alter_column('admin_event', 'downtime',
    #                 existing_type=mysql.INTEGER(display_width=11),
    #                 nullable=True,
    #                 existing_server_default=sa.text("'0'"))
    op.add_column('process_info', sa.Column('percent', sa.Integer(), server_default='100', nullable=True))
    # op.alter_column('process_info', 'downtime',
    #                 existing_type=mysql.INTEGER(display_width=11),
    #                 nullable=True,
    #                 existing_server_default=sa.text("'0'"))
    # op.alter_column('rule_override', 'key',
    #            existing_type=mysql.VARCHAR(length=256),
    #            nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('rule_override', 'key',
               existing_type=mysql.VARCHAR(length=256),
               nullable=False)
    op.alter_column('process_info', 'downtime',
                    existing_type=mysql.INTEGER(display_width=11),
                    nullable=False,
                    existing_server_default=sa.text("'0'"))
    op.drop_column('process_info', 'percent')
    op.alter_column('admin_event', 'downtime',
                    existing_type=mysql.INTEGER(display_width=11),
                    nullable=False,
                    existing_server_default=sa.text("'0'"))
    op.drop_table('user2device')
    op.drop_table('ruleset')
    op.drop_table('user')
    op.drop_table('device')
    # ### end Alembic commands ###
