## Descrição:

### Fase 1 - Definição da Linguagem
<p align="justify">
    Na fase um sua tarefa será criar uma linguagem de programação que permita a criação de programas para o sistema embarcado escolhido. Esta linguagem será criada a partir de um esboço, definido a seguir. Caberá a você completar este esboço de forma que existam declarações para interagir com o hardware (ler e escrever em pinos do microcomputador, ler e escrever nas portas serias, ler e escrever em componentes opcionais como conversores digital – analógico e analógico – digital).
    Um programa consiste em um bloco de declarações definidos por:
</p>

![bloco_declaracao](https://user-images.githubusercontent.com/53230135/232320555-bbb873b0-103a-4feb-a4fe-c167647be67b.png)

<p align="justify">
    O lexema basic expressa os tipos básicos da sua linguagem.
</p>

![image](https://user-images.githubusercontent.com/53230135/232320574-c5f402af-78e3-4421-8281-6ae55798f99e.png)

<p align="justify">
    As produções para as expressões tratam da associatividade e precedência de operadores. Elas usam um não-terminal para cada nível de precedência e um não-terminal, factor, para as expressões entre parênteses, identificadores, referências de arranjos e constantes.
</p>

![image](https://user-images.githubusercontent.com/53230135/232320643-77582585-3fb2-43fb-b411-6d90bd2a21ea.png)

<p align="justify">
    O lexema num indica números inteiros, o lexema real indica números de ponto flutuante com 16 bits segundo o padrão IEEE-754, conhecido como meia precisão. Todas as operações matemáticas, precisam ter a precisão definida no padrão IEEE – 754 para 16bits. A entrega desta fase será composta da apresentação da linguagem definida, destacando as regras de produção criadas para interação com o Hardware. E de, no mínimo, três exemplos de código utilizando a sua linguagem e que apresentem todas as funcionalidades da linguagem.    
</p>


----------
## Desenvolvimento:

### Bloco de declaração:
![image](https://user-images.githubusercontent.com/53230135/232321678-56a88c5d-455f-48b4-863b-692dafe12dbc.png)

<p align="justify">
    Foram modificadas e adicionadas algumas coisas no bloco de declaração, como por exemplo a adição de um Não Terminal 'basic', que é responsável por definir os tipos básicos da linguagem, e em 'type' foi adicionado um Terminal do tipo "void", que é responsável por definir um tipo vazio, que é utilizado para definir funções que não retornam nada.
    Além disso, foi adicionado um 'const' que é responsável por permitir a declaração de constantes que podem ser um 'num' (consequentemente um 'real') ou um 'factor' (bool | loc | num | True | False).
</p>

### Lexema basic:
![image](https://user-images.githubusercontent.com/53230135/232321737-6f9df537-d00b-4ce7-8b9b-edbf2d3a30ae.png)

<p align="justify">
    No Lexema Basic foram incluídos mais 'stmt' que permitem a utilização de laços de repetição, condicionais e etc... Além disso, para cada adição de 'stmt' foi adicionado um Não Terminal que define a sintaxe da declaração.
</p>
<p align="justify">
    Temos também a adição do 'call', que pode ser um 'id (args)', e esse 'args' pode ser um 'arglist' ou um null. Os arglist podem ser booleanos, números e id's. Já os id's podem ser uma 'letter', um 'id letter' ou um 'id num'.
</p>
<p align="justify">
    Por fim os 'cases' para utilização dentro do switch. Dentro do 'cases' podemos ter um 'case bool : stmts' ou um 'default : stmts'.
</p>

### Regras de produção para as expressões:
![image](https://user-images.githubusercontent.com/53230135/232322404-a391a511-367d-4ceb-b802-1f26cc5e146d.png)

<p align="justify">
    As regras de produção para as expressões foram pouco modificadas para que fosse possível continuar a utilização de operadores lógicos e relacionais, além de operadores de incremento e decremento. A diferença foi a inclusão do '%' nos 'terms', dos ++ e -- nos 'unary' e algumas mudanças de nomes para que ficasse mais fácil o entendimento.
</p>

### Tratamento dos números e letras:
![image](https://user-images.githubusercontent.com/53230135/232323681-c7af25a7-2c27-4a13-8ca8-0b99746bafe3.png)

<p align="justify">
    Para o tratamento dos números e letras foi pensado em criar uma lógica para tratar números que são 'float' (com ponto flutuante) e números que são 'int' (inteiros).
    Para isso foi criado um Não Terminal 'num' que é responsável por tratar os números, e dentro dele temos o 'real'. Esse 'real' pode ser um 'DIGITS DOT DIGITSF'.
</p>
<p align="justify">
    'DIGITS' é um regex que permite números de 0 a 9, positivos ou negativos, DOT é um ponto, e 'DIGITSF' pode ser um 'DIGITS', um 'DIGITSF DIGITS' ou 'e FEXP' para tratar pontos flutuantes com exponenciação. O 'FEXP' pode ser 'PLUS DIGITSF' ou 'MINUS DIGITSF'.
</p>

### Comunicando com o Hardware:
![image](https://user-images.githubusercontent.com/53230135/232324061-9e9553b7-511e-40ce-a679-c2466b621738.png)

<p align="justify">
    Para a comunicação com o Hardware foi pensado em criar algumas funções como 'io_input_digital', 'io_output_digital', 'io_input_analog' e 'io_output_analog'. Essas funções são responsáveis por tratar a entrada e saída de dados para o Hardware.
    Todas essas funções recebem 'args' que podem ser um 'arglist' ou um null. Os 'arglist' já foram mencionados acima.
</p>

----------
## Exemplos de código:

<p align="justify">
    Abaixo temos alguns exemplos de código que utilizam as funcionalidades da nova linguagem. São códigos simples que utilizam declarações de variáveis, atribuições, operações matemáticas, operações lógicas, operações relacionais, operações de incremento, operações de saída de dados para o Hardware, operações de laços de repetição, operações condicionais, operações de switch e declaração e utilização de funções.
</p>


### Exemplo 1:
![image](https://user-images.githubusercontent.com/53230135/232322152-7b8921f7-7a81-46cf-9a8a-aa3e652b7a4f.png)

### Exemplo 2:
![image](https://user-images.githubusercontent.com/53230135/232322183-a037b951-8c6e-40e3-aecc-f83b71cc45ac.png)

### Exemplo 3:
![image](https://user-images.githubusercontent.com/53230135/232322224-5a38c1df-051f-478a-88d8-b205638bec63.png)


