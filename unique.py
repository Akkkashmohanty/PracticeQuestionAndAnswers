# Write a Python program to get variable unique identification number or string. 

import uuid

# The uuid.uuid4() function generates a random UUID as a 36-character hexadecimal string. 
# You can convert it to a regular string using str() if needed.
# The generated UUID is designed to be unique across different systems and time, 
# It suitable for generating unique identification numbers or strings in various applications.

#Generate a unique identification number
unique_id = str(uuid.uuid4())

# Print the unique identification number
print("Unique ID:", unique_id)