curl "http://127.0.0.1:8000/hello" && echo -e "\n" && sleep 2
curl "http://127.0.0.1:8000/welcome" && echo -e "\n" && sleep 2
curl "http://127.0.0.1:8000/welcome?name=Rakoto" && echo -e "\n" && sleep 2
curl -X POST "http://localhost:8000/students" -H "Content-Type: application/json" -d '{"Reference": "std24444", "FirstName": "test", "LastName": "content", "age": "15"}'; && echo -e "\n" && sleep 2
