try:
    # Sample Input
    student_name = "Adam"
    assignment_scores = [82, 56, 44, 30]
    lab_scores = [78.20, 77.20]
    test_scores = [78, 77]

    # Create a dictionary to store student information
    student = {
        'name': student_name,
        'assignment': assignment_scores,
        'test': test_scores,
        'lab': lab_scores
    }

    # Output the student dictionary
    print("student =", student)

except Exception as e:
    # Handle exceptions if they occur
    print("An error occurred:", e)