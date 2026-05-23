class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int> res(nums.begin(), nums.end());
        int longest = 0;
        for(auto x : res){
            if(res.find(x - 1) == res.end()){
                int len = 1;
                while(res.find(x + len) != res.end()){
                    len++;
                }
                longest = max(longest, len);
            }
        }
        return longest;
    }
};
