favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

values_list = set(favorite_languages.values())
#print(values_list, type(values_list))

for language in values_list:
    print(language.title())