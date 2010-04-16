import static org.hamcrest.Matchers.*;
import static org.hamcrest.MatcherAssert.*;

import org.junit.Test;

public class InteiroPraRomanoSpec {

	@Test
	public void deveConverter1a10ParaNumeroRomano() {
		assertThat(new Numero(1).paraRomano(), is(equalTo("I")));
		assertThat(new Numero(2).paraRomano(), is(equalTo("II")));
		assertThat(new Numero(3).paraRomano(), is(equalTo("III")));
		assertThat(new Numero(4).paraRomano(), is(equalTo("IV")));
		assertThat(new Numero(5).paraRomano(), is(equalTo("V")));
		assertThat(new Numero(6).paraRomano(), is(equalTo("VI")));
		assertThat(new Numero(7).paraRomano(), is(equalTo("VII")));
		assertThat(new Numero(8).paraRomano(), is(equalTo("VIII")));
		assertThat(new Numero(9).paraRomano(), is(equalTo("IX")));
		assertThat(new Numero(10).paraRomano(), is(equalTo("X")));
	}
	
	@Test
	public void deveConverter11a20ParaNumeroRomano() {
		assertThat(new Numero(11).paraRomano(), is(equalTo("XI")));
		assertThat(new Numero(12).paraRomano(), is(equalTo("XII")));
		assertThat(new Numero(13).paraRomano(), is(equalTo("XIII")));
		assertThat(new Numero(14).paraRomano(), is(equalTo("XIV")));
		assertThat(new Numero(15).paraRomano(), is(equalTo("XV")));
		assertThat(new Numero(16).paraRomano(), is(equalTo("XVI")));
		assertThat(new Numero(17).paraRomano(), is(equalTo("XVII")));
		assertThat(new Numero(18).paraRomano(), is(equalTo("XVIII")));
		assertThat(new Numero(19).paraRomano(), is(equalTo("XIX")));
		assertThat(new Numero(20).paraRomano(), is(equalTo("XX")));
	}
	
	@Test
	public void deveConverter21a99PorAmostragemParaNumeroRomano() {
		assertThat(new Numero(21).paraRomano(), is(equalTo("XXI")));
		assertThat(new Numero(32).paraRomano(), is(equalTo("XXXII")));
		assertThat(new Numero(44).paraRomano(), is(equalTo("XLIV")));
		assertThat(new Numero(53).paraRomano(), is(equalTo("LIII")));
		assertThat(new Numero(69).paraRomano(), is(equalTo("LXIX")));
		assertThat(new Numero(71).paraRomano(), is(equalTo("LXXI")));
		assertThat(new Numero(88).paraRomano(), is(equalTo("LXXXVIII")));
		assertThat(new Numero(95).paraRomano(), is(equalTo("XCV")));
		assertThat(new Numero(99).paraRomano(), is(equalTo("XCIX")));
	}

	
	
}
