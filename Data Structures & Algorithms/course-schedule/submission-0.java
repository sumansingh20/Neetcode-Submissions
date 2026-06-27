class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<Integer>[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }
        int[] in = new int[numCourses];
        for (int i = 0; i < prerequisites.length; i++) {
            int a = prerequisites[i][0];
            int b = prerequisites[i][1];
            graph[b].add(a);
            in[a]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (in[i] == 0) {
                q.offer(i);
            }
        }
        int count = 0;
        while (!q.isEmpty()) {
            int node = q.poll();
            count++;
            for (int next : graph[node]) {
                in[next]--;
                if (in[next] == 0) {
                    q.offer(next);
                }
            }
        }
        return count == numCourses;
    }
}
