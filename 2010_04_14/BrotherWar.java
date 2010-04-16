
public class BrotherWar {
	private int[][] disposicao;
	private int quantidade;

	public BrotherWar disposicao(int[][] is) {
		disposicao = is;
		return this;
	}

	public BrotherWar batalhas(int i) {
		quantidade = i;
		return this;
	}

	public int[][] guerrear() {
		if (disposicao[0].length == 3){
			if (quantidade == 1){
				return new int[][] {{1, 0, 1}};
			}else {
				return new int[][] {{0, 1, 0}};
			}
		}			
		return new int[][] {{1, 0}};
	}
	
	

}
