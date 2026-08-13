class Solution {

    class Node {
        int leftChar, rightChar;
        int leftLen, rightLen;
        int maxLen;
        int len;

        Node() {}

        Node(char c) {
            leftChar = rightChar = c;
            leftLen = rightLen = maxLen = len = 1;
        }
    }

    Node[] tree;
    char[] s;

    void build(int node, int l, int r) {
        if (l == r) {
            tree[node] = new Node(s[l]);
            return;
        }

        int mid = (l + r) / 2;

        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    Node merge(Node a, Node b) {
        Node res = new Node();

        res.len = a.len + b.len;
        res.leftChar = a.leftChar;
        res.rightChar = b.rightChar;

        res.leftLen = a.leftLen;
        res.rightLen = b.rightLen;

        res.maxLen = Math.max(a.maxLen, b.maxLen);

        if (a.rightChar == b.leftChar) {
            res.maxLen = Math.max(res.maxLen, a.rightLen + b.leftLen);

            if (a.leftLen == a.len) {
                res.leftLen = a.len + b.leftLen;
            }

            if (b.rightLen == b.len) {
                res.rightLen = b.len + a.rightLen;
            }
        }

        return res;
    }

    void update(int node, int l, int r, int index, char c) {
        if (l == r) {
            s[index] = c;
            tree[node] = new Node(c);
            return;
        }

        int mid = (l + r) / 2;

        if (index <= mid) {
            update(node * 2, l, mid, index, c);
        } else {
            update(node * 2 + 1, mid + 1, r, index, c);
        }

        tree[node] = merge(tree[node * 2], tree[node * 2 + 1]);
    }

    public int[] longestRepeating(String s, String queryCharacters,
                                  int[] queryIndices) {

        int n = s.length();
        int k = queryIndices.length;

        this.s = s.toCharArray();
        tree = new Node[4 * n];

        build(1, 0, n - 1);

        int[] answer = new int[k];

        for (int i = 0; i < k; i++) {
            update(1, 0, n - 1,
                   queryIndices[i],
                   queryCharacters.charAt(i));

            answer[i] = tree[1].maxLen;
        }

        return answer;
    }
}