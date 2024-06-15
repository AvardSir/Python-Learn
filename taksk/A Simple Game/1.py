

def plan_a():
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            s_ = dict()
            t_ = dict()

            for i in s:
                try:
                    if s_[i] != 0:
                        s_[i] += 1

                except Exception as e:
                    s_[i] = 1

            for i in t:
                try:
                    if t_[i] != 0:
                        t_[i] += 1

                except Exception as e:
                    t_[i] = 1

            if t_ == s_:
                return True
            else:
                return False

def TwoIntegerSum():
    from typing import List
    class Solution:#сам решил
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            d = dict()
            for i in range(len(nums)):
                d[nums[i]] = i
            for i in range(len(nums)):
                gett = d.get(target - nums[i], 0)
                if gett != 0 and gett != i:
                    return [i, gett]
    def cakNado():#сок жизни
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                prevMap = {}  # val -> index

                for i, n in enumerate(nums):
                    diff = target - n
                    if diff in prevMap:
                        return [prevMap[diff], i]
                    prevMap[n] = i


def stuff():

    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    def to_str( s: str):
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        return countS
    answer=[]
    for i in strs:
        answer.append(to_str(i))
    print(answer)


    it_done={}
    for i in range(len(strs)):
        if i not in it_done:
            it_done[i]=i#у нас тут словарь

print('hellp')


class hero:

    def __init__(self, name, hp,atack):
        self.name = name
        self.hp = hp
        self.atack = atack



    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")