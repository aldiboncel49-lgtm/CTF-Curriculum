
public class LoginCheck {
    public static void main(String[] args) {
        String input = args[0];
        String flag = "[REDACTED]";
        if (input.equals(flag)) {
            System.out.println("Access granted!");
        } else {
            System.out.println("Access denied!");
        }
    }
}
