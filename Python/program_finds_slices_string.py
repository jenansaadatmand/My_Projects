first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'

first_name_cap = first_name.capitalize()  # Using method capitalize()
last_name_cap = last_name.capitalize()
print(first_name_cap)
print(last_name_cap)
award_location = note.find('award: ')   # Finding a string using .find() method
print(award_location)  # You will get a value of index 0 indicating that the award is at the start of the string
print()

print(note[0:7])  # Award starts at index 0 to 7 not including 7
award_text = note[7:]  # Slice the remainder, we know that the award starts at index 0 to 6, so we slice from 7 to the end
print(award_text)
