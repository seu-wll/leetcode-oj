'''
**基本的排序算法**
1. 冒泡排序（Bubble Sort）
2. 插入排序（Insertion Sort）

**常考的排序算法**
1. 归并排序（Merge Sort）
2. 快速排序（Quick Sort）
3. 拓扑排序（Topological Sort）图那边的，这里不实现。

**其他排序算法**
1. 堆排序（Heap Sort）
2. 桶排序（Bucket Sort)
'''

# 冒泡排序
from logging.config import dictConfig

from pandas import pivot


def bubble_sort(array):
    array_len=len(array)
    for i in range(array_len-1):
        for j in range(array_len-i-1):
            if array[j]>array[j+1]:
                tmp=array[j]
                array[j]=array[j+1]
                array[j+1]=tmp 


# 插入排序
def insert_sort(array):
    array_len=len(array)
    for i in range(1,array_len):
        for j in range(i,0,-1):
            if array[j]<array[j-1]:
                tmp=array[j]
                array[j]=array[j-1]
                array[j-1]=tmp

# 归并排序
def merge_sort(array):
    # 合并算法
    def merge(array1,array2):
        # 记录array1，array2当前的位置
        i,j=0,0
        merge_array=[]
        while i<len(array1) and j < len(array2):
            if array1[i]<array2[j]:
                merge_array.append(array1[i])
                i+=1
            else:
                merge_array.append(array2[j])
                j+=1
        while i<len(array1):
            merge_array.append(array1[i])
            i+=1
        while j<len(array2):
            merge_array.append(array2[j])
            j+=1       
        return merge_array

    # 归并过程
    if len(array)>1:
        mid=len(array)//2
        array1=merge_sort(array[:mid])
        array2=merge_sort(array[mid:])
        return merge(array1,array2)
    else:
        return array

# 快速排序
# 单次排序把数组划分到pivot的两端，递归地继续排序
def quick_sort(array,low,high):
    def partation(array,low,high):
        pivot=array[low]
        while high>low:
            while array[high]>=pivot and high>low:
                high-=1
            array[low]=array[high]
            while array[low]<=pivot and  high>low:
                low+=1
            array[high]=array[low]
 
        array[low]=pivot
        return low
    if high>low:
        pivot_pos=partation(array,low,high)
        quick_sort(array,low,pivot_pos-1)
        quick_sort(array,pivot_pos+1,high)


from collections import heapq

# 桶排序
#大致思想就是分桶，然后每个数据如桶的时候直接用插入排序进行一个维护直接排序。
def bucket_sort(array,bucket_num,low,high):

    bucket_dic={}

    for i in array:
        bucket_index=i*bucket_num//(high-low)
        # 初始化各个桶
        if bucket_index not in bucket_dic:
            bucket_dic[bucket_index]=[i]
        # 值分桶
        else:
            bucket=bucket_dic[bucket_index]
            bucket.insert(0,i)
            for j in range(len(bucket)-1):
                if bucket[j]>bucket[j+1]:
                    tmp=bucket[j]
                    bucket[j]=bucket[j+1]
                    bucket[j+1]=tmp
    array_sort=[]
    for i in bucket_dic.keys():
        array_sort+=bucket_dic[i]
    return array_sort

#堆排序
#放到堆的实现里面了，需要先构造出一个堆然后再做别的。





array=[1,3,5,1,2,3,4,8,1,3,7,3,2]

#桶排序
bucket_sort_array=bucket_sort(array,bucket_num=3,low=0,high=10)
print(bucket_sort_array)

# 快速排序
# quick_sort(array,0,len(array)-1)
# print(array)

# 归并排序
# merge_sort_array=merge_sort(array)
# print(merge_sort_array)

# 插入排序
# insert_sort(array)
# print(array)

# 冒泡排序
# bubble_sort(array)
# print(array)




