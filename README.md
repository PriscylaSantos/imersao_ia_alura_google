# Projeto de Descrição de Imagens com Tradução e Braille

## Descrição

Este projeto utiliza a API do Gemini e o Streamlit para criar uma aplicação web interativa que permite aos usuários 
carregar imagens e receber descrições automáticas dessas imagens. Além de fornecer a descrição em inglês, a aplicação 
traduz as descrições para o português e converte o texto traduzido para Braille. Cada descrição e sua tradução podem ser
baixadas como arquivos de texto separados, assim como a versão em Braille.

> É importante dizer que a tradução para braille feita nesse projeto é um **protótipo** e pode conter erros de 
tradução.

![foto1.png](imagens%2Ffoto1.png)

![Descrição da imagem em inglês](imagens%2Ffoto2.png)

![Descrição da imagem em pt-br](imagens%2Ffoto3.png)

![Descrição da imagem em braille](imagens%2Ffoto4.png)


## Funcionalidades

- **Carregamento de Imagens**: Os usuários podem carregar várias imagens nos formatos PNG e JPG.
- **Descrição Automática de Imagens**: A aplicação gera descrições automáticas para as imagens carregadas.
- **Tradução para Português**: Cada descrição é traduzida para o português.
- **Conversão para Braille**: A tradução em português de cada descrição é convertida para Braille.
- **Download de Textos**: Os usuários podem baixar as descrições originais, as traduções e os textos em Braille.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para desenvolver a aplicação.
- **API do Gemini**: Para descrição das imagens e tradução de texto para português do Brasil
- **Streamlit**: Biblioteca usada para construir a interface da aplicação.
- **Braille**: Módulo utilizado para converter textos em Braille.

## Estrutura do Código

O projeto é composto pelos seguintes componentes principais:

1. **Interface Streamlit**: Permite aos usuários interagir com a aplicação através de uma interface web.
2. **Gemini**: Classe responsável pelas operações de descrição de imagem e tradução de texto.
3. **Utils**: Contém funções auxiliares, incluindo a codificação de imagens em base64.
4. **Braille**: Funcionalidade que lida com a conversão de textos para Braille.

## Configuração e Execução

Para executar este projeto localmente, siga os passos abaixo:

### Pré-requisitos

As bibliotecas necessárias estão especificadas em `requirements.txt`

#### SDK Python da Google AI para a API Gemini

1. Acesse [Google AI Studio](https://aistudio.google.com/).
2. Faça login com sua conta Google.
3. [Crie](https://aistudio.google.com/app/apikey) uma chave API.
4. Experimente um [início rápido](https://github.com/google-gemini/gemini-api-cookbook/blob/main/quickstarts/Prompting.ipynb) do SDK Python no [Gemini API Cookbook](https://github.com/google-gemini/gemini-api-cookbook/).
5. Para instruções detalhadas, consulte o 
[tutorial do SDK Python](https://ai.google.dev/tutorials/python_quickstart) em [ai.google.dev](https://ai.google.dev).


### Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/PriscylaSantos/imersao_ia_alura_google.git
cd imersao_ia_alura_google
pip install -r requirements.txt
```

Insira sua chave da API do Gemini na variavel **GOOGLE_API_KEY** no arquivo `config.py `. Tambem pode alterar os parametros das variáveis **GENERATION_CONFIG** e **SAFETY_SETTINGS**

![config.png](imagens%2Fconfig.png)

### Execução

Execute a aplicação utilizando Streamlit:

```bash
streamlit run main.py
```

A aplicação será acessível no navegador em `http://localhost:8501`.

## Sobre o Braille

> É importante dizer que a tradução para braille feita nesse projeto é um **protótipo** e pode conter erros de 
tradução.

Quando se trata de adaptar sistemas de escrita para braille, cada idioma pode apresentar desafios únicos devido às suas 
características linguísticas específicas. A adaptação do alfabeto brasileiro para o braille inclui caracteres como letras 
acentuadas e o "ç". No entanto, é importante destacar que o sistema original de braille, desenvolvido por 
[Louis Braille](https://pt.wikipedia.org/wiki/Louis_Braille) não foi concebido para acomodar diretamente caracteres 
acentuados ou o "ç", que são típicos de idiomas como o português.

### Desafios de Tradução para o Braille em Português

O braille padrão é constituído por seis pontos, que permitem 64 combinações possíveis (incluindo a posição em branco). 
Isso é suficiente para cobrir o alfabeto básico de 26 letras, números e alguns sinais de pontuação, mas não é adequado 
para representar todos os acentos e caracteres especiais presentes em muitas línguas, incluindo o português. Como 
resultado, vários sistemas de braille têm sido adaptados regionalmente para incluir esses caracteres. 

No caso específico do português, o sistema de braille deve acomodar caracteres como `"á", "é", "í", "ó", "ú", "â", "ê", "ô", "ã", "õ", "à", "ç"`, 
entre outros. Para lidar com essa necessidade, foram desenvolvidas convenções adicionais que utilizam combinações de 
células de braille para representar um único caractere impresso. 

### Implicações da Adaptação

Essas adaptações podem levar a erros de tradução, especialmente quando ferramentas automáticas de conversão de texto 
para braille são utilizadas sem as devidas adaptações para o idioma específico. Um sistema de tradução que não reconheça 
e trate corretamente esses caracteres acentuados e especiais pode falhar ao representá-los adequadamente em braille, o 
que resulta em uma transcrição incorreta e potencialmente confusa para o leitor.

### Exemplo

O texto **Hoje você pode comprar maçã?** traduzido por esse projeto:

![terminal.png](imagens%2Fterminal.png)


Essa é a resposta gerada: ⠓⠕⠚⠑⠀⠧⠕⠉⠖⠀⠏⠕⠙⠑⠀⠉⠕⠍⠏⠗⠁⠗⠀⠍⠁⠉⠯⠹

Inserindo esse texto em um [tradutor de braille](https://symbl.cc/pt/tools/braille/):

![site.png](imagens%2Fsite.png)


## Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para criar um fork do repositório, fazer suas alterações e submeter um Pull Request.


---

Este `README.md` fornece uma visão geral detalhada do projeto, explicando suas funcionalidades, tecnologias utilizadas, e como configurar e executar a aplicação localmente. 
Ele serve como um guia tanto para usuários quanto para desenvolvedores interessados em contribuir para o projeto.
