"""      
      *         =>   row = 6,sp=6,co=1      
     * *        =>   row = 5,sp=5,co=2
    * * *       =>   row = 4,sp=4,co=3
   * * * *      =>   row = 3,sp=3,co=4
  * * * * *     =>   row = 2,sp=2,co=5
 * * * * * *    =>   row = 1,sp=1,co=6

"""

for r in range(6,0,-1):
    for s in range(1,r):
        print(" ",end = "")
    for c in range(1,(7-r)+1):
        print("*",end = " ")
    print()
