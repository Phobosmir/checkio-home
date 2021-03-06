"""
"Your power to choose can never be taken from you.
It can be neglected and it can be ignored.
But if used, it can make all the difference."
― Steve Goodier

You have a histogram. Try to find size of the biggest rectangle you can build out of the histogram bars.



Input: List of all rectangles heights in histogram

Output: Area of the biggest rectangle

Example:

largest_histogram([5]) == 5
largest_histogram([5, 3]) == 6
largest_histogram([1, 1, 4, 1]) == 4
largest_histogram([1, 1, 3, 1]) == 4
largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8

How it is used: There is no way the solution you come up with will be any useful in a real life. Just have some fun here.

Precondition:
0 < len(data) < 1000
"""

def largest_histogram_own(histogram):
    max_hor_area = 0

    values_in_scope = [(0, 0)]

    max_vert_value = 0
    max_vert_length = 0

    histogram.append(0)
    for cur_val_index, cur_val in enumerate(histogram, start=1):
        prev_index, prev_val = values_in_scope[-1]
        #increasing
        if cur_val > prev_val:
            values_in_scope.append((cur_val_index, cur_val))
        #cont.
        elif cur_val == prev_val:
            pass
        #decreasing
        else:
            while cur_val < values_in_scope[-1][1]:
                prev_index, prev_val = values_in_scope.pop()
                prev_value_length = cur_val_index - prev_index
                area = prev_value_length*prev_val
                if area > max_hor_area:
                    max_hor_area = area
            if values_in_scope[-1][1] != cur_val:
                values_in_scope.append((prev_index, cur_val))

        # For max vertical area
        if cur_val > max_vert_value:
            max_vert_value = cur_val
            max_vert_length = 1
        elif cur_val == max_vert_value and cur_val == histogram[cur_val_index-2]:
            max_vert_length += 1


    max_vert_area = max_vert_length*max_vert_value

    return max(max_vert_area, max_hor_area)



def largest_histogram(histogram):
    max_size = 0
    for i in range(0,len(histogram)) :
        f = i
        b = i
        num = 1
        while histogram[f-1] >= histogram[i] and f>0:
            f-=1
            num+=1
        while b<(len(histogram)-1) and histogram[b+1] >=histogram[i]:
            b+=1
            num+=1
        size = num*histogram[i]
        max_size = max(size,max_size)
    return max_size


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    assert largest_histogram([1, 2, 3, 0, 1, 2, 3, 2, 1, 0, 3, 2, 1]) == 6, "complex"

    assert largest_histogram([70,60,67,78,89,87,74,40,100,24,66,84,11,99,4,34,21,23,66,34,47,54,51,88,53,7,94,72,28,59,30,44,0,17,96,34,63,6,81,61,26,96,72,5,32,57,1,3,47,13,97,96,9,7,80,5,89,77,7,75,63,59,90,88,16,48,93,33,70,35,57,15,61,81,63,83,33,3,55,63,86,33,94,45,76,99,86,14,96,81,33,32,76,37,56,54,63,11,82,41,90,81,53,42,89,75,98,74,18,73,7,30,10,14,67,59,25,56,41,90,80,17,84,16,45,6,29,87,79,56,33,94,73,72,31,18,30,17,81,64,92,3,94,12,65,23,50,54,52,16,19,39,26,12,75,19,11,69,48,25,64,6,22,19,19,29,41,90,43,41,36,66,91,23,28,4,15,94,89,6,87,4,98,19,12,54,3,66,84,83,28,95,3,55,44,64,86,15,15,37,89,65,100,9,11,6,38,26,62,89,14,29,81,94,47,63,71,56,31,96,68,30,96,77,32,28,82,39,75,67,73,83,70,70,74,50,89,98,27,50,2,42,46,11,59,60,96,90,20,14,92,20,59,8,16,23,69,41,7,64,66,38,30,47,87,82,73,12,82,0,45,100,59,10,42,19,21,22,17,67,33,69,12,100,14,11,20,43,30,20,93,43,14,28,68,55,89,57,48,97,95,88,4,41,61,45,91,0,22,57,40,18,21,97,51,36,67,14,22,6,57,11,31,48,45,83,97,60,14,32,27,65,24,48,94,63,25,50,52,91,55,81,96,33,89,82,21,8,100,93,100,47,18,80,88,81,1,10,81,25,68,95,81,95,53,93,79,23,9,87,63,95,4,68,42,73,16,29,27,44,3,48,90,92,46,66,81,58,98,64,90,95,64,46,73,40,74,67,32,59,61,89,96,42,47,97,70,22,78,70,2,67,39,59,76,78,41,23,84,52,88,89,88,4,17,48,3,41,30,14,30,92,65,87,79,84,21,57,19,62,19,50,13,27,21,83,25,19,72,50,40,12,4,43,60,41,46,45,92,93,16,54,29,38,42,53,93,2,44,98,79,25,34,3,69,74,21,100,92,61,100,22,23,74,70,76,18,10,50,68,96,83,95,69,90,49,61,93,51,55,47,87,53,50,80,31,76,0,64,74,68,11,18,85,99,67,71,88,87,72,10,58,31,82,49,70,10,84,79,23,5,53,25,36,9,33,71,48,4,14,51,71,58,44,17,53,87,62,41,80,90,0,36,48,75,67,28,82,34,75,93,63,66,72,54,41,68,67,82,77,36,74,16,4,96,39,61,64,92,78,86,21,87,43,81,94,76,31,18,50,59,66,57,34,77,27,57,66,65,17,25,90,78,23,52,31,28,71,93,95,62,23,99,48,36,85,22,13,33,13,33,67,63,100,52,94,97,83,45,88,65,9,31,30,97,9,71,45,39,15,39,79,25,62,69,1,30,26,25,74,35,5,22,72,25,3,15,52,94,87,37,46,9,58,90,14,46,39,44,60,53,5,18,12,69,25,55,37,85,3,43,75,20,9,35,1,60,58,83,77,60,75,7,91,76,95,48,91,83,50,3,85,42,31,68,48,94,37,96,89,43,40,24,43,72,8,49,93,26,74,82,63,41,82,74,58,46,39,30,3,58,84,68,84,1,18,26,26,18,40,59,29,22,73,1,74,33,62,73,12,1,43,72,33,44,24,63,18,65,93,18,28,91,87,15,24,84,96,87,6,48,14,99,79,75,25,68,53,26,27,63,74,75,96,94,7,100,91,77,96,32,34,42,19,2,0,68,21,55,21,20,48,84,1,63,96,2,52,53,99,90,82,50,46,23,49,33,26,55,100,37,92,11,70,60,61,30,35,26,10,69,90,54,46,58,96,65,49,8,89,74,52,29,60,93,51,47,27,72,42,12,51,36,34,26,62,13,81,20,97,52,25,44,41,90,18,7,34,99,98,40,49,100,16,84,93,10,35,75,78,96,13,83,38,66,61,26,83,34,13,59,89,22,35,41,45,25,42,69,95,40,43,1,65,44,18,25,81,87,86,43,90,64,16,88,49,6,21,80,89,71,63,25,47,91,93,8,42,61,67,22,67,96,69,45,100,41,48,72,96,3,18,30,37,85,51,84,75,10,99,74,84,91,58,6,8,13,50,94,39,19,73,70,96,0,18,58,29,100,84,92,91,46,48,4,33,60,35,14,45,43,6,42,30,91,0,71,100,55,14,9,99,100,31,83,6,37,48,57]) == 832
    print("Done! Go check it!")


