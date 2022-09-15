def get_grade(score):
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    else: 
        return "F"


score = int(input("점수를 입력해주세요 : "))
grade = get_grade(score)
print(f"당신의 학점은 {grade}입니다.")