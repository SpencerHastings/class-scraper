import requests
import sqlite3
import json
import sys

cookies = {
    '_ga': 'GA1.2.1629102257.1557290941',
}

headers = {
    'Origin': 'http://saasta.byu.edu',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://saasta.byu.edu/noauth/classSchedule/index.php',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
}

data = {
    'courseId': '02859-006',
    'sessionId': 'AAJ2IA0AEXPQHXCS0XDN',
    'yearterm': '20195',
    'no_outcomes': 'true'
}

def add_course_sections(c, courseID, yearterm):
    data = {
        'courseId': courseID,
        'sessionId': 'AAJ2IA0AEXPQHXCS0XDN',
        'yearterm': yearterm,
        'no_outcomes': 'true'
    }
    response = requests.post('http://saasta.byu.edu/noauth/classSchedule/ajax/getSections.php', headers=headers, cookies=cookies, data=data, verify=False)
    course_data = response.json()
    sections = course_data["sections"]
    for section in sections:
        sectionID = section["dept_name"] + " " + section["catalog_number"] + " " + section["section_number"]
        c.execute("insert into sections values (?,?)", [sectionID, json.dumps(section)])
    catalog = course_data["catalog"]
    dept_headers = course_data["dept_headers"]
    course_headers = course_data["course_headers"]