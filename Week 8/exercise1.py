# 1. Use the following dictionary and answer the question 

# favorite_languages = {
#    'jen': 'HTML',
#    'sarah': 'c',
#    'edward': 'ruby',
#    'phil': 'C#',
#    }
# Change the value from C# to Python for the key phil 
# Add an item in the dictionary 
# Remove an item from the dictionary
# List all the values in the dictionary

favorite_languages = {
    'jen': 'HTML',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'C#',
}

favorite_languages['phil'] = 'Python'
favorite_languages['yaatu'] = 'java'
favorite_languages.pop('sarah')
print(favorite_languages)