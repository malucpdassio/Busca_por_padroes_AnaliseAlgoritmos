TEXTO = """Neste capítulo você executará seu primeiro programa
Python, hello_world.py. Em primeiro lugar, verifique se
Python está instalado em seu computador; se não estiver,
instale-o. Instale também um editor de texto para
trabalhar com seus programas Python. Editores de texto
reconhecem código Python e enfatizam determinadas
seções à medida que você escrever o código, facilitando
entender a sua estrutura.
Configurando seu ambiente de programação
Python difere um pouco em sistemas operacionais distintos, portanto, você
deverá ter algumas considerações em mente. Veremos aqui duas versões
importantes de Python atualmente em uso, e apresentaremos os passos
para configurar Python em seu sistema.
Python 2 e Python 3
Atualmente, duas versões de Python estão disponíveis: Python 2 e Python
3, a mais recente. Toda linguagem de programação evolui à medida que
surgem novas ideias e tecnologias, e os desenvolvedores de Python têm
deixado a linguagem mais versátil e eficaz de forma contínua. A maioria
das alterações é incremental e dificilmente perceptível, mas, em alguns
casos, um código escrito para Python 2 poderá não executar de modo
apropriado em sistemas com a versão Python 3 instalada. Ao longo deste
livro, destacarei as áreas em que houver diferenças significativas entre
Python 2 e Python 3, portanto, independentemente da versão usada, você
poderá seguir as instruções.
Se as duas versões estiverem instaladas em seu sistema ou se precisar
instalar Python, instale Python 3. Se Python 2 for a única versão em seu
sistema e você prefira escrever código de imediato em vez de instalar
Python, poderá começar com Python 2. Porém, quanto antes fizer o
upgrade para Python 3, melhor será, pois você estará trabalhando com a
versão mais recente.
Executando trechos decódigo Python
Python tem um interpretador que executa em uma janela de terminal,
permitindo que você teste porções de código Python sem precisar salvar e
executar um programa completo.
Neste livro você verá trechos de código semelhantes a:
u >>> print("Hello Python interpreter!")
Hello Python interpreter!
O texto em negrito é o que você digitará e então executará teclando
ENTER. A maioria dos exemplos do livro são programas pequenos,
autocontidos, que serão executados a partir de seu editor, pois é assim que
você escreverá a maior parte de seu código. Às vezes, porém, conceitos
básicos serão mostrados em uma série de trechos de código executados em
uma sessão de terminal Python para demonstrar conceitos isolados de
modo mais eficiente. Sempre que você vir os três sinais de maior em uma
listagem de código u, estará vendo a saída de uma sessão de terminal.
Experimentaremos programar no interpretador de seu sistema em breve.
HelloWorld!
Uma crença de longa data no mundo da programação é que exibir uma
mensagem Hello world! na tela como seu primeiro programa em uma nova
linguagem trará sorte.
Em Python, podemos escrever o programa Hello World com uma linha:
print("Hello world!")
Um programa simples como esse tem um verdadeiro propósito. Se
executar corretamente em seu sistema, qualquer programa Python que
você escrever também deverá funcionar. Em breve, veremos como escrever
esse programa em seu sistema em particular.
Python emsistemas operacionais diferentes
Python é uma linguagem de programação para diversas plataformas, o que
significa que ela executará em todos os principais sistemas operacionais.
Qualquer programa Python que você escrever deverá executar em qualquer
computador moderno que tenha Python instalado. No entanto, os
métodos para configurar Python em diferentes sistemas operacionais
variam um pouco.
Nesta seção aprenderemos a configurar Python e a executar o programa
Hello World em seu próprio sistema. Em primeiro lugar, verifique se
Python está instalado em seu sistema e instale-o, se não estiver. Em
seguida, você instalará um editor de texto simples e salvará um arquivo
Python vazio chamado hello_world.py. Por fim, executará o programa
Hello World e solucionará qualquer problema que houver. Acompanharei
você nesse processo em cada sistema operacional para que você tenha um
ambiente de programação Python amigável a iniciantes.
Python no Linux
Sistemas Linux são projetados para programação, portanto, Python já está
instalado na maioria dos computadores Linux. As pessoas que escrevem e
dão manutenção em Linux esperam que você programe por conta própria
em algum momento e o incentivam a fazê-lo. Por esse motivo, há poucos
itens que precisam ser instalados e poucos parâmetros que devem ser
alterados para começar a programar.
Verificando suaversão de Python
Abra uma janela de terminal executando a aplicação Terminal em seu
sistema (no Ubuntu, você pode pressionar CTRL-ALT-T). Para descobrir se
Python está instalado, digite python com p minúsculo. Você deverá ver uma
saída que informa qual versão de Python está instalada e um prompt >>>
em que poderá começar a fornecer comandos Python, assim:
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:38)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
Essa saída informa que, no momento, Python 2.7.6 é a versão-padrão de
Python instalada nesse computador. Quando vir essa saída, pressione
CTRL-D ou digite exit() para sair do prompt de Python e retornar a um
prompt do terminal.
Para verificar se Python 3 está instalada, talvez você precise especificar
essa versão; portanto, mesmo que a saída tenha mostrado Python 2.7 como
a versão-padrão, experimente executar o comando python3:
$ python3
Python 3.5.0 (default, Sep 17 2015, 13:05:18)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
Essa saída quer dizer que você também tem Python 3 instalada, portanto,
poderá usar qualquer uma das versões. Sempre que vir o comando python
neste livro, digite python3 em seu lugar. A maioria das distribuições Linux
já tem Python instalada, mas se, por algum motivo, a sua não tiver ou se
seu sistema veio com Python 2 e você quer instalar Python 3, consulte o
Apêndice A.
Instalando umeditor detexto
O Geany é um editor de texto simples: é fácil de instalar, permitirá
executar quase todos os seus programas diretamente do editor em vez do
terminal, dá destaque à sintaxe para colorir seu código e executa-o em uma
janela do terminal; desse modo, você se acostumará a usar terminais. O
Apêndice B tem informações sobre outros editores de texto, porém
recomendo usar o Geany, a menos que você tenha um bom motivo para
utilizar um editor diferente.
Você pode instalar o Geany com uma linha na maioria dos sistemas
Linux:
$ sudo apt-get install geany
Se isso não funcionar, veja as instruções em
http://geany.org/Download/ThirdPartyPackages/.
Executando o programa HelloWorld
Para começar seu primeiro programa, abra o Geany. Pressione a tecla Super
(muitas vezes chamada de tecla Windows) e procure o Geany em seu
sistema. Crie um atalho arrastando o ícone para sua barra de tarefas ou o
desktop. Em seguida, crie uma pasta para seus projetos em algum lugar de
seu sistema e chame-a de python_work. (É melhor usar letras minúsculas e
underscores para espaços em nomes de arquivos e de pastas, pois fazem
parte das convenções de nomenclatura de Python.) Volte para o Geany e
salve um arquivo Python vazio (File4Save As, ou Arquivo4Salvar como)
chamado hello_world.py em sua pasta python_work. A extensão .py
informa o Geany que seu arquivo conterá um programa Python. Também
diz ao Geany como executar seu programa e dar destaque ao texto de
modo conveniente.
Após ter salvado seu arquivo, forneça a linha a seguir:
print("Hello Python world!")
Se várias versões de Python estiverem instaladas em seu sistema, será
preciso garantir que o Geany esteja configurado para utilizar a versão
correta. Acesse Build4Set Build Commands (Construir 4Definir
Comandos de Construção). Você deverá ver as palavras Compile e Execute
com um comando ao lado de cada um. O Geany pressupõe que o comando
correto para cada um é python, mas se seu sistema utiliza o comando
python3, será necessário alterar essa informação.
Se o comando python3 funcionou em uma sessão de terminal, mude os
comandos Compile e Execute para que o Geany utilize o interpretador do
Python 3. Seu comando Compile deve ser:
python3 -m py_compile "%f"
É preciso digitar esse comando exatamente como mostrado. Certifique-se
de que o espaçamento e o uso de letras maiúsculas e minúsculas estejam
exatamente iguais ao que foi mostrado aqui.
Seu comando Execute deve ser:
python3 "%f"
Novamente, certifique-se de que o espaçamento e o uso de letras
maiúsculas e minúsculas estejam iguais ao que foi mostrado aqui. A Figura
1.1 mostra como devem ser esses comandos no menu de configuração do
Geany.
Figura 1.1 – Nesse caso, o Geany está configurado para usar Python 3 no Linux.
Agora execute hello_world.py selecionando Build4Execute
(Construir4Executar) no menu, clicando no ícone Execute (Executar, que
mostra um conjunto de engrenagens) ou pressionando F5. Uma janela de
terminal deve aparecer com a saída a seguir:
Hello Python world!
------------------
(program exited with code: 0)
Press return to continue
Se não vir isso, confira todos os caracteres da linha que você inseriu. Você
não usou letra maiúscula acidentalmente em print? Você não esqueceu
uma das aspas, ou as duas, ou os parênteses? As linguagens de
programação esperam uma sintaxe bem específica e, se você não a
fornecer, haverá erros. Se não conseguir fazer o programa executar, veja a
seção “Resolvendo problemas de instalação”.
Executando Python emumasessão determinal
Você pode tentar executar trechos de código Python abrindo um terminal e
digitando python ou python3, como fizemos quando conferimos sua versão.
Faça isso novamente, porém, desta vez, digite a linha a seguir na sessão do
terminal:
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>
Você deverá ver sua mensagem exibida diretamente na janela de terminal
usada no momento. Lembre-se de que você pode fechar o interpretador
Python teclando CTRL-D ou digitando o comando exit().
Python no OSX
Python já vem instalado na maioria dos sistemas OS X. Depois que tiver
certeza de que Python está presente, você precisará instalar um editor de
texto e garantir que esteja configurado corretamente.
Verificando se Python estáinstalado
Abra uma janela de terminal acessando Applications4Utilities4Terminal
(Aplicativos4Utilitários4Terminal). Você também pode pressionar
COMMAND-barra de espaço, digitar terminal e, então, teclar ENTER. Para
descobrir se Python está instalado, digite python com p minúsculo. Você
deverá ver uma saída que informa qual versão de Python está instalada em
seu sistema e um prompt >>> em que poderá começar a fornecer comandos
Python, assim:
$ python
Python 2.7.5 (default, Mar 9 2014, 22:15:05)
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>
Essa saída informa que, no momento, Python 2.7.5 é a versão-padrão de
Python instalada nesse computador. Quando vir essa saída, pressione
CTRL-D ou digite exit() para sair do prompt de Python e retornar a um
prompt do terminal.
Para conferir se você tem Python 3, experimente executar o comando
python3. Você pode obter uma mensagem de erro, mas se a saída mostrar
que Python 3 está instalada, você poderá usar essa versão sem precisar
instalá-la. Se python3 funcionar em seu sistema, sempre que vir o comando
python neste livro, lembre-se de usar python3 em seu lugar. Se, por algum
motivo, seu sistema não veio com Python ou se você só tem Python 2 e
quer instalar Python 3 agora, consulte o Apêndice A.
Executando Python emumasessão determinal
Você pode testar trechos de código Python abrindo um terminal e
digitando python ou python3, como fizemos quando conferimos nossa
versão. Faça isso novamente, porém, dessa vez, digite a linha a seguir na
sessão do terminal:
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>
Você deverá ver sua mensagem exibida diretamente na janela de terminal
usada no momento. Lembre-se de que o interpretador Python pode ser
fechado teclando CTRL-D ou digitando o comando exit().
Instalando umeditor detexto
O Sublime Text é um editor de texto simples: é fácil de instalar no OS X,
permitirá executar quase todos os seus programas diretamente do editor
em vez do terminal, dá destaque à sintaxe para colorir seu código e
executa-o em uma sessão de terminal incluída na janela do Sublime Text
para que seja mais fácil ver a saída. O Apêndice B tem informações sobre
outros editores de texto, mas recomendo usar o Sublime Text, a menos que
você tenha um bom motivo para utilizar um editor diferente.
Você pode fazer download do instalador do Sublime Text a partir de
http://sublimetext.com/3. Clique no link para download e procure um
instalador para OS X. O Sublime Text tem uma política de licença bem
liberal: você pode usar o editor gratuitamente durante o tempo que quiser,
mas o autor pede que você compre uma licença se gostar dele e quiser
utilizá-lo continuamente. Após ter baixado o instalador, abra-o e então
arraste o ícone do Sublime Text para sua pasta Applications.
Configurando o SublimeText para Python 3
Se você usa um comando diferente de python para iniciar uma sessão de
terminal Python, será necessário configurar o Sublime Text para que ele
saiba onde encontrar a versão correta de Python em seu sistema. Dê o
seguinte comando para descobrir o path completo de seu interpretador
Python:
$ type -a python3
python3 is /usr/local/bin/python3
Agora abra o Sublime Text e acesse Tools4Build System4New Build
System (Ferramentas4Sistema de Construção4Novo Sistema de
Construção), que abrirá um novo arquivo de configuração para você.
Apague o que vir e insira o seguinte:
Python3.sublime-build
{
"cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
Esse código diz ao Sublime Text para usar o comando python3 de seu
sistema quando executar o arquivo aberto no momento. Lembre-se de usar
o path encontrado ao executar o comando type -a python3 no passo
anterior. Salve o arquivo como Python3.sublime-build no diretório default
aberto pelo Sublime Text quando escolher Save (Salvar).
Executando o programa HelloWorld
Para começar seu primeiro programa, inicie o Sublime Text abrindo a pasta
Applications e dando um clique duplo no ícone desse editor. Você também
pode pressionar COMMAND-barra de espaço e inserir sublime text na barra
de pesquisa que aparecer.
Crie uma pasta chamada python_work para seus projetos em algum lugar
de seu sistema. (É melhor usar letras minúsculas e underscores para
espaços em nomes de arquivos e de pastas, pois fazem parte das
convenções de nomenclatura de Python.) Salve um arquivo Python vazio
(File4Save As, ou Arquivo4Salvar como) chamado hello_world.py em sua
pasta python_work. A extensão .py informa o Sublime Text que seu
arquivo conterá um programa Python e lhe diz como executar seu
programa e dar destaque ao texto de forma conveniente.
Após ter salvado seu arquivo, insira a linha a seguir:
print("Hello Python world!")
Se o comando python funciona em seu sistema, você poderá executar seu
programa selecionando Tools4Build (Ferramentas4Construir) no menu
ou pressionando CTRL-B. Se você configurou o Sublime Text para usar um
comando diferente de python, selecione Tools4Build System
(Ferramentas4Sistema de Construção) e então selecione Python 3. Isso
define Python 3 como a versão default de Python, e você poderá selecionar
Tools4Build ou simplesmente pressionar COMMAND-B para executar seus
programas a partir de agora.
Uma tela do terminal deve aparecer na parte inferior da janela do Sublime
Text, mostrando a saída a seguir:
Hello Python world!
[Finished in 0.1s]
Se não vir isso, confira todos os caracteres da linha que você inseriu. Você
não usou uma letra maiúscula acidentalmente em print? Você não
esqueceu uma das aspas, ou as duas, ou os parênteses? As linguagens de
programação esperam uma sintaxe bem específica e, se você não a
fornecer, haverá erros. Se não conseguir fazer o programa executar, veja a
seção “Resolvendo problemas de instalação”.
Python noWindows
O Windows nem sempre vem com Python, portanto, é provável que você
vá precisar fazer download e instalá-lo e, então, fazer download e instalar
um editor de texto.
Instalando Python
Em primeiro lugar, verifique se Python está instalado em seu sistema. Abra
uma janela de comando digitando command no menu Start (Iniciar) ou
segurando a tecla SHIFT, ao mesmo tempo em que dá um clique com o
botão direito do mouse em seu desktop, e selecione Open command
window here (Abrir janela de comando aqui). Na janela do terminal, digite
python com letras minúsculas. Se você obtiver um prompt Python (>>>), é
sinal de que Python está instalado em seu sistema. No entanto, é provável
que você vá ver uma mensagem de erro, informando que python não é um
comando reconhecido.
Nesse caso, faça download do instalador de Python para Windows
acessando http://python.org/downloads/. Você verá dois botões, um para
fazer download de Python 3 e outro para download de Python 2. Clique no
botão para Python 3, o que deverá iniciar automaticamente o download do
instalador correto para o seu sistema. Depois de baixar o arquivo, execute
o instalador. Certifique-se de marcar a opção Add Python to PATH
(Adicionar Python ao PATH), que facilitará configurar o seu sistema
corretamente. A Figura 1.2 mostra essa opção marcada.
Figura 1.2 – Lembre-se de marcar a caixa identificada com Add Python to PATH
(Acrescentar Python ao PATH).
Iniciando umasessão determinal Python
Configurar seu editor de texto será simples se você configurar antes o seu
sistema para executar Python em uma sessão de terminal. Abra uma janela
de comandos e digite python com letras minúsculas. Se você obtiver o
prompt de Python (>>>), é sinal de que o Windows encontrou a versão de
Python que você acabou de instalar:
C:> python
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 22:15:05) [MSC v.1900
32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Se esse comando funcionou, você poderá passar para a próxima seção,
“Executando Python em uma sessão de terminal”.
No entanto, talvez você veja uma saída mais parecida com esta:
C:> python
'python' is not recognized as an internal or external command, operable
program or batch file.
Nesse caso, precisamos informar como o Windows poderá encontrar a
versão de Python que acabamos de instalar. O comando python de seu
sistema normalmente é salvo em seu drive C, portanto, abra o Windows
Explorer e acesse esse drive. Procure uma pasta que começa com o nome
Python, abra-a e localize o arquivo python (com letras minúsculas). Por
exemplo, eu tenho uma pasta Python35 com um arquivo chamado python,
portanto, o path para o comando python em meu sistema é
C:Python35python. Se não encontrar esse arquivo, digite python na caixa
de pesquisa do Windows Explorer para mostrar exatamente em que lugar
o comando python está armazenado em seu sistema.
Quando achar que sabe qual é o path, teste-o fornecendo esse path em
uma janela do terminal. Abra uma janela de comandos e digite o path
completo que você acabou de encontrar:
C:> C:Python35python
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 22:15:05) [MSC v.1900
32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
Se isso funcionar, você saberá como acessar Python em seu sistema.
Executando Python emumasessão determinal
Forneça a linha a seguir em sua sessão de Python e certifique-se de que verá
a saída Hello Python world!
>>> print("Hello Python world!")
Hello Python world!
>>>
Sempre que quiser executar um trecho de código Python, abra uma janela
de comandos e inicie uma sessão de terminal de Python. Para fechar a
sessão de terminal, pressione CTRL-Z e então ENTER, ou digite o comando
exit().
Instalando umeditor detexto
O Geany é um editor de texto simples: é fácil de instalar, permitirá
executar quase todos os seus programas diretamente do editor em vez do
terminal, dá destaque à sintaxe para colorir seu código e executa-o em uma
janela do terminal; desse modo, você se acostumará a usar terminais. O
Apêndice B tem informações sobre outros editores de texto, porém,
recomendo usar o Geany, a menos que você tenha um bom motivo para
utilizar um editor diferente.
Você pode fazer download de um instalador do Geany para Windows a
partir de http://geany.org/. Clique em Releases (Versões) no menu
Download e procure o instalador geany-1.25_setup.exe ou algo semelhante.
Execute o instalador e aceite todos os defaults.
Para iniciar seu primeiro programa, abra o Geany: pressione a tecla
Windows e procure o Geany em seu sistema. Crie um atalho arrastando o
ícone para sua barra de tarefas ou o desktop. Crie uma pasta chamada
python_work para seus projetos em algum lugar de seu sistema. (É melhor
usar letras minúsculas e underscores para espaços em nomes de arquivos e
de pastas, pois fazem parte das convenções de nomenclatura de Python.)
Volte para o Geany e salve um arquivo Python vazio (File4Save As, ou
Arquivo4Salvar como) chamado hello_world.py em sua pasta
python_work. A extensão .py informa ao Geany que seu arquivo conterá
um programa Python. Também diz ao Geany como executar seu programa
e dar destaque ao texto de modo conveniente.
Após ter salvado seu arquivo, insira a linha a seguir:
print("Hello Python world!")
Se o comando python funcionou em seu sistema, não será necessário
configurar o Geany; vá direto para a próxima seção e prossiga para
“Executando o programa Hello Word”. Se você precisou fornecer um path
como C:Python35python para iniciar um interpretador Python, siga as
instruções da próxima seção para configurar o Geany em seu sistema.
Configurando o Geany
Para configurar o Geany, acesse Build4Set Build Commands
(Construir4Definir Comandos de Construção). Você deverá ver as
palavras Compile e Execute com um comando ao lado de cada um. Os
comandos Compile e Execute começam com python em letras minúsculas,
mas o Geany não sabe em que lugar seu sistema armazenou o comando
python. É preciso acrescentar o path usado na sessão de terminal.
Nos comandos Compile e Execute, acrescente o drive em que está o seu
comando python e a pasta em que esse comando está armazenado. Seu
comando Compile deve ter o seguinte aspecto:
C:Python35python -m py_compile "%f"
Seu path pode ser um pouco diferente, mas certifique-se de que o
espaçamento e o uso de letras maiúsculas e minúsculas estejam iguais ao
que foi mostrado aqui.
Seu comando Execute deve ter o seguinte aspecto:
C:Python35python "%f"
Novamente, certifique-se de que o espaçamento e o uso de letras
maiúsculas e minúsculas em seu comando Execute estejam iguais ao que
foi mostrado aqui. A Figura 1.3 mostra como devem ser esses comandos no
menu de configuração do Geany.
Figura 1.3 – Nesse caso, o Geany está configurado para usar Python 3 no Windows.
Após ter configurado esses comandos corretamente, clique em OK.
Executando o programa HelloWorld
Agora você deverá ser capaz de executar seu programa com sucesso.
Execute hello_world.py selecionando Build4Execute
(Construir4Executar) no menu, clicando no ícone Execute (Executar, que
mostra um conjunto de engrenagens) ou pressionando F5. Uma janela de
terminal deve aparecer com a saída a seguir:
Hello Python world!
------------------
(program exited with code: 0)
Press return to continue
Se não vir isso, confira todos os caracteres da linha que você inseriu. Você
não usou uma letra maiúscula acidentalmente em print? Você não
esqueceu uma das aspas, ou as duas, ou os parênteses? As linguagens de
programação esperam uma sintaxe bem específica e, se você não a
fornecer, haverá erros. Se não conseguir fazer o programa executar,
consulte a próxima seção para obter ajuda.
Resolvendo problemas deinstalação
Esperamos que a configuração de seu ambiente de programação tenha sido
um sucesso, mas se você não conseguiu executar hello_world.py,
apresentamos a seguir algumas alternativas que você poderá experimentar:
• Quando um programa contiver um erro significativo, Python exibirá
um traceback. O interpretador olha o arquivo e tenta informar o
problema. O traceback pode oferecer uma pista sobre o problema que
está impedindo seu programa de executar.
• Afaste-se de seu computador, faça um pequeno intervalo e, então, tente
novamente. Lembre-se de que a sintaxe é muito importante em
programação, de modo que, até mesmo a falta de um caractere de dois￾pontos, uma aspa ausente ou um parêntese sem par pode impedir que
um programa execute de forma apropriada. Releia as partes relevantes
deste capítulo, verifique o que você fez e veja se consegue encontrar o
erro.
• Comece de novo. Provavelmente você não precisará desinstalar nada,
mas pode ser que faça sentido apagar seu arquivo hello_world.py e criá-
lo novamente do zero.
• Peça a outra pessoa para seguir os passos deste capítulo em seu
computador, ou em um computador diferente, e observe essa pessoa
atentamente. Talvez você tenha deixado passar um pequeno passo que
outra pessoa, por acaso, percebeu.
• Encontre alguém que conheça Python e peça-lhe ajuda. Se perguntar
por aí, talvez você descubra que conhece alguém que use Python.
• As instruções de configuração deste capítulo também estão disponíveis
online em https://www.nostarch.com/pythoncrashcourse/. A versão
online dessas instruções talvez seja mais adequada a você.
• Peça ajuda online. O Apêndice C apresenta vários recursos e áreas
online, como fóruns e sites com bate-papos ao vivo, em que é possível
pedir soluções para pessoas que já passaram pelo problema que você
está enfrentando no momento.
Não se preocupe em incomodar programadores experientes. Todo
programador já ficou sem saber o que fazer em algum momento, e a
maioria deles ficará feliz em ajudar você a configurar seu sistema
corretamente. Desde que você consiga explicar claramente o que está
tentando fazer, o que já tentou e os resultados que está obtendo, há uma
boa chance de que alguém possa ajudá-lo. Como mencionamos na
Introdução, a comunidade Python é bem receptiva aos iniciantes.
Python deve executar bem em qualquer computador moderno, portanto,
encontre uma maneira de pedir ajuda se estiver com problemas até o
momento. Problemas iniciais podem ser frustrantes, mas vale a pena
resolvê-los. Depois que conseguir executar o programa hello_world.py,
você poderá começar a aprender Python e seu trabalho de programação se
tornará mais interessante e satisfatório.
Executando programas Python a partir de umterminal
A maior parte dos programas que você escrever em seu editor de texto será
executada diretamente do editor, mas, às vezes, será conveniente executar
programas a partir de um terminal. Por exemplo, talvez você queira
executar um programa existente sem abri-lo para edição.
Você pode fazer isso em qualquer sistema com Python instalado se
souber como acessar o diretório em que seu arquivo de programa está
armazenado. Para testar isso, certifique-se de ter salvo o arquivo
hello_world.py na pasta python_work em seu desktop.
No Linuxe no OSX
Executar um programa Python a partir de uma sessão de terminal é igual
no Linux e no OS X. O comando de terminal cd, de change directory
(mudar diretório), é usado para navegar pelo seu sistema de arquivos em
uma sessão de terminal. O comando ls, de list (listar), mostra todos os
arquivos não ocultos do diretório atual.
Abra uma nova janela de terminal e dê os comandos a seguir para
executar hello_world.py:
u ~$ cd Desktop/python_work/
v ~/Desktop/python_work$ ls
hello_world.py
w ~/Desktop/python_work$ python hello_world.py
Hello Python world!
Em u usamos cd para navegar até a pasta python_work, que está na pasta
Desktop. Em seguida, utilizamos ls para garantir que hello_world.py está
nessa pasta v. Então executamos o arquivo usando o comando python
hello_world.py w.
É simples assim. Basta usar o comando python (ou python3) para executar
programas Python.
NoWindows
O comando de terminal cd, de change directory (mudar diretório), é usado
para navegar pelo seu sistema de arquivos em uma sessão de terminal. O
comando dir, de directory (diretório), mostra todos os arquivos do
diretório atual.
Abra uma nova janela e dê os comandos a seguir para executar
hello_world.py:
u C:> cd Desktoppython_work
v C:Desktoppython_work> dir
hello_world.py
w C:Desktoppython_work> python hello_world.py
Hello Python world!
Em u usamos o comando cd para navegar até a pasta python_work, que
está na pasta Desktop. Em seguida, utilizamos o comando dir para garantir
que hello_world.py está nessa pasta v. Então executamos o arquivo usando
o comando python hello_world.py w.
Se você não havia configurado seu sistema para usar o comando simples
python, talvez seja necessário usar a versão mais longa desse comando:
C:$ cd Desktoppython_work
C:Desktoppython_work$ dir
hello_world.py
C:Desktoppython_work$ C:Python35python hello_world.py
Hello Python world!
A maior parte de seus programas executará de forma apropriada,
diretamente de seu editor, mas, à medida que seu trabalho se tornar mais
complexo, você poderá escrever programas que precisarão ser executados a
partir de um terminal.
FAÇA VOCÊ MESMO
Os exercícios deste capítulo são exploratórios por natureza. A partir do Capítulo 2,
os desafios que você resolverá serão baseados no que você aprendeu.
1.1 – python.org: Explore a página inicial de Python (http://python.org/) para
encontrar tópicos pelos quais você se interesse. À medida que tiver mais
familiaridade com Python, diferentes partes do site serão mais úteis a você.
1.2 – Erros de digitação em Hello World: Abra o arquivo hello_world.py que
você acabou de criar. Introduza um erro de digitação em algum ponto da linha e
execute o programa novamente. Você é capaz de inserir um erro de digitação que
gere um erro? Consegue entender a mensagem de erro? É capaz de inserir um erro
de digitação que não produza um erro? Por que você acha que isso não gerou um
erro?
1.3 – Habilidades infinitas: Se tivesse infinitas habilidades de programação, o que
você desenvolveria? Você está prestes a aprender a programar. Se tiver um
objetivo final em mente, você terá um uso imediato para suas novas habilidades;
agora é um ótimo momento para esboçar descrições do que você gostaria de criar.
É um bom hábito manter um caderno com “ideias” que você possa consultar sempre
que quiser iniciar um novo projeto. Reserve alguns minutos para descrever três
programas que você gostaria de criar.
Resumo
Neste capítulo aprendemos um pouco sobre Python em geral, e instalamos
Python em seu sistema caso ainda não estivesse presente. Também
instalamos um editor de texto para facilitar escrever código Python.
Aprendemos a executar trechos de código Python em uma sessão de
terminal e executamos nosso primeiro programa, hello_world.py. É
provável que você também tenha aprendido um pouco sobre resolução de
problemas.
No próximo capítulo conheceremos diferentes tipos de dados com os
quais podemos trabalhar em nossos programas Python e aprenderemos a
usar variáveis também.

Neste capítulo conheceremos os diferentes tipos de dados
com os quais podemos trabalhar em nossos programas
Python. Aprenderemos também a armazenar dados em
variáveis e usar essas variáveis em nossos programas.
O querealmenteacontece quando executamos hello_world.py
Vamos observar com mais detalhes o que Python faz quando executamos
hello_world.py. O fato é que Python realiza muitas tarefas, mesmo quando
executa um programa simples:
hello_world.py
print("Hello Python world!")
Quando executar esse código, você deverá ver a saída a seguir:
Hello Python world!
Ao executar hello_world.py, o arquivo terminado em .py indica que é um
programa Python. Seu editor então passa o programa pelo interpretador
Python, que lê o programa todo e determina o que cada palavra significa.
Por exemplo, quando vê a palavra print, o interpretador exibe na tela o que
quer que esteja dentro dos parênteses.
À medida que você escrever seus programas, o editor dará destaque a
diferentes partes do código de modo distinto. Por exemplo, ele reconhece
que print é o nome de uma função e exibe essa palavra em azul. Reconhece
que “Hello Python world!” não é um código Python e exibe essa frase em
laranja. Esse recurso se chama destaque de sintaxe e é muito útil quando
você começar a escrever seus próprios programas.
Variáveis
Vamos experimentar usar uma variável em hello_world.py. Acrescente uma
nova linha no início do arquivo e modifique a segunda linha:
message = "Hello Python world!"
print(message)
Execute esse programa para ver o que acontece. Você deverá ver a mesma
saída vista anteriormente:
Hello Python world!
Acrescentamos uma variável chamada message. Toda variável armazena
um valor, que é a informação associada a essa variável. Nesse caso, o valor
é o texto “Hello Python world!”.
Acrescentar uma variável implica um pouco mais de trabalho para o
interpretador Python. Quando processa a primeira linha, ele associa o
texto “Hello Python world!” à variável message. Quando chega à segunda
linha, o interpretador exibe o valor associado à message na tela.
Vamos expandir esse programa modificando hello_world.py para que
exiba uma segunda mensagem. Acrescente uma linha em branco em
hello_world.py e, em seguida, adicione duas novas linhas de código:
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)
Ao executar hello_world.py agora você deverá ver duas linhas na saída:
Hello Python world!
Hello Python Crash Course world!
Podemos mudar o valor de uma variável em nosso programa a qualquer
momento, e Python sempre manterá o controle do valor atual.
Nomeando e usando variáveis
Ao usar variáveis em Python, é preciso seguir algumas regras e diretrizes.
Quebrar algumas dessas regras provocará erros; outras diretrizes
simplesmente ajudam a escrever um código mais fácil de ler e de entender.
Lembre-se de ter as seguintes regras em mente:
• Nomes de variáveis podem conter apenas letras, números e
underscores. Podem começar com uma letra ou um underscore, mas
não com um número. Por exemplo, podemos chamar uma variável de
message_1, mas não de 1_message.
• Espaços não são permitidos em nomes de variáveis, mas underscores
podem ser usados para separar palavras em nomes de variáveis. Por
exemplo, greeting_message funciona, mas greeting message causará
erros.
• Evite usar palavras reservadas e nomes de funções em Python como
nomes de variáveis, ou seja, não use palavras que Python reservou para
um propósito particular de programação, por exemplo, a palavra print.
(Veja a seção “Palavras reservadas e funções embutidas de Python”.)
• Nomes de variáveis devem ser concisos, porém descritivos. Por
exemplo, name é melhor que n, student_name é melhor que s_n e
name_length é melhor que length_of_persons_name.
• Tome cuidado ao usar a letra minúscula l e a letra maiúscula O, pois
elas podem ser confundidas com os números 1 e 0.
Aprender a criar bons nomes de variáveis, em especial quando seus
programas se tornarem mais interessantes e complicados, pode exigir um
pouco de prática. À medida que escrever mais programas e começar a ler
códigos de outras pessoas, você se tornará mais habilidoso na criação de
nomes significativos.
NOTA As variáveis Python que você está usando no momento devem utilizar letras
minúsculas. Você não terá erros se usar letras maiúsculas, mas é uma boa ideia
evitá-las por enquanto.
Evitando errosemnomesao usarvariáveis
Todo programador comete erros, e a maioria comete erros todos os dias.
Embora bons programadores possam criar erros, eles também sabem
responder a esses erros de modo eficiente. Vamos observar um erro que
você provavelmente cometerá no início e vamos aprender a corrigi-lo.
Escreveremos um código que gera um erro propositadamente. Digite o
código a seguir, incluindo a palavra mesage com um erro de ortografia,
conforme mostrada em negrito:
message = "Hello Python Crash Course reader!"
print(mesage)
Quando houver um erro em seu programa, o interpretador Python faz o
melhor que puder para ajudar você a descobrir onde está o problema. O
interpretador oferece um traceback quando um programa não é capaz de
executar com sucesso. Um traceback é um registro do ponto em que o
interpretador se deparou com problemas quando tentou executar seu
código. Eis um exemplo do traceback fornecido por Python após o nome
da variável ter sido digitado incorretamente por engano:
Traceback (most recent call last):
u File "hello_world.py", line 2, in <module>
v print(mesage)
w NameError: name 'mesage' is not defined
A saída em u informa que um erro ocorreu na linha 2 do arquivo
hello_world.py. O interpretador mostra essa linha para nos ajudar a
identificar o erro rapidamente v e informa o tipo do erro encontrado w.
Nesse caso, ele encontrou um erro de nome e informa que a variável
exibida, mesage, não foi definida. Python não é capaz de identificar o nome
da variável especificada. Um erro de nome geralmente quer dizer que
esquecemos de definir o valor de uma variável antes de usá-la ou que
cometemos um erro de ortografia quando fornecemos o nome da variável.
É claro que, nesse exemplo, omitimos a letra s do nome da variável
message na segunda linha. O interpretador Python não faz uma verificação
de ortografia em seu código, mas garante que os nomes das variáveis
estejam escritos de forma consistente. Por exemplo, observe o que acontece
quando escrevemos message incorretamente em outro ponto do código
também:
mesage = "Hello Python Crash Course reader!"
print(mesage)
Nesse caso, o programa executa com sucesso!
Hello Python Crash Course reader!
Os computadores são exigentes, mas não se preocupam com uma
ortografia correta ou incorreta. Como resultado, você não precisa levar em
consideração a ortografia ou as regras gramaticais do inglês (ou de
português) quando tentar criar nomes de variáveis e escrever código.
Muitos erros de programação são apenas erros de digitação de um
caractere em uma linha de um programa. Se você gasta muito tempo
procurando um desses erros, saiba que está em boa companhia. Muitos
programadores experientes e talentosos passam horam caçando esses tipos
de pequenos erros. Tente rir da situação e siga em frente, sabendo que isso
acontecerá com frequência durante sua vida de programador.
NOTA A melhor maneira de entender novos conceitos de programação é tentar usá-
los em seus programas. Se não souber o que fazer quando estiver trabalhando
em um exercício deste livro, procure dedicar-se a outra tarefa por um tempo. Se
continuar sem conseguir avançar, analise a parte relevante do capítulo. Se ainda
precisar de ajuda, veja as sugestões no Apêndice C.
FAÇA VOCÊ MESMO
Escreva um programa separado para resolver cada um destes exercícios. Salve
cada programa com um nome de arquivo que siga as convenções-padrão de
Python, com letras minúsculas e underscores, por exemplo, simple_message.py e
simple_messages.py.
2.1 – Mensagem simples: Armazene uma mensagem em uma variável e, em
seguida, exiba essa mensagem.
2.2 – Mensagens simples: Armazene uma mensagem em uma variável e, em
seguida, exiba essa mensagem. Então altere o valor de sua variável para uma
nova mensagem e mostre essa nova mensagem.
Strings
Como a maior parte dos programas define e reúne algum tipo de dado e
então faz algo útil com eles, classificar diferentes tipos de dados é
conveniente. O primeiro tipo de dado que veremos é a string. As strings, à
primeira vista, são bem simples, mas você pode usá-las de vários modos
diferentes.
Uma string é simplesmente uma série de caracteres. Tudo que estiver
entre aspas é considerada uma string em Python, e você pode usar aspas
simples ou duplas em torno de suas strings, assim:
"This is a string."
'This is also a string.'
Essa flexibilidade permite usar aspas e apóstrofos em suas strings:
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
Vamos explorar algumas das maneiras de usar strings.
Mudando para letras maiúsculas e minúsculas em uma string usando
métodos
Uma das tarefas mais simples que podemos fazer com strings é mudar o
tipo de letra, isto é, minúscula ou maiúscula, das palavras de uma string.
Observe o código a seguir e tente determinar o que está acontecendo:
name.py
name = "ada lovelace"
print(name.title())
Salve esse arquivo como name.py e então execute-o. Você deverá ver esta
saída:
Ada Lovelace
Nesse exemplo, a string com letras minúsculas "ada lovelace" é
armazenada na variável name. O método title() aparece depois da variável
na instrução print(). Um método é uma ação que Python pode executar em
um dado. O ponto (.) após name em name.title() informa a Python que o
método title() deve atuar na variável name. Todo método é seguido de um
conjunto de parênteses, pois os métodos, com frequência, precisam de
informações adicionais para realizar sua tarefa. Essas informações são
fornecidas entre os parênteses. A função title() não precisa de nenhuma
informação adicional, portanto seus parênteses estão vazios.
title() exibe cada palavra com uma letra maiúscula no início. Isso é útil,
pois, muitas vezes, você vai querer pensar em um nome como uma
informação. Por exemplo, você pode querer que seu programa reconheça
os valores de entrada Ada, ADA e ada como o mesmo nome e exiba todos eles
como Ada.
Vários outros métodos úteis estão disponíveis para tratar letras
maiúsculas e minúsculas também. Por exemplo, você pode mudar uma
string para que tenha somente letras maiúsculas ou somente letras
minúsculas, assim:
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
Essas instruções exibirão o seguinte:
ADA LOVELACE
ada lovelace
O método lower() é particularmente útil para armazenar dados. Muitas
vezes, você não vai querer confiar no fato de seus usuários fornecerem
letras maiúsculas ou minúsculas, portanto fará a conversão das strings para
letras minúsculas antes de armazená-las. Então, quando quiser exibir a
informação, usará o tipo de letra que fizer mais sentido para cada string.
Combinando ou concatenando strings
Muitas vezes, será conveniente combinar strings. Por exemplo, você pode
querer armazenar um primeiro nome e um sobrenome em variáveis
separadas e, então, combiná-las quando quiser exibir o nome completo de
alguém:
first_name = "ada"
last_name = "lovelace"
u full_name = first_name + " " + last_name
print(full_name)
Python usa o símbolo de adição (+) para combinar strings. Nesse
exemplo, usamos + para criar um nome completo combinando first_name,
um espaço e last_name u, o que resultou em:
ada lovelace
Esse método de combinar strings se chama concatenação. Podemos usar
concatenação para compor mensagens completas usando informações
armazenadas em uma variável. Vamos observar um exemplo:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
u print("Hello, " + full_name.title() + "!")
Nesse caso, o nome completo é usado em u, em uma sentença que saúda
o usuário, e o método title() é utilizado para formatar o nome de forma
apropriada. Esse código devolve uma saudação simples, porém formatada
de modo elegante:
Hello, Ada Lovelace!
Podemos usar concatenação para compor uma mensagem e então
armazenar a mensagem completa em uma variável:
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
u message = "Hello, " + full_name.title() + "!"
v print(message)
Esse código também exibe a mensagem “Hello, Ada Lovelace!”, mas
armazenar a mensagem em uma variável em u deixa a instrução print final
em v muito mais simples.
Acrescentando espaçosem branco em strings com tabulações ou quebras
delinha
Em programação, espaços em branco se referem a qualquer caractere que
não é mostrado, como espaços, tabulações e símbolos de fim de linha.
Podemos usar espaços em branco para organizar a saída de modo que ela
seja mais legível aos usuários.
Para acrescentar uma tabulação em seu texto, utilize a combinação de
caracteres t como mostrado em u:
>>> print("Python")
Python
u >>> print("tPython")
Python
Para acrescentar uma quebra de linha em uma string, utilize a
combinação de caracteres n:
>>> print("Languages:nPythonnCnJavaScript")
Languages:
Python
C
JavaScript
Também podemos combinar tabulações e quebras de linha em uma única
string. A string "nt" diz a Python para passar para uma nova linha e
iniciar a próxima com uma tabulação. O exemplo a seguir mostra como
usar uma string de uma só linha para gerar quatro linhas na saída:
>>> print("Languages:ntPythonntCntJavaScript")
Languages:
Python
C
JavaScript
Quebras de linha e tabulações serão muito úteis nos próximos dois
capítulos, quando começaremos a gerar muitas linhas de saída usando
apenas algumas linhas de código.
Removendo espaçosembranco
Espaços em branco extras podem ser confusos em seus programas. Para os
programadores, 'python' e 'python ' parecem praticamente iguais.
Contudo, para um programa, são duas strings diferentes. Python identifica
o espaço extra em 'python ' e o considera significativo, a menos que você
informe o contrário.
É importante pensar em espaços em branco, pois, com frequência, você
vai querer comparar duas strings para determinar se são iguais. Por
exemplo, uma situação importante pode envolver a verificação dos nomes
de usuário das pessoas quando elas fizerem login em um site. Espaços em
branco extras podem ser confusos em situações muito mais simples
também. Felizmente, Python facilita eliminar espaços em branco extras dos
dados fornecidos pelas pessoas.
Python é capaz de encontrar espaços em branco dos lados direito e
esquerdo de uma string. Para garantir que não haja espaços em branco do
lado direito de uma string, utilize o método rstrip().
u >>> favorite_language = 'python '
v >>> favorite_language
'python '
w >>> favorite_language.rstrip()
'python'
x >>> favorite_language
'python '
O valor armazenado em favorite_language em u contém um espaço em
branco extra no final da string. Quando solicitamos esse valor a Python em
uma sessão de terminal, podemos ver o espaço no final do valor v. Quando
o método rstrip() atua na variável favorite_language em w, esse espaço
extra é removido. Entretanto, a remoção é temporária. Se solicitar o valor
de favorite_language novamente, você poderá ver que a string é a mesma
que foi fornecida, incluindo o espaço em branco extra x.
Para remover o espaço em branco da string de modo permanente, você
deve armazenar o valor com o caractere removido de volta na variável:
>>> favorite_language = 'python '
u >>> favorite_language = favorite_language.rstrip()
>>> favorite_language
'python'
Para remover o espaço em branco da string, você deve remover o espaço
em branco do lado direito da string e então armazenar esse valor de volta
na variável original, como mostrado em u. Alterar o valor de uma variável e
então armazenar o novo valor de volta na variável original é uma operação
frequente em programação. É assim que o valor de uma variável pode
mudar à medida que um programa é executado ou em resposta à entrada
de usuário.
Também podemos remover espaços em branco do lado esquerdo de uma
string usando o método lstrip(), ou remover espaços em branco dos dois
lados ao mesmo tempo com strip():
u >>> favorite_language = ' python '
v >>> favorite_language.rstrip()
' python'
w >>> favorite_language.lstrip()
'python '
x >>> favorite_language.strip()
'python'
Nesse exemplo, começamos com um valor que tem espaços em branco
no início e no fim u. Então removemos os espaços extras do lado direito
em v, do lado esquerdo em w e de ambos os lados em x. Fazer
experimentos com essas funções de remoção pode ajudar você a ter
familiaridade com a manipulação de strings. No mundo real, essas funções
de remoção são usadas com mais frequência para limpar entradas de
usuário antes de armazená-las em um programa.
Evitando erros desintaxecomstrings
Um tipo de erro que você poderá ver com certa regularidade é um erro de
sintaxe. Um erro de sintaxe ocorre quando Python não reconhece uma
seção de seu programa como um código Python válido. Por exemplo, se
usar um apóstrofo entre aspas simples, você produzirá um erro. Isso
acontece porque Python interpreta tudo que estiver entre a primeira aspa
simples e o apóstrofo como uma string. Ele então tenta interpretar o
restante do texto como código Python, o que causa erros.
Eis o modo de usar aspas simples e duplas corretamente. Salve este
programa como apostrophe.py e então execute-o:
apostrophe.py
message = "One of Python's strengths is its diverse community."
print(message)
O apóstrofo aparece entre um conjunto de aspas duplas, portanto o
interpretador Python não terá nenhum problema para ler a string
corretamente:
One of Python's strengths is its diverse community.
No entanto, se você usar aspas simples, o interpretador Python não será
capaz de identificar em que ponto a string deve terminar:
message = 'One of Python's strengths is its diverse community.'
print(message)
Você verá a saída a seguir:
File "apostrophe.py", line 1
message = 'One of Python's strengths is its diverse community.'
^u
SyntaxError: invalid syntax
Na saída, podemos ver que o erro ocorre em u, logo depois da segunda
aspa simples. Esse erro de sintaxe informa que o interpretador não
reconheceu algo como código Python válido. Os erros podem ter origens
variadas, e destacarei alguns erros comuns à medida que surgirem. Você
poderá ver erros de sintaxe com frequência enquanto aprende a escrever
código Python apropriado. Erros de sintaxe também são o tipo menos
específico de erro, portanto podem ser difíceis e frustrantes para identificar
e corrigir. Se você não souber o que fazer quanto a um erro particularmente
persistente, consulte as sugestões no Apêndice C.
NOTA O recurso de destaque de sintaxe de seu editor deve ajudar você a identificar
alguns erros de sintaxe rapidamente quando escrever seus programas. Se você
vir código Python em destaque como se fosse inglês, ou inglês destacado como
se fosse código Python, é provável que haja uma aspa sem correspondente em
algum ponto de seu arquivo.
Exibindo informaçõesemPython 2
A instrução print tem uma sintaxe levemente diferente em Python 2:
>>> python2.7
>>> print "Hello Python 2.7 world!"
Hello Python 2.7 world!
Os parênteses não são necessários em torno de frases que você quer
exibir em Python 2. Tecnicamente, print é uma função em Python 3,
motivo pelo qual os parênteses são necessários. Algumas instruções print
em Python 2 incluem parênteses, mas o comportamento pode ser um
pouco diferente do que você verá em Python 3. Basicamente, quando
estiver vendo código escrito em Python 2, espere ver algumas instruções
print com parênteses e outras sem.
FAÇA VOCÊ MESMO
Salve cada um dos exercícios a seguir em um arquivo separado com um nome
como name_cases.py. Se não souber o que fazer, descase um pouco ou consulte
as sugestões que estão no Apêndice C.
2.3 – Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e
apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples, como
“Alô Eric, você gostaria de aprender um pouco de Python hoje?”.
2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma
pessoa em uma variável e então apresente o nome dessa pessoa em letras
minúsculas, em letras maiúsculas e somente com a primeira letra maiúscula.
2.5 – Citação famosa: Encontre uma citação de uma pessoa famosa que você
admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência a
seguir, incluindo as aspas:
Albert Einstein certa vez disse: “Uma pessoa que nunca cometeu um erro jamais
tentou nada novo.”
2.6 – Citação famosa 2: Repita o Exercício 2.5, porém, desta vez, armazene o
nome da pessoa famosa em uma variável chamada famous_person. Em seguida,
componha sua mensagem e armazene-a em uma nova variável chamada message.
Exiba sua mensagem.
2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre￾se de usar cada combinação de caracteres, "t" e "n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome
sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de
remoção de espaços: lstrip(), rstrip() e strip().
Números
Os números são usados com muita frequência em programação para
armazenar pontuações em jogos, representar dados em visualizações,
guardar informações em aplicações web e assim por diante. Python trata
números de várias maneiras diferentes, de acordo com o modo como são
usados. Vamos analisar inicialmente como Python trata inteiros, pois eles
são os dados mais simples para trabalhar.
Inteiros
Você pode somar (+), subtrair (-), multiplicar (*) e dividir (/) inteiros em
Python.
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
Em uma sessão de terminal, Python simplesmente devolve o resultado da
operação. Dois símbolos de multiplicação são usados em Python para
representar exponenciais:
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
A linguagem Python também aceita a ordem das operações, portanto
você pode fazer várias operações em uma expressão. Também podemos
usar parênteses para modificar a ordem das operações para que Python
possa avaliar sua expressão na ordem que você especificar. Por exemplo:
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
Os espaços nesses exemplos não têm nenhum efeito no modo como
Python avalia as expressões: eles simplesmente ajudam a identificar mais
rapidamente as operações que têm prioridade quando lemos o código.
Números de ponto flutuante
Python chama qualquer número com um ponto decimal de número de
ponto flutuante (float). Esse termo é usado na maioria das linguagens de
programação e refere-se ao fato de um ponto decimal poder aparecer em
qualquer posição em um número. Toda linguagem de programação deve
ser cuidadosamente projetada para lidar de modo adequado com números
decimais de modo que eles se comportem de forma apropriada, não
importa em que lugar o ponto decimal apareça.
Na maioria das ocasiões, podemos usar decimais sem nos preocupar com
o modo como eles se comportam. Basta fornecer os números que você quer
usar, e Python provavelmente fará o que você espera:
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
No entanto, tome cuidado, pois, às vezes, você poderá obter um número
arbitrário de casas decimais em sua resposta:
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
Isso acontece em todas as linguagens e não é motivo para muita
preocupação. Python tenta encontrar uma forma de representar o resultado
do modo mais exato possível, o que, às vezes, é difícil, considerando a
maneira como os computadores devem representar os números
internamente. Basta ignorar as casas decimais extras por enquanto; você
aprenderá a lidar com casas extras quando for necessário nos projetos da
Parte II.
Evitando erros detipo comafunção str()
Com frequência, você vai querer usar o valor de uma variável em uma
mensagem. Por exemplo, suponha que você queira desejar feliz aniversário
a alguém. Você poderia escrever um código como este:
birthday.py
age = 23
message = "Happy " + age + "rd Birthday!"
print(message)
Você esperaria que esse código exibisse a seguinte saudação simples de
feliz aniversário: Happy 23rd birthday!. Contudo, se executar esse código,
verá que ele gera um erro:
Traceback (most recent call last):
File "birthday.py", line 2, in <module>
message = "Happy " + age + "rd Birthday!"
u TypeError: Can't convert 'int' object to str implicitly
É um erro de tipo. Significa que Python não é capaz de reconhecer o tipo
de informação que você está usando. Nesse exemplo, Python vê que você
está usando uma variável em u cujo valor é um inteiro (int), mas não tem
certeza de como interpretar esse valor. O interpretador sabe que a variável
poderia representar um valor numérico 23 ou os caracteres 2 e 3. Quando
usar inteiros em strings desse modo, você precisará especificar
explicitamente que quer que Python utilize o inteiro como uma string de
caracteres. Podemos fazer isso envolvendo a variável com a função str();
essa função diz a Python para representar valores que não são strings como
strings:
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)
Com isso, Python sabe que você quer converter o valor numérico 23 em
uma string e exibir os caracteres 2 e 3 como parte da mensagem de feliz
aniversário. Agora você obterá a mensagem esperada, sem erros:
Happy 23rd Birthday!
Trabalhar com números em Python é simples na maior parte do tempo.
Se você estiver obtendo resultados inesperados, verifique se Python está
interpretando seus números da forma desejada, seja como um valor
numérico, seja como um valor de string.
InteirosemPython 2
Python 2 devolve um resultado um pouco diferente quando dividimos dois
inteiros:
>>> python2.7
>>> 3 / 2
1
Em vez de 1.5, Python devolve 1. A divisão de inteiros em Python 2
resulta em um inteiro com o resto truncado. Observe que o resultado não é
um inteiro arredondado; o resto é simplesmente omitido.
Para evitar esse comportamento em Python 2, certifique-se de que pelo
menos um dos números seja um número de ponto flutuante. Ao fazer isso,
o resultado também será um número de ponto flutuante:
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
Esse comportamento da divisão é uma fonte comum de confusão quando
as pessoas que estão acostumadas a usar Python 3 começam a usar Python
2 ou vice-versa. Se você usa ou cria código que mistura inteiros e números
de ponto flutuante, tome cuidado com comportamentos irregulares.
FAÇA VOCÊ MESMO
2.8 – Número oito: Escreva operações de adição, subtração, multiplicação e
divisão que resultem no número 8. Lembre-se de colocar suas operações em
instruções print para ver os resultados. Você deve criar quatro linhas como esta:
print(5 + 3)
Sua saída deve simplesmente ser composta de quatro linhas, com o número 8 em
cada uma das linhas.
2.9 – Número favorito: Armazene seu número favorito em uma variável. Em
seguida, usando essa variável, crie uma mensagem que revele o seu número
favorito. Exiba essa mensagem.
Comentários
Comentários são um recurso extremamente útil na maioria das linguagens
de programação. Tudo que você escreveu em seus programas até agora é
código Python. À medida que seus programas se tornarem mais longos e
complicados, você deve acrescentar notas que descrevam a abordagem
geral adotada para o problema que você está resolvendo. Um comentário
permite escrever notas em seus programas em linguagem natural.
Como escrever comentários?
Em Python, o caractere sustenido (#) indica um comentário. Tudo que vier
depois de um caractere sustenido em seu código será ignorado pelo
interpretador Python. Por exemplo:
comment.py
# Diga olá a todos
print("Hello Python people!")
Python ignora a primeira linha e executa a segunda.
Hello Python people!
Quetipos decomentário você deveescrever?
O principal motivo para escrever comentários é explicar o que seu código
deve fazer e como você o faz funcionar. Quando estiver no meio do
trabalho de um projeto, você entenderá como todas as partes se encaixam.
Porém, quando retomar um projeto depois de passar um tempo afastado, é
provável que você vá esquecer alguns detalhes. É sempre possível estudar
seu código por um tempo e descobrir como os segmentos deveriam
funcionar, mas escrever bons comentários pode fazer você economizar
tempo ao sintetizar sua abordagem geral em linguagem natural clara.
Se quiser se tornar um programador profissional ou colaborar com outros
programadores, escreva comentários significativos. Atualmente, a maior
parte dos softwares é escrita de modo colaborativo, seja por um grupo de
funcionários em uma empresa, seja por um grupo de pessoas que
trabalham juntas em um projeto de código aberto. Programadores
habilidosos esperam ver comentários no código, portanto é melhor
começar a adicionar comentários descritivos em seus programas agora.
Escrever comentários claros e concisos em seu código é um dos hábitos
mais benéficos que você pode desenvolver como um novo programador.
Quando estiver decidindo se deve escrever um comentário, pergunte a si
mesmo se você precisou considerar várias abordagens antes de definir uma
maneira razoável de fazer algo funcionar; em caso afirmativo, escreva um
comentário sobre sua solução. É muito mais fácil apagar comentários
extras depois que retornar e escrever comentários em um programa pouco
comentado. A partir de agora, usarei comentários em exemplos deste livro
para ajudar a explicar algumas seções de código.
FAÇA VOCÊ MESMO
2.10 – Acrescentando comentários: Escolha dois dos programas que você
escreveu e acrescente pelo menos um comentário em cada um. Se você não tiver
nada específico para escrever porque o programa é muito simples no momento,
basta adicionar seu nome e a data de hoje no início de cada arquivo de
programa. Em seguida, escreva uma frase que descreva o que o programa faz.
Zen de Python
Durante muito tempo, a linguagem de programação Perl foi o principal
sustentáculo da internet. A maioria dos primeiros sites interativos usava
scripts Perl. O lema da comunidade Perl na época era: “Há mais de uma
maneira de fazer algo”. As pessoas gostaram dessa postura por um tempo
porque a flexibilidade inscrita na linguagem possibilitava resolver a maior
parte dos problemas de várias maneiras. Essa abordagem era aceitável
enquanto trabalhávamos em nossos próprios projetos, mas, em algum
momento, as pessoas perceberam que a ênfase na flexibilidade dificultava a
manutenção de projetos grandes em longo prazo. Revisar código e tentar
descobrir o que outra pessoa pensou quando resolvia um problema
complexo era difícil, tedioso e consumia bastante tempo.
Programadores Python experientes incentivarão você a evitar a
complexidade e buscar a simplicidade sempre que for possível. A filosofia
da comunidade Python está contida no “Zen de Python” de Tim Peters.
Você pode acessar esse conjunto resumido de princípios para escrever um
bom código Python fornecendo import this ao seu interpretador. Não
reproduzirei todo o “Zen de Python” aqui, mas compartilharei algumas
linhas para ajudar a entender por que elas devem ser importantes para você
como um programador Python iniciante.
>>> import this
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
(Bonito é melhor que feio) Os programadores Python adotam a noção de
que o código pode ser bonito e elegante. Em programação, as pessoas
resolvem problemas. Os programadores sempre respeitaram soluções bem
projetadas, eficientes e até mesmo bonitas para os problemas. À medida
que conhecer mais a linguagem Python e usá-la para escrever mais códigos,
uma pessoa poderá espiar por sobre seu ombro um dia e dizer: “Uau, que
código bonito!”.
Simple is better than complex.
(Simples é melhor que complexo) Se você puder escolher entre uma
solução simples e outra complexa, e as duas funcionarem, utilize a solução
simples. Seu código será mais fácil de manter, e será mais simples para você
e para outras pessoas desenvolverem com base nesse código
posteriormente.
Complex is better than complicated.
(Complexo é melhor que complicado) A vida real é confusa e, às vezes,
uma solução simples para um problema não é viável. Nesse caso, utilize a
solução mais simples possível que funcione.
Readability counts.
(Legibilidade conta) Mesmo quando seu código for complexo, procure
deixá-lo legível. Quando trabalhar com um projeto que envolva códigos
complexos, procure escrever comentários informativos para esse código.
There should be one-- and preferably only one --obvious way to do it.
(Deve haver uma – e, de preferência, apenas uma – maneira óbvia de
fazer algo) Se for solicitado a dois programadores Python que resolvam o
mesmo problema, eles deverão apresentar soluções razoavelmente
compatíveis. Isso não quer dizer que não haja espaço para a criatividade
em programação. Pelo contrário! No entanto, boa parte da programação
consiste em usar abordagens pequenas e comuns para situações simples em
um projeto maior e mais criativo. Os detalhes de funcionamento de seus
programas devem fazer sentido para outros programadores Python.
Now is better than never.
(Agora é melhor que nunca) Você poderia passar o resto de sua vida
conhecendo todas as complexidades de Python e da programação em geral,
mas, nesse caso, jamais concluiria qualquer projeto. Não tente escrever um
código perfeito; escreva um código que funcione e, então, decida se deve
aperfeiçoá-lo nesse projeto ou passar para algo novo.
Ao prosseguir para o próximo capítulo e começar a explorar tópicos mais
sofisticados, procure ter em mente essa filosofia de simplicidade e clareza.
Programadores experientes respeitarão mais o seu código e ficarão felizes
em oferecer feedback e colaborar com você em projetos interessantes.
FAÇA VOCÊ MESMO
2.11 – Zen de Python: Digite import this em uma sessão de terminal de Python e
dê uma olhada nos princípios adicionais.
Resumo
Neste capítulo aprendemos a trabalhar com variáveis. Aprendemos a usar
nomes descritivos para as variáveis e a resolver erros de nomes e de sintaxe
quando surgirem. Vimos o que são strings e como exibi-las usando letras
minúsculas, letras maiúsculas e iniciais maiúsculas. No início, utilizamos
espaços em branco para organizar a saída e aprendemos a remover
caracteres em branco desnecessários de diferentes partes de uma string.
Começamos a trabalhar com inteiros e números de ponto flutuante, e
lemos a respeito de alguns comportamentos inesperados com os quais
devemos tomar cuidado quando trabalharmos com dados numéricos.
Também aprendemos a escrever comentários explicativos para que você e
outras pessoas leiam seu código com mais facilidade. Por fim, lemos a
respeito da filosofia de manter seu código o mais simples possível, sempre
que puder.
No Capítulo 3 aprenderemos a armazenar coleções de informações em
variáveis chamadas listas. Veremos como percorrer uma lista, manipulando
qualquer informação que ela tiver. 
Neste capítulo e no próximo, veremos o que são listas e
como começar a trabalhar com os elementos de uma lista.
As listas permitem armazenar conjuntos de informações
em um só lugar, independentemente de termos alguns
itens ou milhões deles. As listas são um dos recursos mais
eficazes de Python, prontamente acessíveis aos novos
programadores, e elas agregam muitos conceitos
importantes em programação.
O queé umalista?
Uma lista é uma coleção de itens em uma ordem em particular. Podemos
criar uma lista que inclua as letras do alfabeto, os dígitos de 0 a 9 ou os
nomes de todas as pessoas de sua família. Você pode colocar qualquer
informação que quiser em uma lista, e os itens de sua lista não precisam
estar relacionados de nenhum modo em particular. Como uma lista
geralmente contém mais de um elemento, é uma boa ideia deixar seu nome
no plural, por exemplo, letters, digits ou names.
Em Python, colchetes ([]) indicam uma lista, e elementos individuais da
lista são separados por vírgulas. Eis um exemplo simples de uma lista que
contém alguns tipos de bicicleta:
bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
Se você pedir a Python que exiba uma lista, ela devolverá a representação
da lista, incluindo os colchetes:
['trek', 'cannondale', 'redline', 'specialized']
Como essa não é a saída que você quer que seus usuários vejam, vamos
aprender a acessar os elementos individuais de uma lista.
Acessando elementos de umalista
Listas são coleções ordenadas, portanto você pode acessar qualquer
elemento de uma lista informando a posição – ou índice – do item desejado
ao interpretador Python. Para acessar um elemento de uma lista, escreva o
nome da lista seguido do índice do item entre colchetes.
Por exemplo, vamos extrair a primeira bicicleta da lista bicycles:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
u print(bicycles[0])
A sintaxe para isso está em u. Quando solicitamos um item simples de
uma lista, Python devolve apenas esse elemento, sem colchetes ou aspas:
trek
Esse é o resultado que você quer que seus usuários vejam – uma saída
limpa, formatada de modo elegante.
Também podemos usar os métodos de string do Capítulo 2 em qualquer
elemento de uma lista. Por exemplo, podemos formatar o elemento 'trek'
de modo mais bonito usando o método title():
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
Esse exemplo gera a mesma saída do exemplo anterior, exceto pelo fato
de 'Trek' começar com uma letra maiúscula.
A posição dos índices começaem0,e não em1
Python considera que o primeiro item de uma lista está na posição 0, e não
na posição 1. Isso é válido para a maioria das linguagens de programação, e
o motivo tem a ver com o modo como as operações em lista são
implementadas em um nível mais baixo. Se estiver recebendo resultados
inesperados, verifique se você não está cometendo um erro simples de
deslocamento de um.
O segundo item de uma lista tem índice igual a 1. Usando esse sistema
simples de contagem, podemos obter qualquer elemento que quisermos de
uma lista subtraindo um de sua posição na lista. Por exemplo, para acessar
o quarto item de uma lista, solicite o item no índice 3.
As instruções a seguir acessam as bicicletas nos índices 1 e 3:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
Esse código devolve a segunda e a quarta bicicletas da lista:
cannondale
specialized
Python tem uma sintaxe especial para acessar o último elemento de uma
lista. Ao solicitar o item no índice -1, Python sempre devolve o último item
da lista:
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])
Esse código devolve o valor 'specialized'. Essa sintaxe é bem útil, pois,
com frequência, você vai querer acessar os últimos itens de uma lista sem
saber exatamente o tamanho dela. Essa convenção também se estende a
outros valores negativos de índice. O índice -2 devolve o segundo item a
partir do final da lista, o índice -3 devolve o terceiro item a partir do final, e
assim sucessivamente.
Usando valores individuais de umalista
Você pode usar valores individuais de uma lista, exatamente como faria
com qualquer outra variável. Por exemplo, podemos usar concatenação
para criar uma mensagem com base em um valor de uma lista.
Vamos tentar obter a primeira bicicleta da lista e compor uma mensagem
usando esse valor.
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
u message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
Em u, compomos uma frase usando o valor em bicycles[0] e a
armazenamos na variável message. A saída é uma frase simples sobre a
primeira bicicleta da lista:
My first bicycle was a Trek.
FAÇA VOCÊ MESMO
Experimente criar estes programas pequenos para ter um pouco de experiência
própria com listas em Python. Você pode criar uma nova pasta para os exercícios
de cada capítulo a fim de mantê-los organizados.
3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista
chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista,
um de cada vez.
3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de
simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas. O
texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar
personalizada com o nome da pessoa.
3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como
motocicleta ou carro, e crie uma lista que armazene vários exemplos. Utilize sua
lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma
moto Honda”.
Alterando,acrescentando eremovendo elementos
A maioria das listas que você criar será dinâmica, o que significa que você
criará uma lista e então adicionará e removerá elementos dela à medida que
seu programa executar. Por exemplo, você poderia criar um jogo em que
um jogador atire em alienígenas que caem do céu. Poderia armazenar o
conjunto inicial de alienígenas em uma lista e então remover um item da
lista sempre que um alienígena for atingido. Sempre que um novo
alienígena aparecer na tela, adicione-o à lista. Sua lista de alienígenas
diminuirá e aumentará de tamanho no decorrer do jogo.
Modificando elementos de umalista
A sintaxe para modificar um elemento é semelhante à sintaxe para acessar
um elemento de uma lista. Para alterar um elemento, use o nome da lista
seguido do índice do elemento que você quer modificar e, então, forneça o
novo valor que você quer que esse item tenha.
Por exemplo, vamos supor que temos uma lista de motocicletas, e que o
primeiro item da lista seja 'honda'. Como mudaríamos o valor desse
primeiro item?
motorcycles.py
u motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
v motorcycles[0] = 'ducati'
print(motorcycles)
O código em u define a lista original, com 'honda' como o primeiro
elemento. O código em v altera o valor do primeiro item para 'ducati'. A
saída mostra que o primeiro item realmente foi modificado e o restante da
lista permaneceu igual:
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
Você pode mudar o valor de qualquer item de uma lista, e não apenas o
primeiro.
Acrescentando elementosemumalista
Você pode acrescentar um novo elemento em uma lista por diversos
motivos. Por exemplo, talvez você queira que novos alienígenas apareçam
no jogo, pode querer acrescentar novos dados em uma visualização ou
adicionar novos usuários registrados em um site que você criou. Python
oferece várias maneiras de acrescentar novos dados em listas existentes.
Concatenando elementos no final de umalista
A maneira mais simples de acrescentar um novo elemento em uma lista é
concatenar o item na lista. Quando concatenamos um item em uma lista, o
novo elemento é acrescentado no final. Usando a mesma lista que
tínhamos no exemplo anterior, adicionaremos o novo elemento 'ducati'
no final da lista:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
u motorcycles.append('ducati')
print(motorcycles)
O método append() em u acrescenta 'ducati' no final da lista sem afetar
qualquer outro elemento:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
O método append() facilita criar listas dinamicamente. Por exemplo,
podemos começar com uma lista vazia e então acrescentar itens à lista
usando uma série de instruções append(). Usando uma lista vazia, vamos
adicionar os elementos 'honda', 'yamaha' e 'suzuki' à lista:
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
A lista resultante tem exatamente o mesmo aspecto da lista dos exemplos
anteriores:
['honda', 'yamaha', 'suzuki']
Criar listas dessa maneira é bem comum, pois, com frequência, você não
conhecerá os dados que seus usuários querem armazenar em um programa
até que ele esteja executando. Para deixar que seus usuários tenham o
controle, comece definindo uma lista vazia que armazenará os valores dos
usuários. Em seguida, concatene cada novo valor fornecido à lista que você
acabou de criar.
Inserindo elementosemumalista
Você pode adicionar um novo elemento em qualquer posição de sua lista
usando o método insert(). Faça isso especificando o índice do novo
elemento e o valor do novo item.
motorcycles = ['honda', 'yamaha', 'suzuki']
u motorcycles.insert(0, 'ducati')
print(motorcycles)
Nesse exemplo, o código em u insere o valor 'ducati' no início da lista. O
método insert() abre um espaço na posição 0 e armazena o valor 'ducati'
nesse local. Essa operação desloca todos os demais valores da lista uma
posição à direita:
['ducati', 'honda', 'yamaha', 'suzuki']
Removendo elementos de umalista
Com frequência, você vai querer remover um item ou um conjunto de itens
de uma lista. Por exemplo, quando um jogador atinge um alienígena no
céu com um tiro, é bem provável que você vá querer removê-lo da lista de
alienígenas ativos. Se um usuário decidir cancelar a conta em sua aplicação
web, você vai querer remover esse usuário da lista de usuários ativos. Você
pode remover um item de acordo com sua posição na lista ou seu valor.
Removendo umitemusando ainstrução del
Se a posição do item que você quer remover de uma lista for conhecida, a
instrução del poderá ser usada.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
u del motorcycles[0]
print(motorcycles)
O código em u usa del para remover o primeiro item, 'honda', da lista de
motocicletas:
['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']
Você pode remover um item de qualquer posição em uma lista usando a
instrução del, se souber qual é o seu índice. Por exemplo, eis o modo de
remover o segundo item, 'yamaha', da lista:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[1]
print(motorcycles)
A segunda motocicleta é apagada da lista:
['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']
Nos dois exemplos não podemos mais acessar o valor que foi removido
da lista após a instrução del ter sido usada.
Removendo umitemcomométodo pop()
Às vezes, você vai querer usar o valor de um item depois de removê-lo de
uma lista. Por exemplo, talvez você queira obter as posições x e y de um
alienígena que acabou de ser atingido para que possa desenhar uma
explosão nessa posição. Em uma aplicação web, você poderia remover um
usuário de uma lista de membros ativos e então adicioná-lo a uma lista de
membros inativos.
O método pop() remove o último item de uma lista, mas permite que
você trabalhe com esse item depois da remoção. O termo pop deriva de
pensar em uma lista como se fosse uma pilha de itens e remover um item
(fazer um pop) do topo da pilha. Nessa analogia, o topo da pilha
corresponde ao final da lista.
Vamos fazer um pop de uma motocicleta da lista de motocicletas:
u motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
v popped_motorcycle = motorcycles.pop()
w print(motorcycles)
x print(popped_motorcycle)
Começamos definindo e exibindo a lista motorcycles em u. Em v fazemos
pop de um valor da lista e o armazenamos na variável popped_motorcycle.
Exibimos a lista em w para mostrar que um valor foi removido da lista.
Então exibimos o valor removido em x para provar que ainda temos acesso
ao valor removido.
A saída mostra que o valor 'suzuki' foi removido do final da lista e agora
está armazenado na variável popped_motorcycle:
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki
Como esse método pop() poderia ser útil? Suponha que as motocicletas
da lista estejam armazenadas em ordem cronológica, de acordo com a
época em que fomos seus proprietários. Se for esse o caso, podemos usar o
método pop() para exibir uma afirmação sobre a última motocicleta que
compramos:
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")
A saída é uma frase simples sobre a motocicleta mais recente que
tivemos:
The last motorcycle I owned was a Suzuki.
Removendo itens de qualquer posição emumalista
Na verdade, você pode usar pop() para remover um item de qualquer
posição em uma lista se incluir o índice do item que você deseja remover
entre parênteses.
motorcycles = ['honda', 'yamaha', 'suzuki']
u first_owned = motorcycles.pop(0)
v print('The first motorcycle I owned was a ' + first_owned.title() +
'.')
Começamos fazendo pop da primeira motocicleta da lista em u e, então,
exibimos uma mensagem sobre essa motocicleta em v. A saída é uma frase
simples que descreve a primeira motocicleta que eu tive:
The first motorcycle I owned was a Honda.
Lembre-se de que, sempre que usar pop(), o item com o qual você
trabalhar não estará mais armazenado na lista.
Se você não tiver certeza se deve usar a instrução del ou o método pop(),
eis um modo fácil de decidir: quando quiser apagar um item de uma lista e
esse item não vai ser usado de modo algum, utilize a instrução del; se
quiser usar um item à medida que removê-lo, utilize o método pop().
Removendo umitemdeacordo como valor
Às vezes, você são saberá a posição do valor que quer remover de uma
lista. Se conhecer apenas o valor do item que deseja remover, o método
remove() poderá ser usado.
Por exemplo, vamos supor que queremos remover o valor 'ducati' da
lista de motocicletas.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
u motorcycles.remove('ducati')
print(motorcycles)
O código em u diz a Python para descobrir em que lugar 'ducati' aparece
na lista e remover esse elemento:
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
Também podemos usar o método remove() para trabalhar com um valor
que está sendo removido de uma lista. Vamos remover o valor 'ducati' e
exibir um motivo para removê-lo da lista:
u motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
v too_expensive = 'ducati'
w motorcycles.remove(too_expensive)
print(motorcycles)
x print("nA " + too_expensive.title() + " is too expensive for me.")
Após definir a lista em u, armazenamos o valor 'ducati' em uma variável
chamada too_expensive v. Então utilizamos essa variável para dizer a
Python qual valor deve ser removido da lista em w. Em x, o valor 'ducati'
foi removido da lista, mas continua armazenado na variável too_expensive,
permitindo exibir uma frase sobre o motivo pelo qual removemos 'ducati'
da lista de motocicletas:
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
A Ducati is too expensive for me.
NOTA O método remove() apaga apenas a primeira ocorrência do valor que você
especificar. Se houver a possibilidade de o valor aparecer mais de uma vez na
lista, será necessário usar um laço para determinar se todas as ocorrências desse
valor foram removidas. Aprenderemos a fazer isso no Capítulo 7.
FAÇA VOCÊ MESMO
Os exercícios a seguir são um pouco mais complexos que aqueles do Capítulo 2,
porém darão a você a oportunidade de usar listas de todas as formas descritas.
3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o
jantar, quem você convidaria? Crie uma lista que inclua pelo menos três pessoas
que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir
uma mensagem para cada pessoa, convidando-a para jantar.
3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus
convidados não poderá comparecer ao jantar, portanto será necessário enviar um
novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá
comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá
comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada
pessoa que continua presente em sua lista.
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,
portanto agora tem mais espaço disponível. Pense em mais três convidados para o
jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente
uma instrução print no final de seu programa informando às pessoas que você
encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que
está em sua lista.
3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova
mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
dois convidados.
• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
mostre uma mensagem informando que você pode convidar apenas duas pessoas
para o jantar.
• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que
apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de
sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que
você sente muito por não poder convidá-la para o jantar.
• Apresente uma mensagem para cada uma das duas pessoas que continuam na
lista, permitindo que elas saibam que ainda estão convidadas.
• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma
lista vazia no final de seu programa.
Organizando umalista
Com frequência, suas listas serão criadas em uma ordem imprevisível, pois
nem sempre você poderá controlar a ordem em que seus usuários fornecem
seus dados. Embora isso seja inevitável na maioria das circunstâncias, com
frequência você vai querer apresentar suas informações em uma ordem em
particular. Às vezes, você vai querer preservar a ordem original de sua lista,
enquanto, em outras ocasiões, vai querer alterar essa ordem. Python
oferece várias maneiras de organizar suas listas de acordo com a situação.
Ordenando umalista deforma permanentecomométodo sort()
O método sort() de Python faz com que seja relativamente fácil ordenar
uma lista. Suponha que temos uma lista de carros e queremos alterar a
ordem da lista para armazenar os itens em ordem alfabética. Para
simplificar essa tarefa, vamos supor que todos os valores da lista usam
letras minúsculas.
cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
u cars.sort()
print(cars)
O método sort() mostrado em u altera a ordem da lista de forma
permanente. Os carros agora estão em ordem alfabética e não podemos
mais retornar à ordem original.
['audi', 'bmw', 'subaru', 'toyota']
Também podemos ordenar essa lista em ordem alfabética inversa,
passando o argumento reverse=True ao método sort(). O exemplo a seguir
ordena a lista de carros em ordem alfabética inversa:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
Novamente, a ordem da lista foi permanentemente alterada:
['toyota', 'subaru', 'bmw', 'audi']
Ordenando umalistatemporariamentecomafunção sorted()
Para preservar a ordem original de uma lista, mas apresentá-la de forma
ordenada, podemos usar a função sorted(). A função sorted() permite
exibir sua lista em uma ordem em particular, mas não afeta a ordem
propriamente dita da lista.
Vamos testar essa função na lista de carros.
cars = ['bmw', 'audi', 'toyota', 'subaru']
u print("Here is the original list:")
print(cars)
v print("nHere is the sorted list:")
print(sorted(cars))
w print("nHere is the original list again:")
print(cars)
Inicialmente, exibimos a lista em sua ordem original em u e depois, em
ordem alfabética em v. Depois que a lista é exibida na nova ordem,
mostramos que a lista continua armazenada em sua ordem original em w.
Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']
Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']
x Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']
Observe que a lista preserva sua ordem original em x, depois que a
função sorted() foi usada. Essa função também pode aceitar um argumento
reverse=True se você quiser exibir uma lista em ordem alfabética inversa.
NOTA Ordenar uma lista em ordem alfabética é um pouco mais complicado quando
todos os valores não utilizam letras minúsculas. Há várias maneiras de
interpretar letras maiúsculas quando decidimos por uma sequência de
ordenação, e especificar a ordem exata pode apresentar um nível de
complexidade maior que aquele com que queremos lidar no momento. No
entanto, a maior parte das abordagens à ordenação terá diretamente como base
o que aprendemos nesta seção.
Exibindo umalistaemordeminversa
Para inverter a ordem original de uma lista, podemos usar o método
reverse(). Se armazenarmos originalmente a lista de carros em ordem
cronológica, de acordo com a época em que fomos seus proprietários,
poderemos facilmente reorganizar a lista em ordem cronológica inversa:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
Observe que reverse() não reorganiza em ordem alfabética inversa; ele
simplesmente inverte a ordem da lista:
['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']
O método reverse() muda a ordem de uma lista de forma permanente,
mas podemos restaurar a ordem original a qualquer momento aplicando
reverse() à mesma lista uma segunda vez.
Descobrindo o tamanho de umalista
Podemos rapidamente descobrir o tamanho de uma lista usando a função
len(). A lista no exemplo a seguir tem quatro itens, portanto seu tamanho
é 4:
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
Você achará len() útil quando precisar identificar o número de
alienígenas que ainda precisam ser atingidos em um jogo, determinar a
quantidade de dados que você precisa administrar em uma visualização ou
descobrir o número de usuários registrados em um site, entre outras
tarefas.
NOTA Python conta os itens de uma lista começando em um, portanto você não
deverá se deparar com nenhum erro de deslocamento de um ao determinar o
tamanho de uma lista.
FAÇA VOCÊ MESMO
3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
você gostaria de visitar.
• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em
ordem alfabética.
• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
elegante; basta exibi-la como uma lista Python pura.
• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.
• Mostre que sua lista manteve sua ordem original exibindo-a.
• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.
• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou.
• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para
mostrar que ela voltou à sua ordem original.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
• Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
3.9 – Convidados para o jantar: Trabalhando com um dos programas dos
Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
informando o número de pessoas que você está convidando para o jantar.
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
uma lista contendo esses itens e então utilize cada função apresentada neste
capítulo pelo menos uma vez.
Evitando erros deíndice quando trabalhar comlistas
Um tipo de erro é comum quando trabalhamos com listas pela primeira
vez. Suponha que temos uma lista com três itens e você solicite o quarto
item:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])
Esse exemplo resulta em um erro de índice:
Traceback (most recent call last):
File "motorcycles.py", line 3, in <module>
print(motorcycles[3])
IndexError: list index out of range
Python tenta fornecer o item no índice 3. Porém, quando pesquisa a lista,
nenhum item de motorcycles tem índice igual a 3. Por causa da natureza
deslocada de um na indexação de listas, esse erro é característico. As
pessoas acham que o terceiro item é o item de número 3, pois começam a
contar a partir de 1. Contudo, em Python, o terceiro item é o de número 2,
pois a indexação começa em 0.
Um erro de índice quer dizer que Python não é capaz de determinar o
índice solicitado. Se um erro de índice ocorrer em seu programa, tente
ajustar o índice que você está solicitando em um. Então execute o
programa novamente para ver se os resultados estão corretos.
Tenha em mente que, sempre que quiser acessar o último item de uma
lista, você deve usar o índice -1. Isso sempre funcionará, mesmo que sua
lista tenha mudado de tamanho desde a última vez que você a acessou:
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
O índice -1 sempre devolve o último item de uma lista – nesse caso, é o
valor 'suzuki':
'suzuki'
A única ocasião em que essa abordagem causará um erro é quando
solicitamos o último item de uma lista vazia:
motorcycles = []
print(motorcycles[-1])
Não há nenhum item em motorcycles, portanto Python devolve outro erro
de índice:
Traceback (most recent call last):
File "motorcyles.py", line 3, in <module>
print(motorcycles[-1])
IndexError: list index out of range
NOTA Se um erro de índice ocorrer e você não consegue descobrir como resolvê-lo,
experimente exibir sua lista ou simplesmente mostrar o tamanho dela. Sua lista
poderá estar bem diferente do que você imaginou, em especial se ela foi tratada
dinamicamente pelo seu programa. Ver a lista propriamente dita ou o número
exato de itens que ela contém pode ajudar a entender esses erros de lógica.
FAÇA VOCÊ MESMO
3.11 – Erro proposital: Se você ainda não recebeu um erro de índice em um de
seus programas, tente fazer um erro desse tipo acontecer. Altere um índice em um
de seus programas de modo a gerar um erro de índice. Não se esqueça de corrigir
o erro antes de fechar o programa.
Resumo
Neste capítulo conhecemos as listas e vimos como trabalhar com os itens
individuais de uma lista. Aprendemos a definir uma lista e a adicionar e
remover elementos. Vimos como ordenar as listas de modo permanente e
temporário para fins de exibição. Também vimos como descobrir o
tamanho de uma lista e aprendemos a evitar erros de índice quando
trabalhamos com listas.
No Capítulo 4 veremos como trabalhar com itens de uma lista de
maneira mais eficiente. Ao percorrer todos os itens em um laço usando
apenas algumas linhas de código, poderemos trabalhar de modo eficiente,
mesmo quando a lista contiver milhares ou milhões de itens.
No Capítulo 3 aprendemos a criar uma lista simples e a
trabalhar com os elementos individuais de uma lista.
Neste capítulo veremos como percorrer uma lista inteira
com um laço usando apenas algumas linhas de código,
independentemente do tamanho da lista. Percorrer listas
com laços permite executar a mesma ação – ou conjunto
de ações – em todos os itens de uma lista. Como
resultado, você poderá trabalhar de modo eficiente com
listas de qualquer tamanho, incluindo aquelas com
milhares ou até mesmo milhões de itens.
Percorrendo umalistainteiracomumlaço
Com frequência, você vai querer percorrer todas as entradas de uma lista,
executando a mesma tarefa em cada item. Por exemplo, em um jogo, você
pode mover todos os elementos da tela de acordo com a mesma distância;
em uma lista de números, talvez você queira executar a mesma operação
estatística em todos os elementos. Quem sabe você queira exibir cada um
dos títulos de uma lista de artigos em um site. Quando quiser executar a
mesma ação em todos os itens de uma lista, você pode usar o laço for de
Python.
Vamos supor que temos uma lista de nomes de mágicos e queremos
exibir todos os nomes da lista. Poderíamos fazer isso recuperando cada
nome da lista individualmente, mas essa abordagem poderia causar vários
problemas. Para começar, seria repetitivo fazer isso com uma lista longa de
nomes. Além disso, teríamos que alterar o nosso código sempre que o
tamanho da lista mudasse. Um laço for evita esses dois problemas ao
permitir que Python administre essas questões internamente.
Vamos usar um laço for para exibir cada um dos nomes de uma lista de
mágicos:
magicians.py
u magicians = ['alice', 'david', 'carolina']
v for magician in magicians:
w print(magician)
Começamos definindo uma lista em u, exatamente como fizemos no
Capítulo 3. Em v definimos um laço for. Essa linha diz a Python para
extrair um nome da lista magicians e armazená-lo na variável magician. Em
w dizemos a Python para exibir o nome que acabou de ser armazenado em
magician. O interpretador então repete as linhas v e w, uma vez para cada
nome da lista. Ler esse código como “para todo mágico na lista de
mágicos, exiba o nome do mágico” pode ajudar. A saída é uma exibição
simples de cada nome da lista:
alice
david
carolina
Observando os laços commais detalhes
O conceito de laços é importante porque é uma das maneiras mais comuns
para um computador automatizar tarefas repetitivas. Por exemplo, em um
laço simples como o que usamos em magicians.py, Python inicialmente lê a
primeira linha do laço:
for magician in magicians:
Essa linha diz a Python para extrair o primeiro valor da lista magicians e
armazená-lo na variável magician. O primeiro valor é 'alice'. O
interpretador então lê a próxima linha:
print(magician)
Python exibe o valor atual de magician, que ainda é 'alice'. Como a lista
contém mais valores, o interpretador retorna à primeira linha do laço:
for magician in magicians:
Python recupera o próximo nome da lista, que é 'david', e armazena esse
valor em magician. Então ele executa a linha:
print(magician)
Python exibe o valor atual de magician, que agora é 'david', novamente.
O interpretador repete todo o laço mais uma vez com o último valor da
lista, que é 'carolina'. Como não há mais valores na lista, Python passa
para a próxima linha do programa. Nesse caso, não há mais nada depois
do laço for, portanto o programa simplesmente termina.
Quando usar laços pela primeira vez, tenha em mente que o conjunto de
passos será repetido, uma vez para cada item da lista, não importa quantos
itens haja na lista. Se você tiver um milhão de itens em sua lista, Python
repetirá esses passos um milhão de vezes – e geralmente o fará bem rápido.
Tenha em mente também que quando escrever seus próprios laços for,
você poderá escolher qualquer nome que quiser para a variável temporária
que armazena cada valor da lista. No entanto, é conveniente escolher um
nome significativo, que represente um único item da lista. Por exemplo, eis
uma boa maneira de iniciar um laço for para uma lista de gatos, uma lista
de cachorros e uma lista genérica de itens:
for cat in cats:
for dog in dogs:
for item in list_of_items:
Essas convenções de nomenclatura podem ajudar você a acompanhar a
ação executada em cada item em um laço for. O uso de nomes no singular
e no plural pode ajudar a identificar se a seção de código atua em um único
elemento da lista ou em toda a lista.
Executandomais tarefasemumlaço for
Você pode fazer praticamente de tudo com cada item em um laço for.
Vamos expandir o exemplo anterior exibindo uma mensagem a cada
mágico, informando-lhes que realizaram um ótimo truque:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
u print(magician.title() + ", that was a great trick!")
A única diferença nesse código está em u, em que compomos uma
mensagem para cada mágico, começando com o nome desse mágico. Na
primeira vez em que passamos pelo laço, o valor do mágico é 'alice',
portanto Python inicia a primeira mensagem com o nome 'Alice'. Na
segunda vez que compormos a mensagem, ela começará com 'David' e na
terceira vez, a mensagem começará com 'Carolina'.
A saída mostra uma mensagem personalizada para cada mágico da lista:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
Também podemos escrever tantas linhas de código quantas quisermos no
laço for. Considera-se que toda linha indentada após a linha for magician
in magicians está dentro do laço, e cada linha indentada é executada uma
vez para cada valor da lista. Assim, você pode executar o volume de
trabalho que quiser com cada valor da lista.
Vamos acrescentar uma segunda linha em nossa mensagem, informando
a cada mágico que estamos ansiosos para ver o seu próximo truque:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a great trick!")
u print("I can't wait to see your next trick, " + magician.title() +
".n")
Como indentamos as duas instruções print, cada linha será executada
uma vez para cada mágico da lista. A quebra de linha ("n") na segunda
instrução print u insere uma linha em branco após cada passagem pelo
laço. Com isso, criamos um conjunto de mensagens agrupadas de forma
organizada para cada pessoa na lista:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
Podemos usar quantas linhas quisermos em nossos laços for. Na prática,
muitas vezes você achará útil efetuar várias operações com cada item de
uma lista quando usar um laço for.
Fazendo algo após umlaço for
O que acontece quando um laço for acaba de executar? Geralmente você
vai querer fazer uma síntese de um bloco de saída ou passar para outra
atividade que seu programa deva executar.
Qualquer linha de código após o laço for que não estiver indentada será
executada uma vez, sem repetição. Vamos escrever um agradecimento ao
grupo de mágicos como um todo, agradecendo-lhes por apresentar um
show excelente. Para exibir essa mensagem ao grupo após todas as
mensagens individuais terem sido apresentadas, colocamos a mensagem de
agradecimento depois do laço for, sem indentação:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() +
".n")
u print("Thank you, everyone. That was a great magic show!")
As duas primeiras instruções print são repetidas uma vez para cada
mágico da lista, como vimos antes. No entanto, como a linha em u não
está indentada, ela será exibida apenas uma vez:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
David, that was a great trick!
I can't wait to see your next trick, David.
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
Thank you, everyone. That was a great magic show!
Quando processar dados com um laço for, você verá que essa é uma boa
maneira de sintetizar uma operação realizada em todo um conjunto de
dados. Por exemplo, um laço for pode ser usado para inicializar um jogo
percorrendo uma lista de personagens e exibindo cada um deles na tela.
Você pode então escrever um bloco não indentado após esse laço, que
exiba um botão Play Now (Jogue agora) depois que todos os personagens
tiverem sido desenhados na tela.
Evitando erros deindentação
Python usa indentação para determinar se uma linha de código está
conectada à linha antes dela. Nos exemplos anteriores, as linhas que
exibiam mensagens aos mágicos individuais faziam parte do laço for
porque estavam indentadas. O uso de indentação por Python deixa o
código bem fácil de ler. Basicamente, Python usa espaços em branco para
forçar você a escrever um código formatado de modo organizado, com
uma estrutura visual clara. Em programas Python mais longos, você
perceberá que há blocos de código indentados em alguns níveis diferentes.
Esses níveis de indentação ajudam a ter uma noção geral da organização do
programa como um todo.
Quando começar a escrever código que dependa de uma indentação
apropriada, você deverá tomar cuidado com alguns erros comuns de
indentação. Por exemplo, às vezes, as pessoas indentam blocos de código
que não precisam estar indentados ou se esquecem de indentar blocos que
deveriam estar indentados. Ver exemplos desses erros agora ajudará a
evitá-los no futuro e a corrigi-los quando aparecerem em seus próprios
programas.
Vamos analisar alguns dos erros mais comuns de indentação.
Esquecendo-se deindentar
Sempre indente a linha após a instrução for em um laço. Se você se
esquecer, Python o avisará:
magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
u print(magician)
A instrução print em u deveria estar indentada, mas não está. Quando
Python espera um bloco indentado e não encontra um, ele mostra a linha
em que o problema ocorreu.
File "magicians.py", line 3
print(magician)
^
IndentationError: expected an indented block
Geralmente podemos resolver esse tipo de erro indentando a linha ou as
linhas logo depois da instrução for.
Esquecendo-se deindentar linhasadicionais
Às vezes, seu laço executará sem erros, mas não produzirá o resultado
esperado. Isso pode acontecer quando você tenta realizar várias tarefas em
um laço e se esquece de indentar algumas de suas linhas.
Por exemplo, eis o que acontece quando nos esquecemos de indentar a
segunda linha do laço que diz a cada mágico que estamos ansiosos para ver
o seu próximo truque:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a great trick!")
u print("I can't wait to see your next trick, " + magician.title() +
".n")
A instrução print em u deveria estar indentada, mas como Python
encontra pelo menos uma linha indentada após a instrução for, um erro
não é informado. Como resultado, a primeira instrução print é executada
uma vez para cada nome da lista, pois está indentada. A segunda instrução
print não está indentada, portanto é executada somente uma vez, depois
que o laço terminar de executar. Como o valor final de magician é
'carolina', ela é a única que recebe a mensagem de “ansiosos pelo próximo
truque”:
Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
Esse é um erro de lógica. É um código Python com sintaxe válida, mas ele
não gera o resultado desejado, pois há um problema em sua lógica. Se você
espera ver uma determinada ação ser repetida uma vez para cada item de
uma lista, mas ela é executada apenas uma vez, verifique se não é preciso
simplesmente indentar uma linha ou um grupo de linhas.
Indentando desnecessariamente
Se você, acidentalmente, indentar uma linha que não precisa ser indetada,
Python o informará a respeito da indentação inesperada:
hello_world.py
message = "Hello Python world!"
u print(message)
Não precisamos indentar a instrução print em u, pois ela não pertence à
linha antes dela; assim, Python informa esse erro:
File "hello_world.py", line 2
print(message)
^
IndentationError: unexpected indent
Você pode evitar erros inesperados de indentação ao indentar apenas
quando houver um motivo específico para isso. Nos programas que
estamos escrevendo no momento, as únicas linhas que precisam ser
indentadas são as ações que queremos repetir para cada item em um laço
for.
Indentando desnecessariamenteapós o laço
Se você acidentalmente indentar um código que deva executar após um
laço ter sido concluído, esse código será repetido uma vez para cada item
da lista. Às vezes, isso faz Python informar um erro, mas, geralmente, você
terá um erro de lógica simples.
Por exemplo, vamos ver o que acontece quando indentamos por acidente
a linha que agradece aos mágicos como um grupo por apresentarem um
bom show:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() +
".n")
u print("Thank you everyone, that was a great magic show!")
Pelo fato de a linha em u estar indentada, ela é exibida uma vez para cada
pessoa da lista, como podemos ver em v:
Alice, that was a great trick!
I can't wait to see your next trick, Alice.
v Thank you everyone, that was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.
v Thank you everyone, that was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.
v Thank you everyone, that was a great magic show!
Há outro erro de lógica, semelhante àquele da seção “Esquecendo-se de
indentar linhas adicionais”. Como Python não sabe o que você está
querendo fazer com seu código, ele executará todo código que estiver
escrito com uma sintaxe válida. Se uma ação for repetida muitas vezes
quando deveria ser executada apenas uma vez, verifique se você não
precisa simplesmente deixar de indentar o código dessa ação.
Esquecendo os dois-pontos
Os dois-pontos no final de uma instrução for diz a Python para interpretar
a próxima linha como o início de um laço.
magicians = ['alice', 'david', 'carolina']
u for magician in magicians
print(magician)
Se você se esquecer acidentalmente de colocar os dois-pontos, como em
u, você terá um erro de sintaxe, pois Python não sabe o que você está
tentando fazer. Embora esse seja um erro fácil de corrigir, nem sempre é
um erro fácil de identificar. Você ficaria surpreso com a quantidade de
tempo gasto pelos programadores à procura de erros de um único caractere
como esse. Erros desse tipo são difíceis de encontrar, pois, com frequência,
vemos somente aquilo que esperamos ver.
FAÇA VOCÊ MESMO
4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez
de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na
saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas
sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo,
Eu realmente adoro pizza!
4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma
característica em comum. Armazene os nomes desses animais em uma lista e,
então, utilize um laço for para exibir o nome de cada animal.
• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo,
Um cachorro seria um ótimo animal de estimação.
• Acrescente uma linha no final de seu programa informando o que esses animais
têm em comum. Você poderia exibir uma frase como Qualquer um desses
animais seria um ótimo animal de estimação!
Criando listas numéricas
Há muitos motivos para armazenar um conjunto de números. Por
exemplo, você precisará manter um controle das posições de cada
personagem em um jogo, e talvez queira manter um registro das
pontuações mais altas de um jogador também. Em visualizações de dados,
quase sempre você trabalhará com conjuntos de números, como
temperaturas, distâncias, tamanhos de população ou valores de latitudes e
longitudes, entre outros tipos de conjuntos numéricos.
As listas são ideais para armazenar conjuntos de números, e Python
oferece várias ferramentas para ajudar você a trabalhar com listas de
números de forma eficiente. Depois que souber usar efetivamente essas
ferramentas, seu código funcionará bem, mesmo quando suas listas
tiverem milhões de itens.
Usando afunção range()
A função range() de Python facilita gerar uma série de números. Por
exemplo, podemos usar a função range() para exibir uma sequência de
números, assim:
numbers.py
for value in range(1,5):
print(value)
Embora esse código dê a impressão de que deveria exibir os números de 1
a 5, ele não exibe o número 5:
1
2
3
4
Nesse exemplo, range() exibe apenas os números de 1 a 4. Esse é outro
resultado do comportamento deslocado de um que veremos com
frequência nas linguagens de programação. A função range() faz Python
começar a contar no primeiro valor que você lhe fornecer e parar quando
atingir o segundo valor especificado. Como ele para nesse segundo valor, a
saída não conterá o valor final, que seria 5, nesse caso.
Para exibir os números de 1 a 5, você deve usar range(1,6):
for value in range(1,6):
print(value)
Dessa vez, a saída começa em 1 e termina em 5:
1
2
3
4
5
Se sua saída for diferente do esperado ao usar range(), experimente
ajustar seu valor final em 1.
Usando range() paracriar umalista de números
Se quiser criar uma lista de números, você pode converter os resultados de
range() diretamente em uma lista usando a função list(). Quando
colocamos list() em torno de uma chamada à função range(), a saída será
uma lista de números.
No exemplo da seção anterior, simplesmente exibimos uma série de
números. Podemos usar list() para converter esse mesmo conjunto de
números em uma lista:
numbers = list(range(1,6))
print(numbers)
E o resultado será este:
[1, 2, 3, 4, 5]
Também podemos usar a função range() para dizer a Python que ignore
alguns números em um dado intervalo. Por exemplo, eis o modo de listar
os números pares entre 1 e 10:
even_numbers.py
even_numbers = list(range(2,11,2))
print(even_numbers)
Nesse exemplo, a função range() começa com o valor 2 e então soma 2 a
esse valor. O valor 2 é somado repetidamente até o valor final, que é 11, ser
alcançado ou ultrapassado, e o resultado a seguir é gerado:
[2, 4, 6, 8, 10]
Podemos criar praticamente qualquer conjunto de números que
quisermos com a função range(). Por exemplo, considere como criaríamos
uma lista dos dez primeiros quadrados perfeitos (isto é, o quadrado de
cada inteiro de 1 a 10). Em Python, dois asteriscos (**) representam
exponenciais. Eis o modo como podemos colocar os dez primeiros
quadrados perfeitos em uma lista:
squares.py
u squares = []
v for value in range(1,11):
w square = value**2
x squares.append(square)
y print(squares)
Começamos com uma lista vazia chamada squares em u. Em v, dizemos a
Python para percorrer cada valor de 1 a 10 usando a função range(). No
laço, o valor atual é elevado ao quadrado e armazenado na variável square
em w. Em x, cada novo valor de square é concatenado à lista squares. Por
fim, quando o laço acaba de executar, a lista de quadrados é exibida em y:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Para escrever esse código de modo mais conciso, omita a variável
temporária square e concatene cada novo valor diretamente na lista:
squares = []
for value in range(1,11):
u squares.append(value**2)
print(squares)
O código em u faz a mesma tarefa executada pelas linhas w e x em
squares.py. Cada valor do laço é elevado ao quadrado e, então, é
imediatamente concatenado à lista de quadrados.
Você pode usar qualquer uma dessas duas abordagens quando criar listas
mais complexas. Às vezes, usar uma variável temporária deixa o código
mais legível; em outras ocasiões, deixa o código desnecessariamente longo.
Concentre-se primeiro em escrever um código que você entenda
claramente e faça o que você quer que ele faça. Em seguida, procure
abordagens mais eficientes à medida que revisar seu código.
Estatísticas simples comumalista de números
Algumas funções Python são específicas para listas de números. Por
exemplo, podemos encontrar facilmente o valor mínimo, o valor máximo e
a soma de uma lista de números:
>>> digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
NOTA Os exemplos desta seção utilizam listas pequenas de números para que
caibam facilmente na página. Esses exemplos também funcionarão bem se sua
lista contiver um milhão de números ou mais.
List comprehensions
A abordagem descrita antes para gerar a lista squares usou três ou quatro
linhas de código. Uma list comprehension (abrangência de lista) permite
gerar essa mesma lista com apenas uma linha de código. Uma list
comprehension combina o laço for e a criação de novos elementos em uma
linha, e concatena cada novo elemento automaticamente. As list
comprehensions nem sempre são apresentadas aos iniciantes, mas eu as
incluí aqui porque é bem provável que você as veja assim que começar a
analisar códigos de outras pessoas.
O exemplo a seguir cria a mesma lista de quadrados perfeitos que vimos
antes, porém utiliza uma list comprehension:
squares.py
squares = [value**2 for value in range(1,11)]
print(squares)
Para usar essa sintaxe, comece com um nome descritivo para a lista, por
exemplo, squares. Em seguida, insira um colchete de abertura e defina a
expressão para os valores que você quer armazenar na nova lista. Nesse
exemplo, a expressão é value**2, que eleva o valor ao quadrado. Então
escreva um laço for para gerar os números que você quer fornecer à
expressão e insira um colchete de fechamento. O laço for nesse exemplo é
for value in range(1,11), que fornece os valores de 1 a 10 à expressão
value**2. Observe que não usamos dois-pontos no final da instrução for.
O resultado é a mesma lista de valores ao quadrado que vimos antes:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Escrever suas próprias list comprehensions exige um pouco de prática,
mas você verá que vale a pena conhecê-las depois que se sentir à vontade
para criar listas comuns. Quando escrever três ou quatro linhas de código
para gerar listas e isso começar a parecer repetitivo, considere escrever suas
próprias list comprehensions.
FAÇA VOCÊ MESMO
4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os.
4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais, interrompa
pressionando CTRL-C ou feche a janela de saída.)
4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em
seguida, use min() e max() para garantir que sua lista realmente começa em um e
termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
que Python é capaz de somar um milhão de números.
4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os
números.
4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.
4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por
exemplo, o cubo de 2 é escrito como 2**3 em Python. Crie uma lista dos dez
primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for
para exibir o valor de cada cubo.
4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.
Trabalhando comparte de umalista
No Capítulo 3 aprendemos a acessar elementos únicos de uma lista e, neste
capítulo, aprendemos a trabalhar com todos os elementos de uma lista.
Também podemos trabalhar com um grupo específico de itens de uma
lista, que Python chama de fatia.
Fatiando umalista
Para criar uma fatia, especifique o índice do primeiro e do último elemento
com os quais você quer trabalhar. Como ocorre na função range(), Python
para em um item antes do segundo índice que você especificar. Para exibir
os três primeiros elementos de uma lista, solicite os índices de 0 a 3; os
elementos 0, 1 e 2 serão devolvidos.
O exemplo a seguir envolve uma lista de jogadores de um time:
players.py
players = ['charles', 'martina', 'michael', 'florence', 'eli']
u print(players[0:3])
O código em u exibe uma fatia dessa lista, que inclui apenas os três
primeiros jogadores. A saída mantém a estrutura de lista e inclui os três
primeiros jogadores:
['charles', 'martina', 'michael']
Você pode gerar qualquer subconjunto de uma lista. Por exemplo, se
quiser o segundo, o terceiro e o quarto itens de uma lista, comece a fatia no
índice 1 e termine no índice 4:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
Dessa vez, a fatia começa com 'martina' e termina com 'florence':
['martina', 'michael', 'florence']
Se o primeiro índice de uma fatia for omitido, Python começará sua fatia
automaticamente no início da lista:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
Sem um índice de início, Python usa o início da lista:
['charles', 'martina', 'michael', 'florence']
Uma sintaxe semelhante funcionará se você quiser uma fatia que inclua o
final de uma lista. Por exemplo, se quiser todos os itens do terceiro até o
último item, podemos começar com o índice 2 e omitir o segundo índice:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
Python devolve todos os itens, do terceiro item até o final da lista:
['michael', 'florence', 'eli']
Essa sintaxe permite apresentar todos os elementos a partir de qualquer
ponto de sua lista até o final, independentemente do tamanho da lista.
Lembre-se de que um índice negativo devolve um elemento a uma
determinada distância do final de uma lista; assim, podemos exibir
qualquer fatia a partir do final de uma lista. Por exemplo, se quisermos
apresentar os três últimos jogadores da lista, podemos usar a fatia
players[-3:]:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
Esse código exibe os nomes dos três últimos jogadores e continuaria a
funcionar à medida que a lista de jogadores mudar de tamanho.
Percorrendo umafatiacomumlaço
Você pode usar uma fatia em um laço for se quiser percorrer um
subconjunto de elementos de uma lista. No próximo exemplo,
percorreremos os três primeiros jogadores e exibiremos seus nomes como
parte de uma lista simples:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
u for player in players[:3]:
print(player.title())
Em vez de percorrer a lista inteira de jogadores em u, Python percorre
somente os três primeiros nomes:
Here are the first three players on my team:
Charles
Martina
Michael
As fatias são muito úteis em várias situações. Por exemplo, quando criar
um jogo, você poderia adicionar a pontuação final de um jogador em uma
lista sempre que esse jogador acabar de jogar. Seria possível então obter as
três pontuações mais altas de um jogador ordenando a lista em ordem
decrescente e obtendo uma lista que inclua apenas as três primeiras
pontuações. Ao trabalhar com dados, você pode usar fatias para processar
seus dados em porções de tamanho específico. Quando criar uma
aplicação web, fatias poderiam ser usadas para exibir informações em uma
série de páginas, com uma quantidade apropriada de informações em cada
página.
Copiando umalista
Com frequência, você vai querer começar com uma lista existente e criar
uma lista totalmente nova com base na primeira. Vamos explorar o modo
de copiar uma lista e analisar uma situação em que copiar uma lista é útil.
Para copiar uma lista, podemos criar uma fatia que inclua a lista original
inteira omitindo o primeiro e o segundo índices ([:]). Isso diz a Python
para criar uma lista que começa no primeiro item e termina no último,
gerando uma cópia da lista toda.
Por exemplo, suponha que temos uma lista de nossos alimentos
prediletos e queremos criar uma lista separada de comidas que um amigo
gosta. Esse amigo gosta de tudo que está em nossa lista até agora, portanto
podemos criar sua lista copiando a nossa:
foods.py
u my_foods = ['pizza', 'falafel', 'carrot cake']
v friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("nMy friend's favorite foods are:")
print(friend_foods)
Em u criamos uma lista de alimentos de que gostamos e a chamamos de
my_foods. Em v criamos uma nova lista chamada friend_foods. Fizemos uma
cópia de my_foods solicitando uma fatia de my_foods sem especificar
qualquer índice e armazenamos a cópia em friend_foods. Quando exibimos
cada lista, vemos que as duas contêm os mesmos alimentos:
My favorite foods are:
['pizza', 'falafel', 'carrot cake']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
Para provar que realmente temos duas listas separadas, acrescentaremos
um alimento em cada lista e mostraremos que cada lista mantém um
registro apropriado das comidas favoritas de cada pessoa:
my_foods = ['pizza', 'falafel', 'carrot cake']
u friend_foods = my_foods[:]
v my_foods.append('cannoli')
w friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("nMy friend's favorite foods are:")
print(friend_foods)
Em u, copiamos os itens originais em my_foods para a nova lista
friend_foods, como fizemos no exemplo anterior. Em seguida, adicionamos
um novo alimento em cada lista: em v, acrescentamos 'cannoli' a my_foods
e em w, adicionamos 'ice cream' em friend_foods. Em seguida, exibimos as
duas listas para ver se cada um desses alimentos está na lista apropriada.
My favorite foods are:
x ['pizza', 'falafel', 'carrot cake', 'cannoli']
My friend's favorite foods are:
y ['pizza', 'falafel', 'carrot cake', 'ice cream']
A saída em x mostra que 'cannoli' agora aparece em nossa lista de
alimentos prediletos, mas 'ice cream' não. Em y podemos ver que 'ice
cream' agora aparece na lista de nosso amigo, mas 'cannoli' não. Se
tivéssemos simplesmente definido friend_foods como igual a my_foods, não
teríamos gerado duas listas separadas. Por exemplo, eis o que acontece
quando tentamos copiar uma lista sem usar uma fatia:
my_foods = ['pizza', 'falafel', 'carrot cake']
# Isto não funciona:
u friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("nMy friend's favorite foods are:")
print(friend_foods)
Em vez de armazenar uma cópia de my_foods em friend_foods em u,
definimos que friend_foods é igual a my_foods. Essa sintaxe, na verdade, diz
a Python para conectar a nova variável friend_foods à lista que já está em
my_foods, de modo que, agora, as duas variáveis apontam para a mesma
lista. Como resultado, quando adicionamos 'cannoli' em my_foods, essa
informação aparecerá em friend_foods. De modo semelhante, 'ice cream'
aparecerá nas duas listas, apesar de parecer que foi adicionada somente em
friend_foods.
A saída mostra que as duas listas agora são iguais, mas não é isso que
queríamos fazer:
My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
NOTA Não se preocupe com os detalhes desse exemplo por enquanto. Basicamente,
se você estiver tentando trabalhar com uma cópia de uma lista e vir um
comportamento inesperado, certifique-se de que está copiando a lista usando
uma fatia, como fizemos no primeiro exemplo.
FAÇA VOCÊ MESMO
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo,
acrescente várias linhas no final do programa que façam o seguinte:
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia
para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três
itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir
os três últimos itens da lista.
4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
Então faça o seguinte:
• Adicione uma nova pizza à lista original.
• Adicione uma pizza diferente à lista friend_pizzas.
• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas
favoritas são:; em seguida, utilize um laço for para exibir a primeira lista. Exiba a
mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço
for para exibir a segunda lista. Certifique-se de que cada pizza nova esteja
armazenada na lista apropriada.
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços
for para fazer exibições a fim de economizar espaço. Escolha uma versão de
foods.py e escreva dois laços for para exibir cada lista de comidas.
Tuplas
As listas funcionam bem para armazenar conjuntos de itens que podem
mudar durante a vida de um programa. A capacidade de modificar listas é
particularmente importante quando trabalhamos com uma lista de
usuários em um site ou com uma lista de personagens em um jogo. No
entanto, às vezes, você vai querer criar uma lista de itens que não poderá
mudar. As tuplas permitir fazer exatamente isso. Python refere-se a valores
que não podem mudar como imutáveis, e uma lista imutável é chamada de
tupla.
Definindo umatupla
Uma tupla se parece exatamente com uma lista, exceto por usar parênteses
no lugar de colchetes. Depois de definir uma tupla, podemos acessar
elementos individuais usando o índice de cada item, como faríamos com
uma lista.
Por exemplo, se tivermos um retângulo que sempre deva ter determinado
tamanho, podemos garantir que seu tamanho não mudará colocando as
dimensões em uma tupla:
dimensions.py
u dimensions = (200, 50)
v print(dimensions[0])
print(dimensions[1])
Definimos a tupla dimensions em u, usando parênteses no lugar de
colchetes. Em v exibimos cada elemento da tupla individualmente com a
mesma sintaxe que usamos para acessar elementos de uma lista:
200
50
Vamos ver o que acontece se tentarmos alterar um dos itens da tupla
dimensions:
dimensions = (200, 50)
u dimensions[0] = 250
O código em u tenta mudar o valor da primeira dimensão, mas Python
devolve um erro de tipo. Basicamente, pelo fato de estarmos tentando
alterar uma tupla, o que não pode ser feito para esse tipo de objeto, Python
nos informa que não podemos atribuir um novo valor a um item em uma
tupla:
Traceback (most recent call last):
File "dimensions.py", line 3, in <module>
dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment
Isso é um ponto positivo, pois queremos que Python gere um erro se uma
linha de código tentar alterar as dimensões do retângulo.
Percorrendo todos osvalores de umatuplacomumlaço
Podemos percorrer todos os valores de uma tupla usando um laço for,
assim como fizemos com uma lista:
dimensions = (200, 50)
for dimension in dimensions:
print(dimension)
Python devolve todos os elementos da tupla, como faria com uma lista:
200
50
Sobrescrevendo umatupla
Embora não seja possível modificar uma tupla, podemos atribuir um novo
valor a uma variável que armazena uma tupla. Portanto, se quiséssemos
alterar nossas dimensões, poderíamos redefinir a tupla toda:
u dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
print(dimension)
v dimensions = (400, 100)
w print("nModified dimensions:")
for dimension in dimensions:
print(dimension)
O bloco em u define a tupla original e exibe as dimensões iniciais. Em v
armazenamos uma nova tupla na variável dimensions. Em seguida, exibimos
as novas dimensões em w. Python não gera nenhum erro dessa vez, pois
sobrescrever uma variável é uma operação válida:
Original dimensions:
200
50
Modified dimensions:
400
100
Se comparada com listas, as tuplas são estruturas de dados simples. Use￾as quando quiser armazenar um conjunto de valores que não deva ser
alterado durante a vida de um programa.
FAÇA VOCÊ MESMO
4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de
comida. Pense em cinco pratos simples e armazene-os em uma tupla.
• Use um laço for para exibir cada prato oferecido pelo restaurante.
• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida,
use um laço for para exibir cada um dos itens do cardápio revisado.
Estilizando seu código
Agora que você está escrevendo programas mais longos, vale a pena
conhecer algumas ideias sobre como estilizar seu código. Reserve tempo
para deixar seu código o mais legível possível. Escrever códigos fáceis de ler
ajuda a manter o controle sobre o que seus programas fazem e também
contribui para que outras pessoas entendam seu código.
Programadores Python chegaram a um acordo sobre várias convenções
de estilo a fim de garantir que o código de todos, de modo geral, esteja
estruturado da mesma maneira. Depois que aprender a escrever código
Python limpo, você deverá ser capaz de entender a estrutura geral do
código Python de qualquer pessoa, desde que elas sigam as mesmas
diretrizes. Se você espera tornar-se um programador profissional em algum
momento, comece a seguir essas diretrizes o mais rápido possível, a fim de
desenvolver bons hábitos.
Guia deestilo
Quando alguém quer fazer uma alteração na linguagem Python, essa
pessoa escreve uma PEP (Python Enhancement Proposal, ou Proposta de
Melhoria de Python). Uma das PEPs mais antigas é a PEP 8, que instrui
programadores Python a estilizar seu código. A PEP é bem longa, mas boa
parte dela está relacionada a estruturas de código mais complexas do que
vimos até agora.
O guia de estilo de Python foi escrito considerando que o código é lido
com mais frequência que é escrito. Você escreverá seu código uma vez e
então começará a lê-lo quando começar a depuração. Quando acrescentar
recursos a um programa, você gastará mais tempo lendo o seu código. Ao
compartilhar seu código com outros programadores, eles também o lerão.
Dada a opção entre escrever um código que seja mais fácil de escrever ou
um código que seja mais fácil de ler, os programadores Python quase
sempre incentivarão você a escrever um código que seja mais fácil de ler.
As diretrizes a seguir ajudarão a escrever um código claro desde o início.
Indentação
A PEP 8 recomenda usar quatro espaços por nível de indentação. Usar
quatro espaços melhora a legibilidade, ao mesmo tempo que deixa espaço
para vários níveis de indentação em cada linha.
Em um documento de processador de texto, com frequência, as pessoas
usam tabulações no lugar de espaços para indentar. Isso funciona bem para
documentos de processadores de texto, mas o interpretador Python fica
confuso quando tabulações são misturadas a espaços. Todo editor de texto
oferece uma configuração que permite usar a tecla TAB, mas converte cada
tabulação em um número definido de espaços. Definitivamente, você deve
usar a tecla TAB, mas certifique-se também de que seu editor esteja
configurado para inserir espaços no lugar de tabulações em seu
documento.
Misturar tabulações com espaços em seu arquivo pode causar problemas
que são difíceis de diagnosticar. Se você achar que tem uma mistura de
tabulações e espaços, é possível converter todas as tabulações de um
arquivo em espaços na maioria dos editores.
Tamanho dalinha
Muitos programadores Python recomendavam que cada linha deveria ter
menos de 80 caracteres. Historicamente, essa diretriz se desenvolveu
porque a maioria dos computadores conseguia inserir apenas 79 caracteres
em uma única linha em uma janela de terminal. Atualmente, as pessoas
conseguem colocar linhas mais longas em suas telas, mas há outros
motivos para se ater ao tamanho de linha-padrão de 79 caracteres.
Programadores profissionais muitas vezes têm vários arquivos abertos na
mesma tela, e usar o tamanho-padrão de linha lhes permite ver linhas
inteiras em dois ou três arquivos abertos lado a lado na tela. A PEP 8
também recomenda que você limite todos os seus comentários em 72
caracteres por linha, pois algumas das ferramentas que geram
documentação automática para projetos maiores acrescentam caracteres de
formatação no início de cada linha comentada.
As diretrizes da PEP 8 para tamanho de linha não estão gravadas a ferro e
fogo, e algumas equipes preferem um limite de 99 caracteres. Não se
preocupe demais com o tamanho da linha em seu código enquanto estiver
aprendendo, mas saiba que as pessoas que trabalham de modo
colaborativo quase sempre seguem as orientações da PEP 8. A maioria dos
editores permite configurar uma indicação visual – geralmente é uma linha
vertical na tela – que mostra em que ponto estão esses limites.
NOTA O Apêndice B mostra como configurar seu editor de texto de modo que ele
insira quatro espaços sempre que você pressionar a tecla TAB e mostre uma
linha vertical para ajudá-lo a seguir o limite de 79 caracteres.
Linhasembranco
Para agrupar partes de seu programa visualmente, utilize linhas em branco.
Você deve usar linhas em branco para organizar seus arquivos, mas não as
use de modo excessivo. Ao seguir os exemplos fornecidos neste livro, você
deverá atingir o equilíbrio adequado. Por exemplo, se você tiver cinco
linhas de código que criem uma lista e, então, outras três linhas que façam
algo com essa lista, será apropriado colocar uma linha em branco entre as
duas seções. Entretanto, você não deve colocar três ou quatro linhas em
branco entre as duas seções.
As linhas em branco não afetarão o modo como seu código é executado,
mas influenciarão em sua legibilidade. O interpretador Python utiliza
indentação horizontal para interpretar o significado de seu código, mas
despreza o espaçamento vertical.
Outras diretrizes deestilo
A PEP 8 tem muitas recomendações adicionais para estilo, mas a maioria
das diretrizes refere-se a programas mais complexos que aqueles que você
está escrevendo no momento. À medida que conhecer estruturas Python
mais complexas, compartilharei as partes relevantes das diretrizes da PEP
8.
FAÇA VOCÊ MESMO
4.14 – PEP 8: Observe o guia de estilo da PEP 8 original em
https://python.org/dev/peps/pep-0008/. Você não usará boa parte dele agora,
mas pode ser interessante dar uma olhada.
4.15 – Revisão de código: Escolha três programas que você escreveu neste
capítulo e modifique-os para que estejam de acordo com a PEP 8:
• Use quatro espaços para cada nível de indentação. Configure seu editor de texto
para inserir quatro espaços sempre que a tecla TAB for usada, caso ainda não
tenha feito isso (consulte o Apêndice B para ver instruções sobre como fazê-lo).
• Use menos de 80 caracteres em cada linha e configure seu editor para que
mostre uma linha vertical na posição do caractere de número 80.
• Não use linhas em branco em demasia em seus arquivos de programa.
Resumo
Neste capítulo aprendemos a trabalhar de modo eficiente com os
elementos de uma lista. Vimos como percorrer uma lista usando um laço
for, como Python usa indentação para estruturar um programa e como
evitar alguns erros comuns de indentação. Aprendemos a criar listas
numéricas simples, além de conhecermos algumas operações que podem
ser realizadas em listas numéricas. Aprendemos a fatiar uma lista para
trabalhar com um subconjunto de itens e a copiar listas de modo adequado
usando uma fatia. Também conhecemos as tuplas, que oferecem um nível
de proteção a um conjunto de valores que não deve ser alterado, e
aprendemos a estilizar seu código cada vez mais complexo para facilitar
sua leitura.
No Capítulo 5 veremos como responder de forma apropriada a diferentes
condições usando instruções if. Aprenderemos a combinar conjuntos
relativamente complexos de testes condicionais para responder de forma
apropriada ao tipo de situação desejada ou oferecer informações que você
esteja procurando. Também aprenderemos a usar instruções if enquanto
percorremos uma lista para realizar ações específicas com elementos
selecionados de uma lista.
Com frequência, a programação envolve analisar um
conjunto de condições e decidir qual ação deve ser
executada de acordo com essas condições. A instrução if
de Python permite analisar o estado atual de um
programa e responder de forma apropriada a esse estado.
Neste capítulo aprenderemos a escrever testes condicionais, que
permitem verificar qualquer condição que seja de seu interesse. Veremos
como escrever instruções if simples e criar uma série de instruções if mais
complexa para identificar se as condições exatas que você quer estão
presentes. Então você aplicará esse conceito a listas, de modo que será
possível escrever um laço for que trate a maioria dos itens de uma lista de
uma maneira, mas determinados itens com valores específicos de modo
diferente.
Umexemplo simples
O pequeno exemplo a seguir mostra como testes if permitem responder a
situações especiais de forma correta. Suponha que você tenha uma lista de
carros e queira exibir o nome de cada carro. Carros têm nomes próprios,
portanto a maioria deles deve ser exibido com a primeira letra maiúscula.
No entanto, o valor 'bmw' deve ser apresentado somente com letras
maiúsculas. O código a seguir percorre uma lista de nomes de carros em
um laço e procura o valor 'bmw'. Sempre que o valor for 'bmw', ele será
exibido com letras maiúsculas, e não apenas com a inicial maiúscula:
cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
u if car == 'bmw':
print(car.upper())
else:
print(car.title())
O laço nesse exemplo inicialmente verifica se o valor atual de car é
'bmw' u. Em caso afirmativo, o valor é exibido com letras maiúsculas. Se o
valor de car for diferente de 'bmw', será exibido com a primeira letra
maiúscula:
Audi
BMW
Subaru
Toyota
Esse exemplo combina vários conceitos que veremos neste capítulo.
Vamos começar observando os tipos de teste que podemos usar para
analisar as condições em seu programa.
Testes condicionais
No coração de cada instrução if está uma expressão que pode ser avaliada
como True ou False, chamada de teste condicional. Python usa os valores
True e False para decidir se o código em uma instrução if deve ser
executado. Se um teste condicional for avaliado como True, Python
executará o código após a instrução if. Se o teste for avaliado como False,
o interpretador ignorará o código depois da instrução if.
Verificando aigualdade
A maioria dos testes condicionais compara o valor atual de uma variável
com um valor específico de interesse. O teste condicional mais simples
verifica se o valor de uma variável é igual ao valor de interesse:
u >>> car = 'bmw'
v >>> car == 'bmw'
True
A linha em u define o valor de car como 'bmw' usando um único sinal de
igualdade, como já vimos muitas vezes. A linha em v verifica se o valor de
car é 'bmw' usando um sinal de igualdade duplo (==). Esse operador de
igualdade devolve True se os valores dos lados esquerdo e direito do
operador forem iguais, e False se forem diferentes. Os valores nesse
exemplo são iguais, portanto Python devolve True.
Quando o valor de car for diferente de 'bmw', esse teste devolverá False:
u >>> car = 'audi'
v >>> car == 'bmw'
False
Um único sinal de igual, na verdade, é uma instrução; você poderia ler o
código em u como “defina o valor de car como 'audi'”. Por outro lado, um
sinal de igualdade duplo, como o que está em v, faz uma pergunta: “O
valor de car é igual a 'bmw'?”. A maioria das linguagens de programação
utiliza sinais de igualdade dessa maneira.
Ignorando as diferençasentreletras maiúsculase minúsculasao verificar
aigualdade
Testes de igualdade diferenciam letras maiúsculas de minúsculas em
Python. Por exemplo, dois valores com diferenças apenas quanto a letras
maiúsculas ou minúsculas não são considerados iguais:
>>> car = 'Audi'
>>> car == 'audi'
False
Se a diferença entre letras maiúsculas e minúsculas for importante, esse
comportamento será vantajoso. Porém, se essa diferença não importar e
você simplesmente quiser testar o valor de uma variável, poderá converter
esse valor para letras minúsculas antes de fazer a comparação:
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
Esse teste deve devolver True, independentemente do modo como o valor
'Audi' estiver formatado, pois o teste agora ignora as diferenças entre letras
maiúsculas e minúsculas. A função lower() não altera o valor originalmente
armazenado em car, portanto você pode fazer esse tipo de comparação sem
afetá-lo:
u >>> car = 'Audi'
v >>> car.lower() == 'audi'
True
w >>> car
'Audi'
Em u armazenamos a string 'Audi' com a primeira letra maiúscula na
variável car. Em v convertemos o valor de car para letras minúsculas e
comparamos esse valor com a string 'audi'. As duas strings são iguais,
portanto Python devolve True. Em w podemos ver que o valor armazenado
em car não foi afetado pelo teste condicional.
Os sites impõem determinadas regras para os dados fornecidos pelos
usuários de modo semelhante a esse. Por exemplo, um site pode usar um
teste condicional desse tipo para garantir que todos os usuários tenham um
nome realmente único, e não apenas uma variação quanto ao uso de letras
maiúsculas em relação ao nome de usuário de outra pessoa. Quando
alguém submeter um novo nome de usuário, esse nome será convertido
para letras minúsculas e comparado às versões com letras minúsculas de
todos os nomes de usuário existentes. Durante essa verificação, um nome
de usuário como 'John' será rejeitado se houver qualquer variação de
'john' já em uso.
Verificando a diferença
Se quiser determinar se dois valores não são iguais, você poderá combinar
um ponto de exclamação e um sinal de igualdade (!=). O ponto de
exclamação representa não, como ocorre em muitas linguagens de
programação.
Vamos usar outra instrução if para ver como o operador “diferente de” é
usado. Armazenaremos o ingrediente pedido em uma pizza em uma
variável e então exibiremos uma mensagem se a pessoa não pediu
anchovas:
toppings.py
requested_topping = 'mushrooms'
u if requested_topping != 'anchovies':
print("Hold the anchovies!")
A linha em u compara o valor de requested_topping com o valor
'anchovies'. Se esses dois valores não forem iguais, Python devolverá True e
executará o código após a instrução if. Se esses dois valores forem iguais,
Python devolverá False e não executará o código após essa instrução.
Como o valor de requested_topping não é 'anchovies', a instrução print é
executada:
Hold the anchovies!
A maior parte das expressões condicionais que você escrever testará a
igualdade, porém, às vezes, você achará mais eficiente testar a não
igualdade.
Comparações numéricas
Testar valores numéricos é bem simples. Por exemplo, o código a seguir
verifica se uma pessoa tem 18 anos:
>>> age = 18
>>> age == 18
True
Também podemos testar se dois números não são iguais. Por exemplo, o
código a seguir exibe uma mensagem se a resposta dada não estiver
correta:
magic_number.py
answer = 17
u if answer != 42:
print("That is not the correct answer. Please try again!")
O teste condicional em u passa porque o valor de answer (17) não é igual a
42. Como o teste passa, o bloco de código indentado é executado:
That is not the correct answer. Please try again!
Você pode incluir também várias comparações matemáticas em suas
instruções condicionais, por exemplo, menor que, menor ou igual a, maior
que e maior ou igual a:
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
Toda comparação matemática pode ser usada como parte de uma
instrução if, o que pode ajudar você a determinar as condições exatas de
interesse.
Testando várias condições
Pode ser que você queira testar várias condições ao mesmo tempo. Por
exemplo, ocasionalmente, você pode precisar de duas condições True para
executar uma ação. Em outros casos, poderia ficar satisfeito com apenas
uma condição True. As palavras reservadas and e or podem ajudar nessas
situações.
Usando and paratestarvárias condições
Para verificar se duas condições são True simultaneamente, utilize a palavra
reservada and para combinar os dois testes condicionais; se cada um dos
testes passar, a expressão como um todo será avaliada como True. Se um
dos testes falhar, ou ambos, a expressão será avaliada como False.
Por exemplo, podemos verificar se duas pessoas têm mais de 21 anos
usando o teste a seguir:
u >>> age_0 = 22
>>> age_1 = 18
v >>> age_0 >= 21 and age_1 >= 21
False
w >>> age_1 = 22
>>> age_0 >= 21 and age_1 >= 21
True
Em u definimos duas idades, age_0 e age_1. Em v verificamos se as duas
idades são maiores ou iguais a 21. O teste à esquerda passa, porém, o teste
à direita falha, portanto a expressão condicional como um todo é avaliada
como False. Em w mudamos age_1 para 22. O valor de age_1 agora é maior
que 21, portanto os dois testes individuais passam, fazendo com que a
expressão condicional como um todo seja avaliada como True.
Para melhorar a legibilidade, podemos usar parênteses em torno dos
testes individuais, mas eles não são obrigatórios. Se usar parênteses, seu
teste terá o seguinte aspecto:
(age_0 >= 21) and (age_1 >= 21)
Usando or paratestarvárias condições
A palavra reservada or permite verificar várias condições também, mas o
teste passa se um dos testes individuais passar, ou ambos. Uma expressão
or falha somente quando os dois testes individuais falharem.
Vamos considerar duas idades novamente, porém, desta vez, queremos
que apenas uma das pessoas tenha mais de 21 anos:
u >>> age_0 = 22
>>> age_1 = 18
v >>> age_0 >= 21 or age_1 >= 21
True
w >>> age_0 = 18
>>> age_0 >= 21 or age_1 >= 21
False
Começamos novamente com duas variáveis para idade em u. Como o
teste para age_0 em v passa, a expressão com um todo é avaliada como
True. Então diminuímos age_0 para 18. Em w os dois testes agora falham e
a expressão como um todo é avaliada como False.
Verificando se umvalorestáemumalista
Às vezes, é importante verificar se uma lista contém um determinado valor
antes de executar uma ação. Por exemplo, talvez você queira verificar se
um novo nome de usuário já existe em uma lista de nomes de usuários
atuais antes de concluir o registro de alguém em um site. Em um projeto de
mapeamento, você pode querer verificar se uma localidade submetida já
existe em uma lista de localidades conhecidas.
Para descobrir se um valor em particular já está em uma lista, utilize a
palavra reservada in. Vamos observar um código que você poderia escrever
para uma pizzaria. Criaremos uma lista de ingredientes que um cliente
pediu em sua pizza e, então, verificaremos se determinados ingredientes
estão na lista.
>>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
u >>> 'mushrooms' in requested_toppings
True
v >>> 'pepperoni' in requested_toppings
False
Em u e em v, a palavra reservada in diz a Python para verificar a
existência de 'mushrooms' e de 'pepperoni' na lista requested_toppings. Essa
técnica é bem eficaz, pois podemos criar uma lista de valores essenciais e
verificar facilmente se o valor que estamos testando é igual a um dos
valores da lista.
Verificando se umvalor não estáemumalista
Em outras ocasiões, é importante saber se um valor não está em uma lista.
Podemos usar a palavra reservada not nesse caso. Por exemplo, considere
uma lista de usuários que foi impedida de fazer comentários em um fórum.
Podemos verificar se um usuário foi banido antes de permitir que essa
pessoa submeta um comentário:
banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
u if user not in banned_users:
print(user.title() + ", you can post a response if you wish.")
A linha em u é bem clara. Se o valor de user não estiver na lista
banned_users, Python devolverá True e executará a linha indentada.
A usuária 'marie' não está na lista banned_users, portanto ela vê uma
mensagem convidando-a a postar uma resposta:
Marie, you can post a response if you wish.
Expressões booleanas
À medida que aprender mais sobre programação, você ouvirá o termo
expressão booleana em algum momento. Uma expressão booleana é apenas
outro nome para um teste condicional. Um valor booleano é True ou False,
exatamente como o valor de uma expressão condicional após ter sido
avaliada.
Valores booleanos muitas vezes são usados para manter o controle de
determinadas condições, como o fato de um jogo estar executando ou se
um usuário pode editar certos conteúdos em um site:
game_active = True
can_edit = False
Valores booleanos oferecem uma maneira eficiente para monitorar o
estado ou uma condição em particular que seja importante para o seu
programa.
FAÇA VOCÊ MESMO
5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma
frase que descreva o teste e o resultado previsto para cada um. Seu código deverá
ser semelhante a:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Observe atentamente seus resultados e certifique-se de que compreende por que
cada linha é avaliada como True ou False.
• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e
outros cinco avaliados como False.
5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que
criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescente￾os em conditional_tests.py. Tenha pelo menos um resultado True e um False para
cada um dos casos a seguir:
• testes de igualdade e de não igualdade com strings;
• testes usando a função lower();
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que,
maior ou igual a e menor ou igual a;
• testes usando as palavras reservadas and e or;
• testes para verificar se um item está em uma lista;
• testes para verificar se um item não está em uma lista.
Instruções if
Quando compreender os testes condicionais, você poderá começar a
escrever instruções if. Há vários tipos de instruções if, e a escolha de qual
deles usar dependerá do número de condições que devem ser testadas.
Vimos vários exemplos de instruções if na discussão sobre testes
condicionais, mas agora vamos explorar mais o assunto.
Instruções if simples
O tipo mais simples de instrução if tem um teste e uma ação:
if teste_condicional:
faça algo
Você pode colocar qualquer teste condicional na primeira linha, e
praticamente qualquer ação no bloco indentado após o teste. Se o teste
condicional for avaliado como True, Python executará o código após a
instrução if. Se o teste for avaliado como False, Python ignorará o código
depois da instrução if.
Suponha que temos uma variável que representa a idade de uma pessoa e
queremos saber se essa pessoa tem idade suficiente para votar. O código a
seguir testa se a pessoa pode votar:
voting.py
age = 19
u if age >= 18:
v print("You are old enough to vote!")
Em u Python verifica se o valor em age é maior ou igual a 18. É maior,
portanto a instrução indentada print em v é executada:
You are old enough to vote!
A indentação tem a mesma função em instruções if que aquela
desempenhada em laços for. Todas as linhas indentadas após uma
instrução if serão executadas se o teste passar, e todo o bloco de linhas
indentadas será ignorado se o teste não passar.
Podemos ter tantas linhas de código quantas quisermos no bloco após a
instrução if. Vamos acrescentar outra linha de saída se a pessoa tiver idade
suficiente para votar, perguntando se o indivíduo já se registrou para votar:
age = 19
if age >= 18:
print("You are old enough to vote!")
print("Have you registered to vote yet?")
O teste condicional passa e as duas instruções print estão indentadas,
portanto ambas as linhas são exibidas:
You are old enough to vote!
Have you registered to vote yet?
Se o valor de age for menor que 18, esse programa não apresentará
nenhuma saída.
Instruções if-else
Com frequência você vai querer executar uma ação quando um teste
condicional passar, e uma ação diferente em todos os demais casos. A
sintaxe if-else de Python torna isso possível. Um bloco if-else é
semelhante a uma instrução if simples, porém a instrução else permite
definir uma ação ou um conjunto de ações executado quando o teste
condicional falhar.
Exibiremos a mesma mensagem mostrada antes se a pessoa tiver idade
suficiente para votar, porém, desta vez, acrescentaremos uma mensagem
para qualquer um que não tenha idade suficiente para votar:
age = 17
u if age >= 18:
print("You are old enough to vote!")
print("Have you registered to vote yet?")
v else:
print("Sorry, you are too young to vote.")
print("Please register to vote as soon as you turn 18!")
Se o teste condicional em u passar, o primeiro bloco de instruções print
indentadas será executado. Se o teste for avaliado como False, o bloco else
em v será executado. Como age é menor que 18 dessa vez, o teste
condicional falha e o código do bloco else é executado:
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
Esse código funciona porque há apenas duas possíveis situações para
avaliar: uma pessoa tem idade suficiente para votar ou não tem. A estrutura
if-else funciona bem em situações em que você quer que Python sempre
execute uma de duas possíveis ações. Em uma cadeia if-else simples como
essa, uma das duas ações sempre será executada.
Sintaxeif-elif-else
Muitas vezes, você precisará testar mais de duas situações possíveis; para
avaliar isso, a sintaxe if-elif-else de Python poderá ser usada. Python
executa apenas um bloco em uma cadeia if-elif-else. Cada teste
condicional é executado em sequência, até que um deles passe. Quando
um teste passar, o código após esse teste será executado e Python ignorará
o restante dos testes.
Muitas situações do mundo real envolvem mais de duas condições
possíveis. Por exemplo, considere um parque de diversões que cobre
preços distintos para grupos etários diferentes:
• a entrada para qualquer pessoa com menos de 4 anos é gratuita;
• a entrada para qualquer pessoa com idade entre 4 e 18 anos custa 5
dólares;
• a entrada para qualquer pessoa com 18 anos ou mais custa 10 dólares.
Como podemos usar uma instrução if para determinar o preço da
entrada de alguém? O código a seguir testa a faixa etária de uma pessoa e
então exibe uma mensagem com o preço da entrada:
amusement_park.py
age = 12
u if age < 4:
print("Your admission cost is $0.")
v elif age < 18:
print("Your admission cost is $5.")
w else:
print("Your admission cost is $10.")
O teste if em u verifica se uma pessoa tem menos de 4 anos. Se o teste
passar, uma mensagem apropriada será exibida e Python ignorará o
restante dos testes. A linha elif em v, na verdade, é outro teste if,
executado somente se o teste anterior falhar. Nesse ponto da cadeia,
sabemos que a pessoa tem pelo menos 4 anos de idade, pois o primeiro
teste falhou. Se a pessoa tiver menos de 18 anos, uma mensagem
apropriada será exibida, e Python ignorará o bloco else. Se tanto o teste em
if quanto o teste em elif falharem, Python executará o código do bloco
else em w.
Nesse exemplo, o teste em u é avaliado como False, portanto seu bloco
de código não é executado. No entanto, o segundo teste é avaliado como
True (12 é menor que 18), portanto seu código é executado. A saída é uma
frase que informa o preço da entrada ao usuário:
Your admission cost is $5.
Qualquer idade acima de 17 anos faria os dois primeiros testes falharem.
Nessas situações, o bloco else seria executado e o preço da entrada seria de
10 dólares.
Em vez de exibir o preço da entrada no bloco if-elif-else, seria mais
conciso apenas definir o preço na cadeia if-elif-else e, então, ter uma
instrução print simples que execute depois que a cadeia for avaliada:
age = 12
if age < 4:
u price = 0
elif age < 18:
v price = 5
else:
w price = 10
x print("Your admission cost is $" + str(price) + ".")
As linhas em u, v e w definem o valor de price conforme a idade da
pessoa, como no exemplo anterior. Depois que o preço é definido pela
cadeia if-elif-else, uma instrução print separada e não indentada x utiliza
esse valor para exibir uma mensagem informando o preço de entrada da
pessoa.
Esse código gera a mesma saída do exemplo anterior, mas o propósito da
cadeia if-elif-else é mais restrito. Em vez de determinar um preço e exibir
uma mensagem, ela simplesmente determina o preço da entrada. Além de
ser mais eficiente, esse código revisado é mais fácil de modificar que a
abordagem original. Para mudar o texto da mensagem de saída, seria
necessário alterar apenas uma instrução print, e não três instruções print
separadas.
Usando vários blocoselif
Podemos usar quantos blocos elif quisermos em nosso código. Por
exemplo, se o parque de diversões implementasse um desconto para
idosos, você poderia acrescentar mais um teste condicional no código a fim
de determinar se uma pessoa está qualificada a receber esse desconto.
Suponha que qualquer pessoa com 65 anos ou mais pague metade do
preço normal da entrada, isto é, 5 dólares:
age = 12
if age < 4:
price = 0
elif age < 18:
price = 5
u elif age < 65:
price = 10
v else:
price = 5
print("Your admission cost is $" + str(price) + ".")
A maior parte desse código não foi alterada. O segundo bloco elif em u
agora faz uma verificação para garantir que uma pessoa tenha menos de 65
anos antes de lhe cobrar o preço da entrada inteira, que é de 10 dólares.
Observe que o valor atribuído no bloco else em v precisa ser alterado para
5 dólares, pois as únicas idades que chegam até esse bloco são de pessoas
com 65 anos ou mais.
Omitindo o bloco else
Python não exige um bloco else no final de uma cadeia if-elif. Às vezes,
um bloco else é útil; outras vezes, é mais claro usar uma instrução elif
adicional que capture a condição específica de interesse:
age = 12
if age < 4:
price = 0
elif age < 18:
price = 5
elif age < 65:
price = 10
u elif age >= 65:
price = 5
print("Your admission cost is $" + str(price) + ".")
O bloco elif extra em u atribui um preço de 5 dólares quando a pessoa
tiver 65 anos ou mais, o que é um pouco mais claro que o bloco else geral.
Com essa mudança, todo bloco de código deve passar por um teste
específico para ser executado.
O bloco else é uma instrução que captura tudo. Ela corresponde a
qualquer condição não atendida por um teste if ou elif específicos e isso,
às vezes, pode incluir dados inválidos ou até mesmo maliciosos. Se você
tiver uma condição final específica para testar, considere usar um último
bloco elif e omitir o bloco else. Como resultado, você terá mais confiança
de que seu código executará somente nas condições corretas.
Testando várias condições
A cadeia if-elif-else é eficaz, mas é apropriada somente quando você
quiser que apenas um teste passe. Assim que encontrar um teste que passe,
o interpretador Python ignorará o restante dos testes. Esse comportamento
é vantajoso, pois é eficiente e permite testar uma condição específica.
Às vezes, porém, é importante verificar todas as condições de interesse.
Nesse caso, você deve usar uma série de instruções if simples, sem blocos
elif ou else. Essa técnica faz sentido quando mais de uma condição pode
ser True e você quer atuar em todas as condições que sejam verdadeiras.
Vamos reconsiderar o exemplo da pizzaria. Se alguém pedir uma pizza
com dois ingredientes, será necessário garantir que esses dois ingredientes
sejam incluídos em sua pizza:
toppings.py
u requested_toppings = ['mushrooms', 'extra cheese']
v if 'mushrooms' in requested_toppings:
print("Adding mushrooms.")
w if 'pepperoni' in requested_toppings:
print("Adding pepperoni.")
x if 'extra cheese' in requested_toppings:
print("Adding extra cheese.")
print("nFinished making your pizza!")
Começamos em u com uma lista contendo os ingredientes solicitados. A
instrução if em v verifica se a pessoa pediu cogumelos ('mushrooms') em
sua pizza. Em caso afirmativo, uma mensagem será exibida para confirmar
esse ingrediente. O teste para pepperoni em w corresponde a outra
instrução if simples, e não a uma instrução elif ou else, portanto esse
teste é executado independentemente de o teste anterior ter passado ou
não. O código em x verifica se queijo extra ('extra cheese') foi pedido, não
importando o resultado dos dois primeiros testes. Esses três testes
independentes são realizados sempre que o programa é executado.
Como todas as condições nesse exemplo são avaliadas, tanto cogumelos
quanto queijo extra são adicionados à pizza:
Adding mushrooms.
Adding extra cheese.
Finished making your pizza!
Esse código não funcionaria de modo apropriado se tivéssemos usado um
bloco if-elif-else, pois o código pararia de executar depois que apenas um
teste tivesse passado. Esse código seria assim:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
print("Adding extra cheese.")
print("nFinished making your pizza!")
O teste para 'mushrooms' é o primeiro a passar, portanto cogumelos são
adicionados à pizza. No entanto, os valores 'extra cheese' e 'pepperoni'
não são verificados, pois Python não executa nenhum teste depois do
primeiro que passar em uma cadeia if-elif-else. O primeiro ingrediente
do cliente será adicionado, mas todos os demais não serão:
Adding mushrooms.
Finished making your pizza!
Em suma, se quiser que apenas um bloco de código seja executado,
utilize uma cadeia if-elif-else. Se mais de um bloco de código deve
executar, utilize uma série de instruções if independentes.
FAÇA VOCÊ MESMO
5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser
atingido em um jogo. Crie uma variável chamada alien_color e atribua-lhe um
valor igual a 'green', 'yellow' ou 'red'.
• Escreva uma instrução if para testar se a cor do alienígena é verde. Se for,
mostre uma mensagem informando que o jogador acabou de ganhar cinco
pontos.
• Escreva uma versão desse programa em que o teste if passe e outro em que ele
falhe. (A versão que falha não terá nenhuma saída.)
5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi
feito no Exercício 5.3, e escreva uma cadeia if-else.
• Se a cor do alienígena for verde, mostre uma frase informando que o jogador
acabou de ganhar cinco pontos por atingir o alienígena.
• Se a cor do alienígena não for verde, mostre uma frase informando que o
jogador acabou de ganhar dez pontos.
• Escreva uma versão desse programa que execute o bloco if e outro que execute
o bloco else.
5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4
em uma cadeia if-elif-else.
• Se o alienígena for verde, mostre uma mensagem informando que o jogador
ganhou cinco pontos.
• Se o alienígena for amarelo, mostre uma mensagem informando que o jogador
ganhou dez pontos.
• Se o alienígena for vermelho, mostre uma mensagem informando que o jogador
ganhou quinze pontos.
• Escreva três versões desse programa, garantindo que cada mensagem seja
exibida para a cor apropriada do alienígena.
5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o
estágio da vida de uma pessoa. Defina um valor para a variável age e então:
• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo
que ela é um bebê.
• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem
dizendo que ela é uma criança.
• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem
dizendo que ela é um(a) garoto(a).
• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma
mensagem dizendo que ela é um(a) adolescente.
• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma
mensagem dizendo que ela é adulto.
• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa
pessoa é idoso.
5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma
série de instruções if independentes que verifiquem se determinadas frutas estão
em sua lista.
• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
• Escreva cinco instruções if. Cada instrução deve verificar se uma determinada
fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por
exemplo, Você realmente gosta de bananas!
Usando instruções if comlistas
Algumas tarefas interessantes podem ser feitas se combinarmos listas com
instruções if. Podemos prestar atenção em valores especiais, que devam ser
tratados de modo diferente de outros valores da lista. Podemos administrar
mudanças de condições de modo eficiente, por exemplo, a disponibilidade
de determinados itens em um restaurante durante um turno. Também
podemos começar a provar que nosso código funciona conforme esperado
em todas as possíveis situações.
Verificando itensespeciais
Este capítulo começou com um exemplo simples mostrando como lidar
com um valor especial como 'bmw', que devia ser exibido em um formato
diferente de outros valores da lista. Agora que você tem uma compreensão
básica a respeito dos testes condicionais e de instruções if, vamos observar
com mais detalhes de que modo podemos prestar atenção em valores
especiais de uma lista e tratá-los de forma apropriada.
Vamos prosseguir com o exemplo da pizzaria. A pizzaria exibe uma
mensagem sempre que um ingrediente é adicionado à sua pizza à medida
que ela é preparada. O código para essa ação pode ser escrito de modo
bem eficiente se criarmos uma lista de ingredientes solicitados pelo cliente
e usarmos um laço para anunciar cada ingrediente à medida que ele é
acrescentado à pizza:
toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
print("Adding " + requested_topping + ".")
print("nFinished making your pizza!")
A saída é simples, pois esse código é composto apenas de um laço for
simples:
Adding mushrooms.
Adding green peppers.
Adding extra cheese.
Finished making your pizza!
E se a pizzaria ficasse sem pimentões verdes? Uma instrução if no laço
for pode tratar essa situação de modo apropriado:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
u if requested_topping == 'green peppers':
print("Sorry, we are out of green peppers right now.")
v else:
print("Adding " + requested_topping + ".")
print("nFinished making your pizza!")
Dessa vez verificamos cada item solicitado antes de adicioná-lo à pizza. O
código em u verifica se a pessoa pediu pimentões verdes. Em caso
afirmativo, exibimos uma mensagem informando por que ela não pode ter
pimentões verdes. O bloco else em v garante que todos os demais
ingredientes serão adicionados à pizza.
A saída mostra que cada ingrediente solicitado é tratado de forma
apropriada.
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.
Finished making your pizza!
Verificando se umalista não estávazia
Fizemos uma suposição simples sobre todas as listas com as quais
trabalhamos até agora: supomos que toda lista continha pelo menos um
item. Em breve, deixaremos os usuários fornecerem as informações a serem
armazenadas em uma lista, portanto não poderemos supor que uma lista
contenha um item sempre que um laço for executado. Nessa situação, será
conveniente testar se uma lista está vazia antes de executar um laço for.
Como exemplo, vamos verificar se a lista de ingredientes solicitados está
vazia antes de prepararmos a pizza. Se a lista estiver vazia, perguntaremos
ao usuário se ele realmente quer uma pizza simples. Se a lista não estiver
vazia, prepararemos a pizza exatamente como fizemos nos exemplos
anteriores:
u requested_toppings = []
v if requested_toppings:
for requested_topping in requested_toppings:
print("Adding " + requested_topping + ".")
print("nFinished making your pizza!")
w else:
print("Are you sure you want a plain pizza?")
Dessa vez, começamos com uma lista vazia de ingredientes solicitados em
u. Em vez de passar diretamente para um laço for, fazemos uma verificação
rápida em v. Quando o nome de uma lista é usado em uma instrução if,
Python devolve True se a lista contiver pelo menos um item; uma lista vazia
é avaliada como False. Se requested_toppings passar no teste condicional,
executamos o mesmo laço for do exemplo anterior. Se o teste condicional
falhar, exibimos uma mensagem perguntando ao cliente se ele realmente
quer uma pizza simples, sem ingredientes adicionais w.
Nesse caso, a lista está vazia, portanto a saída contém uma pergunta para
saber se o usuário realmente quer uma pizza simples:
Are you sure you want a plain pizza?
Se a lista não estiver vazia, a saída mostrará cada ingrediente solicitado
adicionado à pizza.
Usando várias listas
As pessoas pedirão de tudo, em especial quando se tratar de ingredientes
para uma pizza. E se um cliente realmente quiser batatas fritas em sua
pizza? Podemos usar listas e instruções if para garantir que o dado de
entrada faça sentido antes de atuar sobre ele.
Vamos prestar atenção em solicitações de ingredientes incomuns antes de
prepararmos uma pizza. O exemplo a seguir define duas listas. A primeira é
uma lista de ingredientes disponíveis na pizzaria, e a segunda é a lista de
ingredientes que o usuário pediu. Dessa vez, cada item em
requested_toppings é verificado em relação à lista de ingredientes
disponíveis antes de ser adicionado à pizza:
u available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
v requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
w for requested_topping in requested_toppings:
x if requested_topping in available_toppings:
print("Adding " + requested_topping + ".")
y else:
print("Sorry, we don't have " + requested_topping + ".")
print("nFinished making your pizza!")
Em u definimos uma lista de ingredientes disponíveis nessa pizzaria.
Observe que essa informação poderia ser uma tupla se a pizzaria tiver uma
seleção estável de ingredientes. Em v criamos uma lista de ingredientes
solicitados por um cliente. Observe a solicitação incomum, 'french fries'
(batatas fritas). Em w percorremos a lista de ingredientes solicitados em
um laço. Nesse laço, inicialmente verificamos se cada ingrediente solicitado
está na lista de ingredientes disponíveis x. Se estiver, adicionamos esse
ingrediente na pizza. Se o ingrediente solicitado não estiver na lista de
ingredientes disponíveis, o bloco else será executado y. Esse bloco exibe
uma mensagem informando ao usuário quais ingredientes não estão
disponíveis.
A sintaxe desse código gera uma saída clara e informativa:
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.
Finished making your pizza!
Com apenas algumas linhas de código, conseguimos tratar uma situação
do mundo real de modo bem eficiente!
FAÇA VOCÊ MESMO
5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o
nome 'admin'. Suponha que você esteja escrevendo um código que exibirá uma
saudação a cada usuário depois que eles fizerem login em um site. Percorra a lista
com um laço e mostre uma saudação para cada usuário:
• Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo,
Olá admin, gostaria de ver um relatório de status?
• Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por
fazer login novamente.
5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a
lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns
usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a
mensagem correta seja exibida.
5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa
que simule o modo como os sites garantem que todos tenham um nome de usuário
único.
• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que
um ou dois dos novos usuários também estejam na lista current_users.
• Percorra a lista new_users com um laço para ver se cada novo nome de usuário
já foi usado. Em caso afirmativo, mostre uma mensagem informando que a
pessoa deverá fornecer um novo nome. Se um nome de usuário não foi usado,
apresente uma mensagem dizendo que o nome do usuário está disponível.
• Certifique-se de que sua comparação não levará em conta as diferenças entre
letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser
aceito.
5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista,
por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa língua
termina com th, exceto 1, 2 e 3.
• Armazene os números de 1 a 9 em uma lista.
• Percorra a lista com um laço.
• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada
para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", e cada resultado deve estar em uma linha separada.
Estilizando suas instruções if
Em todos os exemplos deste capítulo vimos bons hábitos de estilização. A
única recomendação fornecida pela PEP 8 para estilizar testes condicionais
é usar um único espaço em torno dos operadores de comparação, como ==,
>= e <=. Por exemplo:
if age < 4:
é melhor que:
if age<4:
Esse espaçamento não afeta o modo como Python interpreta seu código;
ele simplesmente deixa seu código mais fácil de ler para você e para outras
pessoas.
FAÇA VOCÊ MESMO
5.12 – Estilizando instruções if: Revise os programas que você escreveu neste
capítulo e certifique-se de que os testes condicionais foram estilizados de forma
apropriada.
5.13 – Suas ideias: A essa altura, você é um programador mais capacitado do
que era quando começou a ler este livro. Agora que você tem melhor noção de
como situações do mundo real são modeladas em programas, talvez esteja
pensando em alguns problemas que poderia resolver com seus próprios programas.
Registre qualquer ideia nova que tiver sobre problemas que você queira resolver à
medida que suas habilidades em programação continuam a melhorar. Considere
jogos que você queira escrever, conjuntos de dados que possa querer explorar e
aplicações web que gostaria de criar.
Resumo
Neste capítulo aprendemos a escrever testes condicionais, que são sempre
avaliados como True ou False. Vimos como escrever instruções if simples,
cadeias if-else e cadeias if-elif-else. Começamos a usar essas estruturas
para identificar condições particulares que deviam ser testadas e
aprendemos a reconhecer quando essas condições foram atendidas em
nossos programas. Aprendemos a tratar determinados itens de uma lista de
modo diferente de todos os demais itens, ao mesmo tempo que
continuamos usando a eficiência do laço for. Também retomamos as
recomendações de estilo de Python para garantir que seus programas cada
vez mais complexos continuem relativamente fáceis de ler e de entender.
No Capítulo 6 conheceremos os dicionários de Python. Um dicionário é
semelhante a uma lista, mas permite conectar informações. Aprenderemos
a criar dicionários, percorrê-los com laços e usá-los em conjunto com listas
e instruções if. Conhecer os dicionários permitirá modelar uma variedade
ainda maior de situações do mundo real.
Neste capítulo aprenderemos a usar dicionários Python,
que permitem conectar informações relacionadas.
Veremos como acessar as informações depois que elas
estiverem em um dicionário e modificá-las. Pelo fato de
os dicionários serem capazes de armazenar uma
quantidade quase ilimitada de informações, mostraremos
como percorrer os dados de um dicionário com um laço.
Além disso, aprenderemos a aninhar dicionários em
listas, listas em dicionários e até mesmo dicionários em
outros dicionários.
Entender os dicionários permite modelar uma diversidade de objetos do
mundo real de modo mais preciso. Você será capaz de criar um dicionário
que representa uma pessoa e armazenar quantas informações quiser sobre
ela. Poderá armazenar o nome, a idade, a localização, a profissão e
qualquer outro aspecto de uma pessoa que possa ser descrito. Você será
capaz de armazenar quaisquer duas informações que possam ser
combinadas, por exemplo, uma lista de palavras e seus significados, uma
lista de nomes de pessoas e seus números favoritos, uma lista de
montanhas e suas altitudes, e assim por diante.
Umdicionário simples
Considere um jogo com alienígenas que possam ter cores e valores de
pontuação diferentes. O dicionário simples a seguir armazena informações
sobre um alienígena em particular:
alien.py
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
O dicionário alien_0 armazena a cor do alienígena e o valor da
pontuação. As duas instruções print acessam e exibem essas informações,
conforme mostrado a seguir:
green
5
Como ocorre com a maioria dos conceitos novos de programação, usar
dicionários exige prática. Depois de trabalhar um pouco com dicionários,
você logo verá a eficiência com que eles podem modelar situações do
mundo real.
Trabalhando comdicionários
Um dicionário em Python é uma coleção de pares chave-valor. Cada chave
é conectada a um valor, e você pode usar uma chave para acessar o valor
associado a ela. O valor de uma chave pode ser um número, uma string,
uma lista ou até mesmo outro dicionário. De fato, podemos usar qualquer
objeto que possa ser criado em Python como valor de um dicionário.
Em Python, um dicionário é representado entre chaves, {}, com uma série
de pares chave-valor entre elas, como mostramos no exemplo anterior:
alien_0 = {'color': 'green', 'points': 5}
Um par chave-valor é um conjunto de valores associados um ao outro.
Quando fornecemos uma chave, Python devolve o valor associado a essa
chave. Toda chave é associada a seu valor por meio de dois-pontos, e pares
chave-valor individuais são separados por vírgulas. Podemos armazenar
quantos pares chave-valor quisermos em um dicionário.
O dicionário mais simples tem exatamente um par chave-valor, como
mostra esta versão modificada do dicionário alien_0:
alien_0 = {'color': 'green'}
Esse dicionário armazena uma informação sobre alien_0, que é a cor do
alienígena. A string 'color' é uma chave nesse dicionário, e seu valor
associado é 'green'.
Acessando valoresemumdicionário
Para obter o valor associado a uma chave, especifique o nome do
dicionário e coloque a chave entre colchetes, como vemos a seguir:
alien_0 = {'color': 'green'}
print(alien_0['color'])
Essa instrução devolve o valor associado à chave 'color' do dicionário
alien_0:
green
Podemos ter um número ilimitado de pares chave-valor em um
dicionário. Por exemplo, eis o dicionário alien_0 original com dois pares
chave-valor:
alien_0 = {'color': 'green', 'points': 5}
Agora podemos acessar a cor ou o valor da pontuação de alien_0. Se um
jogador atingir esse alienígena, podemos consultar quantos pontos ele deve
ganhar usando um código como este:
alien_0 = {'color': 'green', 'points': 5}
u new_points = alien_0['points']
v print("You just earned " + str(new_points) + " points!")
Depois que o dicionário for definido, o código em u extrai o valor
associado à chave 'points' do dicionário. Esse valor então é armazenado na
variável new_points. A linha em v converte esse valor inteiro em uma string
e exibe uma frase sobre quantos pontos o jogador acabou de ganhar:
You just earned 5 points!
Se executar esse código sempre que um alienígena for atingido, o valor da
pontuação para esse alienígena será recuperado.
Adicionando novos pares chave-valor
Dicionários são estruturas dinâmicas, e você pode adicionar novos pares
chave-valor a um dicionário a qualquer momento. Por exemplo, para
acrescentar um novo par chave-valor, especifique o nome do dicionário,
seguido da nova chave entre colchetes, juntamente com o novo valor.
Vamos adicionar duas novas informações ao dicionário alien_0: as
coordenadas x e y do alienígena, que nos ajudarão a exibir o alienígena em
determinada posição da tela. Vamos colocar o alienígena na borda
esquerda da tela, 25 pixels abaixo da margem superior. Como as
coordenadas da tela normalmente começam no canto superior esquerdo da
tela, posicionaremos o alienígena na margem esquerda definindo a
coordenada x com 0, e 25 pixels abaixo da margem superior, definindo a
coordenada y com o valor 25 positivo, como vemos aqui:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
u alien_0['x_position'] = 0
v alien_0['y_position'] = 25
print(alien_0)
Começamos definindo o mesmo dicionário com o qual estávamos
trabalhando. Em seguida, exibimos esse dicionário, mostrando uma
imagem de suas informações. Em u acrescentamos um novo par chave￾valor ao dicionário: a chave 'x_position' e o valor 0. Fizemos o mesmo com
a chave 'y_position' em v. Ao exibir o dicionário modificado, vemos os
dois pares chave-valor adicionais:
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
A versão final do dicionário contém quatro pares chave-valor. Os dois
pares originais especificam a cor e o valor da pontuação, enquanto os dois
pares adicionais especificam a posição do alienígena. Observe que a ordem
dos pares chave-valor não coincide com a ordem em que os adicionamos.
Python não se importa com a ordem em que armazenamos cada par chave￾valor; ele só se importa com a conexão entre cada chave e seu valor.
Começando comumdicionário vazio
Às vezes, é conveniente ou até mesmo necessário começar com um
dicionário vazio e então acrescentar novos itens a ele. Para começar a
preencher um dicionário vazio, defina-o com um conjunto de chaves vazio
e depois acrescente cada par chave-valor em sua própria linha. Por
exemplo, eis o modo de criar o dicionário alien_0 usando esta abordagem:
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
Nesse caso, definimos um dicionário alien_0 vazio e, em seguida,
adicionamos valores para cor e pontuação. O resultado é o dicionário que
usamos nos exemplos anteriores:
{'color': 'green', 'points': 5}
Geralmente usamos dicionários vazios quando armazenamos dados
fornecidos pelo usuário em um dicionário, ou quando escrevemos um
código que gere um grande número de pares chave-valor automaticamente.
Modificando valoresemumdicionário
Para modificar um valor em um dicionário, especifique o nome do
dicionário com a chave entre colchetes e o novo valor que você quer
associar a essa chave. Por exemplo, considere um alienígena que muda de
verde para amarelo à medida que o jogo prossegue:
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
Inicialmente, definimos um dicionário para alien_0 que contém apenas a
cor do alienígena; em seguida, modificamos o valor associado à chave
'color' para 'yellow'. A saída mostra que o alienígena realmente mudou de
verde para amarelo:
The alien is green.
The alien is now yellow.
Para ver um exemplo mais interessante, vamos monitorar a posição de
um alienígena que pode se deslocar com velocidades diferentes.
Armazenaremos um valor que representa a velocidade atual do alienígena
e, então, usaremos esse valor para determinar a distância que o alienígena
deve se mover para a direita:
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move o alienígena para a direita
# Determina a distância que o alienígena deve se deslocar de acordo com
sua
# velocidade atual
u if alien_0['speed'] == 'slow':
x_increment = 1
elif alien_0['speed'] == 'medium':
x_increment = 2
else:
# Este deve ser um alienígena rápido
x_increment = 3
# A nova posição é a posição antiga somada ao incremento
v alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
Começamos definindo um alienígena com uma posição x e y iniciais, e
uma velocidade igual a 'medium'. Omitimos a cor e os valores da pontuação
por questões de simplicidade, mas esse exemplo funcionaria da mesma
maneira se tivéssemos incluído esses pares chave-valor também. Além
disso, exibimos o valor original de x_position para ver a distância com que
o alienígena se desloca para a direita.
Em u uma cadeia if-elif-else determina a distância que o alienígena deve
se mover para a direita e esse valor é armazenado na variável x_increment.
Se a velocidade do alienígena for 'slow', ele se deslocará de uma unidade
para a direita; se a velocidade for 'medium', se deslocará de duas unidades
para a direita e, se for 'fast', se deslocará de três unidades à direita. Depois
de calculado, o incremento é somado ao valor de x_position em v, e o
resultado é armazenado no x_position do dicionário.
Como esse é um alienígena de velocidade média, sua posição se desloca
de duas unidades para a direita:
Original x-position: 0
New x-position: 2
Essa técnica é bem interessante: ao mudar um valor do dicionário do
alienígena, podemos mudar o seu comportamento como um todo. Por
exemplo, para transformar esse alienígena de velocidade média em um
alienígena rápido, acrescente a linha a seguir:
alien_0['speed'] = fast
O bloco if-elif-else então atribuirá um valor maior para x_increment na
próxima vez que o código for executado.
Removendo pares chave-valor
Quando não houver mais necessidade de uma informação armazenada em
um dicionário, podemos usar a instrução del para remover totalmente um
par chave-valor. Tudo de que del precisa é do nome do dicionário e da
chave que você deseja remover.
Por exemplo, vamos remover a chave 'points' do dicionário alien_0,
juntamente com seu valor:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
u del alien_0['points']
print(alien_0)
A linha em u diz a Python para apagar a chave 'points' do dicionário
alien_0 e remover o valor associado a essa chave também. A saída mostra
que a chave 'points' e seu valor igual a 5 foram apagados, porém o restante
do dicionário não foi afetado:
{'color': 'green', 'points': 5}
{'color': 'green'}
NOTA Saiba que o par chave-valor apagado é removido de forma permanente.
Umdicionário de objetos semelhantes
O exemplo anterior envolveu a armazenagem de diferentes tipos de
informação sobre um objeto: um alienígena em um jogo. Também
podemos usar um dicionário para armazenar um tipo de informação sobre
vários objetos. Por exemplo, suponha que você queira fazer uma enquete
com várias pessoas e perguntar-lhes qual é a sua linguagem de
programação favorita. Um dicionário é conveniente para armazenar os
resultados de uma enquete simples, desta maneira:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
Como podemos ver, dividimos um dicionário maior em várias linhas.
Cada chave é o nome de uma pessoa que respondeu à enquete, e cada valor
é a sua opção de linguagem. Quando souber que precisará de mais de uma
linha para definir um dicionário, tecle ENTER depois da chave de abertura.
Em seguida, indente a próxima linha em um nível (quatro espaços) e
escreva o primeiro par chave-valor, seguido de uma vírgula. A partir desse
ponto, quando pressionar ENTER, seu editor de texto deverá indentar
automaticamente todos os pares chave-valor subsequentes para que
estejam de acordo com o primeiro par chave-valor.
Depois que acabar de definir o dicionário, acrescente uma chave de
fechamento em uma nova linha após o último par chave-valor e indente-a
em um nível para que esteja alinhada com as chaves do dicionário. Incluir
uma vírgula após o último par chave-valor também é uma boa prática;
assim você estará preparado para acrescentar um novo par chave-valor na
próxima linha.
NOTA A maioria dos editores tem alguma funcionalidade que ajuda a formatar listas
e dicionários longos, de modo semelhante a esse exemplo. Outras maneiras
aceitáveis de formatar dicionários longos também estão disponíveis, portanto
você poderá ver formatações um pouco diferentes em seu editor ou em outros
códigos-fonte.
Para usar esse dicionário, dado o nome de uma pessoa que tenha
respondido à enquete, podemos consultar facilmente sua linguagem
favorita:
favorite_languages.py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
u print("Sarah's favorite language is " +
v favorite_languages['sarah'].title() +
w ".")
Para ver a linguagem que Sarah escolheu, solicitamos o valor em:
favorite_languages['sarah']
Essa sintaxe é usada na instrução print em v, e a saída mostra a
linguagem predileta de Sarah:
Sarah's favorite language is C.
Esse exemplo também mostra como podemos dividir uma instrução print
longa em várias linhas. A palavra print é menor que a maioria dos nomes
de dicionário, portanto faz sentido incluir a primeira parte do que você
quer exibir logo depois do parêntese de abertura u. Escolha um ponto
apropriado para separar o que está sendo exibido e acrescente um
operador de concatenação (+) no final da primeira linha v. Tecle ENTER e
depois TAB para alinhar todas as linhas subsequentes em um nível de
indentação abaixo da instrução print. Quando terminar de compor sua
saída, você pode colocar o parêntese de fechamento na última linha do
bloco print w.
FAÇA VOCÊ MESMO
6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa
que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a
cidade em que ela vive. Você deverá ter chaves como first_name, last_name,
age e city. Mostre cada informação armazenada em seu dicionário.
6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos
de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu
dicionário. Pense em um número favorito para cada pessoa e armazene cada um
como um valor em seu dicionário. Exiba o nome de cada pessoa e seu número
favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos
e obtenha alguns dados reais para o seu programa.
6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário
de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu nos
capítulos anteriores. Use essas palavras como chaves em seu glossário e
armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo
elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu
significado, ou apresentar a palavra em uma linha e então exibir seu significado
indentado em uma segunda linha. Utilize o caractere de quebra de linha (n)
para inserir uma linha em branco entre cada par palavra-significado em sua
saída.
Percorrendo umdicionário comumlaço
Um único dicionário Python pode conter apenas alguns pares chave-valor
ou milhões deles. Como um dicionário pode conter uma grande
quantidade de dados, Python permite percorrer um dicionário com um
laço. Dicionários podem ser usados para armazenar informações de várias
maneiras; assim, há diversos modos diferentes de percorrê-los com um
laço. Podemos percorrer todos os pares chave-valor de um dicionário
usando suas chaves ou seus valores.
Percorrendo todos os pares chave-valor comumlaço
Antes de explorar as diferentes abordagens para percorrer um dicionário
com um laço, vamos considerar um novo dicionário projetado para
armazenar informações sobre um usuário em um site. O dicionário a seguir
armazenará o nome de usuário, o primeiro nome e o sobrenome de uma
pessoa:
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
Podemos acessar qualquer informação única sobre user_0 com base no
que já aprendemos neste capítulo. E se quiséssemos ver tudo que está
armazenado no dicionário desse usuário? Para isso, podemos percorrer o
dicionário com um laço for:
user.py
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
u for key, value in user_0.items():
v print("nKey: " + key)
w print("Value: " + value)
Como vemos em u, para escrever um laço for para um dicionário,
devemos criar nomes para as duas variáveis que armazenarão a chave e o
valor de cada par chave-valor. Você pode escolher qualquer nome que
quiser para essas duas variáveis. Esse código também funcionaria bem se
usássemos abreviaturas para os nomes das variáveis, assim:
for k, v in user_0.items()
A segunda metade da instrução for em u inclui o nome do dicionário,
seguido do método items(), que devolve uma lista de pares chave-valor. O
laço for então armazena cada um desses pares nas duas variáveis
especificadas. No exemplo anterior, usamos as variáveis para exibir cada
chave (key) v, seguido do valor associado (value) w. O "n" na primeira
instrução print garante que uma linha em branco seja inserida antes de
cada par chave-valor na saída:
Key: last
Value: fermi
Key: first
Value: enrico
Key: username
Value: efermi
Observe novamente que os pares chave-valor não são devolvidos na
ordem em que foram armazenados, mesmo quando percorremos o
dicionário com um laço. Python não se importa com a ordem em que os
pares chave-valor são armazenados; ele só registra as conexões entre cada
chave individual e seu valor.
Percorrer todos os pares chave-valor com um laço funciona bem, em
particular, para dicionários como o do exemplo em favorite_languages.py,
que armazena o mesmo tipo de informação para várias chaves diferentes.
Se percorrermos o dicionário favorite_languages com um laço, teremos o
nome de cada pessoa no dicionário e sua linguagem de programação
favorita. Como as chaves sempre se referem ao nome de uma pessoa e o
valor é sempre uma linguagem, usaremos as variáveis name e language no
laço, em vez de key e value. Isso facilita entender o que está acontecendo:
favorite_languages.py
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
u for name, language in favorite_languages.items():
v print(name.title() + "'s favorite language is " +
language.title() + ".")
O código em u diz a Python para percorrer todos os pares chave-valor do
dicionário com um laço. À medida que cada par é tratado, a chave é
armazenada na variável name e o valor, na variável language. Esses nomes
descritivos fazem com que seja muito mais fácil ver o que a instrução print
em v faz.
Agora, com apenas algumas linhas de código, podemos exibir todas as
informações da enquete:
Jen's favorite language is Python.
Sarah's favorite language is C.
Phil's favorite language is Python.
Edward's favorite language is Ruby.
Esse tipo de laço funcionaria igualmente bem se nosso dicionário
armazenasse os resultados da enquete para mil ou até mesmo para um
milhão de pessoas.
Percorrendo todasas chaves de umdicionário comumlaço
O método keys() é conveniente quando não precisamos trabalhar com
todos os valores de um dicionário. Vamos percorrer o dicionário
favorite_languages com um laço e exibir os nomes de todos que
responderam à enquete:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
u for name in favorite_languages.keys():
print(name.title())
A linha em u diz a Python para extrair todas as chaves do dicionário
favorite_languages e armazená-las, uma de cada vez, na variável name. A
saída mostra os nomes de todos que participaram da enquete:
Jen
Sarah
Phil
Edward
Percorrer as chaves, na verdade, é o comportamento-padrão quando
percorremos um dicionário com um laço, portanto este código produzirá a
mesma saída se escrevêssemos:
for name in favorite_languages:
em vez de:
for name in favorite_languages.keys():
Você pode optar por usar o método keys() explicitamente se isso deixar
seu código mais fácil de ler, ou pode omiti-lo, se quiser.
Podemos acessar o valor associado a qualquer chave que nos interessar
no laço usando a chave atual. Vamos exibir uma mensagem a dois amigos
sobre as linguagens que eles escolheram. Percorreremos os nomes no
dicionário com um laço como fizemos antes, porém, quando o nome for de
um de nossos amigos, apresentaremos uma mensagem sobre sua
linguagem favorita:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
u friends = ['phil', 'sarah']
for name in favorite_languages.keys():
print(name.title())
v if name in friends:
print(" Hi " + name.title() +
", I see your favorite language is " +
w favorite_languages[name].title() + "!")
Em u criamos uma lista de amigos a quem queremos exibir uma
mensagem. No laço, exibimos o nome de cada pessoa. Então, em v,
verificamos se o nome com que estamos trabalhando (name) está na lista
friends. Se estiver, exibimos uma saudação especial, incluindo uma
referência à sua opção de linguagem. Para acessar a linguagem favorita em
w, usamos o nome do dicionário e o valor atual de name como chave. O
nome de todas as pessoas é exibido, porém nossos amigos recebem uma
mensagem especial:
Edward
Phil
Hi Phil, I see your favorite language is Python!
Sarah
Hi Sarah, I see your favorite language is C!
Jen
Você também pode usar o método keys() para descobrir se uma pessoa
em particular participou da enquete. Dessa vez, vamos ver se Erin
respondeu à enquete:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
u if 'erin' not in favorite_languages.keys():
print("Erin, please take our poll!")
O método keys() não serve apenas para laços: na verdade, ele devolve
uma lista de todas as chaves, e a linha em u simplesmente verifica se 'erin'
está nessa lista. Como ela não está, uma mensagem é exibida convidando-a
a participar da enquete:
Erin, please take our poll!
Percorrendo as chaves de umdicionário emordemusando umlaço
Um dicionário sempre mantém uma conexão clara entre cada chave e seu
valor associado, mas você não obterá os itens de um dicionário em uma
ordem previsível. Isso não é um problema, pois, geralmente, queremos
apenas obter o valor correto associado a cada chave.
Uma maneira de fazer os itens serem devolvidos em determinada
sequência é ordenar as chaves à medida que são devolvidas no laço for.
Podemos usar a função sorted() para obter uma cópia ordenada das
chaves:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
print(name.title() + ", thank you for taking the poll.")
Essa instrução for é como as outras instruções for, exceto que a função
sorted() está em torno do método dictionary.keys(). Isso diz a Python para
listar todas as chaves do dicionário e ordenar essa lista antes de percorrê-la
com um laço. A saída mostra os nomes de todos que responderam à
enquete, exibidos de forma ordenada:
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
Percorrendo todos osvalores de umdicionário comumlaço
Se você estiver mais interessado nos valores contidos em um dicionário, o
método values() pode ser usado para devolver uma lista de valores sem as
chaves. Por exemplo, suponha que queremos apenas uma lista de todas as
linguagens escolhidas em nossa enquete sobre linguagens de programação,
sem o nome da pessoa que escolheu cada linguagem:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
print(language.title())
A instrução for, nesse caso, extrai cada valor do dicionário e o armazena
na variável language. Quando esses valores são exibidos, temos uma lista de
todas as linguagens escolhidas:
The following languages have been mentioned:
Python
C
Python
Ruby
Essa abordagem extrai todos os valores do dicionário, sem verificar se há
repetições. Isso pode funcionar bem com uma quantidade pequena de
valores, mas em uma enquete com um número grande de entrevistados, o
resultado seria uma lista com muitas repetições. Para ver cada linguagem
escolhida sem repetições, podemos usar um conjunto (set). Um conjunto é
semelhante a uma lista, exceto que cada item de um conjunto deve ser
único:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
u for language in set(favorite_languages.values()):
print(language.title())
Quando colocamos set() em torno de uma lista que contenha itens
duplicados, Python identifica os itens únicos na lista e cria um conjunto a
partir desses itens. Em u usamos set() para extrair as linguagens únicas em
favorite_languages.values().
O resultado é uma lista de linguagens mencionadas pelas pessoas que
participaram da enquete, sem repetições:
The following languages have been mentioned:
Python
C
Ruby
À medida que continuar a conhecer Python, com frequência você
encontrará um recurso embutido na linguagem que o ajudará a fazer
exatamente o que quiser com seus dados.
FAÇA VOCÊ MESMO
6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um
laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de
instruções print por um laço que percorra as chaves e os valores do dicionário.
Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de
Python ao seu glossário. Ao executar seu programa novamente, essas palavras e
significados novos deverão ser automaticamente incluídos na saída.
6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que
cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre
pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem
favorita. Inclua alguns nomes que já estejam no dicionário e outros que não
estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem
respondido à enquete, mostre uma mensagem agradecendo-lhes por responder.
Se ainda não participaram da enquete, apresente uma mensagem convidando-as
a responder.
Informaçõesaninhadas
Às vezes, você vai querer armazenar um conjunto de dicionários em uma
lista ou uma lista de itens como um valor em um dicionário. Isso é
conhecido como aninhar informações. Podemos aninhar um conjunto de
dicionários em uma lista, uma lista de itens em um dicionário ou até
mesmo um dicionário em outro dicionário. Aninhar informações é um
recurso eficaz, como mostrarão os próximos exemplos.
Umalista de dicionários
O dicionário alien_0 contém várias informações sobre um alienígena, mas
não há espaço para armazenar informações sobre um segundo alienígena,
muito menos para uma tela cheia deles. Como podemos administrar uma
frota de alienígenas? Uma maneira é criar uma lista de alienígenas, em que
cada alienígena seja representado por um dicionário com informações
sobre ele. Por exemplo, o código a seguir cria uma lista com três
alienígenas:
aliens.py
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
u aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
print(alien)
Inicialmente criamos três dicionários, cada um representando um
alienígena diferente. Em u reunimos esses dicionários em uma lista
chamada aliens. Por fim, percorremos a lista com um laço e exibimos cada
alienígena:
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
Um exemplo mais realista envolveria mais de três alienígenas, com um
código que gere automaticamente cada alienígena. No exemplo a seguir,
usamos range() para criar uma frota de 30 alienígenas:
# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
u for alien_number in range(30):
v new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
w aliens.append(new_alien)
# Mostra os 5 primeiros alienígenas
x for alien in aliens[:5]:
print(alien)
print("...")
# Mostra quantos alienígenas foram criados
y print("Total number of aliens: " + str(len(aliens)))
Esse exemplo começa com uma lista vazia para armazenar todos os
alienígenas que serão criados. Em u range() devolve um conjunto de
números, que simplesmente diz a Python quantas vezes queremos que o
laço se repita. A cada vez que o laço é executado, criamos um novo
alienígena v e concatenamos cada novo alienígena à lista aliens w. Em x
usamos uma fatia para exibir os cinco primeiros alienígenas e, em seguida,
em y, exibimos o tamanho da lista para provar que realmente geramos a
frota completa com 30 alienígenas:
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
Total number of aliens: 30
Todos esses alienígenas têm as mesmas características, mas Python
considera cada um como um objeto diferente, o que nos permite modificar
cada alienígena individualmente.
Como podemos trabalhar com um conjunto de alienígenas como esse?
Suponha que um aspecto do jogo consista em fazer alguns alienígenas
mudarem de cor e moverem-se mais rápido à medida que o jogo
prosseguir. Quando for o momento de mudar de cor, podemos usar um
laço for e uma instrução if para alterar a cor dos alienígenas. Por exemplo,
para mudar os três primeiros alienígenas para amarelo, com velocidade
média, valendo dez pontos cada, podemos fazer o seguinte:
# Cria uma lista vazia para armazenar alienígenas
aliens = []
# Cria 30 alienígenas verdes
for alien_number in range (0,30):
new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
aliens.append(new_alien)
for alien in aliens[0:3]:
if alien['color'] == 'green':
alien['color'] = 'yellow'
alien['speed'] = 'medium'
alien['points'] = 10
# Mostra os 5 primeiros alienígenas
for alien in aliens[0:5]:
print(alien)
print("...")
Como queremos modificar os três primeiros alienígenas, percorremos
uma fatia que inclui apenas os três primeiros alienígenas. Todos os
alienígenas são verdes agora, mas isso nem sempre ocorrerá, portanto
escrevemos uma instrução if para garantir que estamos modificando
apenas os alienígenas verdes. Se o alienígena for verde, mudamos a cor
para 'yellow', a velocidade para 'medium' e o valor da pontuação para 10,
como vemos na saída a seguir:
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'medium', 'color': 'yellow', 'points': 10}
{'speed': 'slow', 'color': 'green', 'points': 5}
{'speed': 'slow', 'color': 'green', 'points': 5}
...
Poderíamos expandir esse laço acrescentando um bloco elif que
transforme alienígenas amarelos em alienígenas vermelhos e rápidos, que
valem 15 pontos cada. Sem mostrar o programa todo novamente, esse laço
teria o seguinte aspecto:
for alien in aliens[0:3]:
if alien['color'] == 'green':
alien['color'] = 'yellow'
alien['speed'] = 'medium'
alien['points'] = 10
elif alien['color'] == 'yellow':
alien['color'] = 'red'
alien['speed'] = 'fast'
alien['points'] = 15
É comum armazenar vários dicionários em uma lista quando cada
dicionário tiver diversos tipos de informação sobre um objeto. Por
exemplo, podemos criar um dicionário para cada usuário de um site, como
fizemos em user.py, e armazenar os dicionários individuais em uma lista
chamada users. Todos os dicionários da lista devem ter uma estrutura
idêntica para que possamos percorrer a lista com um laço e trabalhar com
cada objeto representado por um dicionário do mesmo modo.
Umalistaemumdicionário
Em vez de colocar um dicionário em uma lista, às vezes é conveniente
colocar uma lista em um dicionário. Por exemplo, considere como
podemos descrever uma pizza que alguém está pedindo. Se usássemos
apenas uma lista, tudo que poderíamos realmente armazenar é uma lista
dos ingredientes da pizza. Com um dicionário, uma lista de ingredientes
pode ser apenas um dos aspectos da pizza que estamos descrevendo.
No exemplo a seguir, dois tipos de informação são armazenados para
cada pizza: o tipo de massa e a lista de ingredientes. A lista de ingredientes
é um valor associado à chave 'toppings'. Para usar os itens da lista,
fornecemos o nome do dicionário e a chave 'toppings', como faríamos com
qualquer valor do dicionário. Em vez de devolver um único valor, teremos
uma lista de ingredientes:
pizza.py
# Armazena informações sobre uma pizza que está sendo pedida
u pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Resume o pedido
v print("You ordered a " + pizza['crust'] + "-crust pizza " +
"with the following toppings:")
w for topping in pizza['toppings']:
print("t" + topping)
Começamos em u com um dicionário que armazena informações sobre
uma pizza que está sendo pedida. Uma das chaves do dicionário é 'crust',
e o valor associado é a string 'thick'. A próxima chave, 'toppings', tem
como valor uma lista que armazena todos os ingredientes solicitados. Em v
resumimos o pedido antes de preparar a pizza. Para exibir os ingredientes,
escrevemos um laço for w. Para acessar a lista de ingredientes, usamos a
chave 'toppings', e Python obtém a lista de ingredientes do dicionário.
A saída a seguir oferece um resumo da pizza que planejamos preparar:
You ordered a thick-crust pizza with the following toppings:
mushrooms
extra cheese
Você pode aninhar uma lista em um dicionário sempre que quiser que
mais de um valor seja associado a uma única chave em um dicionário. No
exemplo anterior das linguagens de programação favoritas, se
armazenássemos as respostas de cada pessoa em uma lista, elas poderiam
escolher mais de uma linguagem predileta. Se percorrermos o dicionário
com um laço, o valor associado a cada pessoa será uma lista das
linguagens, e não uma única linguagem. No laço for do dicionário, usamos
outro laço for para percorrer a lista de linguagens associada a cada pessoa:
favorite_languages.py
u favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
v for name, languages in favorite_languages.items():
print("n" + name.title() + "'s favorite languages are:")
w for language in languages:
print("t" + language.title())
Como podemos ver em u, o valor associado a cada nome agora é uma
lista. Observe que algumas pessoas têm uma linguagem favorita, enquanto
outras têm várias. Quando percorremos o dicionário em v com um laço,
usamos uma variável de nome languages para armazenar cada valor do
dicionário, pois sabemos que esse valor será uma lista. No laço principal
do dicionário, usamos outro laço for w para percorrer a lista de linguagens
favoritas de cada pessoa. Agora cada pessoa pode listar quantas linguagens
favoritas quiser:
Jen's favorite languages are:
Python
Ruby
Sarah's favorite languages are:
C
Phil's favorite languages are:
Python
Haskell
Edward's favorite languages are:
Ruby
Go
Para aperfeiçoar mais ainda esse programa, podemos incluir uma
instrução if no início do laço for do dicionário para ver se cada pessoa tem
mais de uma linguagem favorita analisando o valor de len(languages). Se
uma pessoa tiver mais de uma linguagem favorita, a saída será a mesma. Se
ela tiver apenas uma linguagem predileta, poderíamos mudar a frase para
refletir esse fato. Por exemplo, você poderia dizer: Sarah's favorite
language is C.
NOTA Não aninhe listas e dicionários com muitos níveis de profundidade. Se estiver
aninhando itens com um nível de profundidade muito maior do que vimos nos
exemplos anteriores ou se estiver trabalhando com o código de outra pessoa, e
esse código tiver níveis significativos de informações aninhadas, é mais provável
que haja uma maneira mais simples de solucionar o problema existente.
Umdicionário emumdicionário
Podemos aninhar um dicionário em outro dicionário, mas o código poderá
ficar complicado rapidamente se isso for feito. Por exemplo, se você tiver
vários usuários em um site, cada um com um nome único, os nomes dos
usuários poderão ser usados como chaves em um dicionário. Você poderá
então armazenar informações sobre cada usuário usando um dicionário
como o valor associado a cada nome de usuário. Na listagem a seguir,
armazenamos três informações sobre cada usuário: seu primeiro nome, o
sobrenome e a localidade. Acessaremos essas informações percorrendo os
nomes dos usuários em um laço e o dicionário de informações associado a
cada nome de usuário:
many_users.py
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
},
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
},
}
u for username, user_info in users.items():
v print("nUsername: " + username)
w full_name = user_info['first'] + " " + user_info['last']
location = user_info['location']
x print("tFull name: " + full_name.title())
print("tLocation: " + location.title())
Inicialmente definimos um dicionário chamado users com duas chaves,
uma para cada um dos seguintes nomes de usuário: 'aeinstein' e 'mcurie'.
O valor associado a cada chave é um dicionário que inclui o primeiro
nome, o sobrenome e a localidade de cada usuário. Em u percorremos o
dicionário users com um laço. Python armazena cada chave na variável
username e o dicionário associado a cada nome de usuário na variável
user_info. Depois que entrarmos no laço principal do dicionário, exibimos
o nome do usuário em v.
Em w começamos a acessar o dicionário interno. A variável user_info,
que contém o dicionário com informações do usuário, tem três chaves:
'first', 'last' e 'location'. Usamos cada chave para gerar um nome
completo e a localidade formatados de modo elegante para cada pessoa x:
Username: aeinstein
Full name: Albert Einstein
Location: Princeton
Username: mcurie
Full name: Marie Curie
Location: Paris
Observe que a estrutura do dicionário de cada usuário é idêntica. Embora
Python não exija, essa estrutura facilita trabalhar com dicionários
aninhados. Se o dicionário de cada pessoa tivesse chaves diferentes, o
código no laço for seria mais complicado.
FAÇA VOCÊ MESMO
6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
(página 147). Crie dois novos dicionários que representem pessoas diferentes e
armazene os três dicionários em uma lista chamada people. Percorra sua lista de
pessoas com um laço. À medida que percorrer a lista, apresente tudo que você
sabe sobre cada pessoa.
6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada
dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o
tipo do animal e o nome do dono. Armazene esses dicionários em uma lista
chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer
isso, apresente tudo que você sabe sobre cada animal de estimação.
6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em
três nomes para usar como chaves do dicionário e armazene de um a três lugares
favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante,
peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o
dicionário com um laço e apresente o nome de cada pessoa e seus lugares
favoritos.
6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página
147) para que cada pessoa possa ter mais de um número favorito. Em seguida,
apresente o nome de cada pessoa, juntamente com seus números favoritos.
6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três
cidades como chaves em seu dicionário. Crie um dicionário com informações sobre
cada cidade e inclua o país em que a cidade está localizada, a população
aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade
devem ser algo como country, population e fact. Apresente o nome de cada
cidade e todas as informações que você armazenou sobre ela.
6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o
bastante para poderem ser estendidos de várias maneiras. Use um dos programas
de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores,
alterando o contexto do programa ou melhorando a formatação da saída.
Resumo
Neste capítulo aprendemos a definir um dicionário e a trabalhar com as
informações armazenadas nele. Vimos como acessar e modificar elementos
individuais de um dicionário e percorrer todas as suas informações com
um laço. Aprendemos a percorrer todos os pares chave-valor de um
dicionário, suas chaves e seus valores com um laço. Também vimos como
aninhar vários dicionários em uma lista, aninhar listas em um dicionário e
um dicionário em outro dicionário.
No próximo capítulo, conheceremos os laços while e veremos como
aceitar dados de entrada das pessoas que usarem seus programas. Será um
capítulo empolgante, pois você aprenderá a deixar todos os seus programas
interativos: eles serão capazes de responder a dados de entrada do usuário
A maioria dos programas é escrita para resolver o
problema de um usuário final. Para isso, geralmente
precisamos obter algumas informações do usuário. Como
exemplo simples, vamos supor que uma pessoa queira
descobrir se ela tem idade suficiente para votar. Se você
escrever um programa que responda a essa pergunta, será
necessário saber a idade do usuário antes de poder
oferecer uma resposta. O programa precisará pedir ao
usuário que forneça a idade, ou entre com ela; depois que
tiver esse dado de entrada, o programa poderá comparar
esse valor com a idade para votar a fim de determinar se o
usuário tem idade suficiente e então informar o resultado.
Neste capítulo aprenderemos a aceitar dados de entrada do usuário para
que seu programa possa então trabalhar com eles. Quando seu programa
precisar de um nome, você poderá solicitá-lo ao usuário. Quando precisar
de uma lista de nomes, você poderá pedir uma série de nomes ao usuário.
Para isso, usaremos a função input().
Também veremos como manter os programas executando pelo tempo
que os usuários quiserem, de modo que eles possam fornecer quantas
informações forem necessárias; em seguida, seu programa poderá trabalhar
com essas informações. Usaremos o laço while de Python para manter os
programas executando enquanto determinadas condições permanecerem
verdadeiras.
Com a capacidade de trabalhar com dados de entrada do usuário e
controlar o tempo que seus programas executam, você poderá escrever
programas totalmente interativos.
Como afunção input() trabalha
A função input() faz uma pausa em seu programa e espera o usuário
fornecer um texto. Depois que Python recebe a entrada do usuário, esse
dado é armazenado em uma variável para que você possa trabalhar com ele
de forma conveniente.
Por exemplo, o programa a seguir pede que o usuário forneça um texto e,
em seguida, exibe essa mensagem de volta ao usuário:
parrot.py
message = input("Tell me something, and I will repeat it back to you:
")
print(message)
A função input() aceita um argumento: o prompt – ou as instruções – que
queremos exibir ao usuário para que eles saibam o que devem fazer. Nesse
exemplo, quando Python executar a primeira linha, o usuário verá o
prompt Tell me something, and I will repeat it back to you: . O
programa espera enquanto o usuário fornece sua resposta e continua
depois que ele tecla ENTER. A resposta é armazenada na variável message;
depois disso, print(message) exibe a entrada de volta ao usuário:
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
NOTA O Sublime Text não executa programas que pedem uma entrada ao usuário.
Você pode usar o Sublime Text para escrever programas que solicitem uma
entrada, mas será necessário executar esses programas a partir de um terminal.
Consulte a seção “Executando programas Python a partir de um terminal”.
Escrevendo prompts claros
Sempre que usar a função input(), inclua um prompt claro, fácil de
compreender, que informe o usuário exatamente que tipo de informação
você procura. Qualquer frase que diga aos usuários o que eles devem
fornecer será apropriada. Por exemplo:
greeter.py
name = input("Please enter your name: ")
print("Hello, " + name + "!")
Acrescente um espaço no final de seus prompts (depois dos dois-pontos
no exemplo anterior) para separar o prompt da resposta do usuário e
deixar claro em que lugar o usuário deve fornecer seu texto. Por exemplo:
Please enter your name: Eric
Hello, Eric!
Às vezes, você vai querer escrever um prompt que seja maior que uma
linha. Por exemplo, talvez você queira explicar ao usuário por que está
pedindo determinada entrada. Você pode armazenar seu prompt em uma
variável e passá-la para a função input(). Isso permite criar seu prompt com
várias linhas e escrever uma instrução input() clara.
greeter.py
prompt = "If you tell us who you are, we can personalize the messages
you see."
prompt += "nWhat is your first name? "
name = input(prompt)
print("nHello, " + name + "!")
Esse exemplo mostra uma maneira de criar uma string multilinha. A
primeira linha armazena a parte inicial da mensagem na variável prompt. Na
segunda linha, o operador += acrescenta a nova string no final da string que
estava armazenada em prompt.
O prompt agora ocupa duas linhas, novamente, com um espaço após o
ponto de interrogação por questões de clareza:
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric
Hello, Eric!
Usando int() paraaceitarentradas numéricas
Se usarmos a função input(), Python interpretará tudo que o usuário
fornecer como uma string. Considere a sessão de interpretador a seguir,
que pergunta a idade do usuário:
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
O usuário digita o número 21, mas quando pedimos o valor de age,
Python devolve '21', que é a representação em string do valor numérico
fornecido. Sabemos que Python interpretou a entrada como uma string
porque o número agora está entre aspas. Se tudo que você quiser fazer é
exibir a entrada, isso funcionará bem. Entretanto, se tentar usar a entrada
como um número, você obterá um erro:
>>> age = input("How old are you? ")
How old are you? 21
u >>> age >= 18
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
v TypeError: unorderable types: str() >= int()
Quando tentamos usar a entrada para fazer uma comparação numérica u,
Python gera um erro, pois não é capaz de comparar uma string com um
inteiro: a string '21' armazenada em age não pode ser comparada ao valor
numérico 18 v.
Podemos resolver esse problema usando a função int(), que diz a Python
para tratar a entrada como um valor numérico. A função int() converte a
representação em string de um número em uma representação numérica,
como vemos a seguir:
>>> age = input("How old are you? ")
How old are you? 21
u >>> age = int(age)
>>> age >= 18
True
Nesse exemplo, quando fornecemos 21 no prompt, Python interpreta o
número como uma string, mas o valor é então convertido para uma
representação numérica por int() u. Agora Python pode executar o teste
condicional: comparar age (que contém o valor numérico 21) com 18 para
ver se age é maior ou igual a 18. Esse teste é avaliado como True.
Como podemos usar a função int() em um programa de verdade?
Considere um programa que determina se as pessoas têm altura suficiente
para andar em uma montanha-russa:
rollercoaster.py
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
print("nYou're tall enough to ride!")
else:
print("nYou'll be able to ride when you're a little older.")
O programa é capaz de comparar height com 36 porque height =
int(height) converte o valor de entrada em uma representação numérica
antes de fazer a comparação. Se o número fornecido for maior ou igual a
36, diremos ao usuário que sua altura é suficiente:
How tall are you, in inches? 71
You're tall enough to ride!
Quando usar uma entrada numérica para fazer cálculos e comparações,
lembre-se de converter o valor da entrada em uma representação numérica
antes.
Operador demódulo
Uma ferramenta útil para trabalhar com informações numéricas é o
operador de módulo (%), que divide um número por outro e devolve o resto:
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
O operador de módulo não diz quantas vezes um número cabe em outro;
ele simplesmente informa o resto.
Quando um número é divisível por outro, o resto é 0, portanto o
operador de módulo sempre devolve 0 nesse caso. Podemos usar esse fato
para determinar se um número é par ou ímpar:
even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd:
")
number = int(number)
if number % 2 == 0:
print("nThe number " + str(number) + " is even.")
else:
print("nThe number " + str(number) + " is odd.")
Números pares são sempre divisíveis por dois, portanto, se o módulo
entre um número e dois for zero (nesse caso, if number % 2 == 0), o número
será par. Caso contrário, será ímpar.
Enter a number, and I'll tell you if it's even or odd: 42
The number 42 is even.
Aceitando entradasemPython 2.7
Se você usa Python 2.7, utilize a função raw_input() quando pedir uma
entrada ao usuário. Essa função interpreta todas as entradas como uma
string, como faz input() em Python 3.
Python 2.7 também tem uma função input(), mas essa função interpreta
a entrada do usuário como código Python e tenta executá-la. No melhor
caso, você verá um erro informando que Python não é capaz de
compreender a entrada; no pior caso, executará um código que não
pretendia executar. Se estiver usando Python 2.7, utilize raw_input() no
lugar de input().
FAÇA VOCÊ MESMO
7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual
tipo de carro ele gostaria de alugar. Mostre uma mensagem sobre esse carro, por
exemplo, “Deixe-me ver se consigo um Subaru para você.”
7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário
quantas pessoas estão em seu grupo para jantar. Se a resposta for maior que oito,
exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso
contrário, informe que sua mesa está pronta.
7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
Introdução aos laços while
O laço for toma uma coleção de itens e executa um bloco de código uma
vez para cada item da coleção. Em comparação, o laço while executa
durante o tempo em que, ou enquanto, uma determinada condição for
verdadeira.
Laço whileemação
Podemos usar um laço while para contar uma série de números. Por
exemplo, o laço while a seguir conta de 1 a 5:
counting.py
current_number = 1
while current_number <= 5:
print(current_number)
current_number += 1
Na primeira linha começamos a contar de 1 ao definir o valor de
current_number com 1. O laço while é então configurado para continuar
executando enquanto o valor de current_number for menor ou igual a 5. O
código no laço exibe o valor current_number e então soma 1 a esse valor com
current_number += 1. (O operador += é um atalho para current_number =
current_number + 1.)
Python repete o laço enquanto a condição current_number <= 5 for
verdadeira. Como 1 é menor que 5, Python exibe 1 e então soma 1, fazendo
o número atual ser igual a 2. Como 2 é menor que 5, Python exibe 2 e soma
1 novamente, fazendo o número atual ser igual a 3, e assim sucessivamente.
Quando o valor de current_number for maior que 5, o laço para de executar
e o programa termina:
1
2
3
4
5
Os programas que você usa no dia a dia provavelmente contêm laços
while. Por exemplo, um jogo precisa de um laço while para continuar
executando enquanto você quiser jogar, e pode parar de executar assim
que você pedir para sair. Os programas não seriam divertidos se parassem
de executar antes que lhes disséssemos para parar ou se continuassem
executando mesmo depois que quiséssemos sair, portanto os laços while
são bem úteis.
Deixando o usuário decidir quando quer sair
Podemos fazer o programa parrot.py executar enquanto o usuário quiser
colocar a maior parte dele em um laço while. Definiremos um valor de
saída e então deixaremos o programa executando enquanto o usuário não
tiver fornecido o valor de saída:
parrot.py
u prompt = "nTell me something, and I will repeat it back to you:"
prompt += "nEnter 'quit' to end the program. "
v message = ""
w while message != 'quit':
message = input(prompt)
print(message)
Em u definimos um prompt que informa quais são as duas opções ao
usuário: fornecer uma mensagem ou o valor de saída (nesse caso, é 'quit').
Em seguida, preparamos uma variável message v para armazenar o valor que
o usuário fornecer. Definimos message como uma string vazia, "", de modo
que Python tenha algo para conferir na primeira vez que alcançar a linha
com while. Na primeira vez que o programa executar e Python alcançar a
instrução while, ele deverá comparar o valor de message com 'quit', mas o
usuário ainda não forneceu nenhuma entrada. Se Python não tiver nada
para comparar, ele não será capaz de continuar executando o programa.
Para resolver esse problema, garantimos que message receba um valor
inicial. Embora seja apenas uma string vazia, ela fará sentido para Python e
permitirá que a comparação que faz o laço while funcionar seja feita. Esse
laço while w executa enquanto o valor de message não for 'quit'.
Na primeira passagem pelo laço, message é apenas uma string vazia,
portanto Python entra no laço. Em message = input(prompt), Python exibe o
prompt e espera o usuário fornecer uma entrada. O que quer que seja
fornecido será armazenado em message e exibido; em seguida, Python avalia
novamente a condição na instrução while. Desde que o usuário não tenha
fornecido a palavra 'quit', o prompt será exibido novamente e Python
esperará mais entradas. Quando o usuário finalmente digitar 'quit',
Python para de executar o laço while e o programa termina:
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
Esse programa funciona bem, exceto que exibe a palavra 'quit' como se
fosse uma mensagem de verdade. Um teste if simples corrige esse
problema:
prompt = "nTell me something, and I will repeat it back to you:"
prompt += "nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
message = input(prompt)
if message != 'quit':
print(message)
Agora o programa faz uma verificação rápida antes de mostrar a
mensagem e só a exibirá se ela não for igual ao valor de saída:
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
Usando umaflag
No exemplo anterior, tínhamos um programa que executava determinadas
tarefas enquanto uma dada condição era verdadeira. E como ficaria em
programas mais complicados, em que muitos eventos diferentes poderiam
fazer o programa parar de executar?
Por exemplo, em um jogo, vários eventos diferentes podem encerrá-lo.
Quando o jogador ficar sem espaçonaves, seu tempo se esgotar ou as
cidades que ele deveria proteger forem todas destruídas, o jogo deverá
terminar. O jogo termina se qualquer um desses eventos ocorrer. Se muitos
eventos possíveis puderem ocorrer para o programa terminar, tentar testar
todas essas condições em uma única instrução while torna-se complicado e
difícil.
Para um programa que deva executar somente enquanto muitas
condições forem verdadeiras, podemos definir uma variável que determina
se o programa como um todo deve estar ativo. Essa variável, chamada de
flag, atua como um sinal para o programa. Podemos escrever nossos
programas de modo que executem enquanto a flag estiver definida com
True e parem de executar quando qualquer um dos vários eventos definir o
valor da flag com False. Como resultado, nossa instrução while geral
precisa verificar apenas uma condição: se a flag, no momento, é True.
Então todos os nossos demais testes (para ver se um evento que deve
definir a flag com False ocorreu) podem estar bem organizados no restante
do programa.
Vamos adicionar uma flag em parrot.py, que vimos na seção anterior.
Essa flag, que chamaremos de active (embora você possa lhe dar o nome
que quiser), controlará se o programa deve ou não continuar executando:
prompt = "nTell me something, and I will repeat it back to you:"
prompt += "nEnter 'quit' to end the program. "
u active = True
v while active:
message = input(prompt)
w if message == 'quit':
active = False
x else:
print(message)
Definimos a variável active com True u para que o programa comece em
um estado ativo. Fazer isso simplifica a instrução while, pois nenhuma
comparação é feita nessa instrução; a lógica é tratada em outras partes do
programa. Enquanto a variável active permanecer True, o laço continuará a
executar v.
Na instrução if contida no laço while, verificamos o valor de message
depois que o usuário fornece sua entrada. Se o usuário fornecer 'quit' w,
definimos active com False e o laço while é encerrado. Se o usuário
fornecer outro dado que não seja 'quit' x, exibimos essa entrada como
uma mensagem.
Esse programa gera a mesma saída do exemplo anterior, em que
havíamos colocado o teste condicional diretamente na instrução while.
Porém, agora que temos uma flag para indicar se o programa como um
todo está em um estado ativo, será mais fácil acrescentar outros testes (por
exemplo, instruções elif) para eventos que devam fazer active se tornar
False. Isso é útil em programas complicados, como jogos, em que pode
haver muitos eventos, e qualquer um deles poderia fazer o programa parar
de executar. Quando um desses eventos fizer a flag active se tornar False, o
laço principal do jogo terminará, uma mensagem de Game Over poderia
ser exibida e o jogador poderia ter a opção de jogar novamente.
Usando break parasair de umlaço
Para sair de um laço while de imediato, sem executar qualquer código
restante no laço, independentemente do resultado de qualquer teste
condicional, utilize a instrução break. A instrução break direciona o fluxo
de seu programa; podemos usá-la para controlar quais linhas de código são
ou não são executadas, de modo que o programa execute apenas o código
que você quiser, quando você quiser.
Por exemplo, considere um programa que pergunte aos usuários os
nomes de lugares que eles já visitaram. Podemos interromper o laço while
nesse programa chamando break assim que o usuário fornecer o valor
'quit':
cities.py
prompt = "nPlease enter the name of a city you have visited:"
prompt += "n(Enter 'quit' when you are finished.) "
u while True:
city = input(prompt)
if city == 'quit':
break
else:
print("I'd love to go to " + city.title() + "!")
Um laço que comece com while True u executará indefinidamente, a
menos que alcance uma instrução break. O laço desse programa
continuará pedindo aos usuários para que entrem com os nomes das
cidades em que eles estiveram até que 'quit' seja fornecido. Quando 'quit'
for digitado, a instrução break é executada, fazendo Python sair do laço:
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
NOTA Você pode usar a instrução break em qualquer laço de Python. Por exemplo,
break pode ser usado para sair de um laço for que esteja percorrendo uma lista
ou um dicionário.
Usando continueemumlaço
Em vez de sair totalmente de um laço sem executar o restante de seu
código, podemos usar a instrução continue para retornar ao início, com
base no resultado de um teste condicional. Por exemplo, considere um laço
que conte de 1 a 10, mas apresente apenas os números ímpares desse
intervalo:
counting.py
current_number = 0
while current_number < 10:
u current_number += 1
if current_number % 2 == 0:
continue
print(current_number)
Inicialmente, definimos current_number com 0. Como esse valor é menor
que 10, Python entra no laço while. Uma vez no laço, incrementamos o
contador de 1 em u, portanto current_number passa a ser 1. A instrução if
então verifica o módulo entre current_number e 2. Se o módulo for 0 (o que
significa que current_number é divisível por 2), a instrução continue diz a
Python para ignorar o restante do laço e voltar ao início. Se o número atual
não for divisível por 2, o restante do laço será executado e Python exibirá o
número atual:
1
3
5
7
9
Evitando loops infinitos
Todo laço while precisa de uma maneira de interromper a execução para
que não continue executando indefinidamente. Por exemplo, o laço a
seguir deve fazer a contagem de 1 a 5:
counting.py
x = 1
while x <= 5:
print(x)
x += 1
Contudo, se você omitir a linha x += 1 (como vemos a seguir) por
acidente, o laço executará para sempre:
# Esse laço executa indefinidamente!
x = 1
while x <= 5:
print(x)
Agora o valor de x começará em 1, mas jamais será modificado. Como
resultado, o teste condicional x <= 5 será sempre avaliado como True e o
laço while executará indefinidamente, exibindo uma série de 1s, assim:
1
1
1
1
--trecho omitido--
Todo programador escreve ocasionalmente um loop infinito (ou laço
infinito) com while por acidente, em especial quando os laços do programa
tiverem condições de saída sutis. Se seu programa ficar preso em um loop
infinito, tecle CTRL-C ou simplesmente feche a janela do terminal que está
exibindo a saída de seu programa.
Para evitar escrever loops infinitos, teste todos os laços while e certifique￾se de que eles serão encerrados conforme esperado. Se quiser que seu
programa termine quando o usuário fornecer determinado valor de
entrada, execute o programa e forneça esse valor. Se o programa não
terminar, analise cuidadosamente o modo como seu programa trata o valor
que deveria fazer o laço parar. Garanta que pelo menos uma parte do
programa possa fazer a condição do laço ser False ou fazer uma instrução
break ser alcançada.
NOTA Alguns editores, como o Sublime Text, tem uma janela de saída incluída. Isso
pode dificultar a interrupção de um loop infinito, e talvez seja necessário fechar
o editor para encerrar o laço.
FAÇA VOCÊ MESMO
7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
7.5 – Ingressos para o cinema: Um cinema cobra preços diferentes para os
ingressos de acordo com a idade de uma pessoa. Se uma pessoa tiver menos de 3
anos de idade, o ingresso será gratuito; se tiver entre 3 e 12 anos, o ingresso
custará 10 dólares; se tiver mais de 12 anos, o ingresso custará 15 dólares.
Escreva um laço em que você pergunte a idade aos usuários e, então, informe-lhes
o preço do ingresso do cinema.
7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício 7.5
que faça o seguinte, pelo menos uma vez:
• use um teste condicional na instrução while para encerrar o laço;
• use uma variável active para controlar o tempo que o laço executará;
• use uma instrução break para sair do laço quando o usuário fornecer o valor
'quit'.
7.7 – Infinito: Escreva um laço que nunca termine e execute-o. (Para encerrar o
laço, pressione CTRL-C ou feche a janela que está exibindo a saída.)
Usando umlaço whilecomlistase dicionários
Até agora trabalhamos com apenas uma informação do usuário a cada vez.
Recebemos a entrada do usuário e então a exibimos ou apresentamos uma
resposta a ela. Na próxima passagem pelo laço while, recebíamos outro
valor de entrada e respondíamos a ela. Contudo, para controlar muitos
usuários e informações, precisaremos usar listas e dicionários com nossos
laços while.
Um laço for é eficiente para percorrer uma lista, mas você não deve
modificar uma lista em um laço for, pois Python terá problemas para
manter o controle dos itens da lista. Para modificar uma lista enquanto
trabalhar com ela, utilize um laço while. Usar laços while com listas e
dicionários permite coletar, armazenar e organizar muitas entradas a fim de
analisá-las e apresentá-las posteriormente.
Transferindo itens de umalista para outra
Considere uma lista de usuários recém-registrados em um site, porém não
verificados. Depois de conferir esses usuários, como podemos transferi-los
para uma lista separada de usuários confirmados? Uma maneira seria usar
um laço while para extrair os usuários da lista de usuários não confirmados
à medida que os verificarmos e então adicioná-los em uma lista separada
de usuários confirmados. Esse código pode ter o seguinte aspecto:
confirmed_users.py
# Começa com os usuários que precisam ser verificados,
# e com uma lista vazia para armazenar os usuários confirmados
u unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários
confirmados
v while unconfirmed_users:
w current_user = unconfirmed_users.pop()
print("Verifying user: " + current_user.title())
x confirmed_users.append(current_user)
# Exibe todos os usuários confirmados
print("nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
print(confirmed_user.title())
Começamos com uma lista de usuários não confirmados em u (Alice,
Brian e Candace) e uma lista vazia para armazenar usuários confirmados.
O laço while em v executa enquanto a lista unconfirmed_users não estiver
vazia. Nesse laço, a função pop() em w remove os usuários não verificados,
um de cada vez, do final de unconfirmed_users. Nesse caso, como Candace é
o último elemento da lista unconfirmed_users, seu nome será o primeiro a
ser removido, armazenado em current_user e adicionado à lista
confirmed_users em x. O próximo é Brian e, depois, Alice.
Simulamos a confirmação de cada usuário exibindo uma mensagem de
verificação e então adicionando-os à lista de usuários confirmados. À
medida que a lista de usuários não confirmados diminui, a lista de usuários
confirmados aumenta. Quando a lista de usuários não confirmados estiver
vazia, o laço para e a lista de usuários confirmados é exibida:
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice
The following users have been confirmed:
Candace
Brian
Alice
Removendo todasas instâncias devaloresespecíficos de umalista
No Capítulo 3 usamos remove() para remover um valor específico de uma
lista. A função remove() era apropriada porque o valor em que estávamos
interessados aparecia apenas uma vez na lista. Porém, e se quiséssemos
remover da lista todas as instâncias de um valor?
Suponha que tenhamos uma lista de animais de estimação com o valor
'cat' repetido várias vezes. Para remover todas as instâncias desse valor,
podemos executar um laço while até 'cat' não estar mais na lista, como
vemos aqui:
pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
pets.remove('cat')
print(pets)
Começamos com uma lista contendo várias instâncias de 'cat'. Após
exibir a lista, Python entra no laço while, pois encontra o valor 'cat' na
lista pelo menos uma vez. Depois que entrar no laço, Python remove a
primeira instância de 'cat', retorna à linha while e então entra novamente
no laço quando descobre que 'cat' ainda está na lista. Cada instância de
'cat' é removida até que esse valor não esteja mais na lista; nesse
momento, Python sai do laço e exibe a lista novamente:
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
Preenchendo umdicionário comdados deentrada do usuário
Podemos pedir a quantidade de entrada que for necessária a cada passagem
por um laço while. Vamos criar um programa de enquete em que cada
passagem pelo laço solicita o nome do participante e uma resposta.
Armazenaremos os dados coletados em um dicionário, pois queremos
associar cada resposta a um usuário em particular:
mountain_poll.py
responses = {}
# Define uma flag para indicar que a enquete está ativa
polling_active = True
while polling_active:
# Pede o nome da pessoa e a resposta
u name = input("nWhat is your name? ")
response = input("Which mountain would you like to climb someday?
")
# Armazena a resposta no dicionário
v responses[name] = response
# Descobre se outra pessoa vai responder à enquete
w repeat = input("Would you like to let another person respond? (yes/
no) ")
if repeat == 'no':
polling_active = False
# A enquete foi concluída. Mostra os resultados
print("n--- Poll Results ---")
x for name, response in responses.items():
print(name + " would like to climb " + response + ".")
O programa inicialmente define um dicionário vazio (responses) e cria
uma flag (polling_active) para indicar que a enquete está ativa. Enquanto
polling_active for True, Python executará o código que está no laço while.
Nesse laço é solicitado ao usuário que entre com seu nome e uma
montanha que gostaria de escalar u. Essa informação é armazenada no
dicionário responses v, e uma pergunta é feita ao usuário para saber se ele
quer que a enquete continue w. Se o usuário responder yes, o programa
entrará no laço while novamente. Se responder no, a flag polling_active será
definida com False, o laço while para de executar e o último bloco de
código em x exibe o resultado da enquete.
Se executar esse programa e fornecer exemplos de respostas, você deverá
ver uma saída como esta:
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes
What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no
--- Poll Results ---
Lynn would like to climb Devil's Thumb.
Eric would like to climb Denali.
FAÇA VOCÊ MESMO
7.8 – Lanchonete: Crie uma lista chamada sandwich_orders e a preencha com os
nomes de vários sanduíches. Em seguida, crie uma lista vazia chamada
finished_sandwiches. Percorra a lista de pedidos de sanduíches com um laço e
mostre uma mensagem para cada pedido, por exemplo, Preparei seu sanduíche
de atum. À medida que cada sanduíche for preparado, transfira-o para a lista de
sanduíches prontos. Depois que todos os sanduíches estiverem prontos, mostre uma
mensagem que liste cada sanduíche preparado.
7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um laço
while para remover todas as ocorrências de 'pastrami' e sandwich_orders.
Garanta que nenhum sanduíche de pastrami acabe em finished_sandwiches.
7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se pudesse
visitar um lugar do mundo, para onde você iria? Inclua um bloco de código que
apresente os resultados da enquete.
Resumo
Neste capítulo aprendemos a usar input() para permitir que os usuários
forneçam suas próprias informações em seus programas. Vimos como
trabalhar com entradas tanto textuais quanto numéricas e a usar laços
while para deixar seus programas executarem pelo tempo que os usuários
quiserem. Conhecemos várias maneiras de controlar o fluxo de um laço
while: definindo uma flag active, usando a instrução break e com a
instrução continue. Aprendemos a usar um laço while para transferir itens
de uma lista para outra e vimos como remover todas as instâncias de um
valor de uma lista. Também vimos como laços while podem ser usados
com dicionários.
No Capítulo 8, conheceremos as funções. As funções permitem dividir
seus programas em partes menores, cada uma fazendo uma tarefa
específica. Podemos chamar uma função quantas vezes quisermos e
armazená-las em arquivos separados. Ao usar funções, podemos escrever
códigos mais eficientes, em que seja mais fácil resolver problemas e dar
manutenção, com possibilidade de serem reutilizados em vários programas
diferentes.
8
FUNÇÕES
Neste capítulo aprenderemos a escrever funções, que são
blocos de código nomeados, concebidos para realizar
uma tarefa específica. Quando queremos executar uma
tarefa em particular, definida em uma função, chamamos
o nome da função responsável por ela. Se precisar
executar essa tarefa várias vezes durante seu programa,
não será necessário digitar todo o código para a mesma
tarefa repetidamente: basta chamar a função dedicada ao
tratamento dessa tarefa e a chamada dirá a Python para
executar o código da função. Você perceberá que usar
funções permite escrever, ler, testar e corrigir seus
programas de modo mais fácil.
Neste capítulo também veremos maneiras de passar informações às
funções. Aprenderemos a escrever determinadas funções cuja tarefa
principal seja exibir informações e outras funções que visam a processar
dados e devolver um valor ou um conjunto de valores. Por fim, veremos
como armazenar funções em arquivos separados, chamados de módulos,
para ajudar a organizar os arquivos principais de seu programa.
Definindo umafunção
Eis uma função simples chamada greet_user() que exibe uma saudação:
greeter.py
u def greet_user():
v Exibe uma saudação simples.
w print("Hello!")
x greet_user()
Esse exemplo mostra a estrutura mais simples possível para uma função.
A linha em u utiliza a palavra reservada def para informar Python que
estamos definindo uma função. Essa é a definição da função, que informa o
nome da função a Python e, se for aplicável, quais são os tipos de
informação necessários à função para que ela faça sua tarefa. Os parênteses
contêm essa informação. Nesse caso, o nome da função é greet_user(), e
ela não precisa de nenhuma informação para executar sua tarefa, portanto
os parênteses estão vazios. (Mesmo assim, eles são obrigatórios.) Por fim, a
definição termina com dois-pontos.
Qualquer linha indentada após def greet_user(): faz parte do corpo da
função. O texto em v é um comentário chamado docstring, que descreve o
que a função faz. As docstrings são colocadas entre aspas triplas, que
Python procura quando gera a documentação das funções de seus
programas.
A linha print("Hello!") w é a única linha com código propriamente dito
no corpo dessa função, portanto greet_user() realiza apenas uma tarefa:
print("Hello!").
Quando quiser usar essa função, você deve chamá-la. Uma chamada de
função diz a Python para executar o código da função. Para chamar uma
função, escreva o nome dela, seguido de qualquer informação necessária
entre parênteses, como vemos em x. Como nenhuma informação é
necessária nesse caso, chamar nossa função é simples e basta fornecer
greet_user(). Como esperado, ela exibe Hello!:
Hello!
Passando informações para umafunção
Se for um pouco modificada, a função greet_user() não só pode dizer
Hello! ao usuário como também pode saudá-lo pelo nome. Para que a
função faça isso, especifique username entre os parênteses da definição da
função em def greet_user(). Ao acrescentar username aqui, permitimos que
a função aceite qualquer valor que você especificar para username. A função
agora espera que um valor seja fornecido para username sempre que ela for
chamada. Ao chamar greet_user(), você poderá lhe passar um nome, por
exemplo, 'jesse', entre parênteses:
def greet_user(username):
Exibe uma saudação simples.
print("Hello, " + username.title() + "!")
greet_user('jesse')
Usar greet_user('jesse') faz greet_user() ser chamada e fornece as
informações de que a função precisa para executar a instrução print. A
função aceita o nome que você passar e exibe a saudação para esse nome:
Hello, Jesse!
De modo semelhante, usar greet_user('sarah') chama greet_user(), passa
'sarah' a essa função e exibe Hello, Sarah!. Você pode chamar greet_user()
quantas vezes quiser e lhe passar qualquer nome desejado de modo a gerar
sempre uma saída previsível.
Argumentose parâmetros
Na função greet_user() anterior, definimos greet_user() para que exija um
valor para a variável username. Depois que chamamos a função e lhe
fornecemos a informação (o nome de uma pessoa), a saudação correta foi
exibida.
A variável username na definição de greet_user() é um exemplo de
parâmetro – uma informação de que a função precisa para executar sua
tarefa. O valor 'jesse' em greet_user('jesse') é um exemplo de
argumento. Um argumento é uma informação passada para uma função em
sua chamada. Quando chamamos a função, colocamos entre parênteses o
valor com que queremos que a função trabalhe. Nesse caso, o argumento
'jesse' foi passado para a função greet_user() e o valor foi armazenado no
parâmetro username.
NOTA Às vezes, as pessoas falam de argumentos e parâmetros de modo indistinto.
Não fique surpreso se vir as variáveis de uma definição de função serem
referenciadas como argumentos, ou as variáveis de uma chamada de função
serem chamadas de parâmetros.
FAÇA VOCÊ MESMO
8.1 – Mensagem: Escreva uma função chamada display_message() que mostre
uma frase informando a todos o que você está aprendendo neste capítulo. Chame
a função e certifique-se de que a mensagem seja exibida corretamente.
8.2 – Livro favorito: Escreva uma função chamada favorite_book() que aceite
um parâmetro title. A função deve exibir uma mensagem como Um dos meus
livros favoritos é Alice no país das maravilhas. Chame a função e não
se esqueça de incluir o título do livro como argumento na chamada da função.
Passando argumentos
Pelo fato de ser possível que uma definição de função tenha vários
parâmetros, uma chamada de função pode precisar de diversos
argumentos. Os argumentos podem ser passados para as funções de várias
maneiras. Podemos usar argumentos posicionais, que devem estar na
mesma ordem em que os parâmetros foram escritos, argumentos nomeados
(keyword arguments), em que cada argumento é constituído de um nome
de variável e de um valor, ou por meio de listas e dicionários de valores.
Vamos analisar cada um deles.
Argumentos posicionais
Quando chamamos uma função, Python precisa fazer a correspondência
entre cada argumento da chamada da função e um parâmetro da definição.
A maneira mais simples de fazer isso é contar com a ordem dos argumentos
fornecidos. Valores cuja correspondência seja feita dessa maneira são
chamados de argumentos posicionais.
Para ver como isso funciona considere uma função que apresente
informações sobre animais de estimação. A função nos informa o tipo de
cada animal de estimação e o nome dele, como vemos aqui:
pets.py
u def describe_pet(animal_type, pet_name):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
v describe_pet('hamster', 'harry')
A definição mostra que essa função precisa de um tipo de animal e de seu
nome u. Quando chamamos describe_pet(), devemos fornecer o tipo do
animal e um nome, nessa ordem. Por exemplo, na chamada da função, o
argumento 'hamster' é armazenado no parâmetro animal_type e o
argumento 'harry' é armazenado no parâmetro pet_name v. No corpo da
função, esses dois parâmetros são usados para exibir informações sobre o
animal de estimação descrito.
A saída apresenta um hamster chamado Harry:
I have a hamster.
My hamster's name is Harry.
Várias chamadas defunção
Podemos chamar uma função quantas vezes forem necessárias. Descrever
um segundo animal de estimação diferente exige apenas mais uma
chamada a describe_pet():
def describe_pet(animal_type, pet_name):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
Nessa segunda chamada da função, passamos os argumentos 'dog' e
'willie' a describe_pet(). Assim como no conjunto anterior de argumentos
que usamos, Python faz a correspondência entre 'dog' e o parâmetro
animal_type e entre 'willie' e o parâmetro pet_name. Como antes, a função
faz sua tarefa, porém, dessa vez, exibe valores para um cachorro chamado
Willie. Agora temos um hamster chamado Harry e um cachorro chamado
Willie:
I have a hamster.
My hamster's name is Harry.
I have a dog.
My dog's name is Willie.
Chamar uma função várias vezes é uma maneira eficiente de trabalhar. O
código que descreve um animal de estimação é escrito uma só vez na
função. Então, sempre que quiser descrever um novo animal de estimação,
podemos chamar a função com as informações sobre esse animal. Mesmo
que o código para descrever um animal de estimação fosse expandido
atingindo dez linhas, poderíamos ainda descrever um novo animal de
estimação chamando a função novamente com apenas uma linha.
Podemos usar tantos argumentos posicionais quantos forem necessários
nas funções. Python trabalha com os argumentos fornecidos na chamada
da função e faz a correspondência de cada um com o parâmetro associado
na definição da função.
A ordeméimportanteemargumentos posicionais
Podemos obter resultados inesperados se confundirmos a ordem dos
argumentos em uma chamada de função quando argumentos posicionais
forem usados:
def describe_pet(animal_type, pet_name):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')
Nessa chamada de função, listamos primeiro o nome e depois o tipo do
animal. Como dessa vez o argumento 'harry' foi definido antes, esse valor
é armazenado no parâmetro animal_type. De modo semelhante, 'hamster' é
armazenado em pet_name. Agora temos um “harry” chamado “Hamster”:
I have a harry.
My harry's name is Hamster.
Se obtiver resultados engraçados como esse, verifique se a ordem dos
argumentos em sua chamada de função corresponde à ordem dos
parâmetros na definição da função.
Argumentos nomeados
Um argumento nomeado (keyword argument) é um par nome-valor
passado para uma função. Associamos diretamente o nome e o valor no
próprio argumento para que não haja confusão quando ele for passado
para a função (você não acabará com um harry chamado Hamster).
Argumentos nomeados fazem com que você não precise se preocupar com
a ordem correta de seus argumentos na chamada da função e deixam claro
o papel de cada valor na chamada.
Vamos reescrever pets.py usando argumentos nomeados para chamar
describe_pet():
def describe_pet(animal_type, pet_name):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')
A função describe_pet() não mudou. Entretanto, quando chamamos a
função, dizemos explicitamente a Python a qual parâmetro cada
argumento deve corresponder. Quando Python lê a chamada da função, ele
sabe que deve armazenar o argumento 'hamster' no parâmetro animal_type
e o argumento 'harry' em pet_name. A saída mostra corretamente que
temos um hamster chamado Harry.
A ordem dos argumentos nomeados não importa, pois Python sabe o que
é cada valor. As duas chamadas de função a seguir são equivalentes:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
NOTA Quando usar argumentos nomeados, lembre-se de usar os nomes exatos dos
parâmetros usados na definição da função.
Valores default
Ao escrever uma função, podemos definir um valor default para cada
parâmetro. Se um argumento para um parâmetro for especificado na
chamada da função, Python usará o valor desse argumento. Se não for, o
valor default do parâmetro será utilizado. Portanto, se um valor default for
definido para um parâmetro, você poderá excluir o argumento
correspondente, que normalmente seria especificado na chamada da
função. Usar valores default pode simplificar suas chamadas de função e
deixar mais claro o modo como suas funções normalmente são utilizadas.
Por exemplo, se perceber que a maioria das chamadas a describe_pet() é
usada para descrever cachorros, você pode definir o valor default de
animal_type com 'dog'. Agora qualquer pessoa que chamar describe_pet()
para um cachorro poderá omitir essa informação:
def describe_pet(pet_name, animal_type='dog'):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
Mudamos a definição de describe_pet() para incluir um valor default
igual a 'dog' para animal_type. A partir de agora, quando a função for
chamada sem um animal_type especificado, Python saberá que deve usar o
valor 'dog' para esse parâmetro:
I have a dog.
My dog's name is Willie.
Observe que a ordem dos parâmetros na definição da função precisou ser
alterada. Como o uso do valor default faz com que não seja necessário
especificar um tipo de animal como argumento, o único argumento
restante na chamada da função é o nome do animal de estimação. Python
continua interpretando esse valor como um argumento posicional,
portanto, se a função for chamada somente com o nome de um animal de
estimação, esse argumento corresponderá ao primeiro parâmetro listado na
definição da função. Esse é o motivo pelo qual o primeiro parâmetro deve
ser pet_name.
O modo mais simples de usar essa função agora é fornecer apenas o
nome de um cachorro na chamada da função:
describe_pet('willie')
Essa chamada de função produzirá a mesma saída do exemplo anterior.
O único argumento fornecido é 'willie', portanto ele é associado ao
primeiro parâmetro da definição da função, que é pet_name. Como nenhum
argumento foi fornecido para animal_type, Python usa o valor default, que é
'dog'.
Para descrever um animal que não seja um cachorro, uma chamada de
função como esta pode ser usada:
describe_pet(pet_name='harry', animal_type='hamster')
Como um argumento explícito para animal_type foi especificado, Python
ignorará o valor default do parâmetro.
NOTA Ao usar valores default, qualquer parâmetro com um valor desse tipo deverá
ser listado após todos os parâmetros que não tenham valores default. Isso
permite que Python continue a interpretar os argumentos posicionais
corretamente.
Chamadas defunção equivalentes
Como os argumentos posicionais, os argumentos nomeados e os valores
default podem ser usados em conjunto, e com frequência você terá várias
maneiras equivalentes de chamar uma função. Considere a definição a
seguir de describe_pets() com um valor default especificado:
def describe_pet(pet_name, animal_type='dog'):
Com essa definição, um argumento sempre deverá ser fornecido para
pet_name e esse valor pode ser especificado por meio do formato posicional
ou nomeado. Se o animal descrito não for um cachorro, um argumento
para animal_type deverá ser incluído na chamada, e esse argumento
também pode ser especificado com o formato posicional ou nomeado.
Todas as chamadas a seguir serão adequadas a essa função:
# Um cachorro chamado Willie
describe_pet('willie')
describe_pet(pet_name='willie')
# Um hamster chamado Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
Cada uma dessas chamadas de função produzirá a mesma saída dos
exemplos anteriores.
NOTA O estilo de chamada que você usar realmente não importa. Desde que suas
chamadas de função gerem a saída desejada, basta usar o estilo que achar mais
fácil de entender.
Evitando errosemargumentos
Quando começar a usar funções, não se surpreenda se você se deparar com
erros sobre argumentos sem correspondência. Argumentos sem
correspondência ocorrem quando fornecemos menos ou mais argumentos
necessários à função para que ela realize sua tarefa. Por exemplo, eis o que
acontece se tentarmos chamar describe_pet() sem argumentos:
def describe_pet(animal_type, pet_name):
Exibe informações sobre um animal de estimação.
print("nI have a " + animal_type + ".")
print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet()
Python reconhece que algumas informações estão faltando na chamada
da função e o traceback nos informa quais são:
Traceback (most recent call last):
u File "pets.py", line 6, in <module>
v describe_pet()
w TypeError: describe_pet() missing 2 required positional arguments:
'animal_
type' and 'pet_name'
Em u o traceback nos informa em que local está o problema, o que nos
permite olhar o código novamente e ver que algo deu errado em nossa
chamada de função. Em v a chamada de função causadora do problema é
apresentada. Em w o traceback nos informa que há dois argumentos
ausentes na chamada da função e mostra o nome desses argumentos. Se
essa função estivesse em um arquivo separado, provavelmente poderíamos
reescrever a chamada de forma correta sem precisar abrir esse arquivo e ler
o código da função.
Python nos ajuda lendo o código da função e informando os nomes dos
argumentos que devemos fornecer. Esse é outro motivo para dar nomes
descritivos às suas variáveis e funções. Se fizer isso, as mensagens de erro
de Python serão mais úteis para você e para qualquer pessoa que possa
usar o seu código.
Se você fornecer argumentos demais, deverá obter um traceback
semelhante, que poderá ajudá-lo a fazer uma correspondência correta entre
a chamada da função e sua definição.
FAÇA VOCÊ MESMO
8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A
função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem
estampada.
Chame a função uma vez usando argumentos posicionais para criar uma
camiseta. Chame a função uma segunda vez usando argumentos nomeados.
8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta de
qualquer tamanho com uma mensagem diferente.
8.5 – Cidades: Escreva uma função chamada describe_city() que aceite o
nome de uma cidade e seu país. A função deve exibir uma frase simples, como
Reykjavik está localizada na Islândia. Forneça um valor default ao
parâmetro que representa o país. Chame sua função para três cidades diferentes
em que pelo menos uma delas não esteja no país default.
Valores deretorno
Uma função nem sempre precisa exibir sua saída diretamente. Em vez
disso, ela pode processar alguns dados e então devolver um valor ou um
conjunto de valores. O valor devolvido pela função é chamado de valor de
retorno. A instrução return toma um valor que está em uma função e o
envia de volta à linha que a chamou. Valores de retorno permitem passar
boa parte do trabalho pesado de um programa para funções, o que pode
simplificar o corpo de seu programa.
Devolvendo umvalor simples
Vamos observar uma função que aceite um primeiro nome e um
sobrenome e devolva um nome completo formatado de modo elegante:
formatted_name.py
u def get_formatted_name(first_name, last_name):
Devolve um nome completo formatado de modo elegante.
v full_name = first_name + ' ' + last_name
w return full_name.title()
x musician = get_formatted_name('jimi', 'hendrix')
print(musician)
A definição de get_formatted_name() aceita um primeiro nome e um
sobrenome u como parâmetros. A função combina esses dois nomes,
acrescenta um espaço entre eles e armazena o resultado em full_name v. O
valor de full_name é convertido para que tenha letras iniciais maiúsculas e é
devolvido para a linha que fez a chamada em w.
Quando chamamos uma função que devolve um valor, precisamos
fornecer uma variável em que o valor de retorno possa ser armazenado.
Nesse caso, o valor devolvido é armazenado na variável musician em x. A
saída mostra um nome formatado de modo elegante, composto das partes
do nome de uma pessoa:
Jimi Hendrix
Pode parecer bastante trabalho para obter um nome formatado de forma
elegante quando poderíamos simplesmente ter escrito:
print("Jimi Hendrix")
No entanto, quando consideramos trabalhar com um programa de
grande porte, que precise armazenar muitos primeiros nomes e
sobrenomes separadamente, funções como get_formatted_name() tornam-se
muito convenientes. Armazenamos os primeiros nomes e os sobrenomes de
forma separada e então chamamos essa função sempre que quisermos
exibir um nome completo.
Deixando umargumento opcional
Às vezes, faz sentido criar um argumento opcional para que as pessoas que
usarem a função possam optar por fornecer informações extras somente se
quiserem. Valores default podem ser usados para deixar um argumento
opcional.
Por exemplo, suponha que queremos expandir get_formatted_name() para
que trate nomes do meio também. Uma primeira tentativa para incluir
nomes do meio poderia ter o seguinte aspecto:
def get_formatted_name(first_name, middle_name, last_name):
Devolve um nome completo formatado de modo elegante.
full_name = first_name + ' ' + middle_name + ' ' + last_name
return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
Essa função é apropriada quando fornecemos um primeiro nome, um
nome do meio e um sobrenome. Ela aceita todas as três partes de um nome
e então compõe uma string a partir delas. A função acrescenta espaços nos
pontos apropriados e converte o nome completo para que as iniciais sejam
maiúsculas:
John Lee Hooker
No entanto, nomes do meio nem sempre são necessários, e essa função,
conforme está escrita, não seria apropriada se tentássemos chamá-la
somente com um primeiro nome e um sobrenome. Para deixar o nome do
meio opcional, podemos associar um valor default vazio ao argumento
middle_name e ignorá-lo, a menos que o usuário forneça um valor. Para que
get_formatted_name() funcione sem um nome do meio, definimos o valor
default de middle_name com uma string vazia e o passamos para o final da
lista de parâmetros:
u def get_formatted_name(first_name, last_name, middle_name=''):
Devolve um nome completo formatado de modo elegante.
v if middle_name:
full_name = first_name + ' ' + middle_name + ' ' + last_name
w else:
full_name = first_name + ' ' + last_name
return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
x musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
Nesse exemplo, o nome é criado a partir de três partes possíveis. Como o
primeiro nome e o sobrenome sempre existem, esses parâmetros são
listados antes na definição da função. O nome do meio é opcional,
portanto é listado por último na definição, e seu valor default é uma string
vazia u.
No corpo da função verificamos se um nome do meio foi especificado.
Python interpreta strings não vazias como True, portanto if middle_name
será avaliado como True se um argumento para o nome do meio estiver na
chamada da função v. Se um nome do meio for especificado, o primeiro
nome, o nome do meio e o sobrenome serão combinados para compor um
nome completo. Esse nome é então alterado para que as iniciais sejam
maiúsculas e é devolvido para a linha que chamou a função: ele será
armazenado em uma variável musician e exibido. Se um nome do meio não
for especificado, a string vazia falhará no teste if e o bloco else será
executado w. O nome completo será composto apenas do primeiro nome e
do sobrenome, e o nome formatado é devolvido para a linha que fez a
chamada: ele será armazenado em musician e exibido.
Chamar essa função com um primeiro nome e um sobrenome é simples.
Se usarmos um nome do meio, porém, precisamos garantir que esse nome
seja o último argumento passado para que Python faça a correspondência
dos argumentos posicionais de forma correta x.
Essa versão modificada de nossa função é apropriada para pessoas que
tenham apenas um primeiro nome e um sobrenome, mas funciona também
para pessoas que tenham um nome do meio:
Jimi Hendrix
John Lee Hooker
Valores opcionais permitem que as funções tratem uma grande variedade
de casos de uso, ao mesmo tempo que simplificam ao máximo as
chamadas de função.
Devolvendo umdicionário
Uma função pode devolver qualquer tipo de valor necessário, incluindo
estruturas de dados mais complexas como listas e dicionários. Por
exemplo, a função a seguir aceita partes de um nome e devolve um
dicionário que representa uma pessoa:
person.py
def build_person(first_name, last_name):
Devolve um dicionário com informações sobre uma pessoa.
u person = {'first': first_name, 'last': last_name}
v return person
musician = build_person('jimi', 'hendrix')
w print(musician)
A função build_person() aceita um primeiro nome e um sobrenome e
então reúne esses valores em um dicionário em u. O valor de first_name é
armazenado com a chave 'first' e o valor de last_name é armazenado com
a chave 'last'. O dicionário completo que representa a pessoa é devolvido
em v. O valor de retorno é exibido em w, com as duas informações textuais
originais agora armazenadas em um dicionário:
{'first': 'jimi', 'last': 'hendrix'}
Essa função aceita informações textuais simples e as coloca em uma
estrutura de dados mais significativa, que permite trabalhar com as
informações além de simplesmente exibi-las. As strings 'jimi' e 'hendrix'
agora estão identificadas como um primeiro nome e um sobrenome.
Podemos facilmente estender essa função para que aceite valores opcionais
como um nome do meio, uma idade, uma profissão ou qualquer outra
informação que você queira armazenar sobre uma pessoa. Por exemplo, a
alteração a seguir permite armazenar a idade de uma pessoa também:
def build_person(first_name, last_name, age=''):
Devolve um dicionário com informações sobre uma pessoa.
person = {'first': first_name, 'last': last_name}
if age:
person['age'] = age
return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
Adicionamos um novo parâmetro opcional age à definição da função e
atribuímos um valor default vazio ao parâmetro. Se a chamada da função
incluir um valor para esse parâmetro, ele será armazenado no dicionário.
Essa função sempre armazena o nome de uma pessoa, mas também pode
ser modificada para guardar outras informações que você quiser sobre ela.
Usando umafunção comumlaço while
Podemos usar funções com todas as estruturas Python que conhecemos até
agora. Por exemplo, vamos usar a função get_formatted_name() com um
laço while para saudar os usuários de modo mais formal. Eis uma primeira
tentativa de saudar pessoas usando seu primeiro nome e o sobrenome:
greeter.py
def get_formatted_name(first_name, last_name):
Devolve um nome completo formatado de modo elegante.
full_name = first_name + ' ' + last_name
return full_name.title()
# Este é um loop infinito!
while True:
u print("nPlease tell me your name:")
f_name = input("First name: ")
l_name = input("Last name: ")
formatted_name = get_formatted_name(f_name, l_name)
print("nHello, " + formatted_name + "!")
Nesse exemplo, usamos uma versão simples de get_formatted_name() que
não envolve nomes do meio. O laço while pede que o usuário forneça seu
nome; além disso, solicitamos o primeiro nome e o sobrenome
separadamente u.
Porém há um problema com esse laço while: não definimos uma
condição de saída. Onde devemos colocar uma condição de saída quando
pedimos uma série de entradas? Queremos que o usuário seja capaz de sair
o mais facilmente possível, portanto cada prompt deve oferecer um modo
de fazer isso. A instrução break permite um modo simples de sair do laço
em qualquer prompt:
def get_formatted_name(first_name, last_name):
Devolve um nome completo formatado de modo elegante.
full_name = first_name + ' ' + last_name
return full_name.title()
while True:
print("nPlease tell me your name:")
print("(enter 'q' at any time to quit)")
f_name = input("First name: ")
if f_name == 'q':
break
l_name = input("Last name: ")
if l_name == 'q':
break
formatted_name = get_formatted_name(f_name, l_name)
print("nHello, " + formatted_name + "!")
Adicionamos uma mensagem que informa como o usuário pode sair e
então encerramos o laço se o usuário fornecer o valor de saída em qualquer
um dos prompts. Agora o programa continuará saudando as pessoas até
que alguém forneça 'q' em algum dos nomes:
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes
Hello, Eric Matthes!
Please tell me your name:
(enter 'q' at any time to quit)
First name: q
FAÇA VOCÊ MESMO
8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim:
"Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
8.7 – Álbum: Escreva uma função chamada make_album() que construa um
dicionário descrevendo um álbum musical. A função deve aceitar o nome de um
artista e o título de um álbum e deve devolver um dicionário contendo essas duas
informações. Use a função para criar três dicionários que representem álbuns
diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão
armazenando as informações do álbum corretamente.
Acrescente um parâmetro opcional em make_album() que permita armazenar o
número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor
para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum.
8.8 – Álbuns dos usuários: Comece com o seu programa do Exercício 8.7.
Escreva um laço while que permita aos usuários fornecer o nome de um artista e o
título de um álbum. Depois que tiver essas informações, chame make_album() com
as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um
valor de saída no laço while.
Passando umalista para umafunção
Com frequência, você achará útil passar uma lista para uma função, seja
uma lista de nomes, de números ou de objetos mais complexos, como
dicionários. Se passarmos uma lista a uma função, ela terá acesso direto ao
conteúdo dessa lista. Vamos usar funções para que o trabalho com listas
seja mais eficiente.
Suponha que tenhamos uma lista de usuários e queremos exibir uma
saudação a cada um. O exemplo a seguir envia uma lista de nomes a uma
função chamada greet_users(), que saúda cada pessoa da lista
individualmente:
greet_users.py
def greet_users(names):
Exibe uma saudação simples a cada usuário da lista.
for name in names:
msg = "Hello, " + name.title() + "!"
print(msg)
u usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
Definimos greet_users() para que espere uma lista de nomes, que é
armazenada no parâmetro names. A função percorre a lista recebida com
um laço e exibe uma saudação para cada usuário. Em u definimos uma
lista de usuários e então passamos a lista usernames para greet_users() em
nossa chamada de função:
Hello, Hannah!
Hello, Ty!
Hello, Margot!
Essa é a saída que queríamos. Todo usuário vê uma saudação
personalizada, e você pode chamar a função sempre que quiser para saudar
um conjunto específico de usuários.
Modificando umalistaemumafunção
Quando passamos uma lista a uma função, ela pode ser modificada.
Qualquer alteração feita na lista no corpo da função é permanente,
permitindo trabalhar de modo eficiente, mesmo quando lidamos com
grandes quantidades de dados.
Considere uma empresa que cria modelos de designs submetidos pelos
usuários e que são impressos em 3D. Os designs são armazenados em uma
lista e, depois de impressos, são transferidos para uma lista separada. O
código a seguir faz isso sem usar funções:
printing_models.py
# Começa com alguns designs que devem ser impressos
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simula a impressão de cada design, até que não haja mais nenhum
# Transfere cada design para completed_models após a impressão
while unprinted_designs:
current_design = unprinted_designs.pop()
# Simula a criação de uma impressão 3D a partir do design
print("Printing model: " + current_design)
completed_models.append(current_design)
# Exibe todos os modelos finalizados
print("nThe following models have been printed:")
for completed_model in completed_models:
print(completed_model)
Esse programa começa com uma lista de designs que devem ser
impressos e uma lista vazia chamada completed_models para a qual cada
design será transferido após a impressão. Enquanto houver designs em
unprinted_designs, o laço while simulará a impressão de cada um deles
removendo um design do final da lista, armazenando-o em current_design e
exibindo uma mensagem informando que o design atual está sendo
impresso. O design então é adicionado à lista de modelos finalizados.
Quando o laço acaba de executar, uma lista de designs impressos é exibida:
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case
The following models have been printed:
dodecahedron
robot pendant
iphone case
Podemos reorganizar esse código escrevendo duas funções, em que cada
uma executa uma tarefa específica. A maior parte do código não sofrerá
alterações; estamos simplesmente deixando-o mais eficiente. A primeira
função tratará a impressão dos designs e a segunda gerará um resumo da
impressão feita:
u def print_models(unprinted_designs, completed_models):

Simula a impressão de cada design, até que não haja mais nenhum.
Transfere cada design para completed_models após a impressão.

while unprinted_designs:
current_design = unprinted_designs.pop()
# Simula a criação de uma impressão 3D a partir do design
print("Printing model: " + current_design)
completed_models.append(current_design)
v def show_completed_models(completed_models):
Mostra todos os modelos impressos.
print("nThe following models have been printed:")
for completed_model in completed_models:
print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
Em u definimos a função print_models() com dois parâmetros: uma lista
de designs a serem impressos e uma lista de modelos concluídos. Dadas
essas duas listas, a função simula a impressão de cada design esvaziando a
lista de designs não impressos e preenchendo a lista de designs completos.
Em v definimos a função show_completed_models() com um parâmetro: a
lista de modelos finalizados. Dada essa lista, show_completed_models() exibe
o nome de cada modelo impresso.
Esse programa produz a mesma saída da versão sem funções, mas o
código está muito mais organizado. O código que faz a maior parte do
trabalho foi transferido para duas funções separadas, que deixam a parte
principal do programa mais fácil de entender. Observe o corpo do
programa para ver como é mais simples entender o que esse programa faz:
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
Definimos uma lista de designs não impressos e uma lista vazia que
armazenará os modelos finalizados. Então, como já definimos nossas duas
funções, tudo que temos a fazer é chamá-las e passar os argumentos
corretos a elas. Chamamos print_models() e passamos as duas listas de que
essa função precisa; conforme esperado, print_models() simula a impressão
dos designs. Em seguida, chamamos show_completed_models() e passamos
uma lista dos modelos concluídos para que ela possa apresentar os
modelos impressos. Os nomes descritivos das funções permitem que outras
pessoas leiam esse código e o entendam, mesmo que não haja comentários.
Esse programa é mais fácil de ser estendido e mantido que a versão sem
funções. Se precisarmos imprimir mais designs depois, poderemos
simplesmente chamar print_models() novamente. Se percebermos que o
código de impressão precisa ser modificado, podemos alterar o código uma
vez, e nossas alterações estarão presentes em todos os lugares em que a
função for chamada. Essa técnica é mais eficiente que ter de atualizar um
código separadamente em vários pontos do programa.
Esse exemplo também mostra a ideia de que toda função deve ter uma
tarefa específica. A primeira função imprime cada design, enquanto a
segunda mostra os modelos concluídos. Isso é mais vantajoso que usar
uma única função para executar as duas tarefas. Se você estiver escrevendo
uma função e perceber que ela está fazendo muitas tarefas diferentes,
experimente dividir o código em duas funções. Lembre-se de que você
sempre pode chamar uma função a partir de outras funções, o que pode ser
conveniente quando dividimos uma tarefa complexa em uma série de
passos.
Evitando que umafunçãomodifique umalista
Às vezes, você vai querer evitar que uma função modifique uma lista. Por
exemplo, suponha que você comece com uma lista de designs não
impressos e escreva uma função que transfira esses designs para uma lista
de modelos terminados, como no exemplo anterior. Talvez você decida
que, apesar de ter imprimido todos os designs, vai querer manter a lista
original de designs não impressos em seus registros. Porém, como você
transferiu todos os nomes de designs de unprinted_designs, a lista agora
está vazia, e essa é a única versão da lista que você tem; a lista original se
perdeu. Nesse caso, podemos tratar esse problema passando uma cópia da
lista para a função, e não a lista original. Qualquer alteração que a função
fizer na lista afetará apenas a cópia, deixando a lista original intacta.
Você pode enviar uma cópia de uma lista para uma função assim:
nome_da_função(nome_da_lista[:])
A notação de fatia [:] cria uma cópia da lista para ser enviada à função.
Se não quiséssemos esvaziar a lista de designs não impressos em
print_models.py, chamaríamos print_models() desta maneira:
print_models(unprinted_designs[:], completed_models)
A função print_models() pode fazer seu trabalho, pois ela continua
recebendo os nomes de todos os designs não impressos. Porém, dessa vez,
ela usa uma cópia da lista original de designs não impressos, e não a lista
unprinted_designs propriamente dita. A lista completed_models será
preenchida com os nomes dos modelos impressos, como antes, mas a lista
original de designs não impressos não será afetada pela função.
Apesar de poder preservar o conteúdo de uma lista passando uma cópia
dela para suas funções, você deve passar a lista original para as funções, a
menos que tenha um motivo específico para passar uma cópia. Para uma
função, é mais eficiente trabalhar com uma lista existente a fim de evitar o
uso de tempo e de memória necessários para criar uma cópia separada, em
especial quando trabalhamos com listas grandes.
FAÇA VOCÊ MESMO
8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da lista.
8.10 – Grandes mágicos: Comece com uma cópia de seu programa do Exercício
8.9. Escreva uma função chamada make_great() que modifique a lista de
mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame
show_magicians() para ver se a lista foi realmente modificada.
8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
lista separada. Chame show_magicians() com cada lista para mostrar que você
tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.
Passando umnúmero arbitrário deargumentos
Às vezes, você não saberá com antecedência quantos argumentos uma
função deve aceitar. Felizmente, Python permite que uma função receba
um número arbitrário de argumentos da instrução de chamada.
Por exemplo, considere uma função que prepare uma pizza. Ela deve
aceitar vários ingredientes, mas não é possível saber com antecedência
quantos ingredientes uma pessoa vai querer. A função no próximo
exemplo tem um parâmetro *toppings, mas esse parâmetro agrupa tantos
argumentos quantos forem fornecidos na linha de chamada:
pizza.py
def make_pizza(*toppings):
Exibe a lista de ingredientes pedidos.
print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
O asterisco no nome do parâmetro *toppings diz a Python para criar uma
tupla vazia chamada toppings e reunir os valores recebidos nessa tupla. A
instrução print no corpo da função gera uma saída que mostra que Python
é capaz de tratar uma chamada de função com um valor e outra chamada
com três valores. As chamadas são tratadas de modo semelhante. Observe
que Python agrupa os argumentos em uma tupla, mesmo que a função
receba apenas um valor:
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
Podemos agora substituir a instrução print por um laço que percorra a
lista de ingredientes e descreva a pizza sendo pedida:
def make_pizza(*toppings):
Apresenta a pizza que estamos prestes a preparar.
print("nMaking a pizza with the following toppings:")
for topping in toppings:
print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
A função responde de forma apropriada, independentemente de receber
um ou três valores:
Making a pizza with the following toppings:
- pepperoni
Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
Essa sintaxe funciona, não importa quantos argumentos a função receba.
Misturando argumentos posicionaisearbitrários
Se quiser que uma função aceite vários tipos de argumentos, o parâmetro
que aceita um número arbitrário de argumentos deve ser colocado por
último na definição da função. Python faz a correspondência de
argumentos posicionais e nomeados antes, e depois agrupa qualquer
argumento remanescente no último parâmetro.
Por exemplo, se a função tiver que aceitar um tamanho para a pizza, esse
parâmetro deve estar antes do parâmetro *toppings:
def make_pizza(size, *toppings):
Apresenta a pizza que estamos prestes a preparar.
print("nMaking a " + str(size) +
"-inch pizza with the following toppings:")
for topping in toppings:
print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
Na definição da função, Python armazena o primeiro valor recebido no
parâmetro size. Todos os demais valores que vierem depois são
armazenados na tupla toppings. As chamadas da função incluem um
argumento para o tamanho antes, seguido de tantos ingredientes quantos
forem necessários.
Agora cada pizza tem um tamanho e alguns ingredientes, e cada
informação é exibida no lugar apropriado, mostrando o tamanho antes e os
ingredientes depois:
Making a 16-inch pizza with the following toppings:
- pepperoni
Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
Usando argumentos nomeadosarbitrários
Às vezes, você vai querer aceitar um número arbitrário de argumentos, mas
não saberá com antecedência qual tipo de informação será passado para a
função. Nesse caso, podemos escrever funções que aceitem tantos pares
chave-valor quantos forem fornecidos pela instrução que faz a chamada.
Um exemplo envolve criar perfis de usuários: você sabe que obterá
informações sobre um usuário, mas não tem certeza quanto ao tipo de
informação que receberá. A função build_profile() no próximo exemplo
sempre aceita um primeiro nome e um sobrenome, mas aceita também um
número arbitrário de argumentos nomeados:
user_profile.py
def build_profile(first, last, **user_info):
Constrói um dicionário contendo tudo que sabemos sobre um
usuário.
profile = {}
u profile['first_name'] = first
profile['last_name'] = last
v for key, value in user_info.items():
profile[key] = value
return profile
user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)
A definição de build_profile() espera um primeiro nome e um
sobrenome e permite que o usuário passe tantos pares nome-valor quantos
ele quiser. Os asteriscos duplos antes do parâmetro **user_info fazem
Python criar um dicionário vazio chamado user_info e colocar quaisquer
pares nome-valor recebidos nesse dicionário. Nessa função, podemos
acessar os pares nome-valor em user_info como faríamos com qualquer
dicionário.
No corpo de build_profile(), criamos um dicionário vazio chamado
profile para armazenar o perfil do usuário. Em u adicionamos o primeiro
nome e o sobrenome nesse dicionário porque sempre receberemos essas
duas informações do usuário. Em v percorremos os pares chave-valor
adicionais do dicionário user_info e adicionamos cada par ao dicionário
profile. Por fim, devolvemos o dicionário profile à linha que chamou a
função.
Chamamos build_profile() passando o primeiro nome 'albert', o
sobrenome 'einstein' e os dois pares chave-valor location='princeton' e
field='physics'. Armazenamos o dicionário profile devolvido em
user_profile e exibimos o valor dessa variável:
{'first_name': 'albert', 'last_name': 'einstein',
'location': 'princeton', 'field': 'physics'}
O dicionário devolvido contém o primeiro nome e o sobrenome do
usuário e, nesse caso, a localidade e o campo de estudo também. A função
será apropriada, não importa quantos pares chave-valor adicionais sejam
fornecidos na chamada da função.
Podemos misturar valores posicionais, nomeados e arbitrários de várias
maneiras diferentes quando escrevermos nossas próprias funções. É
conveniente saber que todos esses tipos de argumento existem, pois você
os verá com frequência quando começar a ler códigos de outras pessoas.
Aprender a usar os diferentes tipos corretamente e saber quando usar cada
um exige prática. Por enquanto, lembre-se de usar a abordagem mais
simples possível, que faça o trabalho necessário. À medida que progredir,
você aprenderá a usar a abordagem mais eficiente a cada vez.
FAÇA VOCÊ MESMO
8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos
itens quantos forem fornecidos pela chamada da função e deve apresentar um
resumo do sanduíche pedido. Chame a função três vezes usando um número
diferente de argumentos a cada vez.
8.13 – Perfil do usuário: Comece com uma cópia de user_profile.py, da página
210. Crie um perfil seu chamando build_profile(), usando seu primeiro nome e
o sobrenome, além de três outros pares chave-valor que o descrevam.
8.14 – Carros: Escreva uma função que armazene informações sobre um carro em
um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
Chame a função com as informações necessárias e dois outros pares nome-valor,
por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma
chamada como esta:
car = make_car(‘subaru’, ‘outback’, color=’blue’, tow_package=True)
Mostre o dicionário devolvido para garantir que todas as informações foram
armazenadas corretamente.
Armazenando suas funçõesemmódulos
Uma vantagem das funções é a maneira como elas separam blocos de
código de seu programa principal. Ao usar nomes descritivos para suas
funções, será bem mais fácil entender o seu programa principal. Você pode
dar um passo além armazenando suas funções em um arquivo separado
chamado módulo e, então, importar esse módulo em seu programa
principal. Uma instrução import diz a Python para deixar o código de um
módulo disponível no arquivo de programa em execução no momento.
Armazenar suas funções em um arquivo separado permite ocultar os
detalhes do código de seu programa e se concentrar na lógica de nível mais
alto. Também permite reutilizar funções em muitos programas diferentes.
Quando armazenamos funções em arquivos separados, podemos
compartilhar esses arquivos com outros programadores sem a necessidade
de compartilhar o programa todo. Saber como importar funções também
possibilita usar bibliotecas de funções que outros programadores
escreveram.
Há várias maneiras de importar um módulo e vou mostrar cada uma
delas rapidamente.
Importando ummódulo completo
Para começar a importar funções, inicialmente precisamos criar um
módulo. Um módulo é um arquivo terminado em .py que contém o código
que queremos importar para o nosso programa. Vamos criar um módulo
que contenha a função make_pizza(). Para criar esse módulo, removeremos
tudo que está no arquivo pizza.py, exceto a função make_pizza():
pizza.py
def make_pizza(size, *toppings):
Apresenta a pizza que estamos prestes a preparar.
print("nMaking a " + str(size) +
"-inch pizza with the following toppings:")
for topping in toppings:
print("- " + topping)
Agora criaremos um arquivo separado chamado making_pizzas.py no
mesmo diretório em que está pizza.py. Esse arquivo importa o módulo que
acabamos de criar e, em seguida, faz duas chamadas para make_pizza():
making_pizzas.py
import pizza
u pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
Quando Python lê esse arquivo, a linha import pizza lhe diz para abrir o
arquivo pizza.py e copiar todas as funções dele para esse programa. Você
não vê realmente o código sendo copiado entre os arquivos porque Python
faz isso internamente, à medida que o programa executa. Tudo que você
precisa saber é que qualquer função definida em pizza.py agora estará
disponível em making_pizzas.py.
Para chamar uma função que está em um módulo importado, forneça o
nome do módulo, que é pizza nesse caso, seguido do nome da função,
make_pizza(), separados por um ponto u. Esse código gera a mesma saída
que o programa original, que não importava um módulo:
Making a 16-inch pizza with the following toppings:
- pepperoni
Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
Essa primeira abordagem à importação, em que simplesmente
escrevemos import seguido do nome do módulo, deixa todas as funções do
módulo disponíveis ao seu programa. Se você usar esse tipo de instrução
import para importar um módulo completo chamado nome_do_módulo.py,
todas as funções do módulo estarão disponíveis por meio da sintaxe a
seguir:
nome_do_módulo.nome_da_função()
Importando funçõesespecíficas
Podemos também importar uma função específica de um módulo. Eis a
sintaxe geral para essa abordagem:
from nome_do_módulo import nome_da_função
Você pode importar quantas funções quiser de um módulo separando o
nome de cada função com uma vírgula:
from nome_do_módulo import função_0, função_1, função_2
O exemplo com making_pizzas.py teria o seguinte aspecto, se
quiséssemos importar somente a função que será utilizada:
from pizza import make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
Com essa sintaxe não precisamos usar a notação de ponto ao chamar
uma função. Como importamos explicitamente a função make_pizza() na
instrução import, podemos chamá-la pelo nome quando ela for utilizada.
Usando a palavrareservadaas paraatribuir umaliasa umafunção
Se o nome de uma função que você importar puder entrar em conflito com
um nome existente em seu programa ou se o nome da função for longo,
podemos usar um alias único e conciso, que é um nome alternativo,
semelhante a um apelido para a função. Dê esse apelido especial à função
quando importá-la.
A seguir, atribuímos um alias mp() para a função make_pizza() importando
make_pizza as mp. A palavra reservada as renomeia uma função usando o
alias que você fornecer:
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
A instrução import no exemplo renomeia a função make_pizza() para mp()
nesse programa. Sempre que quiser chamar make_pizza(), você pode
simplesmente escrever mp() em seu lugar, e Python executará o código de
make_pizza(), ao mesmo tempo que evitará confusão com outra função
make_pizza() que você possa ter escrito nesse arquivo de programa.
A sintaxe geral para fornecer um alias é:
from nome_do_módulo import nome_da_função as nf
Usando a palavrareservadaas paraatribuir umaliasa ummódulo
Também podemos fornecer um alias para um nome de módulo. Dar um
alias conciso a um módulo, por exemplo, p para pizza, permite chamar
mais rapidamente as funções do módulo. Chamar p.make_pizza() é mais
compacto que chamar pizza.make_pizza():
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
O módulo pizza recebe o alias p na instrução import, mas todas as funções
do módulo preservam seus nomes originais. Chamar as funções escrevendo
p.make_pizza() não só é mais compacto que escrever pizza.make_pizza()
como também desvia sua atenção do nome do módulo e permite dar
enfoque aos nomes descritivos de suas funções. Esses nomes de função,
que claramente informam o que cada função faz, são mais importantes
para a legibilidade de seu código que usar o nome completo do módulo.
A sintaxe geral para essa abordagem é:
import nome_do_módulo as nm
Importando todasas funções de ummódulo
Podemos dizer a Python para importar todas as funções de um módulo
usando o operador asterisco (*):
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
O asterisco na instrução import diz a Python para copiar todas as funções
do módulo pizza para esse arquivo de programa. Como todas as funções
são importadas, podemos chamar qualquer função pelo nome, sem usar a
notação de ponto. No entanto, é melhor não usar essa abordagem quando
trabalhar com módulos maiores, que não foram escritos por você: se o
módulo tiver um nome de função que seja igual a um nome existente em
seu projeto, você poderá ter alguns resultados inesperados. Python poderá
ver várias funções ou variáveis com o mesmo nome e, em vez de importar
todas as funções separadamente, ele as sobrescreverá.
A melhor abordagem é importar a função ou as funções que você quiser
ou importar o módulo todo e usar a notação de ponto. Isso resulta em um
código claro, mais fácil de ler e de entender. Incluí esta seção para que você
possa reconhecer instruções import como esta quando as vir no código de
outras pessoas:
from nome_do_módulo import *
Estilizando funções
Você precisa ter alguns detalhes em mente quando estilizar funções. As
funções devem ter nomes descritivos, e esses nomes devem usar letras
minúsculas e underscores. Nomes descritivos ajudam você e outras pessoas
a entenderem o que seu código está tentando fazer. Os nomes de módulos
devem usar essas convenções também.
Toda função deve ter um comentário que explique o que ela faz de modo
conciso. Esse comentário deve estar imediatamente após a definição da
função e deve utilizar o formato de docstring. Se uma função estiver bem
documentada, outros programadores poderão usá-la apenas lendo a
descrição da docstring. Eles poderão crer que o código funcionará
conforme descrito e, desde que saibam o nome da função, os argumentos
necessários e o tipo de valor que ela devolve, deverão ser capazes de usá-la
em seus programas.
Se você especificar um valor default para um parâmetro, não deve haver
espaços em nenhum dos lados do sinal de igualdade:
def nome_da_função(parâmetro_0, parâmetro_1='valor default')
A mesma convenção deve ser usada para argumentos nomeados em
chamadas de função:
nome_da_função(valor_0, parâmetro_1='valor')
A PEP 8 (https://www.python.org/dev/peps/pep-0008/ ) recomenda limitar
as linhas de código em 79 caracteres para que todas as linhas permaneçam
visíveis em uma janela de editor com um tamanho razoável. Se um
conjunto de parâmetros fizer com que a definição de uma função
ultrapasse 79 caracteres, tecle ENTER após o parêntese de abertura na linha
da definição. Na próxima linha, tecle TAB duas vezes para separar a lista de
argumentos do corpo da função, que estará indentado com apenas um
nível.
A maioria dos editores fará automaticamente o alinhamento de qualquer
parâmetro adicional para que corresponda à indentação que você
determinar na primeira linha:
def nome_da_função(
parâmetro_0, parâmetro_1, parâmetro_2,
parâmetro_3, parâmetro_4, parâmetro_5):
corpo da função...
Se seu programa ou módulo tiver mais de uma função, você poderá
separá-las usando duas linhas em branco para facilitar ver em que lugar
uma função termina e a próxima começa.
Todas as instruções import devem estar no início de um arquivo. A única
exceção ocorre quando você usa comentários no início de seu arquivo para
descrever o programa como um todo.
FAÇA VOCÊ MESMO
8.15 – Impressão de modelos: Coloque as funções do exemplo print_models.py
em um arquivo separado de nome printing_functions.py. Escreva uma instrução
import no início de print_models.py e modifique o arquivo para usar as funções
importadas.
8.16 – Importações: Usando um programa que você tenha escrito e que contenha
uma única função, armazene essa função em um arquivo separado. Importe a
função para o arquivo principal de seu programa e chame-a usando cada uma das
seguintes abordagens:
import nome_do_módulo
from nome_do_módulo import nome_da_função
from nome_do_módulo import nome_da_função as nf
import nome_do_módulo as nm
from nome_do_módulo import *
8.17 – Estilizando funções: Escolha quaisquer três programas que você escreveu
neste capítulo e garanta que estejam de acordo com as diretrizes de estilo descritas
nesta seção.
Resumo
Neste capítulo aprendemos a escrever funções e a passar argumentos de
modo que suas funções tenham acesso às informações necessárias para
realizarem sua tarefa. Vimos como usar argumentos posicionais e
nomeados, e aprendemos a aceitar um número arbitrário de argumentos.
Conhecemos funções que exibem uma saída e funções que devolvem
valores. Aprendemos a usar funções com listas, dicionários, instruções if e
laços while. Também vimos como armazenar suas funções em arquivos
separados chamados de módulos; desse modo, seus arquivos de programa
serão mais simples e mais fáceis de entender. Por fim, aprendemos a
estilizar as funções para que seus programas continuem bem estruturados e
o mais fácil possível para você e outras pessoas lerem.
Um de nossos objetivos como programador deve ser escrever um código
simples, que faça o que você quer, e as funções ajudam nessa tarefa. Elas
permitem escrever blocos de código e deixá-los de lado depois que você
souber que eles funcionam. Quando souber que uma função executa sua
tarefa de forma correta, você poderá se sentir seguro de que ela continuará
a funcionar, e poderá prosseguir para a próxima tarefa de programação.
As funções permitem escrever um código uma vez e então reutilizá-lo
quantas vezes você quiser. Quando tiver que executar o código de uma
função, tudo que você precisa fazer é escrever uma chamada de uma linha,
e a função fará o seu trabalho. Quando for necessário modificar o
comportamento de uma função, basta modificar apenas um bloco de
código e sua alteração terá efeito em todos os lugares em que uma
chamada dessa função for feita.
Usar funções deixa seus programas mais fáceis de ler, e bons nomes de
função sintetizam o que cada parte de um programa faz. Ler uma série de
chamadas de função possibilita ter rapidamente uma noção do que um
programa faz, se comparado à leitura de uma série longa de blocos de
código.
As funções também deixam seu código mais fácil de testar e de depurar.
Quando a maior parte do trabalho de seu programa for feita por um
conjunto de funções, em que cada uma tem uma tarefa específica, será
muito mais fácil testar e dar manutenção no código que você escreveu. É
possível escrever um programa separado que chame cada função e testar se
ela funciona em todas as situações com as quais você poderá se deparar. Ao
fazer isso, você se sentirá mais seguro de que suas funções estarão corretas
sempre que forem chamadas.
No Capítulo 9 aprenderemos a escrever classes. As classes combinam
funções e dados em um pacote organizado, que pode ser usado de
maneiras flexíveis e eficientes.
9
CLASSES
A programação orientada a objetos é uma das abordagens
mais eficientes para escrever software. Na programação
orientada a objetos, escrevemos classes que representam
entidades e situações do mundo real, e criamos objetos
com base nessas classes. Quando escrevemos uma classe,
definimos o comportamento geral que toda uma categoria
de objetos pode ter.
Quando criamos objetos individuais a partir da classe, cada objeto será
automaticamente equipado com o comportamento geral; então você
poderá dar a cada objeto as características únicas que desejar. Você ficará
impressionado ao ver como situações do mundo real podem ser bem
modeladas com a programação orientada a objetos.
Criar um objeto a partir de uma classe é uma operação conhecida como
instanciação, e trabalhamos com instâncias de uma classe. Neste capítulo,
escreveremos classes e criaremos instâncias dessas classes. Especificaremos
o tipo de informação que pode ser armazenado nas instâncias e
definiremos ações que podem ser executadas nessas instâncias. Também
escreveremos classes que estendem a funcionalidade de classes existentes,
de modo que classes semelhantes possam compartilhar códigos de forma
eficiente. Armazenaremos nossas classes em módulos e importaremos
classes escritas por outros programadores para nossos próprios arquivos de
programa.
Entender a programação orientada a objetos ajudará a ver o mundo como
um programador o vê. Ela ajudará você a realmente conhecer o seu código,
não apenas o que acontece linha a linha, mas também os conceitos mais
amplos por trás dele. Conhecer a lógica por trás das classes treinará você a
pensar de modo lógico a fim de poder escrever programas que tratem
praticamente todo problema encontrado de forma eficiente.
As classes também facilitam sua vida e a vida de outros programadores
com quem você precisará trabalhar à medida que assumir desafios cada vez
mais complexos. Quando você e outros programadores escreverem códigos
baseados no mesmo tipo de lógica, vocês serão capazes de entender o
trabalho uns dos outros. Seus programas farão sentido para muitos
colaboradores, permitindo que todos façam mais.
Criando e usando umaclasse
Podemos modelar de tudo usando classes. Vamos começar escrevendo uma
classe simples, Dog, que representa um cachorro – não um cachorro em
particular, mas qualquer cachorro. O que sabemos sobre a maioria dos
cachorros de estimação? Bem, todos eles têm um nome e uma idade.
Também sabemos que a maioria deles senta e rola. Essas duas informações
(nome e idade) e esses dois comportamentos (sentar e rolar) farão parte de
nossa classe Dog, pois são comuns à maioria dos cachorros. Essa classe dirá
à Python como criar um objeto que represente um cachorro. Depois que
nossa classe estiver escrita, ela será usada para criar instâncias individuais,
em que cada uma representará um cachorro específico.
Criando aclasse Dog
Cada instância criada a partir da classe Dog armazenará um nome (name) e
uma idade (age), e daremos a cada cachorro a capacidade de sentar (sit())
e rolar (roll_over()):
dog.py
u class Dog():
v Uma tentativa simples de modelar um cachorro.
w def __init__(self, name, age):
Inicializa os atributos name e age.
x self.name = name
self.age = age
y def sit(self):
Simula um cachorro sentando em resposta a um comando.
print(self.name.title() + " is now sitting.")
def roll_over(self):
Simula um cachorro rolando em resposta a um comando.
print(self.name.title() + " rolled over!")
Há vários aspectos a serem observados aqui, mas não se preocupe. Você
verá essa estrutura ao longo deste capítulo e terá bastante tempo para se
acostumar com ela. Em u definimos uma classe chamada Dog. Por
convenção, nomes com a primeira letra maiúscula referem-se a classes em
Python. Os parênteses na definição da classe estão vazios porque estamos
criando essa classe do zero. Em v escrevemos uma docstring que descreve o
que essa classe faz.
Método __init__()
Uma função que faz parte de uma classe é um método. Tudo que
aprendemos sobre funções também se aplica aos métodos; a única
diferença prática, por enquanto, é o modo como chamaremos os métodos.
O método __init__() em w é um método especial que Python executa
automaticamente sempre que criamos uma nova instância baseada na
classe Dog. Esse método tem dois underscores no início e dois no final –
uma convenção que ajuda a evitar que os nomes default de métodos
Python entrem em conflito com nomes de métodos criados por você.
Definimos o método __init__() para que tenha três parâmetros: self,
name e age. O parâmetro self é obrigatório na definição do método e deve
estar antes dos demais parâmetros. Deve estar incluído na definição, pois,
quando Python chama esse método __init__() depois (para criar uma
instância de Dog), a chamada do método passará o argumento self
automaticamente. Toda chamada de método associada a uma classe passa
self, que é uma referência à própria instância, de modo automático; ele dá
acesso aos atributos e métodos da classe à instância individual. Quando
criamos uma instância de Dog, Python chamará o método __init__() da
classe Dog. Passaremos um nome e uma idade como argumentos para Dog();
self é passado automaticamente, portanto não é preciso especificá-lo.
Sempre que quisermos criar uma instância da classe Dog forneceremos
valores apenas para os dois últimos parâmetros, que são name e age.
As duas variáveis definidas em x têm o prefixo self. Qualquer variável
prefixada com self está disponível a todos os métodos da classe; além
disso, podemos acessar essas variáveis por meio de qualquer instância
criada a partir da classe. self.name = name usa o valor armazenado no
parâmetro name e o armazena na variável name, que é então associada à
instância criada. O mesmo processo ocorre com self.age = age. Variáveis
como essas, acessíveis por meio de instâncias, são chamadas de atributos.
A classe Dog tem dois outros dois métodos definidos: sit() e roll_over()
y. Como esses métodos não precisam de informações adicionais como um
nome ou uma idade, simplesmente os definimos com um parâmetro self.
As instâncias que criarmos posteriormente terão acesso a esses métodos.
Em outras palavras, elas terão a capacidade de sentar e rolar. Por enquanto,
sit() e roll_over() não fazem muito. Apenas exibem uma mensagem
dizendo que o cachorro está sentando ou rolando. No entanto, o conceito
pode ser estendido para situações realistas: se essa classe fizesse parte de
um jogo de computador de verdade, esses métodos conteriam código para
fazer a animação de um cachorro sentando e rolando. Se essa classe tivesse
sido escrita para controlar um robô, esses métodos direcionariam os
movimentos para fazer um cachorro-robô sentar e rolar.
Criando classesemPython 2.7
Quando criar uma classe em Python 2.7, será necessário fazer uma
pequena mudança. Inclua o termo object entre parênteses quando criá-la:
class NomeClasse(object):
--trecho omitido--
Isso faz as classes de Python 2.7 se comportarem de modo mais próximo
das classes de Python 3, o que, de modo geral, tornará seu trabalho mais
simples.
A classe Dog seria definida assim em Python 2.7:
class Dog(object):
--trecho omitido--
Criando umainstânciaa partir de umaclasse
Pense em uma classe como um conjunto de instruções para criar uma
instância. A classe Dog é um conjunto de instruções que diz a Python como
criar instâncias individuais que representem cachorros específicos.
Vamos criar uma instância que represente um cachorro específico:
class Dog():
--trecho omitido--
u my_dog = Dog('willie', 6)
v print("My dog's name is " + my_dog.name.title() + ".")
w print("My dog is " + str(my_dog.age) + " years old.")
A classe Dog que usamos aqui é aquela que acabamos de escrever no
exemplo anterior. Em u dizemos a Python para criar um cachorro de nome
'willie' e idade igual a 6. Quando Python lê essa linha, ele chama o
método __init__() de Dog com os argumentos 'willie' e 6. O método
__init__() cria uma instância que representa esse cachorro em particular e
define os atributos name e age com os valores que fornecemos. Esse método
não tem uma instrução return explícita, mas Python devolve
automaticamente uma instância que representa esse cachorro.
Armazenamos essa instância na variável my_dog. A convenção de
nomenclatura é útil nesse caso: em geral, podemos supor que um nome
com a primeira letra maiúscula como Dog refere-se a uma classe, enquanto
um nome com letras minúsculas como my_dog refere-se a uma única
instância criada a partir de uma classe.
Acessando atributos
Para acessar os atributos de uma instância utilize a notação de ponto. Em v
acessamos o valor do atributo name de my_dog escrevendo:
my_dog.name
A notação de ponto é usada com frequência em Python. Essa sintaxe
mostra como Python encontra o valor de um atributo. Nesse caso, o
interpretador olha para a instância my_dog e encontra o atributo name
associado a ela. É o mesmo atributo referenciado como self.name na classe
Dog. Em w usamos a mesma abordagem para trabalhar com o atributo age.
Em nossa primeira instrução print, my_dog.name.title() faz com que
'willie' – o valor do atributo name de my_dog – comece com uma letra
maiúscula. Na segunda instrução print, str(my_dog.age) converte 6 – o
valor do atributo age de my_dog – em uma string.
A saída é um resumo do que sabemos sobre my_dog:
My dog's name is Willie.
My dog is 6 years old.
Chamandométodos
Depois que criarmos uma instância da classe Dog, podemos usar a notação
de ponto para chamar qualquer método definido nessa classe. Vamos fazer
nosso cachorro sentar e rolar:
class Dog():
--trecho omitido--
my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
Para chamar um método, especifique o nome da instância (nesse caso,
my_dog) e o método que você quer chamar, separados por um ponto.
Quando Python lê my_dog.sit(), ele procura o método sit() na classe Dog e
executa esse código. A linha my_dog.roll_over() é interpretada do mesmo
modo.
Agora Willie faz o que lhe dissemos:
Willie is now sitting.
Willie rolled over!
Essa sintaxe é bem conveniente. Quando atributos e métodos recebem
nomes descritivos de forma apropriada, por exemplo, name, age, sit() e
roll_over(), podemos inferir facilmente o que um bloco de código deve
fazer, mesmo um que nunca vimos antes.
Criando várias instâncias
Você pode criar tantas instâncias de uma classe quantas forem necessárias.
Vamos criar um segundo cachorro chamado your_dog:
class Dog():
--trecho omitido--
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
Nesse exemplo, criamos um cachorro chamado Willie e uma cadela de
nome Lucy. Cada cachorro é uma instância separada, com seu próprio
conjunto de atributos, capaz de realizar o mesmo conjunto de ações:
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.
Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
Mesmo que usássemos o mesmo nome e a mesma idade para o segundo
cachorro, Python criaria uma instância separada da classe Dog. Você pode
criar tantas instâncias de uma classe quantas forem necessárias, desde que
dê a cada instância um nome de variável único ou que ela ocupe uma única
posição em uma lista ou dicionário.
FAÇA VOCÊ MESMO
9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type.
Crie um método chamado describe_restaurant() que mostre essas duas
informações, e um método de nome open_restaurant() que exiba uma
mensagem informando que o restaurante está aberto.
Crie uma instância chamada restaurant a partir de sua classe. Mostre os dois
atributos individualmente e, em seguida, chame os dois métodos.
9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância.
9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada ao
usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário.
Trabalhando comclasseseinstâncias
Podemos usar classes para representar muitas situações do mundo real.
Depois que escrever uma classe, você gastará a maior parte de seu tempo
trabalhando com instâncias dessa classe. Uma das primeiras tarefas que
você vai querer fazer é modificar os atributos associados a uma instância
em particular. Podemos modificar os atributos de uma instância
diretamente, ou escrever métodos que atualizem os atributos de formas
específicas.
ClasseCar
Vamos escrever uma nova classe que represente um carro. Nossa classe
armazenará informações sobre o tipo de carro com que estamos
trabalhando e terá um método que sintetiza essa informação:
car.py
class Car():
Uma tentativa simples de representar um carro.
u def __init__(self, make, model, year):
Inicializa os atributos que descrevem um carro.
self.make = make
self.model = model
self.year = year
v def get_descriptive_name(self):
Devolve um nome descritivo, formatado de modo elegante.
long_name = str(self.year) + ' ' + self.make + ' ' + self.model
return long_name.title()
w my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
Na classe Car em u definimos o método __init__() com o parâmetro self
em primeiro lugar, exatamente como fizemos antes com nossa classe Dog.
Também fornecemos outros três parâmetros: make, model e year. O método
__init__() aceita esses parâmetros e os armazena nos atributos que serão
associados às instâncias criadas a partir dessa classe. Quando criarmos
uma nova instância de Car, precisaremos especificar um fabricante, um
modelo e o ano para a nossa instância.
Em v definimos um método chamado get_descriptive_name() que coloca
os atributos year, make e model de um carro em uma string, descrevendo o
carro de modo elegante. Isso evitará a necessidade de exibir o valor de cada
atributo individualmente. Para trabalhar com os valores dos atributos nesse
método, usamos self.make, self.model e self.year. Em w criamos uma
instância da classe Car e a armazenamos na variável my_new_car. Então
chamamos get_descriptive_name() para mostrar o tipo de carro que temos:
2016 Audi A4
Para deixar a classe mais interessante, vamos adicionar um atributo que
mude com o tempo. Acrescentaremos um atributo que armazena a
milhagem do carro.
Definindo umvalor default para umatributo
Todo atributo de uma classe precisa de um valor inicial, mesmo que esse
valor seja 0 ou uma string vazia. Em alguns casos, por exemplo, quando
definimos um valor default, faz sentido especificar esse valor inicial no
corpo do método __init__(); se isso for feito para um atributo, você não
precisará incluir um parâmetro para ele.
Vamos acrescentar um atributo chamado odometer_reading que sempre
começa com o valor 0. Também adicionaremos um método
read_odometer() que nos ajudará a ler o hodômetro de cada carro:
class Car():
def __init__(self, make, model, year):
Inicializa os atributos que descrevem um carro.
self.make = make
self.model = model
self.year = year
u self.odometer_reading = 0
def get_descriptive_name(self):
--trecho omitido--
v def read_odometer(self):
Exibe uma frase que mostra a milhagem do carro.
print("This car has " + str(self.odometer_reading) + " miles on
it.")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
Dessa vez, quando Python chama o método __init__() para criar uma
nova instância, os valores para o fabricante, o modelo e o ano são
armazenados como atributos, como fizemos no exemplo anterior. Em
seguida, Python cria um novo atributo chamado odometer_reading e define
seu valor inicial com 0 u. Também temos um novo método de nome
read_odometer() em v que facilita a leitura da milhagem de um carro.
Nosso carro tem a milhagem iniciada com 0:
2016 Audi A4
This car has 0 miles on it.
Não há muitos carros vendidos com o hodômetro marcando exatamente
0, portanto precisamos de uma maneira de alterar o valor desse atributo.
Modificando valores deatributos
Você pode alterar o valor de um atributo de três maneiras: podemos
modificar o valor diretamente por meio de uma instância, definir o valor
com um método ou incrementá-lo (somar um determinado valor a ele).
Vamos analisar cada uma dessas abordagens.
Modificando o valor de umatributo diretamente
A maneira mais simples de modificar o valor de um atributo é acessá-lo
diretamente por meio de uma instância. A seguir, definimos o valor de
leitura do hodômetro para 23, de forma direta:
class Car():
--trecho omitido--
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
u my_new_car.odometer_reading = 23
my_new_car.read_odometer()
Em u usamos a notação de ponto para acessar o atributo odometer_reading
do carro e definir seu valor diretamente. Essa linha diz a Python para usar a
instância my_new_car, encontrar o atributo odometer_reading associado a ela e
definir o valor desse atributo com 23:
2016 Audi A4
This car has 23 miles on it.
Às vezes, você vai querer acessar os atributos de forma direta como
fizemos, mas, em outras ocasiões, vai querer escrever um método que
atualize o valor para você.
Modificando o valor de umatributo comummétodo
Pode ser conveniente ter métodos que atualizem determinados atributos
para você. Em vez de acessar o atributo de modo direto, passe o novo valor
para um método que trate a atualização internamente.
Eis um exemplo que mostra um método de nome update_odometer():
class Car():
--trecho omitido--
u def update_odometer(self, mileage):
Define o valor de leitura do hodômetro com o valor
especificado.
self.odometer_reading = mileage
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
v my_new_car.update_odometer(23)
my_new_car.read_odometer()
A única modificação em Car foi o acréscimo de update_odometer() em u.
Esse método aceita um valor de milhagem e o armazena em
self.odometer_reading. Em v chamamos update_odometer() e lhe passamos o
valor 23 como argumento (correspondendo ao parâmetro mileage na
definição do método). Esse método define o valor de leitura do hodômetro
com 23 e read_odometer() exibe essa leitura:
2016 Audi A4
This car has 23 miles on it.
Podemos estender o método update_odometer() para que faça uma tarefa
adicional sempre que a leitura do hodômetro for modificada. Vamos
acrescentar um pouco de lógica para garantir que ninguém tente diminuir
o valor lido no hodômetro:
class Car():
--trecho omitido--
def update_odometer(self, mileage):

Define o valor de leitura do hodômetro com o valor especificado
Rejeita a alteração se for tentativa de definir um valor menor
para o hodômetro

u if mileage >= self.odometer_reading:
self.odometer_reading = mileage
else:
v print("You can't roll back an odometer!")
Agora update_odometer() verifica se o novo valor do hodômetro faz
sentido antes de modificar o atributo. Se a nova milhagem, mileage, for
maior ou igual à milhagem existente, self.odometer_reading, você poderá
atualizar o valor de leitura do hodômetro com a nova milhagem u. Se a
nova milhagem for menor que a milhagem existente, você receberá um
aviso informando que não pode diminuir o valor lido no hodômetro v.
Incrementando o valor de umatributo comummétodo
Às vezes, você vai querer incrementar o valor de um atributo de
determinada quantidade, em vez de definir um valor totalmente novo.
Suponha que compramos um carro usado e andamos cem milhas entre o
instante em que o compramos e o momento em que o registramos. Eis um
método que nos permite passar essa quantidade incremental e somar esse
valor ao valor de leitura do hodômetro:
class Car():
--trecho omitido--
def update_odometer(self, mileage):
--trecho omitido--
u def increment_odometer(self, miles):
Soma a quantidade especificada ao valor de leitura do
hodômetro.
self.odometer_reading += miles
v my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
w my_used_car.update_odometer(23500)
my_used_car.read_odometer()
x my_used_car.increment_odometer(100)
my_used_car.read_odometer()
O novo método increment_odometer() em u aceita uma quantidade de
milhas e soma esse valor a self.odometer_reading. Em v criamos um carro
usado, my_used_car. Definimos seu hodômetro com o valor 23.500
chamando update_odometer() e passando-lhe o valor 23500 em w. Em x
chamamos increment_odometer() e passamos o valor 100 para somar as cem
milhas que dirigimos entre comprar o carro e registrá-lo:
2013 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
Você pode modificar facilmente esse método para rejeitar incrementos
negativos, de modo que ninguém possa usar essa função para reduzir o
valor lido no hodômetro.
NOTA Podemos usar métodos como esse para controlar o modo como os usuários
de seu programa atualizam informações como o valor de leitura do hodômetro,
mas qualquer pessoa com acesso ao programa poderá definir o valor do
hodômetro com um valor qualquer acessando o atributo diretamente. Uma
segurança eficiente exige atenção extrema aos detalhes, além de verificações
básicas como essas mostradas aqui.
FAÇA VOCÊ MESMO
9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0. Crie
uma instância chamada restaurant a partir dessa classe. Apresente o número de
clientes atendidos pelo restaurante e, em seguida, mude esse valor e exiba-o
novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e mostre o
valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento.
9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à sua
classe User do Exercício 9.3 (página 226). Escreva um método chamado
increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts()
várias vezes. Exiba o valor de login_attempts para garantir que ele foi
incrementado de forma apropriada e, em seguida, chame
reset_login_attempts(). Exiba login_attempts novamente para garantir que
seu valor foi reiniciado com 0.
Herança
Nem sempre você precisará começar do zero para escrever uma classe. Se a
classe que você estiver escrevendo for uma versão especializada de outra
classe já criada, a herança poderá ser usada. Quando uma classe herda de
outra, ela assumirá automaticamente todos os atributos e métodos da
primeira classe. A classe original se chama classe-pai e a nova classe é a
classe-filha. A classe-filha herda todos os atributos e método de sua classe￾pai, mas também é livre para definir novos atributos e métodos próprios.
Método __init__() de umaclasse-filha
A primeira tarefa de Python ao criar uma instância de uma classe-filha é
atribuir valores a todos os atributos da classe-pai. Para isso, o método
__init__() de uma classe-filha precisa da ajuda de sua classe-pai.
Como exemplo, vamos modelar um carro elétrico. Um carro elétrico é
apenas um tipo específico de carro, portanto podemos basear nossa nova
classe ElectricCar na classe Car que escrevemos antes. Então só
precisaremos escrever código para os atributos e os comportamentos
específicos de carros elétricos.
Vamos começar criando uma versão simples da classe ElectricCar que faz
tudo que a classe Car faz:
electric_car.py
u class Car():
Uma tentativa simples de representar um carro.
def __init__(self, make, model, year):
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
long_name = str(self.year) + ' ' + self.make + ' ' + self.model
return long_name.title()
def read_odometer(self):
print("This car has " + str(self.odometer_reading) + " miles on
it.")
def update_odometer(self, mileage):
if mileage >= self.odometer_reading:
self.odometer_reading = mileage
else:
print("You can't roll back an odometer!")
def increment_odometer(self, miles):
self.odometer_reading += miles
v class ElectricCar(Car):
Representa aspectos específicos de veículos elétricos.
w def __init__(self, make, model, year):
Inicializa os atributos da classe-pai.
x super().__init__(make, model, year)
y my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
Em u começamos com Car. Quando criamos uma classe-filha, a classe-pai
deve fazer parte do arquivo atual e deve aparecer antes da classe-filha no
arquivo. Em v definimos a classe-filha, que é ElectricCar. O nome da
classe-pai deve ser incluído entre parênteses na definição da classe-filha. O
método __init__() em w aceita as informações necessárias para criar uma
instância de Car.
A função super() em x é uma função especial que ajuda Python a criar
conexões entre a classe-pai e a classe-filha. Essa linha diz a Python para
chamar o método __init__() da classe-pai de ElectricCar, que confere
todos os atributos da classe-pai a ElectricCar. O nome super é derivado de
uma convenção segundo a qual a classe-pai se chama superclasse e a classe￾filha é a subclasse.
Testamos se a herança está funcionando de forma apropriada tentando
criar um carro elétrico com o mesmo tipo de informação que fornecemos
quando criamos um carro comum. Em y criamos uma instância da classe
ElectricCar e a armazenamos em my_tesla. Essa linha chama o método
__init__() definido em ElectricCar que, por sua vez, diz a Python para
chamar o método __init__() definido na classe-pai Car. Fornecemos os
argumentos 'tesla', 'model s' e 2016.
Além de __init__() não há outros atributos nem métodos que sejam
particulares a um carro elétrico. A essa altura, estamos apenas garantindo
que o carro elétrico tenha o comportamento apropriado de Car:
2016 Tesla Model S
A instância de ElectricCar funciona exatamente como uma instância de
Car, portanto podemos agora começar a definir atributos e métodos
específicos aos carros elétricos.
HerançaemPython 2.7
Em Python 2.7, a herança é um pouco diferente. A classe ElectricCar teria
o seguinte aspecto:
class Car(object):
def __init__(self, make, model, year):
--trecho omitido--
class ElectricCar(Car):
def __init__(self, make, model, year):
super(ElectricCar, self).__init__(make, model, year)
--trecho omitido--
A função super() precisa de dois argumentos: uma referência à classe￾filha e o objeto self. Esses argumentos são necessários para ajudar Python
a fazer as conexões apropriadas entre as classes pai e filha. Quando usar
herança em Python 2.7, lembre-se de definir a classe-pai usando a sintaxe
object também.
Definindo atributosemétodos daclasse-filha
Depois que tiver uma classe-filha que herde de uma classe-pai, você pode
adicionar qualquer atributo ou método novo necessários para diferenciar a
classe-filha da classe-pai.
Vamos acrescentar um atributo que seja específico aos carros elétricos
(uma bateria, por exemplo) e um método para mostrar esse atributo.
Armazenaremos a capacidade da bateria e escreveremos um método que
mostre uma descrição dela:
class Car():
--trecho omitido--
class ElectricCar(Car):
Representa aspectos específicos de veículos elétricos.
def __init__(self, make, model, year):

Inicializa os atributos da classe pai
Em seguida, inicializa os atributos específicos de um carro
elétrico

super().__init__(make, model, year)
u self.battery_size = 70
v def describe_battery(self):
Exibe uma frase que descreve a capacidade da bateria.
print("This car has a " + str(self.battery_size) + "-kWh
battery.")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
Em u adicionamos um novo atributo self.battery_size e definimos seu
valor inicial, por exemplo, com 70. Esse atributo será associado a todas as
instâncias criadas a partir da classe ElectricCar, mas não será associado a
nenhuma instância de Car. Também adicionamos um método chamado
describe_battery(), que exibe informações sobre a bateria em v. Quando
chamamos esse método, temos uma descrição que é claramente específica
de um carro elétrico:
2016 Tesla Model S
This car has a 70-kWh battery.
Não há limites de quanto você pode especializar a classe ElectricCar.
Você pode acrescentar a quantidade de atributos e métodos de que precisar
para modelar um carro elétrico com qualquer grau de precisão necessário.
Um atributo ou método que possa pertencer a qualquer carro, isto é, que
não seja específico de um carro elétrico, deve ser adicionado à classe Car,
em vez de ser colocado na classe ElectricCar. Então qualquer pessoa que
usar a classe Car terá essa funcionalidade disponível também, e a classe
ElectricCar conterá apenas códigos para as informações e comportamentos
específicos de veículos elétricos.
Sobrescrevendométodos daclasse-pai
Qualquer método da classe-pai que não se enquadre no que você estiver
tentando modelar com a classe-filha pode ser sobrescrito. Para isso, defina
um método na classe-filha com o mesmo nome do método da classe-pai
que você deseja sobrescrever. Python desprezará o método da classe-pai e
só prestará atenção no método definido na classe-filha.
Suponha que a classe Car tenha um método chamado fill_gas_tank().
Esse método não faz sentido para um veículo totalmente elétrico, portanto
você pode sobrescrever esse método. Eis uma maneira de fazer isso:
def ElectricCar(Car):
--trecho omitido--
def fill_gas_tank():
Carros elétricos não têm tanques de gasolina.
print("This car doesn't need a gas tank!")
Agora, se alguém tentar chamar fill_gas_tank() com um carro elétrico,
Python ignorará esse método de Car e executará o código apresentado em
seu lugar. Ao usar herança, você pode fazer suas classes-filhas preservarem
o que for necessário e sobrescrever tudo o que não for utilizado da classe-
pai.
Instâncias como atributos
Ao modelar algo do mundo real no código você poderá perceber que está
adicionando cada vez mais detalhes em uma classe. Poderá notar que há
uma lista crescente de atributos e métodos e que seus arquivos estão
começando a ficar extensos. Nessas situações, talvez você perceba que
parte de uma classe pode ser escrita como uma classe separada. Sua classe
maior poderá ser dividida em partes menores que funcionem em conjunto.
Por exemplo, se continuarmos adicionando detalhes à classe ElectricCar,
podemos perceber que estamos acrescentando muitos atributos e métodos
específicos à bateria do carro. Se percebermos que isso está acontecendo,
podemos parar e transferir esses atributos e métodos para uma classe
diferente chamada Battery. Então podemos usar uma instância de Battery
como atributo da classe ElectricCar:
class Car():
--trecho omitido--
u class Battery():
Uma tentativa simples de modelar uma bateria para um carro
elétrico.
v def __init__(self, battery_size=70):
Inicializa os atributos da bateria.
self.battery_size = battery_size
w def describe_battery(self):
Exibe uma frase que descreve a capacidade da bateria.
print("This car has a " + str(self.battery_size) + "-kWh
battery.")
class ElectricCar(Car):
Representa aspectos específicos de veículos elétricos.
def __init__(self, make, model, year):

Inicializa os atributos da classe-pai
Em seguida, inicializa os atributos específicos de um carro
elétrico

super().__init__(make, model, year)
x self.battery = Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
Em u definimos uma nova classe chamada Battery que não herda de
nenhuma outra classe. O método __init__() em v tem um parâmetro,
battery_size, além de self. É um parâmetro opcional que define a
capacidade da bateria com 70 se nenhum valor for especificado. O método
describe_battery() também foi transferido para essa classe w.
Na classe ElectricCar, adicionamos um atributo chamado self.battery x.
Essa linha diz a Python para criar uma nova instância de Battery (com
capacidade default de 70, pois não estamos especificando nenhum valor) e
armazenar essa instância no atributo self.battery. Isso acontecerá sempre
que o método __init__() for chamado; qualquer instância de ElectricCar
agora terá uma instância de Battery criada automaticamente.
Criamos um carro elétrico e o armazenamos na variável my_tesla.
Quando quisermos descrever a bateria, precisaremos trabalhar com o
atributo battery do carro:
my_tesla.battery.describe_battery()
Essa linha diz a Python para usar a instância my_tesla, encontrar seu
atributo battery e chamar o método describe_battery() associado à
instância de Battery armazenada no atributo.
A saída é idêntica àquela que vimos antes:
2016 Tesla Model S
This car has a 70-kWh battery.
Parece ser bastante trabalho extra, mas agora podemos descrever a
bateria com quantos detalhes quisermos sem deixar a classe ElectricCar
entulhada. Vamos acrescentar outro método em Battery que informe a
distância que o carro pode percorrer de acordo com a capacidade da
bateria:
class EuroCalc
--trecho omitido--
class Battery():
--trecho omitido--
u def get_range(self):
Exibe uma frase sobre a distância que o carro é capaz de
percorrer com essa bateria.
if self.battery_size == 70:
range = 240
elif self.battery_size == 85:
range = 270
message = "This car can go approximately " + str(range)
message += " miles on a full charge."
print(message)
class ElectricCar(Car):
--trecho omitido--
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
v my_tesla.battery.get_range()
O novo método get_range() em u efetua uma análise simples. Se a
capacidade da bateria for de 70 kWh, get_range() define o alcance do carro
com 240 milhas; se a capacidade for de 85 kWh, o alcance será definido
com 270 milhas. Esse valor é então apresentado. Quando quisermos usar
esse método, novamente, devemos chamá-lo por meio do atributo battery
do carro v.
A saída nos informa a distância que o carro é capaz de percorrer de
acordo com a capacidade de sua bateria.
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
Modelando objetos domundo real
À medida que começar a modelar itens mais complexos como carros
elétricos, você vai ter que encarar perguntas interessantes. A distância que
um carro elétrico é capaz de percorrer é uma propriedade da bateria ou do
carro? Se estivermos descrevendo apenas um carro, provavelmente não
haverá problemas em manter a associação do método get_range() com a
classe Battery. Entretanto, se estivermos descrevendo toda uma linha de
carros de um fabricante, é provável que vamos querer transferir get_range()
para a classe ElectricCar. O método get_range() continuaria verificando a
capacidade da bateria antes de determinar a distância que o carro é capaz
de percorrer, mas informaria um alcance específico para o tipo de carro
com o qual está associado. De modo alternativo, poderíamos manter a
associação entre o método get_range() e a bateria, mas passaríamos um
parâmetro a ele, por exemplo, car_model. O método get_range() então
informaria a distância que o carro poderá percorrer de acordo com a
capacidade da bateria e o modelo do carro.
Isso leva você a um ponto interessante em seu crescimento como
programador. Quando tiver que encarar questões como essa, você estará
pensando em um nível lógico mais alto, em vez de se concentrar no nível
da sintaxe. Estará pensando não em Python, mas no modo de representar o
mundo real como um código. Quando atingir esse ponto, você perceberá
que, muitas vezes, não há abordagens certas ou erradas para modelar
situações do mundo real. Algumas abordagens são mais eficientes que
outras, mas descobrir as representações mais eficientes exige prática. Se seu
código estiver funcionando conforme desejado, é sinal de que você está se
saindo bem! Não desanime se perceber que está destruindo suas classes e
reescrevendo-as várias vezes usando diferentes abordagens. No caminho
para escrever um código preciso e eficiente, todos passam por esse
processo.
FAÇA VOCÊ MESMO
9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma
classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer versão da
classe funcionará; basta escolher aquela de que você mais gosta. Adicione um
atributo chamado flavors que armazene uma lista de sabores de sorvete. Escreva
um método para mostrar esses sabores. Crie uma instância de IceCreamStand e
chame esse método.
9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma classe
chamada Admin que herde da classe User escrita no Exercício 9.3 (página 226),
ou no Exercício 9.5 (página 232). Adicione um atributo privileges que armazene
uma lista de strings como "can add post", "can delete post" "can ban user",
e assim por diante. Escreva um método chamado show_privileges() que liste o
conjunto de privilégios de um administrador. Crie uma instância de Admin e chame
seu método.
9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie uma
instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.
9.9 – Upgrade de bateria: Use a última versão de electric_car.py desta seção.
Acrescente um método chamado upgrade_battery() na classe Battery. Esse
método deve verificar a capacidade da bateria e defini-la com 85 se o valor for
diferente. Crie um carro elétrico com uma capacidade de bateria default, chame
get_range() uma vez e, em seguida, chame get_range() uma segunda vez após
fazer um upgrade da bateria. Você deverá ver um aumento na distância que o
carro é capaz de percorrer.
Importando classes
À medida que acrescentar mais funcionalidades às classes, seus arquivos
ficarão maiores, mesmo quando usar herança de forma apropriada. Para
estar de acordo com a filosofia geral de Python, quanto menos entulhados
estiverem seus arquivos, melhor será. Para ajudar, Python permite
armazenar classes em módulos e então importar as classes necessárias em
seu programa principal.
Importando uma únicaclasse
Vamos criar um módulo que contenha apenas a classe Car. Isso cria um
problema sutil de nomenclatura: já temos um arquivo chamado car.py
neste capítulo, mas esse módulo deve se chamar car.py porque contém
código que representa um carro. Resolveremos esse problema de
nomenclatura armazenando a classe Car em um módulo chamado car.py,
substituindo o arquivo car.py que estávamos usando antes. A partir de
agora, qualquer programa que use esse módulo precisará de um nome de
arquivo mais específico, por exemplo, my_car.py. Eis o arquivo car.py
somente com o código da classe Car:
car.py
u Uma classe que pode ser usada para representar um carro.
class Car():
Uma tentativa simples de representar um carro.
def __init__(self, make, model, year):
Inicializa os atributos que descrevem um carro.
self.make = make
self.model = model
self.year = year
self.odometer_reading = 0
def get_descriptive_name(self):
Devolve um nome descritivo formatado de modo elegante.
long_name = str(self.year) + ' ' + self.make + ' ' + self.model
return long_name.title()
def read_odometer(self):
Exibe uma frase que mostra a milhagem do carro.
print("This car has " + str(self.odometer_reading) + " miles on
it.")
def update_odometer(self, mileage):

Define o valor de leitura do hodômetro com o valor especificado
Rejeita alteração se for tentativa de definir um valor menor
para o hodômetro

if mileage >= self.odometer_reading:
self.odometer_reading = mileage
else:
print("You can't roll back an odometer!")
def increment_odometer(self, miles):
Soma a quantidade especificada ao valor de leitura do
hodômetro.
self.odometer_reading += miles
Em u incluímos uma docstring no nível de módulo que descreve
rapidamente o conteúdo desse módulo. Escreva uma docstring para cada
módulo que criar.
Agora criamos um arquivo separado chamado my_car.py. Esse arquivo
importará a classe Car e então criará uma instância dessa classe:
my_car.py
u from car import Car
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
A instrução import em u diz a Python para abrir o módulo car e importar
a classe Car. Agora podemos usar a classe Car como se ela estivesse definida
nesse arquivo. A saída é a mesma que vimos antes:
2016 Audi A4
This car has 23 miles on it.
Importar classes é uma maneira eficiente de programar. Imagine o
tamanho que esse programa teria se a classe Car inteira estivesse incluída.
Quando transferimos a classe para um módulo e o importamos,
continuamos usufruindo da mesma funcionalidade, porém o arquivo com
o programa principal permanece limpo e fácil de ler. Também
armazenamos a maior parte da lógica em arquivos separados; depois que
suas classes estiverem funcionando conforme esperado, você poderá deixar
de lado esses arquivos e se concentrar na lógica de mais alto nível de seu
programa principal.
Armazenando várias classesemummódulo
Você pode armazenar tantas classes quantas forem necessárias em um
único módulo, embora cada classe em um módulo deva estar, de algum
modo, relacionada com outra classe. Ambas as classes, Battery e
ElectricCar, ajudam a representar carros, portanto vamos acrescentá-las ao
módulo car.py:
car.py
Um conjunto de classes usado para representar carros à gasolina e
elétricos.
class Car():
--trecho omitido--
class Battery():
Uma tentativa simples de modelar uma bateria para um carro
elétrico.
def __init__(self, battery_size=60):
Inicializa os atributos da bateria.
self.battery_size = battery_size
def describe_battery(self):
Exibe uma frase que descreve a capacidade da bateria.
print("This car has a " + str(self.battery_size) + "-kWh
battery.")
def get_range(self):
Exibe frase sobre a distância que o carro pode percorrer com
essa bateria.
if self.battery_size == 70:
range = 240
elif self.battery_size == 85:
range = 270
message = "This car can go approximately " + str(range)
message += " miles on a full charge."
print(message)
class ElectricCar(Car):
Modela aspectos de um carro específicos de veículos
elétricos.
def __init__(self, make, model, year):

Inicializa os atributos da classe-pai.
Em seguida, inicializa os atributos específicos de um carro
elétrico.

super().__init__(make, model, year)
self.battery = Battery()
Agora podemos criar um novo arquivo chamado my_electric_car.py,
importar a classe ElectricCar e criar um carro elétrico:
my_electric_car.py
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
Esse código gera a mesma saída que vimos antes, embora a maior parte
da lógica esteja oculta em um módulo:
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
Importando várias classes de ummódulo
Podemos importar quantas classes forem necessárias em um arquivo de
programa. Se quisermos criar um carro comum e um carro elétrico no
mesmo arquivo, precisaremos importar tanto a classe Car quanto a classe
ElectricCar:
my_cars.py
u from car import Car, ElectricCar
v my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
w my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
Importe várias classes de um módulo separando cada classe com uma
vírgula u. Depois que importar as classes de que precisará, você poderá
criar quantas instâncias de cada classe quantas forem necessárias.
Nesse exemplo, criamos um Volkswagen Beetle comum em v e um Tesla
Roadster elétrico em w:
2016 Volkswagen Beetle
2016 Tesla Roadster
Importando ummódulo completo
Também podemos importar um módulo completo e então acessar as
classes necessárias usando a notação de ponto. Essa abordagem é simples e
resulta em um código fácil de ler. Como toda chamada que cria uma
instância de uma classe inclui o nome do módulo, você não terá conflito de
nomes com qualquer nome usado no arquivo atual.
Eis a aparência do código para importar o módulo car inteiro e então
criar um carro comum e um carro elétrico:
my_cars.py
u import car
v my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
w my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
Em u importamos o módulo car inteiro. Então acessamos as classes
necessárias por meio da sintaxe nome_do_módulo.nome_da_classe. Em v
criamos novamente um Volkswagen Beetle e em w, um Tesla Roadster.
Importando todasas classes de ummódulo
Você pode importar todas as classes de um módulo usando a sintaxe a
seguir:
from nome_do_módulo import *
Esse método não é recomendado por dois motivos. Em primeiro lugar, é
conveniente ser capaz de ler as instruções import no início de um arquivo e
ter uma noção clara de quais classes um programa utiliza. Com essa
abordagem, não fica claro quais são as classes do módulo que você está
usando. Essa abordagem também pode resultar em confusão com nomes
presentes no arquivo. Se você acidentalmente importar uma classe com o
mesmo nome que outro item em seu arquivo de programa, poderá gerar
erros difíceis de serem diagnosticados. Estou mostrando essa opção aqui
porque, embora não seja uma abordagem recomendada, é provável que
você vá vê-la no código de outras pessoas.
Se precisar importar muitas classes de um módulo, é melhor importar o
módulo todo e usar a sintaxe nome_do_módulo.nome_da_classe. Você não verá
todas as classes usadas no início do arquivo, mas verá claramente em que
lugares o módulo é utilizado no programa. Possíveis conflitos de nomes
que possam ocorrer ao importar todas as classes de um módulo também
serão evitados.
Importando ummódulo emummódulo
Às vezes, você vai querer espalhar suas classes em vários módulos para
impedir que um arquivo cresça demais e evitar a armazenagem de classes
não relacionadas no mesmo módulo. Ao armazenar suas classes em vários
módulos, você poderá descobrir que uma classe em um módulo depende
de uma classe que está em outro módulo. Se isso acontecer, importe a
classe necessária no primeiro módulo.
Por exemplo, vamos armazenar a classe Car em um módulo e as classes
ElectricCar e Battery em um módulo separado. Criaremos um novo
módulo chamado electric_car.py – substituindo o arquivo electric_car.py
que criamos antes – e copiaremos apenas as classes Battery e ElectricCar
para esse arquivo:
electric_car.py
Um conjunto de classes que pode ser usado para representar carros
elétricos.
u from car import Car
class Battery():
--trecho omitido--
class ElectricCar(Car):
--trecho omitido--
A classe ElectricCar precisa ter acesso à sua classe-pai Car, portanto
importamos Car diretamente para o módulo em u. Se esquecermos de
colocar essa linha, Python gerará um erro quando tentarmos criar uma
instância de ElectricCar. Também precisamos atualizar o módulo Car para
que ele contenha apenas a classe Car:
car.py
Uma classe que pode ser usada para representar um carro.
class Car():
--trecho omitido--
Agora podemos fazer a importação de cada módulo separadamente e
criar o tipo de carro que for necessário:
my_cars.py
u from car import Car
from electric_car import ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
Em u importamos Car de seu módulo e ElectricCar de seu módulo. Em
seguida, criamos um carro comum e um carro elétrico. Os dois tipos de
carro são criados corretamente:
2016 Volkswagen Beetle
2016 Tesla Roadster
Definindo o seu próprio fluxo detrabalho
Como podemos ver, Python oferece muitas opções para estruturar o código
em um projeto de grande porte. É importante conhecer todas essas
possibilidades para que você possa determinar a melhor maneira de
organizar seus projetos, assim como entender o projeto de outras pessoas.
Quando estiver começando a programar, mantenha a estrutura de seu
código simples. Procure fazer tudo em um só arquivo e transfira suas
classes para módulos separados depois que tudo estiver funcionando. Se
gostar do modo como os módulos e os arquivos interagem, experimente
armazenar suas classes em módulos quando iniciar um projeto. Encontre
uma abordagem que permita escrever um código que funcione, e comece a
partir daí.
FAÇA VOCÊ MESMO
9.10 – Importando Restaurant: Usando sua classe Restaurant mais recente,
armazene-a em um módulo. Crie um arquivo separado que importe Restaurant.
Crie uma instância de Restaurant e chame um de seus métodos para mostrar que
a instrução import funciona de forma apropriada.
9.11 – Importando Admin: Comece com seu programa do Exercício 9.8 (página
241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
arquivo separado e uma instância de Admin e chame show_privileges() para
mostrar que tudo está funcionando de forma apropriada.
9.12 – Vários módulos: Armazene a classe User em um módulo e as classes
Privileges e Admin em um módulo separado. Em outro arquivo, crie uma instância
de Admin e chame show_privileges() para mostrar que tudo continua
funcionando de forma apropriada.
Biblioteca-padrão de Python
A biblioteca-padrão de Python é um conjunto de módulos incluído em
todas as instalações de Python. Agora que temos uma compreensão básica
de como as classes funcionam, podemos começar a usar módulos como
esses, escritos por outros programadores. Podemos usar qualquer função
ou classe da biblioteca-padrão incluindo uma instrução import simples no
início do arquivo. Vamos analisar a classe OrderedDict do módulo
collections.
Os dicionários permitem associar informações, mas eles não mantêm um
controle da ordem em que os pares chave-valor são acrescentados. Se você
estiver criando um dicionário e quiser manter o controle da ordem em que
os pares chave-valor são adicionados, a classe OrderedDict do módulo
collections poderá ser usada. Instâncias da classe OrderedDict se
comportam quase do mesmo modo que os dicionários, exceto que mantêm
o controle da ordem em que os pares chave-valor são adicionados.
Vamos retomar o exemplo favorite_languages.py do Capítulo 6. Dessa
vez, vamos manter o controle da ordem em que as pessoas responderam à
enquete:
favorite_languages.py
u from collections import OrderedDict
v favorite_languages = OrderedDict()
w favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
x for name, language in favorite_languages.items():
print(name.title() + "'s favorite language is " +
language.title() + ".")
Começamos importando a classe OrderedDict do módulo collections em
u. Em v criamos uma instância da classe OrderedDict e a armazenamos em
favorite_languages. Observe que não há chaves; a chamada a OrderedDict()
cria um dicionário ordenado vazio para nós e o armazena em
favorite_languages. Então adicionamos cada nome e linguagem em
favorite_languages, um de cada vez w. Agora, quando percorremos
favorite_languages com um laço em x, sabemos que sempre teremos as
respostas na ordem em que os itens foram adicionados:
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
É uma ótima classe para conhecer, pois combina a principal vantagem
das listas (preservar a ordem original) com o principal recurso dos
dicionários (associar informações). Quando começar a modelar situações
do mundo real que sejam de seu interesse, é provável que você vá se
deparar com uma situação em que um dicionário ordenado seja
exatamente o que você precisa. À medida que conhecer melhor a
biblioteca-padrão, você passará a ter familiaridade com vários módulos
como esse, que ajudam a tratar situações comuns.
NOTA Você também pode fazer download de módulos de fontes externas. Veremos
vários desses exemplos na Parte II, quando precisaremos de módulos externos
para concluir cada projeto.
FAÇA VOCÊ MESMO
9.13 – Reescrevendo o programa com OrderedDict: Comece com o Exercício
6.4 (página 155), em que usamos um dicionário-padrão para representar um
glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
que a ordem da saída coincida com a ordem em que os pares chave-valor foram
adicionados ao dicionário.
9.14 – Dados: O módulo random contém funções que geram números aleatórios
de várias maneiras. A função randint() devolve um inteiro no intervalo
especificado por você. O código a seguir devolve um número entre 1 e 6:
from random import randint
x = randint(1, 6)
Crie uma classe Die com um atributo chamado sides, cujo valor default é 6.
Escreva um método chamado roll_die() que exiba um número aleatório entre 1 e
o número de lados do dado. Crie um dado de seis dados e lance-o dez vezes.
Crie um dado de dez lados e outro de vinte lados. Lance cada dado dez vezes.
9.15 – Módulo Python da semana: Um excelente recurso para explorar a
biblioteca-padrão de Python é um site chamado Python Module of the Week
(Módulo Python da semana). Acesse http://pymotw.com/ e observe a tabela de
conteúdo. Encontre um módulo que pareça ser interessante e leia a sua descrição
ou explore a documentação dos módulos collections e random.
Estilizando classes
Vale a pena esclarecer algumas questões ligadas à estilização de classes, em
especial quando seus programas se tornarem mais complexos.
Os nomes das classes devem ser escritos com CamelCaps. Para isso, cada
palavra do nome deve ter a primeira letra maiúscula, e você não deve usar
underscores. Nomes de instâncias e de módulos devem ser escritos com
letras minúsculas e underscores entre as palavras.
Toda classe deve ter uma docstring logo depois de sua definição. A
docstring deve conter uma breve descrição do que a classe faz, e as mesmas
convenções de formatação devem ser usadas para escrever docstrings em
funções. Cada módulo também deve ter uma docstring que descreva para
que servem as classes de um módulo.
Podemos usar linhas em branco para organizar o código, mas você não
deve utilizá-las de modo excessivo. Em uma classe, podemos usar uma
linha em branco entre os métodos; em um módulo, podemos usar duas
linhas em branco para separar as classes.
Se houver necessidade de importar um módulo da biblioteca-padrão e
um módulo escrito por você, coloque a instrução de importação do
módulo da biblioteca-padrão antes. Então acrescente uma linha em branco
e a instrução de importação para o módulo que você escreveu. Em
programas com várias instruções de importação, essa convenção facilita ver
a origem dos diferentes módulos utilizados pelo programa.
Resumo
Neste capítulo, vimos como escrever nossas próprias classes. Aprendemos
a armazenar informações em uma classe usando atributos e a escrever
métodos que conferem o comportamento necessário às suas classes. Vimos
como escrever métodos __init__() que criam instâncias de suas classes
com os atributos específicos que desejamos ter. Aprendemos a modificar os
atributos de uma instância diretamente e por meio de métodos. Vimos que
a herança pode simplificar a criação de classes relacionadas umas às outras
e aprendemos a usar instâncias de uma classe como atributos de outra para
deixá-las mais simples.
Aprendemos a armazenar classes em módulos e a importar as classes
necessárias nos arquivos em que elas serão usadas para deixar seus projetos
organizados. Começamos a conhecer a biblioteca-padrão de Python e
vimos um exemplo com a classe OrderedDict do módulo collections. Por
fim, vimos como estilizar classes usando as convenções de Python.
No Capítulo 10, aprenderemos a trabalhar com arquivos para que
possamos salvar o trabalho feito por você e pelos usuários de seu
programa. Também conheceremos as exceções: uma classe Python especial,
concebida para ajudar você a responder a erros quando esses surgirem.
10
ARQUIVOS E EXCEÇÕES
Agora que você já dominou as habilidades básicas
necessárias para escrever programas organizados, fáceis
de usar, é hora de pensar em deixar seus programas mais
relevantes e utilizáveis. Neste capítulo aprenderemos a
trabalhar com arquivos para que seus programas possam
analisar rapidamente muitos dados.
Veremos como tratar erros a fim de que seus programas não falhem
quando se depararem com situações inesperadas. Conheceremos as
exceções – objetos Python especiais para administrar erros que surgirem
enquanto um programa estiver executando. Também conheceremos o
módulo json, que permite salvar dados de usuário para que não sejam
perdidos quando seu programa parar de executar.
Aprender a trabalhar com arquivos e a salvar dados deixará seus
programas mais fáceis de usar. Os usuários poderão escolher quais dados
devem fornecer e quando. As pessoas podem executar seu programa, fazer
alguma tarefa e então fechá-lo e retomá-lo mais tarde, do ponto em que
pararam. Aprender a tratar exceções ajudará você a lidar com situações em
que os arquivos não existam e com outros problemas que possam fazer
seus programas falharem. Isso deixará seus programas mais robustos
quando dados ruins forem encontrados, sejam eles provenientes de erros
inocentes ou de tentativas maliciosas de fazer seus programas falharem.
Com as habilidades desenvolvidas neste capítulo, você deixará seus
programas mais aplicáveis, utilizáveis e estáveis.
Lendo dados de umarquivo
Uma quantidade incrível de dados está disponível em arquivos-texto. Os
arquivos-texto podem conter dados meteorológicos, de tráfego,
socioeconômicos, trabalhos literários e outros. Ler dados de um arquivo é
particularmente útil em aplicações de análise de dados, mas também se
aplica a qualquer situação em que você queira analisar ou modificar
informações armazenadas em um arquivo. Por exemplo, podemos escrever
um programa que leia o conteúdo de um arquivo-texto e reescreva o
arquivo com uma formatação que permita a um navegador exibi-lo.
Quando quiser trabalhar com as informações de um arquivo-texto, o
primeiro passo será ler o arquivo em memória. Você pode ler todo o
conteúdo de um arquivo ou pode trabalhar com uma linha de cada vez.
Lendo umarquivo inteiro
Para começar, precisamos de um arquivo com algumas linhas de texto.
Vamos iniciar com um arquivo que contenha o valor de pi com trinta casas
decimais, dez casas por linha:
pi_digits.txt
3.1415926535
8979323846
2643383279
Para testar esses exemplos por conta própria, você pode inserir essas
linhas em um editor e salvar o arquivo como pi_digits.txt, ou pode fazer o
download do arquivo a partir da página de recursos do livro em
https://www.nostarch.com/pythoncrashcourse/. Salve o arquivo no mesmo
diretório em que você armazenará os programas deste capítulo.
Aqui está um programa que abre esse arquivo, lê seus dados e exibe o
conteúdo na tela:
file_reader.py
with open('pi_digits.txt') as file_object:
contents = file_object.read()
print(contents)
Muitas atividades acontecem na primeira linha desse programa. Vamos
começar observando a função open(). Para realizar qualquer tarefa com um
arquivo, mesmo que seja apenas exibir o seu conteúdo, você precisará
inicialmente abrir o arquivo para acessá-lo. A função open() precisa de um
argumento: o nome do arquivo que você quer abrir. Python procura esse
arquivo no diretório em que o programa executando no momento está
armazenado. Nesse exemplo, file_reader.py está executando, portanto
Python procura pi_digits.txt no diretório em que o arquivo file_reader.py
está armazenado. A função open() devolve um objeto que representa o
arquivo. Nesse caso, open('pi_digits.txt') devolve um objeto que
representa pi_digits.txt. Python armazena esse objeto em file_object, com
o qual trabalharemos posteriormente no programa.
A palavra reservada with fecha o arquivo depois que não for mais
necessário acessá-lo. Observe como chamamos open() nesse programa, mas
não chamamos close(). Você poderia abrir e fechar o arquivo chamando
open() e close(), mas se um bug em seu programa impedir que a instrução
close() seja executada, o arquivo não será fechado. Isso pode parecer
trivial, mas arquivos indevidamente fechados podem provocar perda de
dados ou estes podem ser corrompidos. Além disso, se close() for
chamado cedo demais em seu programa, você se verá tentando trabalhar
com um arquivo fechado (um arquivo que não pode ser acessado), o que
resultará em mais erros. Nem sempre é fácil saber exatamente quando
devemos fechar um arquivo, mas com a estrutura mostrada aqui, Python
descobrirá isso para você. Tudo que você precisa fazer é abrir o arquivo e
trabalhar com ele conforme desejado, com a confiança de que Python o
fechará automaticamente no momento certo.
Depois que tivermos um objeto arquivo que represente pi_digits.txt,
usamos o método read() na segunda linha de nosso programa para ler todo
o conteúdo do arquivo e armazená-lo em uma longa string em contents.
Quando exibimos o valor de contents, vemos o arquivo-texto completo:
3.1415926535
8979323846
2643383279
A única diferença entre essa saída e o arquivo original é a linha em branco
extra no final da saída. A linha em branco aparece porque read() devolve
uma string vazia quando alcança o final do arquivo; essa string vazia
aparece como uma linha em branco. Se quiser remover essa linha em
branco extra, rstrip() pode ser usada na instrução print:
with open('pi_digits.txt') as file_object:
contents = file_object.read()
print(contents.rstrip())
Lembre-se de que o método rstrip() de Python remove qualquer
caractere branco do lado direito de uma string. Agora a saída será
exatamente igual ao conteúdo do arquivo original:
3.1415926535
8979323846
2643383279
Paths dearquivo
Quando um nome de arquivo simples como pi_digits.txt é passado para a
função open(), Python observa o diretório em que o arquivo executado no
momento (isto é, seu arquivo de programa .py) está armazenado.
Às vezes, dependendo de como o seu trabalho estiver organizado, o
arquivo que você quer abrir não estará no mesmo diretório que o seu
arquivo de programa. Por exemplo, você pode armazenar seus arquivos de
programa em uma pasta chamada python_work; nessa pasta pode haver
outra pasta chamada text_files para distinguir seus arquivos de programa
dos arquivos-texto que eles manipulam. Apesar de text_files estar em
python_work, simplesmente passar o nome de um arquivo que está em
text_files para open() não funcionará, pois Python procurará o arquivo
apenas em python_work; ele não prosseguirá procurando em text_files.
Para fazer Python abrir arquivos de um diretório que não seja aquele em
que seu arquivo de programa está armazenado, é preciso fornecer um path
de arquivo, que diz a Python para procurar em um local específico de seu
sistema.
Como text_files está em python_work, você pode usar um path de
arquivo relativo para abrir um arquivo em text_files. Um path de arquivo
relativo diz a Python para procurar um local especificado, relativo ao
diretório em que o arquivo de programa em execução no momento está
armazenado. No Linux e no OS X, você escreveria o seguinte:
with open('text_files/nome_do_arquivo.txt') as file_object:
Essa linha diz a Python para procurar o arquivo .txt desejado na pasta
text_files e supõe que essa pasta está localizada em python_work (e está).
Em sistemas Windows, use uma barra invertida () no lugar da barra para a
frente (/) no path do arquivo:
with open('text_filesnome_do_arquivo.txt') as file_object:
Você também pode dizer a Python exatamente em que local está o
arquivo em seu computador, não importando o lugar em que o programa
em execução no momento esteja armazenado. Isso é chamado de path
absoluto do arquivo. Utilize um path absoluto se um path relativo não
funcionar. Por exemplo, se você colocou text_files em alguma pasta
diferente de python_work – por exemplo, em uma pasta chamada
other_files – então simplesmente passar o path
'text_files/nome_do_arquivo.txt' para open() não funcionará porque
Python procurará esse local somente em python_work. Você precisará
fornecer um path completo para deixar claro em que lugar você quer que
Python procure.
Paths absolutos geralmente são mais longos que paths relativos, portanto
é conveniente armazená-los em uma variável e então passar essa variável
para open(). No Linux e no OS X, paths absolutos têm o seguinte aspecto:
file_path =
'/home/ehmatthes/other_files/text_files/nome_do_arquivo.txt'
with open(file_path) as file_object:
No Windows, eles se parecem com:
file_path =
'C:Usersehmatthesother_filestext_filesnome_do_arquivo.txt'
with open(file_path) as file_object:
Ao usar paths absolutos, podemos ler arquivos de qualquer lugar do
sistema. Por enquanto, é mais fácil armazenar arquivos no mesmo diretório
em que estão seus arquivos de programa ou em uma pasta como text_files
no diretório em que estiverem seus arquivos de programa.
NOTA Sistemas Windows às vezes interpretam corretamente as barras para a frente
nos paths de arquivo. Se você usa Windows e não está obtendo os resultados
esperados, tente usar barras invertidas.
Lendo dados linhaalinha
Quando estiver lendo um arquivo, com frequência você vai querer analisar
cada linha do arquivo. Talvez você esteja procurando determinada
informação no arquivo ou queira modificar o texto do arquivo de alguma
maneira. Por exemplo, você pode ler um arquivo de dados meteorológicos
e trabalhar com qualquer linha que inclua a palavra ensolarado na
descrição da previsão do tempo para esse dia. Em uma notícia, talvez você
queira procurar todas as linhas com a tag <headline> e reescrever essa linha
com um tipo específico de formatação.
Podemos usar um laço for no objeto arquivo para analisar cada uma de
suas linhas, uma de cada vez:
file_reader.py
u filename = 'pi_digits.txt'
v with open(filename) as file_object:
w for line in file_object:
print(line)
Em u armazenamos o nome do arquivo que estamos lendo em uma
variável filename. Essa é uma convenção comum quando trabalhamos com
arquivos. Como a variável filename não representa o arquivo propriamente
dito – é apenas uma string que diz a Python em que lugar o arquivo se
encontra – você pode facilmente trocar 'pi_digits.txt' pelo nome de outro
arquivo com o qual você queira trabalhar. Depois da chamada a open(), um
objeto que representa o arquivo e seu conteúdo é armazenado na variável
file_object v. Novamente, usamos a sintaxe with para deixar Python abrir
e fechar o arquivo de modo apropriado. Para analisar o conteúdo do
arquivo, trabalhamos com cada linha do arquivo percorrendo o objeto
arquivo em um laço w.
Quando exibimos cada linha, encontramos outras linhas em branco:
3.1415926535
8979323846
2643383279
Essas linhas em branco aparecem porque um caractere invisível de
quebra de linha está no final de cada linha do arquivo-texto. A instrução
print adiciona a sua própria quebra de linha sempre que a chamamos,
portanto acabamos com dois caracteres de quebra de linha no final de cada
linha: um do arquivo e outro da instrução print. Se usarmos rstrip() em
cada linha na instrução print, eliminamos essas linhas em branco extras:
filename = 'pi_digits.txt'
with open(filename) as file_object:
for line in file_object:
print(line.rstrip())
Agora a saída é igual ao conteúdo do arquivo novamente:
3.1415926535
8979323846
2643383279
Criando umalista delinhas de umarquivo
Quando usamos with, o objeto arquivo devolvido por open() estará
disponível somente no bloco with que o contém. Se quiser preservar o
acesso ao conteúdo de um arquivo fora do bloco with, você pode
armazenar as linhas do arquivo em uma lista dentro do bloco e então
trabalhar com essa lista. Pode processar partes do arquivo imediatamente e
postergar parte do processamento de modo que seja feito mais tarde no
programa.
O exemplo a seguir armazena as linhas de pi_digits.txt em uma lista no
bloco with e, em seguida, exibe as linhas fora desse bloco:
filename = 'pi_digits.txt'
with open(filename) as file_object:
u lines = file_object.readlines()
v for line in lines:
print(line.rstrip())
Em u o método readlines() armazena cada linha do arquivo em uma
lista. Essa lista é então armazenada em lines, com a qual podemos
continuar trabalhando depois que o bloco with terminar. Em v usamos um
laço for simples para exibir cada linha de lines. Como cada item de lines
corresponde a uma linha do arquivo, a saída será exatamente igual ao
conteúdo do arquivo.
Trabalhando como conteúdo de umarquivo
Depois de ler um arquivo em memória, você poderá fazer o que quiser com
esses dados; desse modo, vamos explorar rapidamente os dígitos de pi. Em
primeiro lugar, tentaremos criar uma única string contendo todos os
dígitos do arquivo, sem espaços em branco:
pi_string.py
filename = 'pi_digits.txt'
with open(filename) as file_object:
lines = file_object.readlines()
u pi_string = ''
v for line in lines:
pi_string += line.rstrip()
w print(pi_string)
print(len(pi_string))
Começamos abrindo o arquivo e armazenando cada linha de dígitos em
uma lista, como fizemos no exemplo anterior. Em u criamos uma variável
pi_string para armazenar os dígitos de pi. Então criamos um laço que
acrescenta cada uma das linhas de dígitos em pi_string removendo o
caractere de quebra de linha v. Em w exibimos essa string e mostramos
também o seu tamanho:
3.1415926535 8979323846 2643383279
36
A variável pi_string contém os espaços em branco que estavam do lado
esquerdo dos dígitos em cada linha, mas podemos nos livrar deles usando
strip() no lugar de rstrip():
filename = 'pi_30_digits.txt'
with open(filename) as file_object:
lines = file_object.readlines()
pi_string = ''
for line in lines:
pi_string += line.strip()
print(pi_string)
print(len(pi_string))
Agora temos uma string que contém pi com trinta casas decimais. A
string tem 32 caracteres de tamanho porque inclui também o número 3 na
frente e um ponto decimal:
3.141592653589793238462643383279
32
NOTA Quando Python lê um arquivo-texto, todo o texto do arquivo é interpretado
como uma string. Se você ler um número e quiser trabalhar com esse valor em
um contexto numérico, será necessário convertê-lo em um inteiro usando a
função int() ou convertê-lo em um número de ponto flutuante com a função
float().
Arquivos grandes: ummilhão de dígitos
Até agora, nosso enfoque foi analisar um arquivo-texto que continha
apenas três linhas, mas o código desses exemplos também funcionará bem
em arquivos muito maiores. Se começarmos com um arquivo-texto que
contenha pi com um milhão de casas decimais, e não trinta, uma única
string contendo todos esses dígitos poderá ser criada. Não precisamos
alterar nada em nosso programa, exceto para lhe passar um arquivo
diferente. Além disso, exibiremos as cinquenta primeiras casas decimais
para que não seja necessário assistirmos a um milhão de dígitos rolando
pelo terminal:
pi_string.py
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
lines = file_object.readlines()
pi_string = ''
for line in lines:
pi_string += line.strip()
print(pi_string[:52] + "...")
print(len(pi_string))
A saída mostra que, realmente, temos uma string contendo pi com um
milhão de casas decimais:
3.14159265358979323846264338327950288419716939937510...
1000002
Python não tem nenhum limite inerente para a quantidade de dados com
que podemos trabalhar; podemos trabalhar com tantos dados quantos a
memória de seu sistema for capaz de tratar.
NOTA Para executar esse programa (e vários dos próximos exemplos), você deverá
fazer download dos recursos disponíveis em
https://www.nostarch.com/pythoncrashcourse/.
Seu aniversário estácontido empi?
Sempre tive curiosidade de saber se a minha data de nascimento aparece
em algum lugar nos dígitos de pi. Vamos usar o programa que acabamos de
escrever para descobrir se a data de nascimento de alguém aparece em
algum ponto no primeiro milhão de dígitos de pi. Podemos fazer isso
expressando cada data de nascimento como uma string de dígitos e
verificando se essa string aparece em algum ponto de pi_string:
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
lines = file_object.readlines()
pi_string = ''
for line in lines:
pi_string += line.rstrip()
u birthday = input("Enter your birthday, in the form mmddyy: ")
v if birthday in pi_string:
print("Your birthday appears in the first million digits of pi!")
else:
print("Your birthday does not appear in the first million digits of
pi.")
Em u pedimos a data de nascimento do usuário e, em seguida, em v,
verificamos se essa string está em pi_string. Vamos testar isso:
Enter your birthdate, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!
Minha data de nascimento está nos dígitos de pi! Depois de ter lido um
arquivo, podemos analisar seu conteúdo de praticamente qualquer modo
que pudermos imaginar.
FAÇA VOCÊ MESMO
10.1 – Aprendendo Python: Abra um arquivo em branco em seu editor de texto e
escreva algumas linhas que sintetizem o que você aprendeu sobre Python até
agora. Comece cada linha com a expressão Em Python podemos.... Salve o
arquivo como learning_python.txt no mesmo diretório em que estão seus exercícios
deste capítulo. Escreva um programa que leia o arquivo e mostre o que você
escreveu, três vezes. Exiba o conteúdo uma vez lendo o arquivo todo, uma vez
percorrendo o objeto arquivo com um laço e outra armazenando as linhas em uma
lista e então trabalhando com ela fora do bloco with.
10.2 – Aprendendo C: Você pode usar o método replace() para substituir
qualquer palavra por uma palavra diferente em uma string. Eis um exemplo rápido
que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Leia cada linha do arquivo learning_python.txt que você acabou de criar e
substitua a palavra Python pelo nome de outra linguagem, por exemplo, C. Mostre
cada linha modificada na tela.
Escrevendo dadosemumarquivo
Uma das maneiras mais simples de salvar dados é escrevê-los em um
arquivo. Quando um texto é escrito em um arquivo, o resultado estará
disponível depois que você fechar o terminal que contém a saída de seu
programa. Podemos analisar a saída depois que um programa acabar de
executar e compartilhar os arquivos de saída com outras pessoas também.
Além disso, podemos escrever programas que leiam o texto de volta para a
memória e trabalhar com esses dados novamente.
Escrevendo dadosemumarquivo vazio
Para escrever um texto em um arquivo, chame open() com um segundo
argumento que diga a Python que você quer escrever dados no arquivo.
Para ver como isso funciona, vamos escrever uma mensagem simples e
armazená-la em um arquivo em vez de exibi-la na tela:
write_message.py
filename = 'programming.txt'
u with open(filename, 'w') as file_object:
v file_object.write("I love programming.")
A chamada a open() nesse exemplo tem dois argumentos u. O primeiro
argumento ainda é o nome do arquivo que queremos abrir. O segundo
argumento, 'w', diz a Python que queremos abrir o arquivo em modo de
escrita. Podemos abrir um arquivo em modo de leitura ('r'), em modo de
escrita ('w'), em modo de concatenação ('a') ou em um modo que permita
ler e escrever no arquivo ('r+'). Se o argumento de modo for omitido, por
padrão Python abrirá o arquivo em modo somente de leitura.
A função open() cria automaticamente o arquivo no qual você vai escrever
caso ele ainda não exista. No entanto, tome cuidado ao abrir um arquivo
em modo de escrita ('w') porque se o arquivo já existir, Python o apagará
antes de devolver o objeto arquivo.
Em v usamos o método write() no objeto arquivo para escrever uma
string nesse arquivo. Esse programa não tem saída no terminal, mas se
abrir o arquivo programming.txt, você verá uma linha:
programming.txt
I love programming.
Esse arquivo se comporta como qualquer outro arquivo de seu
computador. Você pode abri-lo, escrever um novo texto nele, copiar ou
colar dados e assim por diante.
NOTA Python escreve apenas strings em um arquivo-texto. Se quiser armazenar
dados numéricos em um arquivo-texto, será necessário converter os dados em
um formato de string antes usando a função str().
Escrevendo várias linhas
A função write() não acrescenta nenhuma quebra de linha ao texto que
você escrever. Portanto, se escrever mais de uma linha sem incluir
caracteres de quebra de linha, seu arquivo poderá não ter a aparência
desejada:
filename = 'programming.txt'
with open(filename, 'w') as file_object:
file_object.write("I love programming.")
file_object.write("I love creating new games.")
Ao abrir o arquivo programming.txt, você verá duas linhas emendadas:
I love programming.I love creating new games.
A inclusão de quebras de linha em suas instruções write() faz cada string
aparecer em sua própria linha:
filename = 'programming.txt'
with open(filename, 'w') as file_object:
file_object.write("I love programming.n")
file_object.write("I love creating new games.n")
A saída agora aparece em linhas separadas:
I love programming.
I love creating new games.
Podemos também usar espaços, caracteres de tabulação e linhas em
branco para formatar a saída, exatamente como viemos fazendo com as
saídas no terminal.
Concatenando dadosemumarquivo
Se quiser acrescentar conteúdos em um arquivo em vez de sobrescrever o
conteúdo existente, você pode abrir o arquivo em modo de concatenação.
Ao abrir um arquivo em modo de concatenação, Python não apagará o
arquivo antes de devolver o objeto arquivo. Qualquer linha que você
escrever no arquivo será adicionada no final. Se o arquivo ainda não existe,
Python criará um arquivo vazio para você.
Vamos modificar write_message.py acrescentando alguns novos motivos
pelos quais amamos programar no arquivo existente programming.txt:
write_message.py
filename = 'programming.txt'
u with open(filename, 'a') as file_object:
v file_object.write("I also love finding meaning in large
datasets.n")
file_object.write("I love creating apps that can run in a
browser.n")
Em u usamos o argumento 'a' para abrir o arquivo para concatenação,
em vez de sobrescrever o arquivo existente. Em v escrevemos duas linhas
novas, que são acrescentadas em programming.txt:
programming.txt
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
Ao final, temos o conteúdo original do arquivo, seguido do novo
conteúdo que acabamos de acrescentar.
FAÇA VOCÊ MESMO
10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
acrescente uma linha que registre a visita do usuário em um arquivo chamado
guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
arquivo.
10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
pessoas por que elas gostam de programação. Sempre que alguém fornecer um
motivo, acrescente-o em um arquivo que armazene todas as respostas.
Exceções
Python usa objetos especiais chamados exceções para administrar erros que
surgirem durante a execução de um programa. Sempre que ocorrer um erro
que faça Python não ter certeza do que deve fazer em seguida, um objeto
exceção será criado. Se você escrever um código que trate a exceção, o
programa continuará executando. Se a exceção não for tratada, o programa
será interrompido e um traceback, que inclui uma informação sobre a
exceção levantada, será exibido.
As exceções são tratadas com blocos try-except. Um bloco try-except
pede que Python faça algo, mas também lhe diz o que deve ser feito se uma
exceção for levantada. Ao usar blocos try-except, seus programas
continuarão a executar, mesmo que algo comece a dar errado. Em vez de
tracebacks, que podem ser confusos para os usuários lerem, os usuários
verão mensagens de erro simpáticas escritas por você.
Tratando aexceção ZeroDivisionError
Vamos observar um erro simples, que faz Python levantar uma exceção.
Provavelmente, você sabe que é impossível dividir um número por zero,
mas vamos pedir que Python faça isso, de qualquer modo:
division.py
print(5/0)
É claro que Python não pode fazer essa operação, portanto veremos um
traceback:
Traceback (most recent call last):
File "division.py", line 1, in <module>
print(5/0)
u ZeroDivisionError: division by zero
O erro informado em u no traceback, ZeroDivisionError, é um objeto
exceção. Python cria esse tipo de objeto em resposta a uma situação em
que ele não é capaz de fazer o que lhe pedimos. Quando isso acontece,
Python interrompe o programa e informa o tipo de exceção levantado.
Podemos usar essa informação para modificar nosso programa. Diremos a
Python o que ele deve fazer quando esse tipo de exceção ocorrer; desse
modo, se ela ocorrer novamente, estaremos preparados.
Usando blocos try-except
Quando achar que um erro pode ocorrer, você poderá usar um bloco try￾except para tratar a exceção possível de ser levantada. Dizemos a Python
para tentar executar um código e lhe dizemos o que ele deve fazer caso o
código resulte em um tipo particular de exceção.
Eis a aparência de um bloco try-except para tratar a exceção
ZeroDivisionError:
try:
print(5/0)
except ZeroDivisionError:
print("You can't divide by zero!")
Colocamos print(5/0) – a linha que causou o erro – em um bloco try. Se
o código em um bloco try funcionar, Python ignorará o bloco except. Se o
código no bloco try causar um erro, o interpretador procurará um bloco
except cujo erro coincida com aquele levantado e executará o código desse
bloco.
Nesse exemplo, o código no bloco try gera um ZeroDivisionError,
portanto Python procura um bloco except que lhe diga como deve
responder. O interpretador então executa o código desse bloco e o usuário
vê uma mensagem de erro simpática no lugar de um traceback:
You can't divide by zero!
Se houver mais código depois do bloco try-except, o programa
continuará executando, pois dissemos a Python como o erro deve ser
tratado. Vamos observar um exemplo em que a captura de um erro permite
que um programa continue executando.
Usando exceções paraevitar falhas
Tratar erros de forma correta é importante, em especial quando o
programa tiver outras atividades para fazer depois que o erro ocorrer. Isso
acontece com frequência em programas que pedem dados de entrada aos
usuários. Se o programa responder a entradas inválidas de modo
apropriado, ele poderá pedir mais entradas válidas em vez de causar uma
falha.
Vamos criar uma calculadora simples que faça apenas divisões:
division.py
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
u first_number = input("nFirst number: ")
if first_number == 'q':
break
v second_number = input("Second number: ")
if second_number == 'q':
break
w answer = int(first_number) / int(second_number)
print(answer)
Esse programa pede que o usuário forneça um primeiro número
(first_number) u e, se o usuário não digitar q para sair, pede um segundo
número (second_number) v. Então dividimos esses dois números para obter
uma resposta (answer) w. O programa não faz nada para tratar erros,
portanto pedir que uma divisão por zero seja feita causará uma falha no
programa:
Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
Traceback (most recent call last):
File "division.py", line 9, in <module>
answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
O fato de o programa falhar é ruim, mas também não é uma boa ideia
deixar que os usuários vejam os tracebacks. Usuários que não sejam
técnicos ficarão confusos com eles e, em um ambiente malicioso, invasores
aprenderão mais do que você quer que eles saibam a partir de um
traceback. Por exemplo, eles saberão o nome de seu arquivo de programa e
verão uma parte de seu código que não está funcionando de forma
apropriada. Às vezes, um invasor habilidoso pode usar essas informações
para determinar os tipos de ataque que podem usar contra o seu código.
Bloco else
Podemos deixar esse programa mais resistente a erros colocando a linha
capaz de produzir erros em um bloco try-except. O erro ocorre na linha
que calcula a divisão, portanto é aí que colocaremos o bloco try-except.
Esse exemplo também inclui um bloco else. Qualquer código que dependa
do bloco try executar com sucesso deve ser colocado no bloco else:
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
first_number = input("nFirst number: ")
if first_number == 'q':
break
second_number = input("Second number: ")
u try:
answer = int(first_number) / int(second_number)
v except ZeroDivisionError:
print("You can't divide by 0!")
w else:
print(answer)
Pedimos a Python para tentar concluir a operação de divisão em um
bloco try u, que inclui apenas o código que pode causar um erro. Qualquer
código que dependa do sucesso do bloco try é adicionado no bloco else.
Nesse caso, se a operação de divisão for bem-sucedida, usamos o bloco
else para exibir o resultado w.
O bloco except diz como Python deve responder quando um
ZeroDivisionError ocorrer v. Se a instrução try não for bem-sucedida por
causa de um erro de divisão por zero, mostraremos uma mensagem
simpática informando o usuário de que modo esse tipo de erro pode ser
evitado. O programa continua executando e o usuário jamais verá um
traceback:
Give me two numbers, and I'll divide them.
Enter 'q' to quit.
First number: 5
Second number: 0
You can't divide by 0!
First number: 5
Second number: 2
2.5
First number: q
O bloco try-except-else funciona assim: Python tenta executar o código
que está na instrução try. O único código que deve estar em uma instrução
try é aquele que pode fazer uma exceção ser levantada. Às vezes, você terá
um código adicional que deverá ser executado somente se o bloco try tiver
sucesso; esse código deve estar no bloco else. O bloco except diz a Python
o que ele deve fazer, caso uma determinada exceção ocorra quando ele
tentar executar o código que está na instrução try.
Ao prever possíveis fontes de erros, podemos escrever programas
robustos, que continuarão a executar mesmo quando encontrarem dados
inválidos ou se depararem com recursos ausentes. Seu código será
resistente a erros inocentes do usuário e a ataques maliciosos.
Tratando aexceção FileNotFoundError
Um problema comum ao trabalhar com arquivos é o tratamento de
arquivos ausentes. O arquivo que você está procurando pode estar em
outro lugar, o nome do arquivo pode estar escrito de forma incorreta ou o
arquivo talvez simplesmente não exista. Podemos tratar todas essas
situações de um modo simples com um bloco try-except.
Vamos tentar ler um arquivo que não existe. O programa a seguir tenta
ler o conteúdo de Alice in Wonderland (Alice no país das maravilhas), mas
não salvei o arquivo alice.txt no mesmo diretório em que está alice.py:
alice.py
filename = 'alice.txt'
with open(filename) as f_obj:
contents = f_obj.read()
Python não é capaz de ler um arquivo ausente, portanto uma exceção é
levantada:
Traceback (most recent call last):
File "alice.py", line 3, in <module>
with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
A última linha do traceback informa um FileNotFoundError: essa é a
exceção criada por Python quando não encontra o arquivo que está
tentando abrir. Nesse exemplo, a função open() gera o erro, portanto, para
tratá-lo, o bloco try tem início imediatamente antes da linha que contém
essa função:
filename = 'alice.txt'
try:
with open(filename) as f_obj:
contents = f_obj.read()
except FileNotFoundError:
msg = "Sorry, the file " + filename + " does not exist."
print(msg)
Nesse exemplo, o código no bloco try gera um FileNotFoundError,
portanto Python procura um bloco except que trate esse erro. O
interpretador então executa o código que está nesse bloco e o resultado é
uma mensagem de erro simpática no lugar de um traceback:
Sorry, the file alice.txt does not exist.
O programa não tem mais nada a fazer caso o arquivo não exista,
portanto o código de tratamento de erro não acrescenta muito a esse
programa. Vamos expandir esse exemplo e ver como o tratamento de
exceções pode ajudar quando trabalhamos com mais de um arquivo.
Analisando textos
Podemos analisar arquivos-texto que contenham blocos inteiros. Muitas
obras clássicas de literatura estão disponíveis como arquivos-texto simples,
pois estão em domínio público. Os textos usados nesta seção foram
extraídos do Projeto Gutenberg (http://gutenberg.org/). O Projeto
Gutenberg mantém uma coleção de obras literárias disponíveis em
domínio público, e é um ótimo recurso se você estiver interessado em
trabalhar com textos literários em seus projetos de programação.
Vamos obter o texto de Alice in Wonderland e tentar contar o número de
palavras do texto. Usaremos o método de string split(), que cria uma lista
de palavras a partir de uma string. Eis o que split() faz com uma string
que contém apenas o título "Alice in Wonderland":
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
O método split() separa uma string em partes sempre que encontra um
espaço, e armazena todas as partes da string em uma lista. O resultado é
uma lista de palavras da string, embora algumas pontuações possam
também aparecer com determinadas palavras. Para contar o número de
palavras em Alice in Wonderland, usaremos split() no texto todo. Em
seguida, contaremos os itens da lista para ter uma ideia geral da
quantidade de palavras no texto:
filename = 'alice.txt'
try:
with open(filename) as f_obj:
contents = f_obj.read()
except FileNotFoundError:
msg = "Sorry, the file " + filename + " does not exist."
print(msg)
else:
# Conta o número aproximado de palavras no arquivo
u words = contents.split()
v num_words = len(words)
w print("The file " + filename + " has about " + str(num_words) + "
words.")
Movi o arquivo alice.txt para o diretório correto, portanto o bloco try
funcionará dessa vez. Em u usamos a string contents, que agora contém
todo o texto de Alice in Wonderland como uma string longa, e aplicamos o
método split() para obter uma lista de todas as palavras do livro. Quando
usamos len() nessa lista para verificar o seu tamanho, obtemos uma boa
aproximação do número de palavras na string original v. Em w exibimos
uma frase que informa quantas palavras encontramos no arquivo. Esse
código é colocado no bloco else porque funcionará somente se o código no
bloco try for executado com sucesso. A saída nos informa quantas palavras
estão em alice.txt:
The file alice.txt has about 29461 words.
A contagem é um pouco alta devido a informações extras fornecidas pela
editora no arquivo-texto usado aqui, mas é uma boa aproximação do
tamanho de Alice in Wonderland.
Trabalhando comváriosarquivos
Vamos acrescentar outros livros para analisar. Porém, antes disso, vamos
passar a parte principal desse programa para uma função chamada
count_words(). Com isso, será mais fácil fazer a análise para diversos livros:
word_count.py
def count_words(filename):
u Conta o número aproximado de palavras em um arquivo.
try:
with open(filename) as f_obj:
contents = f_obj.read()
except FileNotFoundError:
msg = "Sorry, the file " + filename + " does not exist."
print(msg)
else:
# Conta o número aproximado de palavras no arquivo
words = contents.split()
num_words = len(words)
print("The file " + filename + " has about " + str(num_words) +
" words.")
filename = 'alice.txt'
count_words(filename)
A maior parte desse código não foi alterada. Simplesmente, indentamos o
código e o movemos para o corpo de count_words(). Manter os comentários
atualizados é um bom hábito quando modificamos um programa; assim,
transformamos o comentário em uma docstring e o alteramos um pouco u.
Agora podemos escrever um laço simples para contar as palavras de
qualquer texto que quisermos analisar. Fazemos isso armazenando os
nomes dos arquivos que desejamos analisar em uma lista e, em seguida,
chamando count_words() para cada arquivo da lista. Vamos experimentar
contar as palavras das obras Alice in Wonderland, Siddhartha, Moby Dick e
Little Women, todas disponíveis em domínio público. Deixei siddhartha.txt
fora do diretório que contém word_count.py de propósito para que
possamos ver como nosso programa trata um arquivo ausente de modo
apropriado:
def count_words(filename):
--trecho omitido--
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
'little_women.txt']
for filename in filenames:
count_words(filename)
O arquivo siddhartha.txt ausente não tem efeito algum no restante da
execução do programa:
The file alice.txt has about 29461 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
O uso do bloco try-except nesse exemplo oferece duas vantagens
significativas. Evitamos que nossos usuários vejam um traceback e
deixamos o programa continuar a análise dos textos que puder encontrar.
Se não capturássemos e erro FileNotFoundError gerado por siddhartha.txt, o
usuário veria um traceback completo e o programa pararia de executar
após tentar analisar Siddhartha. Moby Dick e Little Women não seriam
analisados.
Falhando silenciosamente
No exemplo anterior, informamos nossos usuários que um dos arquivos
estava indisponível. Porém, não precisamos informar todas as exceções
capturadas. Às vezes, queremos que o programa falhe silenciosamente
quando uma exceção ocorrer e continue como se nada tivesse acontecido.
Para fazer um programa falhar em silêncio, escreva um bloco try como
seria feito normalmente, mas diga de forma explícita a Python para não
fazer nada no bloco except. Python tem uma instrução pass que lhe diz para
não fazer nada em um bloco:
def count_words(filename):
Conta o número aproximado de palavras em um arquivo.
try:
--trecho omitido--
except FileNotFoundError:
u pass
else:
--trecho omitido--
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt',
'little_women.txt']
for filename in filenames:
count_words(filename)
A única diferença entre essa listagem e a listagem anterior está na
instrução pass em u. Agora, quando um FileNotFoundError é levantado, o
código no bloco except é executado, mas nada acontece. Nenhum
traceback é gerado e não há nenhuma saída em resposta ao erro levantado.
Os usuários veem os contadores de palavras para cada arquivo existente,
mas não há indicação sobre um arquivo não encontrado:
The file alice.txt has about 29461 words.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
A instrução pass também atua como um marcador. É um lembrete de que
você optou por não fazer nada em um ponto específico da execução de seu
programa, mas talvez queira fazer algo nesse local, no futuro. Por exemplo,
nesse programa, podemos decidir escrever os nomes de qualquer arquivo
ausente em um arquivo chamado missing_files.txt. Nossos usuários não
verão esse arquivo, mas poderemos lê-lo e tratar qualquer texto ausente.
Decidindo quaiserros devemser informados
Como sabemos quando devemos informar um erro aos usuários e quando
devemos falhar silenciosamente? Se os usuários souberem quais textos
devem ser analisados, poderão apreciar uma mensagem que lhes informe
por que alguns textos não foram analisados. Se os usuários esperam ver
alguns resultados, mas não sabem quais livros deveriam ser analisados,
talvez não precisem saber que alguns textos estavam indisponíveis. Dar
informações que os usuários não estejam esperando pode reduzir a
usabilidade de seu programa. As estruturas de tratamento de erros de
Python permitem ter um controle minucioso sobre o que você deve
compartilhar com os usuários quando algo sair errado; cabe a você decidir
a quantidade de informações a serem compartilhadas.
Um código bem escrito, testado de modo apropriado, não será muito
suscetível a erros internos, como erros de sintaxe ou de lógica. Contudo,
sempre que seu programa depender de algo externo, por exemplo, de uma
entrada de usuário, da existência de um arquivo ou da disponibilidade de
uma conexão de rede, existe a possibilidade de uma exceção ser levantada.
Um pouco de experiência ajudará você a saber em que pontos deverá
incluir blocos de tratamento de exceções em seu programa e a quantidade
de informações que deverá ser fornecida aos usuários sobre os erros que
ocorrerem.
FAÇA VOCÊ MESMO
10.6 – Adição: Um problema comum quando pedir entradas numéricas ocorre
quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
entrada para um int, você obterá um TypeError. Escreva um programa que peça
dois números ao usuário. Some-os e mostre o resultado. Capture o TypeError caso
algum dos valores de entrada não seja um número e apresente uma mensagem de
erro simpática. Teste seu programa fornecendo dois números e, em seguida, digite
um texto no lugar de um número.
10.7 – Calculadora para adição: Coloque o código do Exercício 10.6 em um
laço while para que o usuário possa continuar fornecendo números, mesmo se
cometerem um erro e digitarem um texto no lugar de um número.
10.8 – Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo
menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no
segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o
conteúdo do arquivo na tela. Coloque seu código em um bloco try-except para
capturar o erro FileNotFound e apresente uma mensagem simpática caso o
arquivo não esteja presente. Mova um dos arquivos para um local diferente de seu
sistema e garanta que o código no bloco except seja executado de forma
apropriada.
10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.
10.10 – Palavras comuns: Acesse o Projeto Gutenberg (http://gutenberg.org/ ) e
encontre alguns textos que você gostaria de analisar. Faça download dos arquivos￾texto dessas obras ou copie o texto puro de seu navegador para um arquivo-texto
em seu computador.
Você pode usar o método count() para descobrir quantas vezes uma palavra ou
expressão aparece em uma string. Por exemplo, o código a seguir conta quantas
vezes a palavra 'row' aparece em uma string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Observe que converter a string para letras minúsculas usando lower() faz com
que todas as formas da palavra que você está procurando sejam capturadas,
independentemente do modo como elas estiverem grafadas.
Escreva um programa que leia os arquivos que você encontrou no Projeto
Gutenberg e determine quantas vezes a palavra 'the' aparece em cada texto.
Armazenando dados
Muitos de seus programas pedirão aos usuários que forneçam
determinados tipos de informação. Você pode permitir que os usuários
armazenem suas preferências em um jogo ou forneçam dados para uma
visualização. Qualquer que seja o foco de seu programa, você armazenará
as informações fornecidas pelos usuários em estruturas de dados como
listas e dicionários. Quando os usuários fecham um programa, quase
sempre você vai querer salvar as informações que eles forneceram. Uma
maneira simples de fazer isso envolve armazenar seus dados usando o
módulo json.
O módulo json permite descarregar estruturas de dados Python simples
em um arquivo e carregar os dados desse arquivo na próxima vez que o
programa executar. Também podemos usar json para compartilhar dados
entre diferentes programas Python. Melhor ainda, o formato de dados
JSON não é específico de Python, portanto podemos compartilhar dados
armazenados em formato JSON com pessoas que trabalhem com várias
outras linguagens de programação. É um formato útil e portável, além de
ser fácil de aprender.
NOTA O formato JSON (JavaScript Object Notation, ou Notação de Objetos
JavaScript) foi originalmente desenvolvido para JavaScript. Apesar disso,
tornou-se um formato comum, usado por muitas linguagens, incluindo Python.
Usando json.dump()ejson.load()
Vamos escrever um pequeno programa que armazene um conjunto de
números e outro que leia esses números de volta para a memória. O
primeiro programa usará json.dump() para armazenar o conjunto de
números, e o segundo programa usará json.load().
A função json.dump() aceita dois argumentos: um dado para armazenar e
um objeto arquivo que pode ser usado para armazenar o dado. Eis o modo
como podemos usar essa função para armazenar uma lista de números:
number_writer.py
import json
numbers = [2, 3, 5, 7, 11, 13]
u filename = 'numbers.json'
v with open(filename, 'w') as f_obj:
w json.dump(numbers, f_obj)
Inicialmente importamos o módulo json e criamos uma lista de números
com a qual trabalharemos. Em u escolhemos o nome de um arquivo em
que armazenaremos a lista de números. É comum usar a extensão de
arquivo .json para indicar que os dados do arquivo estão armazenados em
formato JSON. Em seguida, abrimos o arquivo em modo de escrita, o que
permite a json escrever os dados no arquivo v. Em w usamos a função
json.dump() para armazenar a lista numbers no arquivo numbers.json.
Esse programa não tem uma saída, mas vamos abrir o arquivo
numbers.json e observá-lo. Os dados estão armazenados em um formato
que se parece com Python:
[2, 3, 5, 7, 11, 13]
Agora escreveremos um programa que use json.load() para ler a lista de
volta para a memória:
number_reader.py
import json
u filename = 'numbers.json'
v with open(filename) as f_obj:
w numbers = json.load(f_obj)
print(numbers)
Em u garantimos que o mesmo arquivo em que escrevemos os dados será
lido. Dessa vez, quando abrirmos o arquivo, fazemos isso em modo de
leitura, pois Python precisará apenas ler dados do arquivo v. Em w usamos
a função json.load() para carregar as informações armazenadas em
numbers.json e as guardamos na variável numbers. Por fim, exibimos a lista
de números recuperada; podemos ver que é a mesma lista criada em
number_writer.py:
[2, 3, 5, 7, 11, 13]
Essa é uma maneira simples de compartilhar dados entre dois programas.
Salvando elendo dados gerados pelo usuário
Salvar dados com json é conveniente quando trabalhamos com dados
gerados pelo usuário porque, se você não salvar as informações de seus
usuários de algum modo, elas serão perdidas quando o programa parar de
executar. Vamos observar um exemplo em que pedimos aos usuários que
forneçam seus nomes na primeira vez em que o programa executar e,
então, o programa deverá lembrar esses nomes quando for executado
novamente.
Vamos começar armazenando o nome do usuário:
remember_me.py
import json
u username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
v json.dump(username, f_obj)
w print("We'll remember you when you come back, " + username + "!")
Em u pedimos o nome do usuário para que seja armazenado. Em
seguida, usamos json.dump(), passando-lhe um nome de usuário e um
objeto arquivo em que esse nome será armazenado v. Então exibimos uma
mensagem informando o usuário que armazenamos suas informações w:
What is your name? Eric
We'll remember you when you come back, Eric!
Vamos agora escrever um novo programa que faça uma saudação a um
usuário cujo nome já esteja armazenado:
greet_user.py
import json
filename = 'username.json'
with open(filename) as f_obj:
u username = json.load(f_obj)
v print("Welcome back, " + username + "!")
Em u usamos json.load() para ler as informações armazenadas em
username.json na variável username. Agora que recuperamos o nome do
usuário, podemos lhe desejar as boas-vindas de voltav:
Welcome back, Eric!
Precisamos combinar esses dois programas em um só arquivo. Quando
alguém executar remember_me.py, queremos recuperar seu nome de
usuário da memória, se for possível; assim, começaremos com um bloco
try, que tentará recuperar o nome do usuário. Se o arquivo username.json
não existir, faremos o bloco except pedir um nome de usuário e armazená-
lo em username.json para ser usado da próxima vez:
remember_me.py
import json
# Carrega o nome do usuário se foi armazenado anteriormente
# Caso contrário, pede que o usuário forneça o nome e armazena essa
informação
filename = 'username.json'
try:
u with open(filename) as f_obj:
v username = json.load(f_obj)
w except FileNotFoundError:
x username = input("What is your name? ")
y with open(filename, 'w') as f_obj:
json.dump(username, f_obj)
print("We'll remember you when you come back, " + username +
"!")
else:
print("Welcome back, " + username + "!")
Não há nenhum código novo aqui; os blocos de código dos dois últimos
exemplos simplesmente foram combinados em um só arquivo. Em u
tentamos abrir o arquivo username.json. Se esse arquivo existir, lemos o
nome do usuário de volta para a memória v e exibimos uma mensagem
desejando boas-vindas de volta ao usuário no bloco else. Se essa é a
primeira vez que o usuário executa o programa, username.json não existirá
e um FileNotFoundError ocorrerá w. Python prosseguirá para o bloco except,
em que pedimos ao usuário que forneça o seu nome x. Então usamos
json.dump() para armazenar o nome do usuário e exibimos uma saudação
y.
Qualquer que seja o bloco executado, o resultado será um nome de
usuário e uma saudação apropriada. Se essa for a primeira vez que o
programa é executado, a saída será assim:
What is your name? Eric
We'll remember you when you come back, Eric!
Caso contrário, será:
Welcome back, Eric!
Essa é a saída que você verá se o programa já foi executado pelo menos
uma vez.
Refatoração
Com frequência você chegará a um ponto em que seu código funcionará,
mas reconhecerá que ele poderia ser melhorado se fosse dividido em uma
série de funções com tarefas específicas. Esse processo se chama
refatoração. A refatoração deixa seu código mais limpo, mais fácil de
compreender e de estender.
Podemos refatorar remember_me.py passando a maior parte de sua lógica
para uma ou mais funções. O foco de remember_me.py está na saudação ao
usuário, portanto vamos transferir todo o código existente para uma
função chamada greet_user():
remember_me.py
import json
def greet_user():
uSaúda o usuário pelo nome.
filename = 'username.json'
try:
with open(filename) as f_obj:
username = json.load(f_obj)
except FileNotFoundError:
username = input("What is your name? ")
with open(filename, 'w') as f_obj:
json.dump(username, f_obj)
print("We'll remember you when you come back, " + username
+ "!")
else:
print("Welcome back, " + username + "!")
greet_user()
Como estamos usando uma função agora, atualizamos os comentários
com uma docstring que reflete como o programa funciona no momento u.
Esse arquivo é um pouco mais limpo, porém a função greet_user() faz mais
do que simplesmente saudar o usuário – ela também recupera um nome de
usuário armazenado, caso haja um, e pede que o usuário forneça um novo
nome, caso não exista.
Vamos refatorar greet_user() para que não faça tantas tarefas diferentes.
Começaremos transferindo o código para recuperar um nome de usuário já
armazenado para uma função diferente:
import json
def get_stored_username():
u Obtém o nome do usuário já armazenado se estiver disponível.
filename = 'username.json'
try:
with open(filename) as f_obj:
username = json.load(f_obj)
except FileNotFoundError:
v return None
else:
return username
def greet_user():
Saúda o usuário pelo nome.
username = get_stored_username()
w if username:
print("Welcome back, " + username + "!")
else:
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
json.dump(username, f_obj)
print("We'll remember you when you come back, " + username
+ "!")
greet_user()
A nova função get_stored_username() tem um propósito claro, conforme
informado pela docstring em u. Essa função recupera um nome de usuário
já armazenado e devolve esse nome se encontrar um. Se o arquivo
username.json não existir, a função devolverá None v. Essa é uma boa
prática: uma função deve devolver o valor esperado ou None. Isso nos
permite fazer um teste simples com o valor de retorno da função. Em w
exibimos uma mensagem de boas-vindas de volta ao usuário se a tentativa
de recuperar um nome foi bem-sucedida; caso contrário, pedimos que um
novo nome de usuário seja fornecido.
Devemos fatorar mais um bloco de código, removendo-o de greet_user().
Se o nome do usuário não existir, devemos transferir o código que pede um
novo nome de usuário para uma função dedicada a esse propósito:
import json
def get_stored_username():
Obtém o nome do usuário já armazenado se estiver disponível.
--trecho omitido--
def get_new_username():
Pede um novo nome de usuário.
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f_obj:
json.dump(username, f_obj)
return username
def greet_user():
Saúda o usuário pelo nome.
username = get_stored_username()
if username:
print("Welcome back, " + username + "!")
else:
username = get_new_username()
print("We'll remember you when you come back, " + username +
"!")
greet_user()
Cada função nessa última versão de remember_me.py tem um propósito
único e claro. Chamamos greet_user() e essa função exibe uma mensagem
apropriada: ela dá as boas-vindas de volta a um usuário existente ou saúda
um novo usuário. Isso é feito por meio da chamada a
get_stored_username(), que é responsável somente por recuperar um nome
de usuário já armazenado, caso exista. Por fim, greet_user() chama
get_new_username() se for necessário; essa função é responsável somente por
obter um novo nome de usuário e armazená-lo. Essa separação do trabalho
em compartimentos é uma parte essencial na escrita de um código claro,
que seja fácil de manter e de estender.
FAÇA VOCÊ MESMO
10.11 – Número favorito: Escreva um programa que pergunte qual é o número
favorito de um usuário. Use json.dump() para armazenar esse número em um
arquivo. Escreva um programa separado que leia esse valor e apresente a
mensagem “Eu sei qual é o seu número favorito! É _____.”.
10.12 – Lembrando o número favorito: Combine os dois programas do Exercício
10.11 em um único arquivo. Se o número já estiver armazenado, informe o número
favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu número
favorito e armazene-o em um arquivo. Execute o programa duas vezes para
garantir que ele funciona.
10.13 – Verificando se é o usuário correto: A última listagem de
remember_me.py supõe que o usuário já forneceu seu nome ou que o programa
está executando pela primeira vez. Devemos modificá-lo para o caso de o usuário
atual não ser a pessoa que usou o programa pela última vez.
Antes de exibir uma mensagem de boas-vindas de volta em greet_user(),
pergunte ao usuário se seu nome está correto. Se não estiver, chame
get_new_username() para obter o nome correto.
Resumo
Neste capítulo aprendemos a trabalhar com arquivos. Vimos como ler um
arquivo todo de uma só vez e como ler o conteúdo de um arquivo uma
linha de cada vez. Aprendemos a escrever dados em um arquivo e a
concatenar texto no final dele. Lemos sobre as exceções e o modo de tratar
aquelas que provavelmente você verá em seus programas. Por fim,
aprendemos a armazenar estruturas de dados Python para que possamos
salvar as informações fornecidas pelos usuários, evitando que eles precisem
fazer tudo de novo sempre que executarem um programa.
No Capítulo 11, conheceremos maneiras eficientes de testar o seu código.
Isso ajudará você a ter mais confiança de que o código desenvolvido está
correto e ajudará a identificar bugs introduzidos à medida que você
continuar a estender os programas que escreveu"""