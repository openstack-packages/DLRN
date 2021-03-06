# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""Add component to CIVote

Revision ID: 00a31f1f39c0
Revises: 7bed5ff86925
Create Date: 2019-10-07 10:47:29.032909

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = '00a31f1f39c0'
down_revision = '7bed5ff86925'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('civotes', sa.Column('component', sa.String(64)))
    civotes = table('civotes',
                    column('id', sa.Integer),
                    column('component', sa.String))
    # For existing civotes, set component to None
    op.execute(civotes.update()
               .where(civotes.c.id == civotes.c.id)
               .values(component=None))


def downgrade():
    with op.batch_alter_table('civotes') as batch_op:
        batch_op.drop_column('component')
