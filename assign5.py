champ = int(input("Enter a number: "))
mal = int(input("Enter the power it is raised to: "))
eli=1
for i in range(1,mal+1):
    eli= eli * champ
print(champ,"raised to power",mal,"is",eli)