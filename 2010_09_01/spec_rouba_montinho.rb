require 'rouba_montinho'

describe 'Rouba montinho' do

  it 'Jogador não tem carta igual' do
    
    jogo = Jogo.new([1, 4, 5, 7], [8, 9, 10])
    jogo.jogar(8).should == [[1, 4, 5, 7, 8], [9, 10]]
  end

  it 'Jogador tem carta igual' do

    jogo = Jogo.new([1, 4, 5, 7], [1, 9, 10])
    jogo.jogar(1).should == [[4, 5, 7], [9, 10]]
  end
end
