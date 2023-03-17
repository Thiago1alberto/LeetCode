class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int m = nums1.length;
        int n = nums2.length;
        
        if (m > n) {
            int[] temp = nums1;
            nums1 = nums2;
            nums2 = temp;
            m = nums1.length;
            n = nums2.length;
        }
        
        int i_min = 0;
        int i_max = m;
        int half_len = (m + n + 1) / 2;
        int max_left, min_right;
        
        while (i_min <= i_max) {
            int i = (i_min + i_max) / 2;
            int j = half_len - i;
            
            if (i < m && nums2[j-1] > nums1[i]) {
                i_min = i + 1;
                continue;
            } 
            if (i > 0 && nums1[i-1] > nums2[j]) {
                i_max = i - 1;
                continue;
            } 
            
            if (i == 0) {
                max_left = nums2[j-1];
            } else if (j == 0) {
                max_left = nums1[i-1];
            } else {
                max_left = Math.max(nums1[i-1], nums2[j-1]);
            }
            
            if ((m + n) % 2 == 1) {
                return max_left;
            }
            
            if (i == m) {
                min_right = nums2[j];
            } else if (j == n) {
                min_right = nums1[i];
            } else {
                min_right = Math.min(nums1[i], nums2[j]);
            }
            
            return (max_left + min_right) / 2.0;
        }
        
        return 0.0;
    }
}
