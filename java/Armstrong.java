public class Armstrong {
  public static void main(String[] args) {
      int n = Integer.parseInt(args[0]);
      int sum = 0, temp = n, digits = String.valueOf(n).length();
      
      while (temp > 0) {
          int rem = temp % 10;
          sum += Math.pow(rem, digits);
          temp /= 10;
      }
      
      if (sum == n) {
          System.out.println(n + " is an Armstrong number.");
      } else {
          System.out.println(n + " is not an Armstrong number.");
      }
  }
}
