public class Prime {
  public static void main(String[] args) {
      int n = Integer.parseInt(args[0]);
      boolean isPrime = n > 1;

      for (int i = 2; i <= Math.sqrt(n); i++) {
          if (n % i == 0) {
              isPrime = false;
              break;
          }
      }

      if (isPrime) {
          System.out.println(n + " is a prime number.");
      } else {
          System.out.println(n + " is not a prime number.");
      }
  }
}
