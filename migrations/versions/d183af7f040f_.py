"""empty message

Revision ID: d183af7f040f
Revises: 
Create Date: 2024-03-31 15:46:52.139218

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd183af7f040f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doctor_availabilty',
    sa.Column('doctor_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('available_times', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('unavailabile_times', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('doctor_id', name='doctor_availabilty_pkey')
    )
    op.create_table('departments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('department_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('services', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='departments_pkey')
    )
    op.create_table('patient_history',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('doctor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('appointment_time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('diagnosis', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('allergies', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.Column('medications', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='patient_history_pkey')
    )
    op.create_table('patients',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='patients_pkey')
    )
    op.create_table('upcoming_appointments',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('doctor_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('appointment_time', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='upcoming_appointments_pkey')
    )
    op.create_table('doctors',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('specialization', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='doctors_pkey')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doctors')
    op.drop_table('upcoming_appointments')
    op.drop_table('patients')
    op.drop_table('patient_history')
    op.drop_table('departments')
    op.drop_table('doctor_availabilty')
    # ### end Alembic commands ###