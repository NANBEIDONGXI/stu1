# def insert_sort(lst):
#     lst = [1,9,8,5,6]
'''
直接插入排序 Direct insert sort
最好的情况，正好是升序排列，比较迭代n-1次
最差情况，正好是降序排列，比较迭代1,2,3....n-1即n(n-1)/2
使用两层嵌套循环，时间复杂度O(n^2)
稳定排序算法
使用在小规模数据比较
优化：如果比较操作耗时大的话，可以采用二分查找
来提高效率，即二分查找插入排序
'''
origin = [1,9,8,5,6]
nums = [0] + origin
length = len(nums)
for i in range(2,length):
    nums[0] = nums[i]
    j = i -1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -=1
        nums[j+1] = nums[0]
print(nums)
print(nums[1:])

