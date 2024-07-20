import java.io.*;
import java.math.BigInteger;
import java.net.*;
import java.security.*;
import java.security.spec.*;

public class RSAAlice {

    private static final int BIT_LENGTH = 1024;
    private static final BigInteger ONE = BigInteger.ONE;
    private static BigInteger p, q, n, phi, e, d;

    public static void main(String[] args) throws Exception {
        generateKeys();
        sendPublicKey();
        receiveCiphertextAndDecrypt();
    }

    private static void generateKeys() throws NoSuchAlgorithmException {
        SecureRandom random = new SecureRandom();
        p = BigInteger.probablePrime(BIT_LENGTH / 2, random);
        q = BigInteger.probablePrime(BIT_LENGTH / 2, random);
        n = p.multiply(q);
        phi = (p.subtract(ONE)).multiply(q.subtract(ONE));
        e = new BigInteger("65537");  // Common public exponent
        d = e.modInverse(phi);
    }

    private static void sendPublicKey() throws IOException {
        try (Socket socket = new Socket("localhost", 5000);
             ObjectOutputStream out = new ObjectOutputStream(socket.getOutputStream())) {
            out.writeObject(n);
            out.writeObject(e);
        }
    }

    private static void receiveCiphertextAndDecrypt() throws IOException, ClassNotFoundException {
        try (ServerSocket serverSocket = new ServerSocket(5001);
             Socket clientSocket = serverSocket.accept();
             ObjectInputStream in = new ObjectInputStream(clientSocket.getInputStream())) {
            BigInteger ciphertext = (BigInteger) in.readObject();
            BigInteger plaintext = ciphertext.modPow(d, n);
            System.out.println("Decrypted message: " + new String(plaintext.toByteArray()));
        }
    }
}
