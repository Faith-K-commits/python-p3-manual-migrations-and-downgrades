"""Renaming students to scholars

Revision ID: 3805e54c7c8a
Revises: 791279dd0760
Create Date: 2024-09-10 19:49:56.124636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3805e54c7c8a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
