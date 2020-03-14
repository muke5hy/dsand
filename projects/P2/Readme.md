# Problem 1: Finding the Square Root of an Integer
## Analysis:
### Time Complexity: 
The time complexity is O(log(n)). Refer Design Choices section.

### Space Complexity:
The space complexity is O(1). No additional space is required to execute this algorithm.

### Design Choices:
I chose to alternate between finding upper and lower bounds in once iteration. This makes it slightly more efficient than finding first the upper bound in one loop and lower bound in another loop. This generally saves at least one iteration. I update the midpoint after calculating the upper and lower bounds. Then based on the value of the upper bound compared to the delta, I scale accordingly. In this case, It may reduce the upper bound by more than half in each of the first few steps saving unnecessary iterations. Once the delta gets to 0 or 1, then the answer is returned.



# Problem 2: Search in a Rotated Sorted Array

## Analysis:
### Time Complexity:
The time complexity is O(log(n)). Refer Design Choices section.

### Space Complexity:
The space complexity is O(log(n)). The input_list gets split into 2.

### Design Choices:
I chose to do a binary search splitting each list into left and right halves until finding the number provided as an input.


# Problem 3: Rearrange Array Elements
## Analysis:

### Time Complexity:
The time complexity is O(nlog(n)). Refer Design Choices section.

### Space Complexity:
The space complexity is O(n). Additional space is required to sort. I could have chosen other sorting algorithms such as heapsort or quicksort that would only take O(1).

### Design Choices:
Since there was no space complexity constraints, I chose to use mergesort to solve this problem. The list is sorted in ascending order and then I take generate the maximum sum numbers. Per the suggestion of the reviewer, he/she mentioned there is a way to optimize the solution up to O(n) time complexity. I believe this to be using a hashmap to count the frequencies and then use a loop to count down from 9 -> 1 since hashmap lookups are O(1) and a loop would be O(n). That would be more efficient than what I implemented. I also wanted to implement merge sort so I took that approach.


# Problem 4: Dutch National Flag Problem
## Analysis:
### Time Complexity:
The time complexity is O(n). Refer Design Choices section.

### Space Complexity:
The space complexity is O(1). No additional space is required to execute this algorithm.

### Design Choices:
For this problem, it relies on a pivot point (midpoint). While the midpoint is not equal to the endpoint, the start and end indicies are used index into the input list. Depending on the value, the indecies will be adjusted to continue sorting the list.


# Problem 5: Building a Trie in Python
## Analysis:

### Time Complexity:
The time complexity is split into there for insert, find and suffixes. Refer Design Choices section.

### Space Complexity:
The space complexity is split into there for insert, find and suffixes. Refer Design Choices section.

### Design Choices:
I used a Trie with DFS In-order search. This was tricky, but the best way to approach this problem since we had to traverse all the nodes for a given input prefix to find all the suffixes related to it. Time complexity for insert and find is O(n) to loop through each char in word. Space complexity for insert and find is O(mn) where m is the word inserting/finding and n is the total number of words.

Time complexity for suffixes is O(V + E) where V is the vertices and E is the edges. In theory, each branch could be traversed. Space complexity for suffixes is O(bm) where b is the branches to travel and m is the longest word.


# Problem 6: Max and Min in a Unsorted Array
## Analysis:

### Time Complexity:
The time complexity is O(n). Refer Design Choices section.

### Space Complexity:
The space complexity is O(1). No additional space is required to execute this algorithm.

### Design Choices:
There was nothing clever to do here but to track the max and min while traversing through the list.





# Problem 7: HTTPRouter using a Trie

## Analysis:

### Time Complexity:
The time complexity is O(1). Refer Design Choices section.

### Space Complexity:
The space complexity is O(1). No additional space is required to execute this algorithm.

### Design Choices:
This was implemented using a Trie and Node per the suggestion and sample code for this problem. This was similar conceptually to Problem 5, but the main difference is that there is a specific handler to trigger on the lookup if found or return the not found handler. The handler splits the path to insert a new node which can then be traversed for the lookup.