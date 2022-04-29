import json

dic = {'students': [{'firstName': 'Nikki', 'lastName': 'Roysden'}, {'firstName': 'Mervin', 'lastName':
    'Friedland'}, {'firstName': 'Aron ', 'lastName': 'Wilkins'}], 'teachers': [{'firstName': 'Amberly',
                                                                                'lastName': 'Calico'},
                                                                               {'firstName': 'Regine',
                                                                                'lastName': 'Agtarap'}]}

with open("sample.json", "w") as outfile:
    json.dump(dic, outfile)
