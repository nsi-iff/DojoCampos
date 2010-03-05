class TrianguloDePascal
  def initialize(numero_de_linhas)
    @numero_de_linhas = numero_de_linhas
  end

  def to_a
    return [1] if @numero_de_linhas == 1
    resultado = [[1], [1, 1]]
    (2...@numero_de_linhas).each do |indice_linha|
      linha = [1]
      linha_anterior = resultado[indice_linha - 1]
      (1...linha_anterior.size).each do |n| 
         linha << linha_anterior[n-1] + linha_anterior[n]
      end
      resultado << linha + [1]
    end
    resultado
  end

end
