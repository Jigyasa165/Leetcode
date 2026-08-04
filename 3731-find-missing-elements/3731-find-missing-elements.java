class Solution {
    public List<Integer> findMissingElements(int[] nums) {
         List<Integer> ans = new ArrayList<>();

        int min = nums[0];
        int max = nums[0];

        for (int x : nums) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }

        boolean[] present = new boolean[max + 1];

        for (int x : nums)
            present[x] = true;

        for (int i = min; i <= max; i++) {
            if (!present[i])
                ans.add(i);
        }

        return ans;
    }
}