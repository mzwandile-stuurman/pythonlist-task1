ages1= [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20] # two lists to compare
ages2= [2,4,12,14,15,16,16, 17,18, 14, 20, 20]
def common(ages1, ages2): # define function with two variables
    for i in ages1: # move through the ages1 list
        if i in ages2: # if the ages1 is in ages2
            return True
print(common(ages1,ages1))
