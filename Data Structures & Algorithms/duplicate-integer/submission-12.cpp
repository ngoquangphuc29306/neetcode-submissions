class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int> cnt;
        for(int i = 0; i < nums.size(); i++){
            cnt[nums[i]]++;
        }
        for(auto x : cnt){
            if(x.second > 1){
                return true;
            }
        }
        return false;
    }
};