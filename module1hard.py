ball_sr={}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students_sp=list(students)
print(students_sp)
students_sp.sort()
print(students_sp)
grades[0]=sum(grades[0])/len(grades[0])
grades[1]=sum(grades[1])/len(grades[1])
grades[2]=sum(grades[2])/len(grades[2])
grades[3]=sum(grades[3])/len(grades[3])
grades[4]=sum(grades[4])/len(grades[4])
print(grades)
#ball_sr= {students_sp:grades}
ball_sr['Aaron']=grades[0]
ball_sr['Bilbo']=grades[1]
ball_sr['Johnny']=grades[2]
ball_sr['Khendrik']=grades[3]
ball_sr['Steve']=grades[4]
print(ball_sr)
