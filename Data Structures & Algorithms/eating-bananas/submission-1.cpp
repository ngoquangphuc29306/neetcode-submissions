class Solution {
public:
    bool F(vector<int> &piles, int hours, int k){
        int ans = 0;
        for(int i = 0; i < piles.size(); i++){
            ans += (piles[i] + k - 1) / k;
        }
        return ans <= hours;
    }


    int minEatingSpeed(vector<int>& piles, int h) {
        int max_k = 0;
        for(int i = 0; i < piles.size(); i++){
            max_k = max(max_k, piles[i]);
        }

        int left = 1, right = max_k;
        int ans = -1;

        while(left <= right){
            int mid = (left + right) / 2;

            if(F(piles, h, mid)){
                ans = mid;
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return ans;
    }
};
