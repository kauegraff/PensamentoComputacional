public class Calculadora {
    public static double multiplicacao(double a, double b) {
        return a * b;
    }

    public static double soma(double a, double b) {
        return a + b;
    }

    public static double subtracao(double a, double b) {
        return a - b;
    }

    public static double divisao(double a, double b) {
        if (b != 0){
            return a / b;
        } else {
            System.out.println("Operação inválida");
            return 0;
        }
    } 
    public static void main(String[] args) throws Exception {
        //double resultado = multiplicacao(5, 3);
        //double soma = soma(2, 3);
        //System.out.println(soma);
        //System.out.println(resultado);
        double div = divisao(5, 0);
        System.out.println(div);
    }
}
