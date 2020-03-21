class Solution {
public:
    int getSum(int a, int b) {
        int x = a;
        int y = b;
        while (y != 0) {
        
            int carry = x & y;  
 
        
            x = x ^ y; 
 
            y = carry << 1;
        }
        return x;
        
    }
};