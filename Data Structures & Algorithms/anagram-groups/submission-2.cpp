class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> cnt;
        for(auto s : strs){
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            cnt[sortedS].push_back(s);
        }
        vector<vector<string>> res;
        for(auto s : cnt){
            res.push_back(s.second);
        }
        return res;
    }
};
