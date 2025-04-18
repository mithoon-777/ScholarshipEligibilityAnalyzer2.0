def build_prompt(name, age, qualifications, gpa, income, activities, other_info):
    return f"""Based on the following student information:

Name: {name}
Age: {age}
Academic Qualifications: {qualifications}
GPA: {gpa}
Family Income: {income}
Extracurricular Activities: {activities}
Other Info: {other_info}

Evaluate scholarship eligibility, list potential scholarships, and provide application guidance."""
