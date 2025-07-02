import java.util.ArrayList;
import java.util.HashMap;

public class ListaContatos {

    private String nome;
    private String numero;

    public ListaContatos(String nome, String numero) {
        this.nome = nome;
        this.numero = numero;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getNumero() {
        return numero;
    }

    public void setNumero(String numero) {
        this.numero = numero;
    }

    public static void testar_metodos() {
        System.out.println("Funciona");
    }

    public void testar_obj() {
        System.out.println("Funciona com obj");
    }

    public static void main(String[] args) {
        ArrayList<HashMap<String, String>> contatos = new ArrayList<>();

        // Criando contato
        HashMap<String, String> contato1 = new HashMap<>();
        contato1.put("nome", "João");
        contato1.put("telefone", "123456789");
        contatos.add(contato1);

        HashMap<String, String> contato2 = new HashMap<>();
        contato2.put("nome", "Maria");
        contato2.put("telefone", "9999999");
        contatos.add(contato2);

        // listando contatos

        for (HashMap<String, String> contato : contatos) {
            System.out.println("Nome: " + contato.get("nome") +
                    ", Telefone: " + contato.get("telefone"));
        }
    }
}
