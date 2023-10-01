# Start with the list by printing three course’s name like comp100,comp120,comp213 . Print a message saying that you are enrolled in that course.  The text of each message should be the same, but each message should be personalized with the course ’s name.Append a new course GNET 

course = ['comp100', 'comp120', 'comp213']
print(course)

print("You are enrolled in the course: " + course[0])
print("You are enrolled in the course: " + course[1])
print("You are enrolled in the course: " + course[2])

course.append('GNET')