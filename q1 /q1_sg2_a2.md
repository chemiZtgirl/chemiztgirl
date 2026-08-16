# Annex C
## Code Quality Assessment Worksheet
**Section: 9-Balingkilat &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Score:____________<br>**
**C# / Name: #16 Judy Valera&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Date: 08/16/26<br>&emsp;&emsp;&emsp;&emsp;&emsp; #17 Kairi Lian Heart Barayoga<br>&emsp;&emsp;&emsp;&emsp;&emsp; #18 Aeden Ysabel M. Bernardo**


## Instructions:

The problem: Finding the highest (Maximum) number from a given list of numbers.
| PseudoCode 1 | PseudoCode 2 |
| ----------- | ----------- |
| Algorithm FindMax1(numbers)<br>&emsp;max ← numbers[0]<br>&emsp;For i from 1 to length(numbers)-1<br>&emsp;&emsp;If numbers[i] > max Then<br>&emsp;&emsp;&emsp;max ← numbers[i]<br>&emsp;&emsp;EndIf<br>&emsp;EndFor<br>&emsp;Return max<br>EndAlgorithm | Algorithm FindMax2(numbers)<br>&emsp;For i from 0 to length(numbers)-1bigger ← true<br>&emsp;&emsp;For j from 0 to length(numbers)-1<br>&emsp;&emsp;&emsp;If numbers[j] > numbers[i] Then<br>&emsp;&emsp;&emsp;&emsp;bigger ← false<br>&emsp;&emsp;&emsp;EndIf<br>&emsp;&emsp;EndFor<br>&emsp;&emsp;If bigger = true Then<br>&emsp;&emsp;&emsp;Return numbers[i]<br>&emsp;&emsp;EndIf<br>&emsp;EndFor<br>EndAlgorithm |


## Questions with Checklists
**1. Efficiency**<br>
Which algorithm is faster when the list of numbers is very large? Why?<br>
Psuedocode 1 is faster as it uses only 1 loop and less steps, compared to psuedocode 2 which has 2 nested loops and more steps.<br>

| PseudoCode 1 | PseudoCode 2 |
|---|---|
|[x] Does the algorithm use one loop*?|[ ] Does the algorithm use one loop?|
|[ ] Does the algorithm repeat work unnecessarily?|[x] Does the algorithm repeat work unnecessarily?|
|[x] Which algorithm finishes in fewer steps?|[ ] Which algorithm finishes in fewer steps?|

**2. Readability**<br>
Which algorithm is easier to understand at first glance? What makes it clearer?<br>
Pseudocode 1 is easier to understand at first glance, as it has meaningful variables, less lines, and simple structure.<br>

| PseudoCode 1 | PseudoCode 2 |
|---|---|
|[x] Are variable names meaningful (e.g., max vs. bigger)?|[ ] Are variable names meaningful (e.g., max vs. bigger)?|
|[x] Is the logic simple?|[ ] Is the logic simple?|
|[x] Are there fewer lines of code?|[ ] Are there fewer lines of code?|

**3. Maintainability**<br>
If you had to add a new feature (like finding both max and min), which algorithm would be easier to update? Why?<br>
Pseudocode 1 would be easier to update because its structure is straightforward and has fewer conditions and loops. Adding features such as finding both the maximum and minimum would be easier to navigate and edit.

| PseudoCode 1 | PseudoCode 2 |
|---|---|
|[x] Is the structure straightforward?|[ ] Is the structure straightforward?|
|[ ] Would adding new steps break the code easily?|[x] Would adding new steps break the code easily?|
|[x] Is there less chance of errors when updating?|[ ] Is there less chance of errors when updating?|

**4. Testability**<br>
Which algorithm is easier to test with different inputs? Why?<br>
Pseudocode 1 is easier to test using various inputs since it has less conditions and a predictable output, making it easier to fix and track.

| PseudoCode 1 | PseudoCode 2 |
|---|---|
|[x] Can you test with small lists easily?|[ ] Can you test with small lists easily?|
|[x] Does the algorithm have fewer conditions to check?|[ ] Does the algorithm have fewer conditions to check?|
|[x] Is the output predictable and clear?|[ ] Is the output predictable and clear?|

**5. Security**<br>
Imagine the input list comes from a user. What should the algorithm check to avoid errors or misuse?<br>
Both algorithms should check whether the input is empty and whether all inputs are valid to the code. They should also be able handle unusual inputs without crashing.

| PseudoCode 1 | PseudoCode 2 |
|---|---|
|[ ] Does the algorithm check if the list is empty?|[ ] Does the algorithm check if the list is empty?|
|[ ] Does it handle invalid inputs (like letters instead of numbers)?|[ ] Does it handle invalid inputs (like letters instead of numbers)?|
|[ ] Does it avoid crashing when inputs are unusual?|[ ] Does it avoid crashing when inputs are unusual?|

**6. Final Answer**<br>
Based on your answers from 1 to 5, which one is the better algorithm that you will use to solve the problem of finding the highest number? Why? Summarize your answer.<br>
Both psuedocodes are lacking in security, but I would prefer using psuedocode 1 to solve the problem, since it is more efficient and fast to use compared to psuedocode 2, <br>
as it is easier to fix and test due to its fewer lines of code, meaningful variables, the usage of only 1 loop, and simple structure overall.

