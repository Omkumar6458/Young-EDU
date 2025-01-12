public class Fibonacci {
  public static void main(String[] args) {
      if (args.length == 0) {
          System.out.println("Please provide a number.");
          return;
      }

      int n;
      try {
          n = Integer.parseInt(args[0]);
      } catch (NumberFormatException e) {
          System.out.println("Invalid number.");
          return;
      }

      if (n <= 0) {
          System.out.println("Please provide a positive number.");
          return;
      }

      StringBuilder fibonacciSeries = new StringBuilder();
      int a = 0, b = 1;
      
      for (int i = 0; i < n; i++) {
          fibonacciSeries.append(a).append(i < n - 1 ? ", " : "");
          int next = a + b;
          a = b;
          b = next;
      }

      System.out.println(fibonacciSeries.toString().substring(1));
  }
}
