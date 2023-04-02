class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int max1 = 0;
        int int1 = 0;
        int max2 = 0;
        for (int i = 0; i < nums.size();i++) {
            if (max1 < nums[i]) {
                max2 = max1;
                max1 = nums[i];
                int1 = i;
            }
            else {
                if (max2 < nums[i]){
                    max2 = nums[i];
                }
            }
        }
        if (max1 >= max2 * 2) {
            return int1;
        }
        return -1;
    }
};