"""
 * * * * * *
  * * * * *
   * * * *
    * * *
     * *
      *


"""
for r in range(1,7):
    for s in range(r,1,-1):
        print(" ",end = "")
    for c in range(1,(7-r)+1):
        print("*",end = " ")
    print()