import java.io.*;
import java.math.BigInteger;
import java.net.*;

public class RSABob {

    public static void main(String[] args) throws Exception {
        BigInteger n, e;

        try (Socket socket = new Socket("localhost", 5000);
             ObjectInputStream in = new ObjectInputStream(socket.getInputStream())) {
            n = (BigInteger) in.readObject();
            e = (BigInteger) in.readObject();
        }

        String message = "Hello Alice!";
        BigInteger plaintext = new BigInteger(message.getBytes());
        BigInteger ciphertext = plaintext.modPow(e, n);

        try (Socket socket = new Socket("localhost", 5001);
             ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream())) {
            out.writeObject(ciphertext);
        }
    }
}
