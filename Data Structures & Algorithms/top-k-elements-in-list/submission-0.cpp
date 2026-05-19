class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> cnt;
        for(auto x : nums){
            cnt[x]++;
        }
        vector<pair<int,int>> v;
        for(auto x : cnt){
            v.push_back({x.first, x.second});
        }
        sort(v.begin(), v.end(), [](pair<int,int> a, pair<int,int> b) {
            return a.second > b.second;
        });
        vector<int> res;
        int dem = 0;
        for(auto x : v){
            if(dem < k){
                dem++;
                res.push_back(x.first);
            }
        }
        return res;
    }
};
