# using Pandas library , produce the following output . using pandas data frame organize the data into rows and columns 

import pandas as pd

data = {
    'subject_id': [1, 2, 3, 4], 
    'student_name': ['Joseph', 'Eva', 'Kevin', 'Joseph'],
    'courses': ['software engineering', 'Artificial Intelligence', 'Gaming', 'Software engineering technician']
}
student_information = pd.DataFrame(data)

print(student_information)