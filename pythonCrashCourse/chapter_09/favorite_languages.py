from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['saarh'] = 'c'
favorite_languages['edward'] = 'ruby'  
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s language is " + language.title() + "." )
    