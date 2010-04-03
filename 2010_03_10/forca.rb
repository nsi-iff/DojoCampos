class JogoDeForca
  def initialize(palavras)
    @palavra = palavras[rand(palavras.size)]
  end
  
  def jogar(letra)
    @palavra.include? letra
  end 
end
