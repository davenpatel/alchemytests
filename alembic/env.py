from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from models.networking.networking_base import NetworkingBase
from models.personnel.personnel_base import PersonnelBase

from alembic import context

import os

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

target_bases = {
    "networking": NetworkingBase,
    "personnel": PersonnelBase,
}

target_metadata = [
    NetworkingBase.metadata,
    PersonnelBase.metadata,
]

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def set_versions_locations():
    # print(f"Versions Path: {context.script.version_locations}")
    for key in target_bases.keys():
        cwd = os.getcwd()
        versions_path = os.path.join(cwd, "alembic", "versions", key)
        context.script.version_locations.append(versions_path)
    # print(f"Versions Path: {context.script.version_locations}")


def get_target_metadata():
    # print('X Arguments:', context.get_x_argument(as_dictionary=True))
    valid_commands = {"revision"}
    # Safely get the currently running command name. context.config.cmd_opts may be None
    # when env.py is invoked in certain contexts (e.g., programmatically), so guard access.
    cmd_opts = getattr(context.config, "cmd_opts", None)
    if cmd_opts is None or not getattr(cmd_opts, "cmd", None):
        command_run = None
    else:
        # cmd is a list of callables; take the first and get its __name__ if available
        first_cmd = cmd_opts.cmd[0]
        command_run = getattr(first_cmd, "__name__", None)
    selected_metadata = target_metadata

    if command_run in valid_commands:
        target_base_key = context.get_x_argument(as_dictionary=True).get("base")
        if target_base_key is None:
            raise ValueError("No base key provided. Use --x base=base_name")

        base = target_bases.get(target_base_key)
        if base is None:
            raise ValueError(f"Invalid base key: {target_base_key}")
        selected_metadata = base.metadata
        # print(f"Selected metadata for base '{target_base_key}': {selected_metadata}")

    return selected_metadata


def include_object(object, name, type_, reflected, compare_to):
    # If the object belongs to a schema you don't care about, ignore it
    target_schema = context.get_x_argument(as_dictionary=True).get("base")
    if type_ == "table" and object.schema != target_schema:
        return False
    return True


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    selected_metadata = (
        get_target_metadata()
    )  # Default to all metadata if no specific base is provided

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=selected_metadata,
            include_schemas=True,
            include_object=include_object,
        )

        with context.begin_transaction():
            context.run_migrations()


set_versions_locations()
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
