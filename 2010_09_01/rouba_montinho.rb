class Mesa
  
  attr_accessor :mesa

  def initialize(cartas)
     @mesa = cartas
  end

  def adicionar(carta)
     @mesa << carta
  end

  def retirar(carta)
     @mesa.delete(carta)
     return @mesa  
  end

end


class Mao

  def initialize(cartas_da_mao)
    @cartas_da_mao = cartas_da_mao
  end
  
  def retirar(carta)
    @cartas_da_mao.delete(carta)
    return @cartas_da_mao  
  end

end


class Jogo

  def initialize(cartas_mesa, cartas_mao)
    @cartas_mesa = Mesa.new(cartas_mesa)
    @cartas_mao = Mao.new(cartas_mao)
  end 

  def jogar(carta)
    if @cartas_mesa.mesa.include? (carta)
      return [@cartas_mesa.retirar(carta), @cartas_mao.retirar(carta)]
    end
    return [@cartas_mesa.adicionar(carta), @cartas_mao.retirar(carta)]
  end

end
