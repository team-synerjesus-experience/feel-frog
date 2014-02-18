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
     L[0] = [3,0,0,0,0,0,0,0,0,0,0]
     m = 3


#start of data generation
for j in range(1, 999):         #runs 999 times, which, added to L[0] and c[0], gives 1000 results
  oldm = m                      #keeps a note of the initial state of m
  for i in range (0, 10)        #runs over 0-9.
    a[i] = random.randint(0, 1) #assigns a[i] a random digit, either 0 or 1
    if a[i] = 1:                   #checks if each a is value 1 (done) or 0 (not done) if done, continues.
      if VT[i[0]] == True:         #checks if the value of that activity is positive
        if (m + VT[i[1]]) > 5 :    #if so, checks if adding the value will exceed the upper limit (5)
          m = 5                    #if so, sets m to the maximum (5)
        else:                      #if not
          m = (m + VT[i[1]])       #adds the value of activity i to the mood.
      else:                        #if the value of the activity is negative, 
        if m - (VT[i[1]] < 1) :    #checks to see if removing the value of a[i] would exceed the lower limit
          m = 1                    #if so, sets m to lower limt (1)
        else:                      #otherwise,
          m = m - VT[i[1]]         #subtracts the value from the mood.

	
  
  L[j] = [m, a0, a1, a2, a3, a4, a5, a6, a7, a8, a9] #stores the values in the list.
#end of data generation.