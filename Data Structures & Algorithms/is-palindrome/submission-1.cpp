class Solution {
public:
    bool isPalindrome(string s) {
        string res;
        for(int i = 0; i < s.size(); i++){
            if(isalpha(s[i]) || isdigit(s[i])){
                if(isalpha(s[i]))
                    res += tolower(s[i]);
                else{
                    res += s[i];
                }
            }
        }
        int l = 0, r = res.size() - 1;
        while(l <= r){
            if(res[l] != res[r]){
                return false;
            }
            l++; r--;
        }
        return true;
    }
};
