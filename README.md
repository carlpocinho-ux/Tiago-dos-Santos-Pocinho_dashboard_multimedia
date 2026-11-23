# Tiago dos Santos Pocinho_dashboard_multimedia.
Projeto Multimédia de Programação com Inteligência Artificial

Nome da Aplicação / Dashboard Web:
Disciplina: Oficina de Multimédia - 12.o Ano - CRSI
Ano Letivo: 2026/2027
Autor: Tiago dos Santos Pocinho
Turma: A3
Link da Aplicação Web: 

1. Visão Geral do Projeto
Descrição: Dashboard web com 3 ferramentas interativas, criadas a partir das minhas fichas de Python e ampliadas com Inteligência Artificial: um analisador semântico de textos com nuvem de palavras, um estúdio de bateria com sequenciador de ritmos e um quiz sobre multimédia e bateria. O projeto junta programação, design de interface e som numa única página.
Proposta Escolhida: Proposta 1 - Dashboard Web de Ferramentas Multimédia com IA.

2. Estrutura do Código e Funcionalidades Integradas
Parte dos exercícios foi adaptada das fichas e parte foi criada de raiz com ajuda da IA. A lógica das fichas, escrita em Python, foi convertida para JavaScript, porque o GitHub Pages só publica páginas estáticas (HTML/CSS/JS). Toda a aplicação está num único ficheiro, o index.html.

Widget 1 - Analisador semântico (adaptado da Ficha 1):
•	Origem nas fichas: strings, listas, dicionários e contagem de frequências de palavras; leitura de ficheiros .txt.

•	Funcionalidades:
o	escrever ou colar um texto (poema, frase ou texto) ou carregar um ficheiro .txt;
o	estatísticas: nº de linhas, palavras e palavras únicas;
o	filtro de stopwords portuguesas e stopwords extra definidas pelo utilizador;
o	nuvem de palavras personalizável: nº de palavras, 5 paletas (uma delas vem do estúdio de bateria), formato (16:9, 1:1, 9:16) e cor de fundo;
o	tamanho e cor das palavras conforme a frequência;
o	sugestões de sinónimos (dicionário local com 15 palavras);
o	exportação da nuvem em PNG de alta resolução.

•	Ampliação com IA: stopwords e limpeza de pontuação, colocação das palavras em espiral sem sobreposição, sinónimos, exportação em alta resolução e carregamento de .txt.

Widget 2 - Estúdio de Bateria (novo exercício, com conceitos das Fichas 1 e 2):
•	Origem nas fichas:
o	Ficha 2, exercício 1.3.1: a classificação da resolução com if / elif / else passou a classificar o andamento (Largo, Adagio, Andante, Moderato, Allegro, Presto);
o	Ficha 1: listas (cada ritmo é uma lista de 0 e 1), dicionários (os presets) e contagem de elementos (notas por peça).

•	Funcionalidades:
o	sequenciador de 16 passos com 8 peças: Bombo, Tarola, Hi-hat, Tom 1, Tom 2, Timbalão, Crash e Ride;
o	sons sintetizados no próprio browser (Web Audio API), sem ficheiros de áudio;
o	slider de BPM (40 a 220) e classificação do andamento;
o	presets: Rock, Funk, Disco, Blast beat e Rock com Ride;
o	bateria desenhada em SVG, vista do baterista (destro), que se pode tocar com o rato ou com as teclas A S D F J K L Ç;
o	seletor de cor em Hexadecimal para cada peça, que muda a grelha e a bateria;
o	estatísticas do ritmo: notas, densidade, síncopas e dificuldade estimada.

•	Ampliação com IA: gerador de grooves por estilo e dificuldade (fácil, médio, difícil), estimativa da dificuldade, síntese de som com afinação própria para cada peça e desenho da bateria.

Widget 3 - Quiz (adaptado da Ficha 2):
•	Origem nas fichas: o jogo Quiz (pontuação e percentagem com if / else) e o jogo Adivinha o Número (níveis de dificuldade e dicas "maior" ou "menor").

•	Funcionalidades:
o	22 perguntas de multimédia e bateria, em 3 níveis (7 fáceis, 8 médias, 7 difíceis) e um modo misto de 8 perguntas;
o	cronómetro com barra visual (20 s, 15 s e 12 s conforme o nível);
o	pergunta aleatória em cada jogo e aceitação de respostas sem acentos nem maiúsculas;
o	pedido de dica (custa meio ponto) e, quando se erra, dica automática e segunda tentativa; nas respostas numéricas a dica diz se o número é maior ou menor;
o	sequência de acertos, mensagens motivacionais que dependem do desempenho, pontuação em % e recorde guardado no browser.

•	Ampliação com IA: dicas automáticas, mensagens adaptativas, níveis de dificuldade e cronómetro.


3. Registo de Utilização da IA
Para demonstrares como trabalhaste em parceria com o Copilot, Gemini, Claude,
Mistral, etc., regista:
1. Prompt para conversão Web/HTML
2. Prompt para ampliação e construção de funcionalidades
3. Dificuldades e erros corrigidos com a IA
4. Otimização de Layout: O que sugeriste à IA para alterar no design - cores,
margens, fontes, botões?

4. Estrutura de Ficheiros do Repositório
Listagem simples dos ficheiros presentes na pasta:
   1. index.html – página principal do Dashboard / Web App
   2. style.css (Se necessário) - Folha de estilos para o layout Web
   3. README.md - Este relatório de projeto.
   4. Assets - Imagens, nuvens de palavras geradas, recursos utilizados, etc.

5. Reflexão Crítica e Aprendizagem
O que correu melhor neste projeto foi transformar a minha experiência de baterista num widget. Ver o sequenciador a tocar e a bateria a acender foi o ponto mais motivante. Também gostei de ver as fichas de Python a ganhar vida numa página web. A maior dificuldade foi adaptar a lógica de Python para JavaScript e perceber o código que a IA escrevia, sobretudo o áudio, que é gerado por código, e os erros que só apareciam quando eu testava (por exemplo, o som do bombo da bateria que estava, inicialmente, menos grave do que gostaria).A IA mudou profundamente a minha forma de programar. Passei a pedir primeiro uma análise e só depois o código, a testar cada resultado e a pedir correções concretas. A IA acelerou muito o trabalho, mas só funcionou bem quando eu dizia exatamente o que queria com bons prompts, e percebi que tenho de rever sempre o que a IA produz.
 - a IA é, sem dúvida, uma mais-valia quando usada corretamente!

