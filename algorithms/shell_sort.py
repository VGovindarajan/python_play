#https://runestone.academy/runestone/static/pythonds/SortSearch/TheShellSort.html
# Vijayarajan Govindarajan 2017
'''
The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort by breaking
 the original list into a number of smaller sublists, each of which is sorted using an insertion sort.
  The unique way that these sublists are chosen is the key to the shell sort. Instead of breaking the list
   into sublists of contiguous items, the shell sort uses an increment i, sometimes called the gap,
    to create a sublist by choosing all items that are i items apart.
'''

def skip_insertion_sort(given_list, start_position,skip_count):

    for list_index in range(start_position+skip_count, len(given_list), skip_count):
        #print("list_index",list_index, "given_list[list_index]", given_list[list_index])
        index_to_insert = list_index
        value_to_insert = given_list[list_index]
        for current_index in range(list_index, start_position, -skip_count):
            #value_to_insert = given_list[list_index]
            #index_to_insert = list_index
            #print("current_index",current_index-skip_count, "given_list[current_index-skip_count]", given_list[current_index-skip_count], "value_to_insert",value_to_insert)
            if given_list[current_index-skip_count] >= value_to_insert:
                index_to_insert = current_index-skip_count

        temp = given_list[index_to_insert]
        given_list[index_to_insert] = value_to_insert
        given_list[list_index] = temp
        #given_list.remove(value_to_insert)
        #given_list.insert(index_to_insert, value_to_insert)
        #print(given_list)


def skip_insertion_sort_while(given_list, start_position,skip_count):

    for list_index in range(start_position+skip_count, len(given_list), skip_count):
        #print("list_index",list_index, "given_list[list_index]", given_list[list_index])
        index_to_insert = list_index
        value_to_insert = given_list[list_index]
        while index_to_insert >= skip_count and given_list[index_to_insert-skip_count] > value_to_insert:
            given_list[index_to_insert] = given_list[index_to_insert-skip_count]
            index_to_insert = index_to_insert-skip_count

        given_list[index_to_insert] = value_to_insert
        #print(given_list)




def shell_sort(given_list):
    len_list = len(given_list)
    skip_count = pow(2,4)-1
    #skip_count = 1
    while skip_count > 0:
        for start_position in range(0,skip_count):
            #print("shell_sort", "start_position",start_position, "skip_count",skip_count)
            skip_insertion_sort_while(given_list, start_position, skip_count)
            #print("Check ....", given_list)
        skip_count = skip_count//2
    #skip_insertion_sort(given_list, 0, 1)
    return

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
def main():
    num_list = [12,21,33,1,25,63,87,4,5,9,50,23]
    print(num_list)
    shell_sort(num_list)
    print(num_list)

    print("")

if __name__ == "__main__":
    main()