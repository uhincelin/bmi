w = raw_input("enter weight in lbs: ") #pounds
h = raw_input("enter height in inches: ") #inches
bmi = (float(w)/float(h)**2)*703
print 'My bmi is %s' % (round(bmi,1))
