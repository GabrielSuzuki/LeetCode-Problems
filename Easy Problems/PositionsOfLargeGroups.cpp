class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        int start = 0;
        int end = 1;
        vector<vector<int>> output;
        vector<int> input;
        for (int i = 1; i < s.size();i++){
            if (s[i] != s[i-1]) {
                if (end-start >= 3) {
                    input.push_back(start);
                    input.push_back(end-1);
                    output.push_back(input);
                    input.clear();
                }
                start = i;
                end = i + 1;
            }
            else {
                end = end + 1;
            }
        }
        if (end- start >= 3) {
            input.push_back(start);
            input.push_back(end-1);
            output.push_back(input);
            input.clear();
        }
        return output;
    }
};