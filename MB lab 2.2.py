try:
    # Sample Input
    student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2]}

    # Check if the student submitted all 6 activities
    submitted_activities = 0

    if 'assignment' in student and len(student['assignment']) == 4:
        submitted_activities += 4

    if 'test' in student and len(student['test']) == 2:
        submitted_activities += 2

    if 'lab' in student and len(student['lab']) == 2:
        submitted_activities += 2

    # Create the submission_check dictionary
    submission_check = {student['name']: submitted_activities}

    # Output the submission_check dictionary
    print(submission_check)

except Exception as e:
    # Handle exceptions if they occur
    print("An error occurred:", e)