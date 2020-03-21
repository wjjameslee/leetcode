class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        
        vector<vector<int>> triangle;
	// Create triangle-like structure
	for (int i=1; i<=numRows; ++i) {
		vector<int> elems;
		for (int j=1; j<=i; ++j) {
			elems.emplace_back(-1);
		}
		triangle.emplace_back(elems);
	}
	
	// Update triangle as we go
	for (int r=0; r<numRows; ++r) {
		for (int c=0; c<=r; ++c) {
			if (c==0 || c==r) {
				triangle[r][c] = 1;
				continue;
			}
			triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c];
		}
	}
	
	return triangle;
    }
};