import json

string = '{"year_term": "20195", "curriculum_id": "08675", "title_code": "003", "dept_name": "ACC", "catalog_number": "503", "catalog_suffix": null, "title": "Adv Financial Accounting", "full_title": "Advanced Financial Accounting.", "sections": [{"section_number": "001", "fixed_or_variable": "F", "credit_hours": "3.00", "minimum_credit_hours": "3.00", "honors": null, "credit_type": "S", "section_type": "DAY", "instructor_name": null, "instructor_id": null}, {"section_number": "002", "fixed_or_variable": "F", "credit_hours": "3.00", "minimum_credit_hours": "3.00", "honors": null, "credit_type": "S", "section_type": "DAY", "instructor_name": null, "instructor_id": null}]}'

values = json.loads(string)
key = "catalog_suffixs"
if key in values.keys():
    print(values[key])
print(type(values))