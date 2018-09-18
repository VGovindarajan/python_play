#https://runestone.academy/runestone/static/pythonds/SortSearch/TheInsertionSort.html
# Vijayarajan Govindarajan 2017
'''
he insertion sort, although still O(n2)O(n2), works in a slightly different way.
 It always maintains a sorted sublist in the lower positions of the list. Each new item is then “inserted” back
 into the previous sublist such that the sorted sublist is one item larger.
'''

def insertion_sort(given_list):
    for list_index in range(1,len(given_list)):
        value_to_insert = given_list[list_index]
        index_to_insert = list_index
        for i in range(list_index,0,-1):
            if given_list[i-1] >= value_to_insert:
                index_to_insert = i-1
        given_list.remove(value_to_insert)
        given_list.insert(index_to_insert, value_to_insert)

def main():
    num_list = [12,21,33,1,25,63,87,4,5,9,50,23]
    print(num_list)
    insertion_sort(num_list)
    print(num_list)


if __name__ == "__main__":
    main()