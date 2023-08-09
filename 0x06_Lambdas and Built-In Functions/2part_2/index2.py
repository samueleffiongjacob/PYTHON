# more on zip
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {ps[0]: max(ps[1], ps[2]) for ps in zip(students, midterms, finals)}


# returns dict with {student:highest score}
#  (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades1 = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0]+pair[1])/2),
            zip(midterms, finals)
        )
    )
)
print(f" seing final grade: using dictionary comprehension:\n {final_grades1} \n")
print(f" seing final grafe: using lambda : \n {final_grades1} \n")
print(f" seing aravage: using lambda:\n {avg_grades}")
