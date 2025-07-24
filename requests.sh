#/bin/bash


curl "http://localhost:8000/" -H "Accept: text/plain"; printf "\n"
curl "http://localhost:8000/" -H "Accept: text/html"; printf "\n"
curl "http://localhost:8000/" -H "Accept: text/plain" -H "x-api-key: 123"; printf "\n"
curl "http://localhost:8000/" -H "Accept: text/plain" -H "x-api-key: 12345678"; printf "\n"
curl "http://localhost:8000/test"; printf "\n"
curl -X POST "http://localhost:8000/events" -H "Content-Type: application/json" -d '{"name": "test", "description": "test content", "start_date": "22 july 2025", "end_date": "15 november 2025"}'; printf "\n"
curl -X POST "http://localhost:8000/events" -H "Content-Type: application/json" -d '{"name": "test", "description": "content modified", "start_date": "22 september 2025", "end_date": "10 december 2025"}'; printf "\n"
curl -X POST "http://localhost:8000/events" -H "Content-Type: application/json" -d '{"name": "data", "description": "client data", "start_date": "21 january 2025", "end_date": "20 april 2025"}'; printf "\n"
