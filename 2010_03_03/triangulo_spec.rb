require 'triangulo'

describe TrianguloDePascal do
  it "deve ter uma linha contendo [1] pro caso inicial" do
    triangulo = TrianguloDePascal.new 1
    triangulo.to_a.should == [1]
  end
  
  it "deve ter duas linhas contendo [1,],[1,1]" do
    triangulo = TrianguloDePascal.new 2
    triangulo.to_a.should == [[1],[1,1]]
  end

  it "deve ter tres linhas contendo [1],[1,1],[1,2,1]" do
    triangulo = TrianguloDePascal.new 3
    triangulo.to_a.should == [[1],[1,1],[1,2,1]]
  end

  it "deve ter quatro linhas contendo [1],[1,1],[1,2,1],[1,3,3,1]" do
    triangulo = TrianguloDePascal.new 4
    triangulo.to_a.should == [[1],[1,1],[1,2,1], [1,3,3,1]]  
  end

  it "deve ter sete linhas contendo [1],[1,1],[1,2,1],[1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1], [1,6,15,20,15,6,1]" do
    triangulo = TrianguloDePascal.new 7
    triangulo.to_a.should == [[1],[1,1],[1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1], [1,6,15,20,15,6,1]]  
  end
end
