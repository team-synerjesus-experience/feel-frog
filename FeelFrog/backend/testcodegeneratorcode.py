import random
#set up reusable variables.
#value table
VT = [[True,0],
     [True,1],
     [False,1],
     [True,0],
     [True,3],
     [True,2],
     [False,2],
     [True,0],
     [True,0],
     [False,4]]
#set up starting mood.
L = [[]]
L[0] = [3,0,0,0,0,0,0,0,0,0,0]
m = 3


#start of data generation
for j in range(1, 1000):         #runs 999 times, which, added to L[0] and c[0], gives 1000 results
  a = [0,0,0,0,0,0,0,0,0,0]
  oldm = m                      #keeps a note of the initial state of m
  for i in range (0, 10):        #runs over 0-9.
    a[i] = random.randint(0, 1) #assigns a[i] a random digit, either 0 or 1
    if a[i] == 1:                   #checks if each a is value 1 (done) or 0 (not done) if done, continues.
      if VT[i][0] == True:         #checks if the value of that activity is positive
        if (m + VT[i][1]) > 5 :    #if so, checks if adding the value will exceed the upper limit (5)
          m = 5                    #if so, sets m to the maximum (5)
        else:                      #if not
          m = (m + VT[i][1])       #adds the value of activity i to the mood.
      else:                        #if the value of the activity is negative, 
        if m - (VT[i][1] < 1) :    #checks to see if removing the value of a[i] would exceed the lower limit
          m = 1                    #if so, sets m to lower limt (1)
        else:                      #otherwise,
          m = m - VT[i][1]         #subtracts the value from the mood.

	
  
  L.append([a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], m]) #stores the values in the list.
#end of data generation.

#for testing porpoises.
#for k in range(0, 1000):
#  print L[k]
 
#for saving to file. hopefully.
#f = open('testfile.txt', 'w')
#S = str(L)
#f.write(S)

#if you want more data, increase the value X in line 21: for j in range(1, x)
#if you want to change the effect of the activities, they are set up as: [A,B], 
#with A being whether the effect is positive or negative, and B being the extent (from 0 to 4)*
#*you can increase this by more, but it will only serve to cancel out other activity effects, since mood caps at 1 and 5.