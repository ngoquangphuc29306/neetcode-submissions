class Solution {
public:
    string encode(vector<string>& strs) {
        string encoded_string;
        // Có dạng ví dụ:  4#Phuc3#Dep3#Trai
        for(int i = 0; i < strs.size(); i++){
            encoded_string += to_string(strs[i].size()) + '#' + strs[i];
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> decoded_string;
        int i = 0;
        while(i < s.size()){
            int j = i;
            // Tìm vị trí có kí tự #
            while(s[j] != '#'){
                j++;
            }
            // Chiều dài xâu cần cắt
            int len = stoi(s.substr(i, j - i));
            // Xâu cần cắt
            string cur =  s.substr(j + 1, len);
            decoded_string.push_back(cur);
            // Cập nhất i
            i = j + 1 + len;
        }
        return decoded_string;
    }
};
