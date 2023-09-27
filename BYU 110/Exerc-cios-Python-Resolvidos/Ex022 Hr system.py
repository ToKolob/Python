#name id_number job_title salary
with open ("hr_system.txt") as hr_system:
    for line in hr_system:
        parts = line.split()
        name = parts[0]
        id = parts[1]
        job = parts[2]
        salary = float(parts[3])
        print(f"Name: {name}, Title: {job}, Salary: ${salary:,.2f} per Year and the ID: {id}")
