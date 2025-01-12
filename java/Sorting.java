import java.util.Arrays;

public class Sorting{
    public static void main(String[] args) {
        if (args.length == 1) {
            String input = args[0];
            String[] numbers = input.split(",");
            int[] array = Arrays.stream(numbers).mapToInt(Integer::parseInt).toArray();

            Arrays.sort(array);

            System.out.println(Arrays.toString(array));
        } else {
            System.out.println("Please provide a single input of comma-separated numbers.");
        }
    }
}
