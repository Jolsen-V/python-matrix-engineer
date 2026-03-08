
# Practica 03:  Datos personales para la entrevista.

print()
print("=== MY FIRST INTERVIEW OF JOB ====")
print("_______________________________________")

name = input("what is your name?: ")
age_birth = int(input("when in their birth year?: "))
age_actual = 2026 - age_birth
experience = input("Do you have work experience?: ")
address = input("Where do you live now?: ")
position = input("what position would you like to apply for?: ")
remuneration = input("How much would you like to earn?: ")

print(f"""Hello,{name} welcome to company.
Tell me your year of birth: {age_birth}.
So his current age is: {age_actual}.
Tell me, do you have experience?: {experience}.
you live in: {address}.
you are applying for the position: {position}.
You monthly payment  would be: {remuneration}

***Congratulations, I passed the job interview; it starts next week. ***""")