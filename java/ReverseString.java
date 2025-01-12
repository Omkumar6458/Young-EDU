public class ReverseString {
  public static void main(String[] args) {
      String input = args[0];
      StringBuilder reversed = new StringBuilder(input).reverse();
      System.out.println("Reversed String: " + reversed);
  }
}
