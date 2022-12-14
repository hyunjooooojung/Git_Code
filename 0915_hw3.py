from pprint import pprint


users = [
    {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
    {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
    {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
    {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
    {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
    {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
    {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
    {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
    {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
    {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
    {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
    {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
    {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
    {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
    {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},
]

def get_filter_user(users):
    filter_users = []
    for i in range(15):
        avg = (users[i]['math_score'] + users[i]['science_score'] + users[i]['english_score'] + users[i]['social_score']) / 4
        
        # update를 하면 각 줄에 avg_score이 추가된다.
        # ! update를 해도 append를 해도 결과값은 같게 출력된다!
        # 근데 내가 만들고 싶었던 건 update를 했을때의 users였기 때문에 update로 돌아가게 할 것이다!
        users[i].update({'avg_score' : avg})
        
        # append를 하면 avg_score 세트가 하나더 추가된다.
        users.append({'avg_score' : avg})
        
        
        if avg > 70:
            name = users[i]['name']
            age = users[i]['age']
            filter_users.append({'name':name, 'age':age})
    return filter_users
        
filter_users = get_filter_user(users)
pprint(filter_users)