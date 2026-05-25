class Solution {
public:
    vector<int> twoSum(vector<int>& a, int target) {
        sort(a.begin(), a.end());
        int n = a.size();
        int l = 0, r = n - 1;
        vector<int> res;
        while(l < r){
            if(a[l] + a[r] == target){
                res.push_back(l + 1);
                res.push_back(r + 1);
                break;
            }
            if(a[l] + a[r] > target){
                r--;
            }
            else if(a[l] + a[r] < target){
                l++;
            }
        }
        return res;
    }
};
