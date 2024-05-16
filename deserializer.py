import requests
import json
URL = "http://127.0.0.1:8000/teacher-create/"

data = {
    'teacher_name': 'Teacher-1',
    'course_name': 'ML',
    'course_duration': 3,
    'seat': 20,
}

json_data = json.dumps(data)
r = requests.post(url=URL, data = json_data)
data = r.json()
print(data)