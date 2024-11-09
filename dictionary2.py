student = {
    'name': 'Lucy',
    'age': '13',
    'city': 'London',
}

print(student['name'])
print(student)

student2 = ['Lucy', '13', 'London']
print(student2[0])

classroom = {
    'Ada': {
        'age': '12',
        'marks': [67, 45, 82, 23, 50],
    },
    'Brian': {
        'age': '13',
        'marks': [44, 12, 59, 30, 66],
    },
    'Collin': {
        'age': '12',
        'marks': [97, 89, 92, 88, 95],
    },
}

print(classroom.keys())
print(classroom.values())
print(classroom['Brian']['age'])
print(classroom['Brian']['marks'])