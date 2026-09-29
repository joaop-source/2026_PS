/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Autor     : JOAO PEDRO OLIVEIRA
 * Descricao : esqueleto do BiblioTech (Aula 36). Ainda nao faz nada:
 *             so prova que o ambiente compila e roda.
 */
public class Main {

    public static void main(String[] args) {

        Livro livro1 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Livro livro2 = new Livro("Capitaes da Areia", "Jorge Amado", 1937);

        Leitor pedro = new Leitor("Pedro Alves", "2026010", 3);

        Bibliotecario marli =
                new Bibliotecario("Marli Souza", "1998002", "F-0421");

        System.out.println("BiblioTech v0.2 - as classes existem");

        System.out.println(livro1);
        System.out.println(livro2);
        System.out.println(pedro);
        System.out.println(marli);

        System.out.println(
                "Nome do leitor, via heranca: " + pedro.getNome()
        );

        System.out.println(
                "Pedro pode pegar livro? " + pedro.podePegarEmprestado()
        );

        System.out.println(
                "Marli entrou? " + marli.entrar()
        );

        livro1.emprestar();
        pedro.pegouLivro();

        System.out.println(
                "Depois do emprestimo: " + livro1
        );

        System.out.println(
                "Depois do emprestimo: " + pedro
        );
    }
}