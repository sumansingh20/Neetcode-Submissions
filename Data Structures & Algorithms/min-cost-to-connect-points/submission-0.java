class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        boolean[] visit = new boolean[n];
        int[] min = new int[n];
        for (int i = 0; i < n; i++) {
            min[i] = Integer.MAX_VALUE;
        }
        min[0] = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int node = -1;
            for (int j = 0; j < n; j++) {
                if (!visit[j] && (node == -1 || min[j] < min[node])) {
                    node = j;
                }
            }
            visit[node] = true;
            ans += min[node];
            for (int j = 0; j < n; j++) {
                if (!visit[j]) {
                    int dist = Math.abs(points[node][0] - points[j][0])
                             + Math.abs(points[node][1] - points[j][1]);
                    if (dist < min[j]) {
                        min[j] = dist;
                    }
                }
            }
        }
        return ans;
    }
}