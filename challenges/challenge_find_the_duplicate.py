# def find_duplicate(nums):
#     if len(nums) == 1 or nums == []:
#         return False

#     num_list = []
#     count_list = []

#     for index in nums:
#         if index is str:
#             return False
#         elif index not in num_list:
#             num_list.append(index)
#         elif index not in count_list:
#             count_list.append(index)

#     if len(count_list) == 1 and count_list[0] >= 0:
#         return count_list[0]
#     else:
#         return False
