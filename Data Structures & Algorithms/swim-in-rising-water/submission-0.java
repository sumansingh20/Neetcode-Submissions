class Solution {
    public int swimInWater(int[][] grid) {
        int n = grid.length;
        boolean[][] visit = new boolean[n][n];
        java.util.PriorityQueue<int[]> pq =
                new java.util.PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.offer(new int[]{0, 0, grid[0][0]});
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int x = cur[0];
            int y = cur[1];
            int time = cur[2];
            if (visit[x][y]) {
                continue;
            }
            visit[x][y] = true;
            if (x == n - 1 && y == n - 1) {
                return time;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visit[nx][ny]) {
                    int nextTime = Math.max(time, grid[nx][ny]);
                    pq.offer(new int[]{nx, ny, nextTime});
                }
            }
        }
        return -1;
    }
}