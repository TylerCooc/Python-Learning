#dictionaries are structures in python that let us store information in key-value pairs.
#can store information and access it through its key

monthConversions ={ #dictionaries in python use open/closed brackets
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",     #3 letter variable is the key and the full month name is the value
    "Apr": "April",     # keys should be unique
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"]) #refer to the dictionary by name and then pass the key into a bracket. Passing the key will return the value from that entry.
print(monthConversions["Oct"])
print(monthConversions.get("Jan")) 