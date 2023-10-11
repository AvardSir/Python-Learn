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
def task_of_kurs():

    import random
    viborka=1000000
    sum=0
    for i in range(1,1000000):

        num=random.randint(1,100)
        if num<=63:
            sum+=80000
        elif num>63 and num<63+25:
            sum+=155000
        elif num>63+25:
            sum+=250000
    sredne_znach=sum/viborka
    print(sredne_znach)
#not today today is lab
#many big math static
#understad what pause in Speak can Help you with More simple Understad you
#not its procrastin
# i do videios!
#print((4117+12)%65+1)
string_o='word'

for i in range(-len(string_o),0,1):
    print(string_o[i])

#so sad so alone

#Жизнь дана чтоб жить. И жизнь важнее програмариования? даж если умру в нищете..