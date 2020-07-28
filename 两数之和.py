def twoSum(nums, target):
    #建立一个空字典
    hashmap = {}
    #enumerate函数用于将一个可遍历的数据对象组合为一个索引序列(index, value)
    for i,num in enumerate(nums):

        if hashmap.get(target - num) is not None:

            return [i, hashmap[target-num]]
        #index取代value
        hashmap[num]=i
#主函数调试
if __name__ == '__main__':
    nums=[2,7,11,15]
    target = 9
    print(twoSum(nums, target))

