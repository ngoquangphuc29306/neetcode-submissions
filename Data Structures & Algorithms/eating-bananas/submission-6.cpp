class Solution {
public:
    // Hàm kiểm tra: với tốc độ ăn k quả/giờ
    bool F(vector<int> &piles, int hours, int k){
        long long ans = 0; // Tổng số giờ cần để ăn hết tất cả các đống chuối
        for(int i = 0; i < piles.size(); i++){
            // Số giờ cần để ăn hết đống này là ceil(piles[i] / k)
            ans += (piles[i] + k - 1) / k; // Công thức tránh số thực

            if(ans > hours) return false;
        }
        // Tổng giờ <= tổng giờ cho phép
        return ans <= hours;
    }


    int minEatingSpeed(vector<int>& piles, int h) {

        int left = 1, right = *max_element(piles.begin(), piles.end());
        int ans = -1;

        // binary search on tốc độ ăn
        while(left <= right){
            int mid = (left + right) / 2;

            if(F(piles, h, mid)){
                ans = mid;
                // Vì tìm min nên tìm kiếm thêm bến trái
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return ans;
    }
};
