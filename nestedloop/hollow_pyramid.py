"""     
      *                             
     * *
    *   *
   *     *
  *       *
 * * * * * *    

"""

for r in range(1,7):
    for c in range(1,12):
        if r +c == 7 or c - r == 5 or r == 6:
            print("*",end = "")
        else:
            print(" ",end = "")
    print()
    