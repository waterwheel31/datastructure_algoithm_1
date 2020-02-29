#### Data Structure and Algorithms Udacity Nanodegree Small Exercises 1


Folloiwngs is the comments on the order of run time 

- Task0 - O(1). The run time wont be affected by the number of inputs
- Task1 - O(n). Since there are several for loop for each data to add and search in a list. The run time is linear
- Task2 - O(n). This does not use sorting
- Task3 A - O(n log n). This uses SampleSort (list.sort())
- Task3 B - O(n). Check each call once at maximum
- Task4  - O(n ^ 2). For each phonenumber, check all phonenumber in another set. So the runtime order  is n ^ 2, considering that the size of the both sets are close. There is also SampleSort, but O(n ^ 2) has larger impact than O(n log n)