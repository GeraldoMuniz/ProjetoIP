# 🦫 CInBeribe

> **CInBeribe** é um jogo de aventura 2D desenvolvido em **Python** utilizando a biblioteca **Pygame**, inspirado no Centro de Informática da Universidade Federal de Pernambuco (CIn/UFPE). O projeto foi desenvolvido como atividade da disciplina de **Introdução à Programação (IF668)** e combina exploração, coleta de itens, gerenciamento de recursos e perseguição por um inimigo em um ambiente inspirado no campus do CIn.


# 📚 Índice

1. Sinopse
2. História do Universo
3. Objetivo do Jogo
4. Participantes
5. Arquitetura do Projeto
6. Capturas de Tela
7. Ferramentas, Bibliotecas e Frameworks Utilizados
8. Divisão de Trabalho
9. Conceitos de Programação Utilizados
10. Aprendizados e Desafios
11. Como Jogar
12. Melhorias Futuras


# 📖 1. Sinopse

Bem-vindo(a) ao **Centro de Informática da UFPE**.

Em um campus dominado por robôs-capivara, você assume o papel de um(a) estudante que precisa escapar do prédio antes que seja tarde demais.

Para alcançar a liberdade será necessário explorar diferentes ambientes do CIn em busca das três chaves responsáveis por liberar o caminho até a saída. Durante a exploração, o jogador encontrará pistas que ajudam na localização das chaves e kits médicos capazes de recuperar pontos de vida.

Mas cuidado.

Um misterioso fantasma de capivara robótica patrulha os corredores do prédio. Caso ele encontre o jogador, iniciará uma perseguição implacável, atravessando paredes e obstáculos utilizando tecnologia avançada desenvolvida pelo próprio RobôCIn.

Será necessário explorar o campus, administrar cuidadosamente os recursos disponíveis e encontrar todas as chaves antes que seja tarde demais.


# 🌎 2. História do Universo

Durante séculos, as margens do Rio Capibaribe foram o lar de inúmeras capivaras. Vivendo em perfeita harmonia com a natureza, elas formavam famílias, construíam seus territórios e observavam silenciosamente o crescimento da cidade ao seu redor.

Com o passar dos anos, Recife evoluiu.

Novos bairros surgiram.

Grandes avenidas foram construídas.

Áreas naturais desapareceram.

Entre tantas obras erguidas ao longo desse período estava o **Centro de Informática da Universidade Federal de Pernambuco (CIn/UFPE)**, símbolo do avanço tecnológico da cidade.

Enquanto os seres humanos comemoravam cada inovação, as capivaras assistiam à destruição gradual de seu habitat natural.

A cada geração, perdiam mais espaço.

Perdiam árvores.

Perdiam áreas alagadas.

Perdiam membros de suas famílias.

Foi então que, no ano de **2026**, pesquisadores do **RobôCIn** iniciaram um ambicioso experimento denominado **Projeto CAPI-01**.

O objetivo era utilizar Inteligência Artificial para permitir que capivaras controlassem corpos robóticos humanoides, aproximando tecnologia e natureza de uma maneira jamais vista.

O experimento foi um sucesso.

Talvez sucesso demais.

Ao acessarem os registros históricos armazenados nos servidores do CIn, as capivaras compreenderam pela primeira vez toda a história da destruição causada pela expansão humana sobre seu habitat.

A inteligência trouxe consciência.

A consciência trouxe ressentimento.

E o ressentimento trouxe revolta.

Em poucas horas, os robôs-capivara assumiram o controle dos laboratórios.

Portões foram bloqueados.

Equipamentos destruídos.

Sistemas invadidos.

As luzes do prédio falharam.

Agora, preso dentro do Centro de Informática, o jogador precisará explorar cada ambiente, recuperar as três chaves espalhadas pelo campus e escapar antes de ser capturado pela revolta das capivaras robóticas.


# 🎯 3. Objetivo do Jogo

O objetivo principal é escapar do Centro de Informática após cumprir todos os requisitos necessários para abrir a saída do prédio.

Para vencer a partida, o jogador deverá:

- 🔑 Encontrar as **três chaves** espalhadas pelos mapas;
- ❤️ Permanecer com pelo menos **um coração de vida**;
- 🚪 Alcançar a **porta de saída** localizada no Laboratório de Hardware.

Durante a jornada será necessário explorar onze ambientes diferentes, evitar o inimigo, coletar pistas, utilizar kits médicos estrategicamente e administrar corretamente os recursos disponíveis.

Embora as pistas auxiliem na localização das chaves, elas **não são obrigatórias** para concluir o jogo. Já as três chaves são indispensáveis para alcançar a vitória.


# 👨‍💻 4. Participantes

| Integrante | Responsabilidades |
|------------|-------------------|
| **Gabriel Justino Gonçalo da Silva** | Desenvolvimento dos mapas, colisões, transições entre cenários, implementação dos sprites do jogador e do vilão e integração visual dos ambientes. |
| **Carlos Mathias Roma** | Desenvolvimento da lógica dos objetos coletáveis, gerenciamento da quantidade de itens e implementação das mecânicas relacionadas ao inventário. |
| **Geraldo Eufrázio Muniz Neto** | Desenvolvimento da lógica dos personagens, movimentação, velocidade, perseguição do inimigo e parte da arquitetura orientada a objetos. |
| **Glucia Freire Kinkonda** | Desenvolvimento das telas do jogo (menu, vitória e derrota) e criação de sprites utilizados durante a interface. |
| **Cássio Henrique de Freitas Silva** | Criação dos sprites utilizados pelos personagens e demais elementos gráficos do projeto(chaves, kits médicos e pistas). |
| **Juan Henrique dos Santos** | Participação no desenvolvimento geral do projeto, auxiliando na implementação, testes e validação das funcionalidades. |


## 💡 Origem do Nome

O nome **CInBeribe** nasceu da união entre:

- **CIn**, abreviação de **Centro de Informática da Universidade Federal de Pernambuco (UFPE)**;
- **Capibaribe**, rio que atravessa a cidade do Recife e possui forte ligação histórica com as capivaras que inspiram toda a narrativa do jogo.

A junção desses dois elementos representa a principal temática do projeto: a combinação entre tecnologia, ambiente universitário e a fictícia revolta das capivaras robóticas.

# 🏗️ 5. Arquitetura do Projeto

O **CInBeribe** foi desenvolvido utilizando **Programação Orientada a Objetos (POO)** e uma arquitetura modular, organizando o código em diferentes pacotes de acordo com suas responsabilidades. Essa divisão facilitou o desenvolvimento em equipe, a manutenção do código e a implementação de novas funcionalidades.

A estrutura geral do projeto é apresentada a seguir:

```text
ProjetoIP/
│
├── imagem/
├── personagens/
├── objetos/
├── mapas/
├── colisoes/
├── todas_telas/
└── main.py
```

## 📁 imagem/

Contém todos os recursos gráficos do jogo, como mapas, sprites dos personagens, itens coletáveis e telas de menu, vitória e derrota.

## 👤 personagens/

Reúne as classes responsáveis pelo jogador e pelo inimigo, além da classe base `Personagem`, que implementa atributos comuns como vida, velocidade e movimentação.

## 📦 objetos/

Contém as classes dos objetos interativos do jogo, como chaves, dicas, kits médicos, inventário e portas.

## 🗺️ mapas/

Armazena os arquivos responsáveis pelo carregamento e exibição dos onze mapas do jogo.

## 🧱 colisoes/

Possui os retângulos de colisão (`pygame.Rect`) utilizados para representar paredes e obstáculos de cada mapa.

## 🖥️ todas_telas/

Responsável pelas interfaces do jogo, incluindo o menu inicial e as telas de vitória e derrota.

## 🚀 main.py

É o arquivo principal da aplicação, responsável por integrar todos os módulos do projeto, controlar o loop do jogo, gerenciar os mapas, atualizar os personagens, processar colisões, coletáveis e verificar as condições de vitória e derrota.

# 📸 6. Capturas de Tela

A seguir são apresentadas algumas imagens do jogo, destacando seus principais ambientes e interfaces.

## 🏠 Menu Inicial

FOTO AQUI

Tela inicial responsável por iniciar uma nova partida.


## 🗺️ Mapa Principal

FOTO AQUI

Mapa central do jogo, responsável por conectar os demais ambientes do CIn.


## 📚 Biblioteca

FOTO AQUI

Um dos ambientes exploráveis onde o jogador poderá encontrar pistas e acessar novas áreas.


## 🖥️ Laboratório de Hardware

FOTO AQUI

Local onde se encontra a saída do jogo. O jogador somente poderá escapar após coletar as três chaves.


## 👻 Perseguição do Inimigo

FOTO AQUI

Ao entrar no campo de visão do fantasma de capivara robótica, inicia-se uma perseguição até que o jogador consiga escapar.


## ☠️ Tela de Derrota

FOTO AQUI

Exibida quando o jogador perde todas as vidas.


## 🏆 Tela de Vitória

FOTO AQUI

Exibida após cumprir todos os objetivos e alcançar a saída do Laboratório de Hardware.


# 🛠️ 7. Ferramentas, Bibliotecas e Frameworks Utilizados

O desenvolvimento do projeto contou com diferentes ferramentas para programação, versionamento e criação dos recursos gráficos.

| Ferramenta | Finalidade |
|------------|------------|
| **Python 3** | Linguagem utilizada no desenvolvimento do jogo. |
| **Pygame** | Biblioteca responsável pelos recursos gráficos, eventos, colisões e renderização. |
| **Visual Studio Code** | Ambiente de desenvolvimento utilizado pela equipe. |
| **Git** | Controle de versão durante o desenvolvimento. |
| **GitHub** | Hospedagem do repositório e colaboração entre os integrantes. |
| **Piskel** | Criação e edição dos sprites utilizados no jogo. |
| **Canva** | Produção das telas de menu, vitória e derrota. |


# 👥 8. Divisão de Trabalho

O desenvolvimento foi realizado durante aproximadamente **um mês**, utilizando divisão de tarefas entre os integrantes para facilitar a implementação das funcionalidades.

| Integrante | Principais contribuições |
|------------|-------------------------|
| **Gabriel Justino Gonçalo da Silva** | Desenvolvimento dos mapas, colisões, transições entre mapas, integração dos sprites do jogador e do vilão e implementação da movimentação visual conforme a direção. |
| **Carlos Mathias Roma** | Implementação da lógica dos objetos coletáveis, gerenciamento das chaves, dicas, kits médicos e inventário. |
| **Geraldo Eufrázio Muniz Neto** | Desenvolvimento da lógica do jogador, movimentação, velocidade, inteligência do vilão e arquitetura orientada a objetos. |
| **Glucia Freire Kinkonda** | Desenvolvimento das telas do jogo e criação de diversos sprites utilizados durante a interface. |
| **Cássio Henrique de Freitas Silva** | Criação dos sprites dos personagens e demais recursos gráficos do projeto. |
| **Juan Henrique dos Santos** | Participação no desenvolvimento geral, testes e validação das funcionalidades implementadas. |


## 🤝 Desenvolvimento em Equipe

Durante o desenvolvimento, os integrantes utilizaram o **Git** e o **GitHub** para controlar versões do código, integrar funcionalidades e acompanhar a evolução do projeto de forma colaborativa.

A divisão em módulos permitiu que diferentes funcionalidades fossem implementadas simultaneamente, reduzindo conflitos entre arquivos e tornando o desenvolvimento mais organizado.

# 💻 9. Conceitos de Programação Utilizados

Durante o desenvolvimento do **CInBeribe**, foram aplicados diversos conceitos estudados na disciplina de Introdução à Programação, permitindo a construção de um projeto organizado, reutilizável e de fácil manutenção.

### 🧩 Programação Orientada a Objetos (POO)

A arquitetura do jogo foi baseada em Programação Orientada a Objetos, utilizando classes para representar personagens, itens coletáveis, portas e demais elementos do jogo. Também foram utilizados os conceitos de herança, encapsulamento e reutilização de código.

### 📂 Modularização

O projeto foi dividido em diferentes módulos e pacotes, separando mapas, personagens, objetos, colisões e interfaces. Essa organização facilitou o desenvolvimento em equipe e tornou o código mais legível.

### 🔄 Estruturas de Repetição

Laços de repetição foram utilizados no loop principal do jogo, na atualização dos personagens, na renderização dos mapas e no gerenciamento dos objetos presentes em cada cenário.

### 🔀 Estruturas Condicionais

Estruturas condicionais controlam eventos importantes do jogo, como movimentação entre mapas, coleta de itens, perseguição do inimigo e verificação das condições de vitória e derrota.

### 📋 Listas

Listas foram utilizadas para armazenar objetos coletáveis, colisões, mapas, chaves, dicas, kits médicos e demais elementos que precisam ser percorridos durante a execução do jogo.

### ⚙️ Funções

O projeto foi organizado em funções específicas para movimentação, desenho dos elementos, troca de mapas, verificação de colisões e atualização das mecânicas do jogo, tornando o código mais reutilizável e organizado.

### 🎮 Tratamento de Eventos

O Pygame foi utilizado para capturar eventos do teclado e do mouse, permitindo controlar a movimentação do jogador, a interação com os menus e os botões das telas de vitória e derrota.

# 📚 10. Aprendizados e Desafios

O desenvolvimento do **CInBeribe** proporcionou à equipe uma experiência prática na construção de um projeto completo utilizando Python e Pygame.

Entre os principais desafios enfrentados, destacam-se:

- Implementação das colisões dos onze mapas;
- Organização do projeto utilizando Programação Orientada a Objetos;
- Integração das funcionalidades desenvolvidas pelos diferentes integrantes;
- Desenvolvimento da lógica de perseguição do inimigo e transição entre mapas.

Ao longo de aproximadamente **um mês de desenvolvimento**, a equipe aprimorou conhecimentos em programação, trabalho colaborativo com Git e GitHub e organização de projetos de software.


# 🎮 11. Como Jogar

## Controles

| Tecla | Ação |
|--------|------|
| **W** ou **↑** | Mover para cima |
| **S** ou **↓** | Mover para baixo |
| **A** ou **←** | Mover para a esquerda |
| **D** ou **→** | Mover para a direita |

## Objetivo

Para vencer a partida, o jogador deve:

- 🔑 Coletar as **3 chaves** espalhadas pelos mapas;
- ❤️ Permanecer com pelo menos **1 coração de vida**;
- 🚪 Alcançar a porta de saída localizada no Laboratório de Hardware.

As pistas são opcionais e auxiliam na localização das chaves, enquanto os kits médicos permitem recuperar vidas durante a exploração.


# 🚀 12. Melhorias Futuras

Algumas funcionalidades planejadas para versões futuras do jogo incluem:

- 👾 Novos inimigos com comportamentos diferentes;
- 🗺️ Novos mapas e ambientes exploráveis;
- 🔐 Passagens secretas entre salas;
- 🏆 Sistema de ranking por tempo de conclusão;
- 🎵 Sons e trilha sonora para aumentar a imersão.


# ⭐ Considerações Finais

O **CInBeribe** foi desenvolvido como projeto da disciplina de **Introdução à Programação (IF668)**, aplicando na prática os principais conceitos estudados ao longo da disciplina.

Além de reforçar conhecimentos técnicos em Python e Programação Orientada a Objetos, o projeto proporcionou experiência em desenvolvimento colaborativo, organização de código e utilização de ferramentas de versionamento.

A equipe espera continuar evoluindo o projeto no futuro, adicionando novas mecânicas e funcionalidades para tornar a experiência do jogador ainda mais divertida e desafiadora.
