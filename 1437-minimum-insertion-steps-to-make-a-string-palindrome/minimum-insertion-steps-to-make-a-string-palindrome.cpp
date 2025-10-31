class Solution {
public:
    int minInsertions(string s) {
        int n = s.size();
        int ans = INT_MAX;

        // quick check for palindrome
        string rev = s;
        reverse(rev.begin(), rev.end());
        if (s == rev)
            return 0;

        // LCS helper
        auto lcs = [&](const string &a, const string &b) {
            int n = a.size(), m = b.size();
            vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

            for (int i = 1; i <= n; ++i) {
                for (int j = 1; j <= m; ++j) {
                    if (a[i - 1] == b[j - 1])
                        dp[i][j] = dp[i - 1][j - 1] + 1;
                    else
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }

            return dp[n][m];
        };

        for (int i = 0; i < n; ++i) {
            int l = i, r = i;

            if (i > 0 && s[i] == s[i - 1])
                l -= 1;

            string a = string(s.begin(), s.begin() + l);
            reverse(a.begin(), a.end());
            string b = string(s.begin() + r + 1, s.end());

            int longest = lcs(a, b);
            int mx = max((int)a.size(), (int)b.size());
            int mn = min((int)a.size(), (int)b.size());
            ans = min(ans, mx - mn + (mn - longest) * 2);
        }

        return ans;
    }
};
