"""initial_schema

Revision ID: b6e13c5d179e
Revises: 
Create Date: 2021-09-17 16:15:12.716109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6e13c5d179e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "usuarios",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("senha", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "plantas",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("especie", sa.String(), nullable=False),
        sa.Column("temperatura", sa.String(), nullable=False),
        sa.Column("regas", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "usuarios_plantas",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("id_planta", sa.String(), nullable=False),
        sa.Column("id_usuario", sa.String(), nullable=False),
        sa.Column("nome", sa.String(), nullable=False),
        sa.Column("temperatura_maxima", sa.String(), nullable=True),
        sa.Column("umidade_minima", sa.String(), nullable=True),
        sa.Column("luminosidade_ideal", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["id_planta"], ["plantas.id"],
            name="fk_id_planta_usuarios_plantas"
        ),
        sa.ForeignKeyConstraint(
            ["id_usuario"], ["usuarios.id"],
            name="fk_id_usuario_usuarios_plantas"
        ),
    )

    op.create_table(
        "medicoes",
        sa.Column("id", sa.String(), nullable=False),
        sa.Column("id_usuario_planta", sa.String(), nullable=False),
        sa.Column("temperatura", sa.String(), nullable=True),
        sa.Column("umidade", sa.String(), nullable=True),
        sa.Column("luminosidade", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(
            ["id_usuario_planta"], ["usuarios_plantas.id"],
            name="fk_id_usuario_planta_medicoes"
        ),
    )


def downgrade():
    op.drop_table("medicoes")
    op.drop_table("usuarios_plantas")
    op.drop_table("plantas")
    op.drop_table("usuarios")
