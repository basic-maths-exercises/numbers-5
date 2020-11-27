# Converting to base n<10

Congratulations on writing a function to convert numbers from base ten to base two.  The discussion in the first of these tasks that talked about how there were multiple ways of representing all numbers is now hopefully starting to make more sense.   We have, after all, seen, that the number twelve is 12 in base ten and 1100 in base two.  

The idea that we have introduced in this exercise is that of the base of a number.  In this exercise, we are going to generalise this idea by noting that if we have ![](https://render.githubusercontent.com/render/math?math=1<A<11) symbols to use to represent a number we can express any of the natural numbers as:

![](https://render.githubusercontent.com/render/math?math=\sum_{n=0}^\infty\a_nA^n)

where each of the ![](https://render.githubusercontent.com/render/math?math=a_n) in this expression is a natural number that is less than ![](https://render.githubusercontent.com/render/math?math=A).  

To complete this exercise I would like you to complete the function `convertToBase`.  This function takes an integer with a value less than or equal to 127, which we will call `N` in input as well as a second integer called `base`, which must be greater than 1 and less than eleven.  Once you have completed it this function should return a numpy array of length 7.   The zeroth element of this array should be the first digit of the base `base` representation of the number, the first element of the array should be the second digit of the base `base` representation of the number and so on.  In other words, the zeroth element in this numpy array should be the equivalent of ![](https://render.githubusercontent.com/render/math?math=a_0) in the sum above, the second will be ![](https://render.githubusercontent.com/render/math?math=a_1), the third ![](https://render.githubusercontent.com/render/math?math=a_2) and so on.  
