public class App {
    public static void main(String[] args) {
        ListaContatos lista = new ListaContatos("Pedro", "999999");
        System.out.println("O nome é: " + lista.getNome());

        ListaContatos.testar_metodos();
    }
}
