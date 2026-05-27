class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        vector<int> left(n, 0);
        vector<int> right(n, 0);
        for(int i = 1; i < n; i++){
            left[i] = max(left[i - 1], height[i - 1]);
        }
        for(int j = n - 2; j >= 0; j--){
            right[j] = max(right[j + 1], height[j + 1]);
        }
        int area = 0;
        for(int i = 0; i < n; i++){
            int water = min(left[i], right[i]) - height[i];
            if(water > 0){
                area += water;
            }
        }
        return area;
    }
};
