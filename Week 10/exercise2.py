# Create a function called project() that store project_id globally and locally . Call the function and display both the id's . 
# Print the statement as 
# "My global project id is :"
# "My internal project id is :"

def project(internal_project_id):
    print("My internal project id is: " + internal_project_id)

project_id = "1234"
print("My global project id is: " + project_id)
project(project_id)