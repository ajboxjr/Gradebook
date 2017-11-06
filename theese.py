def myround(x, base=5):
    if x%5> 2:
        print(int(base* round(x/float(base))))
        return int(base * round(float(x)/base))

def solve(grades):
    # Complete this function
    grade_arr= []
    new_grade = 0
    for grade in grades:
        if grade>= 40:
            grade_arr.append(myround(grade))
        else:
            grade_arr.append(grade)
    return grade_arr

print(myround(67))
