public class Bibliotecario extends Usuario {

    private String funcional;

    public Bibliotecario(String nome, String matricula, String funcional) {
        super(nome, matricula);
        this.funcional = funcional;
    }

    public String getFuncional() {
        return funcional;
    }

    public boolean consultarAcervo() {
        return true;
    }

    @Override
    public String toString() {
        return "Bibliotecario(a) " + getNome() + " ("
                + getMatricula() + ", funcional " + funcional + ")";
    }
}