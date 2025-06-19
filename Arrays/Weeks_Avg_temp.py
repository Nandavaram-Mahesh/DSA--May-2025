# You are given temp of a week and you have to find the average temp of a week

temp = [10,20,30,40,50,60,70,80,90,100]
total_temp = 0

# Avg = sum of all the temp/total number of days

# step 1 : loop trough the temp list and find total temp
# step 2 : find the total number of days
# step 3 : divide the total temp by total number of days

for day in temp:
    total_temp += day

avg_temp = total_temp/len(temp)
print(avg_temp)