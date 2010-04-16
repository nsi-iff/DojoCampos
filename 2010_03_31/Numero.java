import java.util.HashMap;
import java.util.Map;

public class Numero {
	private int numeroInteiro;
	private static Map<Integer, String> unidades, dezenas;
	
	static {
		unidades = new HashMap<Integer, String>();
		unidades.put(0, "");
		unidades.put(1, "I");
		unidades.put(2, "II");
		unidades.put(3, "III");
		unidades.put(4, "IV");
		unidades.put(5, "V");
		unidades.put(6, "VI");
		unidades.put(7, "VII");
		unidades.put(8, "VIII");
		unidades.put(9, "IX");
		
		dezenas = new HashMap<Integer, String>();
		dezenas.put(0, "");
		dezenas.put(1, "X");
		dezenas.put(2, "XX");
		dezenas.put(3, "XXX");
		dezenas.put(4, "XL");
		dezenas.put(5, "L");
		dezenas.put(6, "LX");
		dezenas.put(7, "LXX");
		dezenas.put(8, "LXXX");
		dezenas.put(9, "XC");
	}
	
	public Numero(int n) {
		numeroInteiro = n;
	}

	public String paraRomano() {
		return dezenas.get(numeroInteiro / 10) + 
				unidades.get(numeroInteiro % 10);
	}
}
