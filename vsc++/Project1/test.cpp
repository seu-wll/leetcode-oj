#include<iostream>
#include<vector>
using namespace std;


int search(vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;
    while (left <= right) {
        int middle = (left + right) / 2;
        if (nums[middle] > target) {
            right = middle - 1;
        }
        else if (nums[middle] < target) {
            left = middle + 1;
        }
        else {
            return middle;
        }
    }
    return -1;
}


int main() {
    vector<int> nums;
    int tmp;
    int i = 0;
    while (cin >> tmp) {
        cout << i++<<endl;
        nums.push_back(tmp);
        if (cin.get() == '\n') {
            cin >> tmp;
            break;
        }
    }
    cout << search(nums,tmp) ;
}