import json
# person_string = '{"name":"Ali", "languages":["python","C#"]}'       # json
# result = json.loads(person_string)      # Dict. oluyor
# result = result['name']
# result = result['languages']

# with open('15.4_person.json.py') as f:
#     data = json.load(f)
#     print(data['name'])
#     print(data['languages'])

# print(result)

person_dic = {
    'name': 'Ali',
    'languages': ['Python',['C#']]
}
# result = json.dumps(person_dic)         # dict -> json a çevir
# print(result)

# with open ("15.4_person.json.py",'w') as f:     # dic -> json olarak dosyaya yazma
#     json.dump(person_dic,f)

person_string = '{"name":"Ali", "languages":["python","C#"]}'
person_dic = json.loads(person_string)
result = json.dumps(person_dic, indent= 4, sort_keys=True)          # güzel yazmak için (indent-> kaç karakter boşluk girsin)
print(person_dic)
print(result)