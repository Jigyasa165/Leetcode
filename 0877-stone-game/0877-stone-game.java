class Solution {
    public boolean stoneGame(int[] piles) {
        int n = piles.length;
        int[] dp = piles.clone();

        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len <= n; i++) {
                int j = i + len - 1;
                dp[i] = Math.max(piles[i] - dp[i + 1],
                                 piles[j] - dp[i]);
            }
        }

        return dp[0] > 0; 
    }
}