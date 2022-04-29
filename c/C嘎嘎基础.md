参考资料

【C++库使用基础】：https://blog.csdn.net/huwei039/article/details/104269486

【代码随想录】：https://programmercarl.com/

【OJ输入输出基础总结】：https://blog.csdn.net/m0_38059875/article/details/105205096

【输入输出练习】：https://ac.nowcoder.com/acm/contest/5652

一点点感想：

python和c++的刷题的速度大约是2:1的关系，但是最后的执行的速度上有接近10:1的差距。

---

初始化相关。

一维数据初始化：

```
int record[26] = {0};
```

C++ 相关计算

```
13 / 5 = 2 # 设定好类型就是整除了
13 % 5 = 3
int(12.5) = 12
ceil(12.5) = 13
floor(12.5) = 12
```

数学计算标准库

```c++
#include <math.h>
//平方 pow()
int a = pow(4,2);// 4的平方=16
//开方
int b = pow(4,0.5);// 4的平方根=2
int c = sqrt(4);// 4的平方根=2
//整数绝对值
int c = abs(b-c);
//浮点数绝对值
double d = fabs(b-c);

```

map

找对应的值：```map.find(a)->second;`` ,```mao[a]```都是可以的表达

#### 容器的方法浏览

|                                            | vector | deque | queue | stack | set        | string(不是容器) |
| ------------------------------------------ | ------ | ----- | ----- | ----- | ---------- | ---------------- |
| size()                                     | 1      | 1     | 1     | 1     | 1          | 1                |
| capacity()                                 | 1      |       |       |       |            |                  |
| resize(n,2) 重新赋值大小                   | 1      | 1     |       |       |            |                  |
| resize(n) 重新赋值长度                     | 1      | 1     |       |       |            |                  |
| front() 返回开始的节点                     | 1      | 1     | 1     |       |            | 1                |
| back() 返回最后的节点                      | 1      | 1     | 1     |       |            | 1                |
| clear() 清空整个向量                       | 1      | 1     |       |       | 1          |                  |
| insert(k,n) 在k位置插入n                   | 1      | 1     |       |       | 1 # 单参数 | 1                |
| erase(m,n) 只有m，删除m。mn删除[m,n]的区间 | 1      | 1     |       |       | 1          | 1                |
| push_back()                                | 1      | 1     |       |       |            | 1                |
| pop_back()                                 | 1      | 1     |       |       |            | 1                |
| pop_front()                                |        | 1     |       |       |            |                  |
| empty()                                    | 1      | 1     | 1     | 1     | 1          | 1                |
| top()                                      |        |       |       | 1     |            |                  |
| pop()                                      |        |       | 1     | 1     |            |                  |
| push()                                     |        |       | 1     | 1     |            |                  |
| count()                                    |        |       |       |       | 1          |                  |
| find()                                     |        |       |       |       | 1          | 1                |

#### 常见的算法

```
sort(begin,end)

reverse(begin,end)
```



#### string与数之间的转换

```c++
// string to int|float|long
int a = b //定义变量法。b 是 string  
stoi(b)  //直接转换法。
stol(b) // 转long
stof(b) // 转float
    
// int to string
string to_string(-12);
```

#### 优先级队列

```c++
//自定义优先级队列的模式
    class mycomparison {
    public:
        bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {
            return lhs.second > rhs.second;
        }
    };
//第三个参数可以理解为判定关系的方法，用这样的方法构造的是小根堆。
	priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison> pri_que;
```

c++优先级队列：https://blog.csdn.net/weixin_36888577/article/details/79937886

#### Map的遍历

```c++
for (unordered_map<int, int>::iterator it = map.begin(); it != map.end(); it++)
```

#### .和->的区别

箭头（->）：左边必须为指针；
点号（.）：左边必须为实体。
