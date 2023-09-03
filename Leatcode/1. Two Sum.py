class Solution:
    def twoSum(self, nums, target):

        print(nums)
        print(target)

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


list_ek=[1,2]
#print(list_ek)
targettt=3
print(Solution_example.twoSum(list_ek,targettt))
