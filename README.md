## Compiler Project - Desenvolvimento de um compilador

#### Projeto está sendo desenvolvido baseado em uma nova linguagem - disciplina de Linguagens Formais e Compiladores (LFC) da Pontifícia Universidade Católica do Paraná (PUC-PR)

#### Implementação: Nova linguagem de programação e compilador para a plataforma de sistemas embarcados (Arduino Mega, Raspberry PI, Tiva) baseado na tecnologia ARM.
----------------------
#### @MateusFerroAntunesdeOliveira @tasipasin
* Work In Progress (WIP) - 16/04/2023


----------------------
## Descrição:

<p align="justify">
    O objetivo deste projeto é a construção de um compilador para uma plataforma de sistemas embarcados (Arduino Mega, Raspberry PI, Tiva) baseado na tecnologia ARM. Este projeto pode ser desenvolvido em grupos de até 4 alunos. Este projeto está definido em três fases que correspondem a três entregas e uma apresentação.
    Todas as entregas serão realizadas de forma presencial e constarão da apresentação do trabalho e resultados e de um documento sintetizando estes resultados. E de links para validação dos códigos desenvolvidos na plataforma online Repl.it.
</p>

<p align="justify">
    Todos os documentos precisam ser escritos segundo as normas da ABNT referentes a fontes, espaçamentos, identificação de figuras, quadros e tabelas e, principalmente, ao lançamento e utilização de referências de pesquisa.
    Todas as entregas, sejam elas código, texto ou apresentações, deverão estar disponíveis em um repositório público do Github.
</p>

<p align="justify">
    Todas as entregas, sejam elas código, texto ou apresentações, deverão conter os nomes dos integrantes do grupo e do professor.
    Se você optar pelo Raspberry Pi lembre-se que não poderá utilizar qualquer sistema operacional neste dispositivo.
</p>


## Fases:

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

### Fase 2 - Verificação de Código

<p align="justify">
    Nesta faze você deverá implementar um analisador léxico, usando máquinas de estado finito, um parser, usando LL1, ou LR1 e uma estrutura baseada em cálculo de sequentes para a verificação dos tipos dos identificadores, valores e expressões criadas na sua linguagem.
</p>

<p align="justify">
    Todas as linguagens criadas deverão utilizar tipos estáticos. Ou seja, os tipos precisam ser definidos no código, arquivo de texto, que contém seu programa.
</p>

<p align="justify">
    A Entrega será composta dos documentos necessários para explicar o código desenvolvido, a apresentação deste código em sala e dos links para teste e validação do código desenvolvido. Para os testes, você deverá fornecer, no mínimo três códigos diferentes escritos na sua linguagem. Estes códigos devem apresentar todas as funcionalidades da linguagem e permitir a validação do código por meio de testes de indiquem as capacidades de verificação de erros dos três analisadores.
</p>


### Fase 3 - Geração de Código

<p align="justify">
    Para simplificar, o nosso código intermediário será o Assembler do sistema embarcado que você escolheu para desenvolver o seu projeto.
    Sua tarefa será criar um sistema capaz de recebendo o código que você escreveu, na linguagem que está construindo, e apresentar um arquivo em Assembler do sistema embarcado escolhido.
</p>

<p align="justify">
    Entrega, apresentação do módulo de geração de código, e execução de, no mínimo, três códigos distintos que abranjam todas as funcionalidade da linguagem que você criou rodando diretamente no sistema embarcado escolhido.
</p>

<p align="justify">
    Para execução desta tarefa você poderá desenvolver todas a ferramentas necessárias para converter o Assembler em binário e rodar o binário no sistema embarcado, ou usar algum ambiente de desenvolvimento específico do sistema embarcado escolhido que possa receber um código escrito em Assembler e rodar este código no hardware.
</p>
