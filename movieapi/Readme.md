# API Movie with FastAPI

## Run
fastapi dev app/main.py

## Test api
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
  
curl -X 'POST' \
  'http://localhost:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Civil War"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Civil War",
  "year": "now"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Civil War",
  "year": 2024
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Civil War",
  "year": 2024,
  "duration": "too long"
}'

curl -X 'POST' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Civil War",
  "year": 2024,
  "duration": 120
}'