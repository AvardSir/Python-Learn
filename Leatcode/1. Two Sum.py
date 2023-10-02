def try1():

    class Solution:
        def twoSum(self, nums, target):



            List_more = []
            List = nums
            for i in range(len(List)):
                List_more.append([List[i], i])
            List_more.sort(reverse=True)
            sum = 0
            test_sum = 0
            index_list = []
            for i in List_more:  # перебор
                test_sum += i[0]  # добавление числа
                if test_sum > target:  # если больше цели то уменшим
                    test_sum -= i[0]
                else:
                    sum = test_sum  # сумма прибавляется
                    index_list.append(int(i[1]))
                if sum == target:
                    return index_list
            return None


    Solution_example: Solution = Solution()


    list_ek=[0,4,3,0]

    #print(list_ek)
    targettt=0
    print(Solution_example.twoSum(list_ek,targettt))

def try_with_list():

    list_taks=[[list_taks[i],i] for i in range(len(list_taks))]

    list_taks.sort()
    print(list_taks)
def task():
    list_taks = [0, 4, 3, 0]
    target = 0
    dict_taks=dict()

    for i in range(len(list_taks)):
        dict_taks[list_taks[i]]=i


    for i in range(len(list_taks)):
        temp=target
        temp-=list_taks[i]
        if temp in dict_taks and i!=dict_taks[temp]:
           return [i,dict_taks[temp]]

#print(task())##########a lost my gf what i can do later?# Ohhh  Realy im good in every litle fthon

import random
