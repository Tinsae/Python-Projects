import random
import collections
# compare prob1 and 2 100 times
prob1 = 0
for i in range(100):
    # counts number of ones
    oneone = 0
    total = 0
    trials = 100
    #do hundred trials
    for t in range(trials):
        # reset variable to count for next trial
        oneone = 0
        # roll a die six times
        for d in range(6):
            if(random.randrange(1,7) == 1):
                oneone += 1
        # one occurred atleast one time
        if(oneone >= 1):
            total += 1

    probability1 = total/trials
    #print("Estimated likelihood of 1 once in 6:", probability1)

    total = 0
    two_one = 0
    #do hundred trials
    for t in range(trials):
        # reset variable to count for next trial
        two_one = 0
        # roll a die twelve times
        for d in range(12):
            if(random.randrange(1,7) == 1):
                two_one += 1
        # one occurred atleast twice time
        if(two_one >= 2):
            total += 1

    probability2 = total/trials
    #print("Estimated likelihood of 1 twice in 12:", probability2)

    if(probability1 > probability2):
        prob1 +=1


print(prob1)
