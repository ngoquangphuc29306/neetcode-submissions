class Solution {
public:
    int trap(vector<int>& height) {
        int area = 0;
        for(int i = 0; i < height.size(); i++){
            int maxleft = 0;
            int maxright = 0;
            for(int j = 0; j < i; j++){
                maxleft = max(maxleft, height[j]);
            }
            for(int j = i + 1; j < height.size(); j++){
                maxright = max(maxright, height[j]);
            }
            int water = (min(maxright, maxleft) - height[i]);
            if(water > 0)
                area += water;
        }
        return area;
    }
};
