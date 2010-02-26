class Fixnum
  def extenso
    numeros = { 0 => 'zero',
                1 => 'um',
	              2 => 'dois',
                3 => 'três',
	              4 => 'quatro',
	              5 => 'cinco',
                6 => 'seis',
                7 => 'sete', 
                8 => 'oito',
                9 => 'nove',
                10 => 'dez',
                11 => 'onze',
	              12 => 'doze',
                13 => 'treze',
	              14 => 'quatorze',
	              15 => 'quinze',
                16 => 'dezesseis',
                17 => 'dezessete', 
                18 => 'dezoito',
                19 => 'dezenove',
                100 => 'cem',
    }
    
    numeros_dezenas = { 2 => 'vinte',
                        3 => 'trinta',
                        4 => 'quarenta',
                        5 => 'cinquenta',
                        6 => 'sessenta',
                        7 => 'setenta',
                        8 => 'oitenta',
                        9 => 'noventa',
                        10 => 'cento' 
                      }  

    return numeros[self] if self / 10 < 2
    return 'cem' if self % 100 == 0
    unidade = self % 10
    string_de_unidade = unidade == 0 ? "" : ' e ' + numeros[unidade]
    numeros_dezenas[self / 10] + string_de_unidade 
  end
end
