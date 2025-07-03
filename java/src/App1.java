public class App1 {
    public static void main(String[] args) throws Exception {
        SemaforoVeicular A = new SemaforoVeicular("vermelho", "A");
        SemaforoVeicular B = new SemaforoVeicular("verde", "B");
        while (true) {
            A.esperar(4);
            B.esperar(4);

            System.out.println();
            A.mudarCor();
            B.mudarCor();

            A.esperar(4);
            B.esperar(4);

            System.out.println();
            A.mudarCor();
            B.mudarCor();

            
        }
    }
}
