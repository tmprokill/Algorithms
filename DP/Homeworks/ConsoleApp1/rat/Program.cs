namespace rat;

class Program
{
    static void Main(string[] args)
    {
        static int[][] CreateMatrix(int n, int m, int defaultValue)
        {
            int[][] matrix = new int[n][];
            for (int i = 0; i < n; i++)
            {
                matrix[i] = new int[m];
                for (int j = 0; j < m; j++)
                {
                    matrix[i][j] = defaultValue;
                }
            }
            return matrix;
        }

        static int[][] Multiply(int[][] incidenceMatrix, int[][] secondIncidenceMatrix)
        {
            int n = incidenceMatrix.Length;
            int[][] resultMatrix = CreateMatrix(n, n, 0);
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    for (int k = 0; k < n; k++)
                    {
                        resultMatrix[i][j] = (resultMatrix[i][j] + (int)(((long)incidenceMatrix[i][k] * secondIncidenceMatrix[k][j]) % (1_000_000_007))) % (1_000_000_007);
                    }
                }
            }
            return resultMatrix;
        }

        static int[][] Exponentiation(int[][] incidenceMatrix, long k)
        {
            int n = incidenceMatrix.Length;
            int[][] result = CreateMatrix(n, n, 0);
            for (int i = 0; i < n; i++)
            {
                result[i][i] = 1; // Инициализация единичной матрицы
            }

            while (k > 0)
            {
                if (k % 2 == 1)
                {
                    result = Multiply(result, incidenceMatrix);
                }
                incidenceMatrix = Multiply(incidenceMatrix, incidenceMatrix);
                k /= 2;
            }

            return result;
        }

        static long AllPaths(int n, int m, long k, List<Tuple<int, int>> incidenceList)
        {
            int[][] incidenceMatrix = CreateMatrix(n, n, 0);
            foreach (var edge in incidenceList)
            {
                incidenceMatrix[edge.Item1 - 1][edge.Item2 - 1]++;
            }

            return Sum(Exponentiation(incidenceMatrix, k - 1)[0]) % 1_000_000_007;
        }

        static long Sum(int[] array)
        {
            long sum = 0;
            foreach (var value in array)
            {
                sum = (sum + value) % 1_000_000_007;
            }
            return sum;
        }

        static void Main()
        {
            var input = Console.ReadLine().Split();
            int n = int.Parse(input[0]);
            int m = int.Parse(input[1]);
            long k = long.Parse(input[2]);

            List<Tuple<int, int>> tempIncidence = new List<Tuple<int, int>>();
            for (int i = 0; i < m; i++)
            {
                var edge = Console.ReadLine().Split();
                int a = int.Parse(edge[0]);
                int b = int.Parse(edge[1]);
                tempIncidence.Add(new Tuple<int, int>(a, b));
            }

            Console.WriteLine(AllPaths(n, m, k, tempIncidence));
        }
    }
}