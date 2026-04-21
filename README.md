# Three-Tier Web App on Docker

A production-style three-tier application running on AWS EC2.

## Architecture
Internet → Nginx (port 80) → Flask (port 5000) → PostgreSQL (port 5432)

## Stack
- Nginx — reverse proxy
- Flask — Python web framework
- PostgreSQL — database
- Docker Compose — container orchestration

## Run it
docker-compose up --build -d

## Routes
- GET / — home page
- GET /add?item=something — add item to database
- GET /items — list all items
