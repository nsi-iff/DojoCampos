require 'extenso'

describe 'converter numeral em extenso' do

  it "deve converter numerais de 0 a 20" do
    1.extenso.should == 'um'
		2.extenso.should == 'dois'	
		3.extenso.should == 'três'
		4.extenso.should == 'quatro'
		5.extenso.should == 'cinco'
		6.extenso.should == 'seis'
		7.extenso.should == 'sete'
		8.extenso.should == 'oito'
		9.extenso.should == 'nove'
		0.extenso.should == 'zero'
    10.extenso.should == 'dez'
    11.extenso.should == 'onze'
		12.extenso.should == 'doze'
		13.extenso.should == 'treze'
		14.extenso.should == 'quatorze'
		15.extenso.should == 'quinze'
		16.extenso.should == 'dezesseis'
		17.extenso.should == 'dezessete'
		18.extenso.should == 'dezoito'
		19.extenso.should == 'dezenove'
    20.extenso.should == 'vinte'
	end

  it "deve converter dezenas de 20 a 90" do
    20.extenso.should == 'vinte'
    30.extenso.should == 'trinta'
    40.extenso.should == 'quarenta'
    50.extenso.should == 'cinquenta'
    60.extenso.should == 'sessenta'
    70.extenso.should == 'setenta'
    80.extenso.should == 'oitenta'
    90.extenso.should == 'noventa'
  end

  it '21 deve retornar vinte e um' do
    21.extenso.should == 'vinte e um'
  end

  it '42 deve retornar quarenta e dois' do
    42.extenso.should == 'quarenta e dois'
  end

  it '69 deve retornar sessenta e nove' do
    69.extenso.should == 'sessenta e nove'
  end

  it '100 deve retornar cem' do
    100.extenso.should == 'cem'
  end

  it '101 deve retornar cento e um' do
    101.extenso.should == 'cento e um'
  end
end
