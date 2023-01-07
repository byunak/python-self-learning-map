nums = [0,1,2,3,4,5,6,7,8,9,10,11,12]

for first in range(len(nums)):
    for second in range(len(nums)):
        calculate = nums[first]*nums[second]
        print(nums[first]," x ", nums[second], " = ", calculate)