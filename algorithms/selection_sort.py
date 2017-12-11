#https://runestone.academy/runestone/static/pythonds/SortSearch/TheSelectionSort.html
# Vijayarajan Govindarajan 2017
'''
The selection sort improves on the bubble sort by making only one exchange for every pass through the list.
 In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass,
  places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct
   place. After the second pass, the next largest is in place. This process continues and requires n−1n−1 passes to
    sort n items, since the final item must be in place after the (n−1)(n−1) st pass.
'''

#In memory swap, no return value
def selection_sort(given_list):
    list_len = len(given_list)
    for final_position in range(list_len-1,0,-1):
        swap_value = given_list[final_position]
        swap_position = final_position
        should_swap = False
        for i in range(0,final_position):
            if given_list[i] > swap_value:
                swap_position = i
                swap_value = given_list[i]
                should_swap = True

        if should_swap:
            temp = given_list[final_position]
            given_list[final_position] = given_list[swap_position]
            given_list[swap_position] = temp


def main():
    num_list = [12,21,33,1,25,63,87,4,5,9,50,23]
    print(num_list)
    selection_sort(num_list)
    print(num_list)


if __name__ == "__main__":
    main()