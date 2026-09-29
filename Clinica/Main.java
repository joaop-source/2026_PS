import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    static ArrayList<Produto> produtos = new ArrayList<>();
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int opcao;

        do {
            System.out.println("\n===== MENU =====");
            System.out.println("1 - Cadastrar produto");
            System.out.println("2 - Listar produtos");
            System.out.println("3 - Buscar produto");
            System.out.println("4 - Alterar preço");
            System.out.println("5 - Remover produto");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            opcao = scanner.nextInt();
            scanner.nextLine();

            switch (opcao) {

                case 1:
                    cadastrar();
                    break;

                case 2:
                    listar();
                    break;

                case 3:
                    buscar();
                    break;

                case 4:
                    alterarPreco();
                    break;

                case 5:
                    remover();
                    break;

                case 0:
                    System.out.println("Sistema encerrado.");
                    break;

                default:
                    System.out.println("Opção inválida.");
            }

        } while (opcao != 0);

        scanner.close();
    }

    static void cadastrar() {

        System.out.print("Digite o código: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        if (buscarPorCodigo(codigo) != null) {
            System.out.println(
                "Cadastro recusado: já existe um produto com esse código."
            );
            return;
        }

        System.out.print("Digite o nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite o preço: ");
        double preco = scanner.nextDouble();
        scanner.nextLine();

        Produto produto = new Produto(codigo, nome, preco);

        produtos.add(produto);

        System.out.println("Produto cadastrado com sucesso!");
    }

    static void listar() {

        if (produtos.isEmpty()) {
            System.out.println("Nenhum produto cadastrado.");
            return;
        }

        System.out.println("\n===== PRODUTOS =====");

        for (Produto p : produtos) {
            System.out.println(p);
        }
    }

    static Produto buscarPorCodigo(int codigo) {

        for (Produto p : produtos) {

            if (p.getCodigo() == codigo) {
                return p;
            }
        }

        return null;
    }

    static void buscar() {

        System.out.print("Digite o código do produto: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        Produto produto = buscarPorCodigo(codigo);

        if (produto == null) {
            System.out.println("Produto não encontrado.");
        } else {
            System.out.println("Produto encontrado:");
            System.out.println(produto);
        }
    }

    static void alterarPreco() {

        System.out.print("Digite o código do produto: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        Produto produto = buscarPorCodigo(codigo);

        if (produto == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        System.out.print("Digite o novo preço: ");
        double preco = scanner.nextDouble();
        scanner.nextLine();

        produto.alterarPreco(preco);

        System.out.println("Preço alterado com sucesso!");
    }

    static void remover() {

        System.out.print("Digite o código do produto: ");
        int codigo = scanner.nextInt();
        scanner.nextLine();

        Produto produto = buscarPorCodigo(codigo);

        if (produto == null) {
            System.out.println("Produto não encontrado.");
            return;
        }

        produtos.remove(produto);

        System.out.println("Produto removido com sucesso!");
    }
}
