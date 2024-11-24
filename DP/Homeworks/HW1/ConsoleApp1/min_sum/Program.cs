namespace min_sum;

class Program
{
    static void Main(string[] args)
    {
        var goal = int.Parse(Console.ReadLine());
        var visited = new bool[goal];
        visited[0] = true;
        var queue = new Queue<(int, int)>();
        queue.Enqueue((1,0));

        var parrentNodeArray = new int[goal];
        parrentNodeArray[0] = -1;

        int current;
        int steps;
        while (queue.Count > 0)
        {
            (current, steps) = queue.Dequeue();
            if (current == goal)
            {
                var curr = current;
                var path = new int[steps + 1];
                path[0] = current;
                
                int i = 1;
                while (curr != 1)
                {
                    path[i] = parrentNodeArray[curr - 1];
                    curr = parrentNodeArray[curr - 1];
                    i++;
                }
                
                Console.WriteLine(steps);
                var array=  path.Reverse();
                Console.WriteLine(string.Join(' ', array));
            }
            var nextValues = new int[3];
            nextValues[0] = current + 1;
            nextValues[1] = current * 2;
            nextValues[2] = current * 3;
            foreach (var next in nextValues)
            {
                if (next <= goal && visited[next - 1] != true)
                {
                    visited[next - 1] = true;
                    queue.Enqueue((next, steps + 1));
                    parrentNodeArray[next - 1] = current;
                }
            }
        }
    }
}