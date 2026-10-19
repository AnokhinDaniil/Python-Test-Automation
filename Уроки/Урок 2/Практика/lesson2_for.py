#for x in range(1, 21):
#    print("х=",x, " x^2=",x*x)

students = ["Александр", "Михаил", "Мария", "Ольга", "Кирилл"]

i = 0

for i in range (0, len(students)):
    print(students[i])

for student in students:
    print(student)

word = "test"

for s in word:
    print(s)

# напечатать только нечетные
nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    if(n % 2 == 1):
        print(n)