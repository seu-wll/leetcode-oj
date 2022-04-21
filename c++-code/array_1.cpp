// 本节记录与数组相关的所有的代码的写法，仅用于记忆
#include <iostream>
#include <vector>
using namespace std;


int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size()-1;
        while (left<=right){
            int middle = (left + right)/2;
            if (nums[middle]>target){
                right = middle -1 ;
            }else if (nums[middle]<target){
                left=middle +1;
            }else{
                return middle;
            }
        } 
    return -1;
}

int main(){
    int a[] = {1,4,5,8,9,10};
    vector<int> vec(a, a + sizeof(a) / sizeof(int));
    cout << search(vec,9) << endl;   
}