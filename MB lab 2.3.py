try:
    # Sample Input 1
    student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}
    submission_rate = {'Adam': 6}

    # Calculate the final grade
    if student['name'] in submission_rate and submission_rate[student['name']] >= 4:
        assignment_avg = sum(student['assignment']) / len(student['assignment'])
        lab_avg = sum(student['lab']) / len(student['lab'])
        test_avg = sum(student['test']) / len(student['test'])
        final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
        student['final_grade'] = final_grade
    else:
        student['final_grade'] = 0

    # Output the student dictionary
    print(student)

    # Sample Input 2
    student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2]}
    submission_rate = {'Adam': 6, 'Kevin': 3}

    # Calculate the final grade for student2
    if student2['name'] in submission_rate and submission_rate[student2['name']] >= 4:
        assignment_avg = sum(student2['assignment']) / len(student2['assignment'])
        lab_avg = sum(student2['lab']) / len(student2['lab'])
        test_avg = sum(student2['test']) / len(student2['test'])
        final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg
        student2['final_grade'] = final_grade
    else:
        student2['final_grade'] = 0

    # Output the student2 dictionary
    print(student2)

except Exception as e:
    # Handle exceptions if they occur
    print("An error occurred:", e)