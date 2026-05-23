class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Subproblem 1 : Validate row
        for(int row = 0; row < 9; row++){
            unordered_set<char> seen;
            for(int i = 0; i < 9; i++){
                if(board[row][i] == '.') continue;
                if(seen.count(board[row][i])) return false;
                seen.insert(board[row][i]);
            }
        }
        // Subproblem 2 : Validate col
        for(int col = 0; col < 9; col++){
            unordered_set<char> seen;
            for(int i = 0; i < 9; i++){
                if(board[i][col] == '.') continue;
                if(seen.count(board[i][col])) return false;
                seen.insert(board[i][col]);
            }
        }
        // Subproblem 2 : Validate sub_box
        vector<pair<int,int>> starts{
            {0, 0}, {0, 3}, {0, 6},
            {3, 0}, {3, 3}, {3, 6},
            {6, 0}, {6, 3}, {6, 6}
        };
        for(auto [init_r, init_c]: starts){
            unordered_set<int> seen;
            for(int i = init_r; i < init_r + 3; i++){
                for(int j = init_c; j < init_c + 3; j++){
                    int x = board[i][j];
                    if(x == '.') continue;
                    if(seen.count(x)) return false;
                    seen.insert(x);
                }
            }
        }
        return true;
    }
};
