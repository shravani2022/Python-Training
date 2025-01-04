round1_trainee1 = int(input())
round1_trainee2 = int(input())
round1_trainee3 = int(input())

round2_trainee1 = int(input())
round2_trainee2 = int(input())
round2_trainee3 = int(input())

round3_trainee1 = int(input())
round3_trainee2 = int(input())
round3_trainee3 = int(input())

avg_trainee1 = (round1_trainee1+round2_trainee1+round3_trainee1)/3

avg_trainee2 = (round1_trainee2+round2_trainee2+round3_trainee2)/3

avg_trainee3 = (round1_trainee3+round2_trainee3+round3_trainee3)/3

print(avg_trainee1,avg_trainee2,avg_trainee3)

max_oxygen = max(avg_trainee1,avg_trainee2,avg_trainee3)
print(max_oxygen)

if max_oxygen < 70 :
    print("unfitt")
  