# Metodologia-Artigo

## 1 - Pacotes necessários:
  * Python >= 3.8.5
  
#### 1.1 - Bibliotecas do Python necessárias:
  * numpy
  * memory_profiler
  * sys
  * datetime
  * matplotlib
  * math
  
#### 1.2 - Instalação:
  1. Clone o repositório usando: <code>git clone https://github.com/ArthurGM18/Metodologia-Artigo</code>.
  2. Utilize <code>cd Metodologia-Artigo/codigo/</code> para entrar na pasta com os arquivos.
 
## 2 - Sobre o Sistema

#### 2.1 - Funcionamento geral

  O sistema gera arquivos aleatórios que servem de entrada para testes do algoritmo de ordenação Counting Sort. O primeiro código que deve ser executado é o referente a gerar os arquivos que servem como entrada para os testes. Os arquivos serão armazenados no diretório dados/.
  
#### 2.2 - Gerador de arquivos de entrada
  
  Esse deve ser o primeiro passo durante a execução deste sistema, já que os arquivos de testes devem ser gerados pelo próprio usuário. Os arquivos serão armazenados no diretório dados/. Para executar o código de gerador é necessário estar dentro do diretório codigo/ e rodar o comando:
  
  <code> python3 gerador.py </code>
  
  O processo de execução é um pouco demorado pelo fato do sistema estar criando arquivos com diferentes tamanhos. Ao final do processo o diretório dados/ terá 708.3 MB
