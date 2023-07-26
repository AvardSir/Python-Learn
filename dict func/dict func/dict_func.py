def dict_specific():
    nums = {
      1: "one",
      2: "two",
      3: "three",
    }
    print(1 in nums)
    print("three" in nums)
    print(4 not in nums)
def get_method():

    pairs = {
       1: "apple",
       "orange": [2, 3, 4], 
       True: False, 
       12: "True",
    }

    print(pairs.get("orange"))
    print(pairs['orange'])
    print(pairs.get(7, 42))
    print(pairs.get(12345, "not found"))

    print(pairs)