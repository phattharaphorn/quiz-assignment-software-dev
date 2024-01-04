def min_total_marks(n, marks:list):
    marks.sort()
    start_min = marks[0]

    while n>0:
        get = marks.count(marks[0]) 
        second_min = next((x for x in marks if x != marks[0]), marks[0])
        if(second_min==marks[0]):
            return marks[0]+n/len(marks)-start_min
        difference = second_min-marks[0]
        if get*difference<n:
            temp = ([second_min] * get) + marks[get:]
            n-=difference*get
            marks = sorted(temp)
        else:
            return n/get-start_min+marks[0]

# Example 
input1 = 3
input2 = [1, 6, 2]
print(min_total_marks(input1, input2)) 
'''
1 3 4 4 5 
2 3 4 4 5             b1
3 3 4 4 5             b2
3.5 3.5 4 4 5         b3
4 4 4 4 5             b4
4.25 4.25 4.25 4.25 5 b5
'''