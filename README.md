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

# Alembic Versioning Hack

```text
To force all Alembic commands (like history, heads, and current) to dynamically look at an environment variable, you have two approaches.Approach 1: Enable revision_environment (Simplest)Alembic actually provides a built-in configuration option that forces non-migration commands to read your env.py file.Open your alembic.ini file and look for the revision_environment variable under the [alembic] section. Ensure it is set to true
```
```ini
[alembic]
script_location = alembic
# Add or uncomment this line:
revision_environment = true
```

# Gitlab CI/CD Configuration

```yaml
stages:
  - database-prep
  - deploy
  - rollback

variables:
  # Path to store the current database version between jobs
  DB_VERSION_FILE: "db_version.txt"

# 1. Capture the current DB version before the new app deployment begins
capture-db-version:
  stage: database-prep
  image: python:3.11  # Use your application image with alembic installed
  script:
    - pip install alembic
    - alembic current | awk '{print $1}' > $DB_VERSION_FILE
    - echo "Pre-deploy database version is $(cat $DB_VERSION_FILE)"
  artifacts:
    paths:
      - $DB_VERSION_FILE
    expire_in: 1 hour

# 2. Upgrade the database and deploy your application
deploy-app:
  stage: deploy
  image: python:3.11
  script:
    - pip install alembic
    - echo "Upgrading database..."
    - alembic upgrade head
    - echo "Triggering application deployment..."
    - ./deploy_script.sh  # Replace with your actual deployment/helm/k8s command
    - ./health_check.sh   # CRITICAL: This script must exit with a non-zero code if the app crashes

# 3. This job runs ONLY if the 'deploy-app' job fails
rollback-database:
  stage: rollback
  image: python:3.11
  when: on_failure  # This ensures the job only runs on a failure up the chain
  dependencies:
    - capture-db-version  # Pulls the db_version.txt artifact down to this job
  script:
    - pip install alembic
    - PRE_DEPLOY_VERSION=$(cat $DB_VERSION_FILE)
    - echo "Deployment failed! Rolling back database to $PRE_DEPLOY_VERSION..."
    - alembic downgrade $PRE_DEPLOY_VERSION
```