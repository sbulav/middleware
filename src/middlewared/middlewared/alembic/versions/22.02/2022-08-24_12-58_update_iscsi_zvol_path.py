"""Update iscsi zvol path

Revision ID: 98b2cfaa0e5a
Revises: 7c8da45b515e
Create Date: 2022-08-24 12:58:02.805097+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98b2cfaa0e5a'
down_revision = '7c8da45b515e'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    # ### commands auto generated by Alembic - please adjust! ###
    for extent in conn.execute("SELECT id, iscsi_target_extent_path FROM services_iscsitargetextent"):
        id, path = extent
        if path.startswith('zvol/') and ' ' in path:
            path = path.replace(' ', '+')
            conn.execute(
                "UPDATE services_iscsitargetextent SET iscsi_target_extent_path = ? WHERE id = ?",
                path, id
            )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
