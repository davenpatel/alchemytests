# Code Samples

```bash
# Create a branch
alembic revision -m "create networking branch" --head=base --branch-label=networking --version-path=alembic/versions/networking

alembic revision -m "create personnel branch" --head=base --branch-label=personnel --version-path=alembic/versions/personnel --autogenerate
```

```bash
# Generate migration
alembic revision -m "initial networking models" --head=networking@head
alembic revision -m "initial personnel models" --head=personnel@head --autogenerate
```

```bash
# Run migrations
alembic upgrade heads
```

```bash
# Downgrade branch, remember the -x base=branch_name parameter
alembic downgrade personnel@base
```

# Gotchas

Keep in mind the ini file configuration.

# Code to Test

```python
# https://stackoverflow.com/questions/76779173/dynamically-set-up-the-version-locations-in-env-py-for-alembic-migrations

# Source - https://stackoverflow.com/a/78728716
# Posted by sam2426679
# Retrieved 2026-07-14, License - CC BY-SA 4.0

from alembic import context
import os

script = context.script

def get_versions_path():
  try:
    versions_path = os.environ['ALEMBIC_VERSIONS_PATH']
  except KeyError:
    raise ValueError('You must specify a value for ALEMBIC_VERSIONS_PATH, which is the path to the /versions directory')

  if not os.path.isdir(versions_path):
    raise ValueError(f"ALEMBIC_VERSIONS_PATH of '{versions_path}' does not exist")

  return versions_path

script.__dict__.pop('_version_locations', None)
script.version_locations = [get_versions_path()]

```