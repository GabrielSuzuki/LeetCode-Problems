#include <map>
class Solution {
public:
    void sortColors(vector<int>& nums) {
        map<int,int> numDict;
        for (int i = 0;i<nums.size();i++) {
            if (numDict.count(nums[i]) == 0) {
                numDict[nums[i]] = 1;
            }
            else numDict[nums[i]] += 1;
        }
        int count = 0;
        map<int, int>::iterator it = numDict.begin();
        while (it != numDict.end()){
            for(int j = 0; j < it->second;j++){
                nums[count] = it->first;
                count += 1;
            }
            it++;
        }
    }
};