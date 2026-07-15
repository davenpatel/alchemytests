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