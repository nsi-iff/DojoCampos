import static org.hamcrest.Matchers.*;
import static org.hamcrest.MatcherAssert.*;

import org.junit.Test;

public class BrotherWarSpec {
	@Test
	public void doisIrmaosDoisLotes()
	{
		BrotherWar campo = new BrotherWar()
			.disposicao(new int[][]{ {0, 1}})
			.batalhas(1);
		assertThat(campo.guerrear(), 
				is(equalTo(new int[][] {{1, 0}})));
	}

	@Test
	public void doisIrmaosTresLotes()
	{
		BrotherWar campo = new BrotherWar()
			.disposicao(new int[][] {{0, 1, 1}})
			.batalhas(1);
		assertThat(campo.guerrear(), 
				is(equalTo(new int[][] {{1, 0, 1}})));
	}
	
	@Test
	public void doisIrmaosTresLotesBatalhamDuasVezes()
	{
		BrotherWar campo = new BrotherWar()
			.disposicao(new int[][] {{0, 1, 1}})
			.batalhas(2);
		assertThat(campo.guerrear(), 
				is(equalTo(new int[][] {{0, 1, 0}})));
	}	
    @Test
	public void doisIrmaosQuatroLotes2x2()
	{
		BrotherWar campo = new BrotherWar()
			.disposicao(new int[][] {{0, 1},{0,1}})
			.batalhas(1);
		assertThat(campo.guerrear(), 
				is(equalTo(new int[][] {{1, 0},{1,0}})));
	}
	
}
