
'''
堆相关:
构建一个大根堆
删除元素
添加元素
堆排序
'''
# https://www.jianshu.com/p/d174f1862601

# 构造堆，默认是小根堆
def build_heap(array):
    array_len=len(array)
    for i in range(array_len//2,0,-1):
        headadjust(array,i,array_len)
#调整头节点
def headadjust(array,k,array_len):
    array[0]=array[k]


