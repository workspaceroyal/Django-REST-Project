import requests
import json
URL = "http://127.0.0.1:8000/teacher-create/"

data = {
    'id': 1,
    'teacher_name': 'Teacher-2',
    'course_name': 'Data Science',
}

json_data = json.dumps(data)
r = requests.put(url=URL, data = json_data)
data = r.json()
print(data)