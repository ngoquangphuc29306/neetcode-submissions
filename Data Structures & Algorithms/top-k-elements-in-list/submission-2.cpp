class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(k == nums.size()){
            return nums;
        }
        unordered_map<int,int> cnt;
        for(auto x : nums){
            cnt[x]++;
        }
        priority_queue<
            pair<int, int>,
            vector<pair<int, int>>,
            greater<pair<int, int>>
        > minHeap;
        for(auto x : cnt){
            int value = x.first;
            int freq = x.second;
            minHeap.push({freq, value});
            if(minHeap.size() > k){
                minHeap.pop();
            }
        }
        vector<int> res;
        while(!minHeap.empty()){
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res;
    }
};
