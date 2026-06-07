class Solution {
public:
    vector<vector<int>> res;
    vector<int> path;

    void Try(vector<int>& nums, int i){
        if(i == nums.size()){
            res.push_back(path);
            return;
        }

        // Không chọn nums[i]
        Try(nums, i + 1);

        // Chọn nums[i]
        path.push_back(nums[i]);
        Try(nums, i + 1);

        path.pop_back();
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        Try(nums, 0);
        return res;
    }
};