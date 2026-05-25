class Solution {
public:
    vector<int> twoSum(vector<int>& a, int target) {
        sort(a.begin(), a.end());
        int n = a.size();
        int l = 0, r = n - 1;
        vector<int> res(2, 0);
        while(l <= r){
            if(a[l] + a[r] == target && a[l] != a[r]){
                res[0] = l + 1;
                res[1] = r + 1;
                return res;
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
