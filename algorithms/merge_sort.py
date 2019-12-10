
## Vijayarajan Govindarajan 2019

def merge_lists(left_list, right_list):
    if left_list == None:
        return right_list
    if right_list == None:
        return left_list

    left_length = len(left_list)
    left_index = 0
    right_length = len(right_list)
    right_index = 0
    total_length = left_length + right_length
    merged_list = []

    for i in range(0, total_length):
        if left_index is None and right_index is None:
            return merged_list
        if left_index is None:
            merged_list.append(right_list[right_index])
            right_index += 1
        elif right_index is None:
            merged_list.append(left_list[left_index])
            left_index += 1
        elif left_list[left_index] <= right_list[right_index]:
            merged_list.append(left_list[left_index])
            left_index += 1
        elif left_list[left_index] > right_list[right_index]:
            merged_list.append(right_list[right_index])
            right_index += 1

        if left_index == left_length:
            left_index = None
        if right_index == right_length:
            right_index = None

    return merged_list

def sort_list(given_list):
    if len(given_list) == 0:
        return None
    if len(given_list) == 1:
        return given_list

    if len(given_list) == 2:
        if given_list[0] <= given_list[1]:
            return given_list
        else:
            new_list = [given_list[1], given_list[0]]
            return new_list

    if len(given_list) > 2 :
        slice_end = len(given_list)
        slice_mid = slice_end//2
        left_list = given_list[0:slice_mid]
        right_list = given_list[slice_mid:slice_end]

        left_sorted_list = sort_list(left_list)
        right_sorted_list = sort_list(right_list)

        sorted_list = merge_lists(left_sorted_list, right_sorted_list)

        #print("given_list=", given_list)
        #print("left_list=", left_list)
        #print("right_list=", right_list)

        #print("left_sorted_list=", left_sorted_list)
        #print("right_sorted_list=", right_sorted_list)
        #print("sorted_list=", sorted_list)
        #print("**********************************")
        return sorted_list

def main():
    testList = [1,2,12,1,45,21,34,6,46,8,9,34]
    print(testList)
    sorted_list = sort_list(testList)
    print(sorted_list)

if __name__ =="__main__":
    main()
