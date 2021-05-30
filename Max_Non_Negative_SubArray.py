""" 
Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.

Example
Input 1:

 A = [1, 2, 5, -7, 2, 3]

Output 1:

 [1, 2, 5]

Explanation 1:

 The two sub-arrays are [1, 2, 5] [2, 3].
 The answer is [1, 2, 5] as its sum is larger than [2, 3].

"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(A):
        maxsumlist = []
        cursumlist = []
        maxsum = 0
        currsum = 0
        for i in A:
            if (i >= 0):
                currsum = currsum + i
                cursumlist.append(i)
                #print(currsum)
                #print(maxsum)
                if(currsum > maxsum):
                    maxsum = currsum
                    maxsumlist = cursumlist
                elif(currsum == maxsum):
                    if(len(cursumlist) > len(maxsumlist)):
                        maxsumlist = cursumlist

            elif(i<0):
                currsum = 0
                cursumlist = []

        return maxsumlist
