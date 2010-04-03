require 'forca'

describe "jogo de forca" do

  it "a palavra galinha deve possuir as letras 'a' e 'g'" do
    forca = JogoDeForca.new ['galinha']
    forca.jogar('a').should be_true
    forca.jogar('g').should be_true
  end

  it "a palavra casa nao deve ter a letra 't'" do
    forca = JogoDeForca.new ['casa']
    forca.jogar('t').should_not be_true
  end

  it "deve ser possivel errar até 3 vezes" do
    forca = JogoDeForca.new ['teclado']
    forca.jogar('k')
    forca.jogar('y')
    forca.jogar('w')
    lambda {forca.jogar('z')}.should raise_error Exception
  end

  it "o jogo de forca contendo a palavra 'computador' e 'mouse' deve selecionar a segunda e dizer que não possui a letra 'g'" do
    class JogoDeForca
      def rand(x)
        1
      end
    end
    forca = JogoDeForca.new ['computador', 'mouse']
    forca.jogar('c').should_not be_true
  end
  
  
end
