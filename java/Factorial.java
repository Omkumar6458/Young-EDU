public class Factorial {
  public static void main(String[] args) {
      int n = Integer.parseInt(args[0]);
      long factorial = 1;

      for (int i = 2; i <= n; i++) {
          factorial *= i;
      }

      System.out.println("Factorial of " + n + " is " + factorial);
  }
}
