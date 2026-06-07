class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        unordered_map<char, int> cnt;

        for(auto c : s) cnt[c]++;

        for(auto c : t){
            if(cnt[c] == 0){
                return false;
            }
            cnt[c] -= 1;
        }
        return true;
    }
};
