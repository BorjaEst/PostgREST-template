# Create migration
```bash
alembic revision ----autogenerate -m "<slug>"
```

# Apply migration
```bash
alembic upgrade head
```

# Deploy
```bash
docker-compose up
```
> Go to [localhost:8080](http://localhost:8080)

# Stop
```bash
docker-compose down
```