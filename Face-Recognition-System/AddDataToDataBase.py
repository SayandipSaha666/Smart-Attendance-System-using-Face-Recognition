import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': 'https://faceattendancerealtime-8a108-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    "213002" :
        {
            "name": "Pabitra Kumar Mahato",
            "major": "Mechanical",
            "starting_year": "2021",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 4,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "216007":
        {
            "name": "Swadesh Paul",
            "major": "IT",
            "starting_year": "2021",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 4,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "225003":
        {
            "name": "Purbayan Kumar Das",
            "major": "ECE",
            "starting_year": "2022",
            "Total_attendance": 10,
            "Standing": "E",
            "year": 3,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "225009" :
        {
            "name": "Sayan De",
            "major": "ECE",
            "starting_year": "2022",
            "Total_attendance": 10,
            "Standing": "E",
            "year": 3,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "231012" :
        {
            "name": "Mriganka Barman",
            "major": "Civil ",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "235022" :
        {
            "name": "Jayanta Chakraborty",
            "major": "ECE",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236009" :
        {
            "name": "Sayandip Saha ",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236034" :
        {
            "name": "Chaiti Sen",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "235012" :
        {
            "name": "Santanu Singh Sardar",
            "major": "ECE",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236005" :
        {
            "name": "Soumik Ghatak",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236018" :
        {
            "name": "Sudarshana Bhattacharya",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236021" :
        {
            "name": "Pritam Mohanta",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        },
    "236058" :
        {
            "name": "Dipanjan Das",
            "major": "IT",
            "starting_year": "2023",
            "Total_attendance": 6,
            "Standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-03 17:58:20"
        }
}

for key,value in data.items():
    ref.child(key).set(value)

