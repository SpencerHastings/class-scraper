import requests
import sqlite3
import json
from byu.newsections import add_course_sections

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

def get_courses(yearterm):
    data = {
    'searchObject[yearterm]': yearterm,
    'sessionId': 'AAJ2IA0AEXPQHXCS0XDN'
    }
    response = requests.post('http://saasta.byu.edu/noauth/classSchedule/ajax/getClasses.php', headers=headers, cookies=cookies, data=data, verify=False)
    course_data = response.json()
    try:
        conn = sqlite3.connect('byuclasses2.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS courses (id TEXT, term TEXT, dept TEXT, number TEXT, suffix TEXT, title TEXT, full_title TEXT)")
        #c.execute("CREATE TABLE IF NOT EXISTS sections (id TEXT, data json)")
        c.execute("DELETE FROM courses")
        #c.execute("DELETE FROM sections")
        i = 0
        total = len(course_data)
        
        for courseID in course_data:
            i = i + 1
            course = course_data[courseID]
            term = course["year_term"]
            dept = course["dept_name"]
            number = course["catalog_number"]
            suffix = course["catalog_suffix"]
            title = course["title"]
            full_title = course["full_title"]
            print("Inserting " + title + " " + courseID + " : " + str(i) + "/" + str(total))
            c.execute("insert into courses values (?,?,?,?,?,?,?)", [courseID, term, dept, number, suffix, title, full_title])
            #add_course_sections(c, courseID, yearterm)
        conn.commit()  

    except:
        print("error")
    finally:
        conn.close()
    return "done"

def grab_courses():
    rows = None
    try:
        conn = sqlite3.connect('byuclasses2.db')
        c = conn.cursor()
        c.execute("SELECT DISTINCT dept from courses")
        rows = c.fetchall()
    except:
        print("error")
    finally:
        conn.close()
        return rows

def grab_courses_dept(dept):
    rows = None
    try:
        conn = sqlite3.connect('byuclasses2.db')
        c = conn.cursor()
        c.execute("SELECT dept, number, title from courses where dept = '" + dept + "'")
        rows = c.fetchall()
    except:
        print("error")
    finally:
        conn.close()
        return rows