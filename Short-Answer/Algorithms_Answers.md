#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This algorithm is O(n) time complexity because as the 'n' input changes, the increase in time at scale is linear.


b) This algorithm is O(n^2) because we have a for loop iterating over 'n' and then nested inside we have a while loop that is checking whether 'j' is less than 'n', as the size of n increases, we will require exponential more time as the input scales. 


c) This algorithm is O(n) time complexity because the results have a linear relation to input 'bunnies'.

## Exercise II

Step 1.) If you have an 'n' story building, we want to find out which floor of that building we can drop an egg off of without it breaking while minimizing the amount of broken eggs. 

Step 2.) Find the floor that lies in the middle of the range of possible floors in the building.

Step 3.) Drop an egg off that floor.

Step 4.) If egg breaks, then you know that all floors above you are unsafe to drop the egg, meaning you only have to seach the remaining floors *below* you.

Step 5.) Take sum of floors below you and divide by 2 to find the middle, go to that floor and drop egg, repeat process until you find the floor where the egg does not break and there is only one floor remaining.

Step 6.) This is basically just a binary search, this algorithm would have a runtime of O(logN) or "Logarithmic runtime".


