def map1():

    def add_five(x):
        return x + 5

    nums = [11, 22, 33, 44, 55]
    nums = list(map(add_five, nums))
    print(nums)
def map_with_lamda():
    nums = [11, 22, 33, 44, 55]

    result = list(map(lambda x: x+5, nums))
    print(result)


def salary_quest():

    salaries = [2000, 1800, 3100, 4400, 1500]
    bonus = int(input())

    salaries = list(map(lambda x: x+bonus, salaries))

    print(salaries)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)