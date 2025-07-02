# Exercícios de Segurança e Auditoria de Sistemas – Perguntas e Respostas

---

### **Parte 1: Criptografia Simétrica e Modos de Operação**

**1. O que é um esquema computacionalmente seguro?**

Um esquema de criptografia é considerado computacionalmente seguro se o custo para quebrar a cifra excede o valor da informação criptografada, ou se o tempo necessário para a quebra excede o tempo de vida útil da informação. A segurança de algoritmos modernos não reside em seu desconhecimento, mas em sua robustez matemática. Por exemplo, o DES, com sua chave de 56 bits, tornou-se inseguro pois máquinas especializadas conseguiram quebrá-lo por força bruta em menos de 56 horas, demonstrando que o tempo de quebra se tornou prático.

**2. Para os algoritmos DES, 3DES e AES, complete:**
* **a) Tamanho de bloco.**
    * **DES:** 64 bits (8 bytes).
    * **3DES:** 64 bits (8 bytes), pois utiliza o mesmo bloco do DES.
    * **AES:** 128 bits (16 bytes).
* **b) Possíveis tamanho de chave.**
    * **DES:** 56 bits.
    * **3DES:** Chaves de 112 bits ou 168 bits, alcançando uma segurança efetiva de até 112 bits.
    * **AES:** Suporte para chaves de 128, 192 e 256 bits.

**3. Cite os modos de operação, apresentando o diagrama de bloco e características de duas delas.**

Os modos de operação definem como os blocos de dados são processados. Os cinco principais são:
* ECB (Electronic Codebook)
* CBC (Cipher Block Chaining)
* CFB (Cipher Feedback)
* OFB (Output Feedback)
* CTR (Counter)

**a) Electronic Codebook (ECB)**
* **Características:** É o modo mais simples, onde cada bloco de texto claro é cifrado de forma independente dos outros. A principal desvantagem é que blocos de texto claro idênticos geram blocos de texto cifrado idênticos, o que pode revelar padrões nos dados.
* **Diagrama de Bloco:** O diagrama está ilustrado no documento "Criptografia Moderna  Cifras de Bloco e de Fluxo.pdf" (página 29).

**b) Cipher Block Chaining (CBC)**
* **Características:** Neste modo, cada bloco de texto claro é combinado (via XOR) com o bloco cifrado anterior antes da criptografia, utilizando um Vetor de Inicialização (IV) para o primeiro bloco. Isso garante que blocos de texto claro idênticos resultem em blocos cifrados diferentes.
* **Diagrama de Bloco:** O diagrama está disponível no documento "Criptografia Moderna  Cifras de Bloco e de Fluxo.pdf" (página 37).

**4. Por que existe a necessidade de usar padding?**

Cifras de bloco como DES, 3DES e AES operam em blocos de dados de tamanho fixo. Se a mensagem a ser criptografada não for um múltiplo exato do tamanho do bloco do algoritmo, é necessário usar *padding* (preenchimento) para adicionar bytes e completar o último bloco antes da criptografia.

**5. Cite e explique 4 tipos de paddding.**

O documento "Criptografia Moderna  Cifras de Bloco e de Fluxo.pdf" (páginas 54-55) apresenta vários padrões, incluindo:
1.  **Zero padding:** O último bloco é preenchido com bytes `0x00`.
2.  **ANSI X.923:** O bloco é preenchido com bytes `0x00`, e o último byte indica a quantidade de bytes de preenchimento adicionados.
3.  **ISO/IEC 7816-4:** Adiciona-se um byte `0x80` e o restante é preenchido com bytes `0x00`.
4.  **PKCS#7:** O preenchimento é feito com N bytes, onde cada byte tem o valor N, correspondendo ao número de bytes que faltam para completar o bloco.

**6. Escolha um tipo de padding que você considera bom e argumente sua decisão.**

O **PKCS#7** é um excelente método de padding, pois é inequívoco. O valor do último byte decifrado indica o número de bytes de preenchimento a serem removidos, e o sistema pode verificar se todos os bytes de preenchimento têm esse mesmo valor. Isso elimina a ambiguidade que pode ocorrer em métodos mais simples, como o *Zero padding*, onde um byte `0x00` no final da mensagem original poderia ser confundido com o preenchimento.

**7. Considere as seguintes mensagens (em hexadecimal):**
`i. "00 11 22 33 44 55 66 77 88 99 AA"`
`ii. "FF EE DD CC BB AA 99 88 77 66 55 44 33 22 11"`
**Complete as mensagens i e ii com padding para algoritmo informado:**

* **a) Zero padding e algoritmo DES.**
    * **Resultado:** `00 11 22 33 44 55 66 77 88 99 AA **00 00 00 00 00**`
* **b) Padding ISO/IEC 7816-4 e algoritmo 3DES.**
    * **Resultado:** `FF EE DD CC BB AA 99 88 77 66 55 44 33 22 11 **80**`
* **c) Padding PKCS#7 e algoritmo AES.**
    * **Resultado:** `FF EE DD CC BB AA 99 88 77 66 55 44 33 22 11 **01**`

**8. Utilizando o bloco abaixo, que representa a cifra DES, monte o diagrama de bloco:**
* **a) Criptografar a mensagem com tamanho de 24 bytes, modo de operação CFB, algoritmo DES.**
    * O diagrama está representado textualmente abaixo, com base no esquema do documento "Criptografia Moderna  Cifras de Bloco e de Fluxo.pdf" (página 42).
    ```
                                 Vetor de Inicialização (IV)
                                            |
                                            V
      +------------------+          +-----------------+
      | Chave (K) 56 bits|--------->|  Encriptar (DES)  |
      +------------------+          +-----------------+
                                            |
                                            |   +-------------------+
                                            +-->|        XOR        |<---- Bloco de Texto Claro 1 (P1)
                                                +-------------------+
                                                          |
                                                          V
                                                Bloco Cifrado 1 (C1) --> (Alimenta próximo passo)
    ```
* **b) Decriptografar a mensagem com tamanho de 16 bytes, modo de operação CBC, algoritmo 3DES, chave de 168 bits.**
    * O diagrama está representado textualmente abaixo, com base nos esquemas de "Criptografia Moderna  Cifras de Bloco e de Fluxo.pdf" (página 37) e "Algoritmos de Criptografia  DES, 3DES e AES.pdf" (páginas 16, 18).
    ```
     Bloco Cifrado 1 (C1) --------------------------------+
            |                                             |
            V                                             |
    +-----------------+                                   |
    |Decriptar (3DES) |                                   |
    | Chave 168 bits  |                                   |
    +-----------------+                                   |
            |                                             |
            |          Vetor de Inicialização (IV)        |
            |                  |                          |
            V                  V                          V
    +-------------------+                           Bloco Cifrado 2 (C2)
    |        XOR        |                                   |
    +-------------------+                                   |
            |                                             V
            V                                       +-----------------+
    Bloco de Texto Claro 1 (P1)                     |Decriptar (3DES) |
                                                    | Chave 168 bits  |
                                                    +-----------------+
                                                              |
                                                              |   +-------------------+
                                                              +-->|        XOR        |
                                                                  +-------------------+
                                                                            |
                                                                            V
                                                                  Bloco de Texto Claro 2 (P2)
    ```

---

### **Parte 2: Números Aleatórios e Hash Criptográfico**

**9. Qual a diferença de números aleatórios e pseudoaleatório?**
* **Números Aleatórios Verdadeiros (TRNG):** São gerados a partir de processos físicos e possuem real aleatoriedade. Um número aleatório não pode ser previsto a partir dos membros anteriores de sua série. Conhecer uma longa sequência de bits não ajuda a prever o próximo número.
* **Números Pseudoaleatórios (PRNG):** Possuem a aparência de aleatoriedade, mas são gerados por algoritmos determinísticos. Se o algoritmo e sua semente (estado interno) forem conhecidos, toda a sequência pode ser prevista.

**10. Quais as propriedades desejáveis de números pseudoaleátorios?**
* **Sequências sem correlação:** As sequências de números aleatórios não devem possuir relação com as anteriores.
* **Período longo:** O gerador deve possuir um período entre repetições muito longo.
* **Uniformidade:** A sequência de números aleatórios deve ser uniforme, com frações iguais de números caindo em áreas iguais do espaço de números.
* **Eficiência:** O gerador deve ser eficiente e gerar baixo overhead.

**11. O que é "semente", no contexto de PRNGs?**

A semente é o estado interno ou valor inicial de um Gerador de Números Pseudoaleatórios (PRNG). É a entrada para o algoritmo determinístico que gera a sequência de bits pseudoaleatória.

**12. Como escolher uma boa semente?**

Uma boa semente deve ter bastante entropia. Ela pode ser gerada a partir de fontes físicas externas e imprevisíveis. Exemplos de quantidades físicas usadas para gerar sementes incluem:
* Tempo entre digitações de teclas.
* Turbulência de ar das cabeças de leitura de discos rígidos.
* Medição de atrasos na CPU ou outro dispositivo.
* Captação de interferência em ondas de rádio.
* Tempos de desintegração de átomos radioativos.

**13. Cite e explique algumas aplicações de PRNGs na criptografia.**

PRNGs são muito importantes e são a base para muitas aplicações criptográficas. Aplicações diretas incluem:
* **Geração de chaves**.
* **Nonces**.
* **Salts**.
* **One-time pads**.

**14. O que é e para que serve o "teste do próximo bit"?**

É um teste para verificar se um gerador de números é adequado para criptografia. A ideia é que, após analisar os primeiros *n* bits de uma sequência, um adversário deve tentar adivinhar o bit *n+1*. Um gerador pseudoaleatório é considerado seguro para criptografia se ele passa nesse teste, ou seja, se nenhum adversário consegue prever o próximo bit com probabilidade significativamente maior que 50%.

**15. Por que precisamos de boas fontes de entropia em criptografia? Onde podemos encontrar essas fontes?**

Entropia é a medida de incerteza ou aleatoriedade de um conjunto de números. Precisamos dela porque sistemas iniciados sem entropia suficiente são vulneráveis a ataques. Se as entradas de um PRNG se tornam dedutíveis, a segurança é comprometida. Fontes físicas de entropia, como as listadas na questão 12, são cada vez mais utilizadas para obter números aleatórios verdadeiros. O ESP32, por exemplo, usa ruído térmico e clocks assíncronos como fonte de entropia para gerar números aleatórios verdadeiros.

**16. O que é Hash Criptográfico?**

Uma função de hash criptográfico é uma função que recebe uma entrada de tamanho arbitrário (como um documento ou mensagem) e produz uma saída de tamanho fixo, chamada de "valor hash" ou "resumo". Ela é usada em contextos de segurança e precisa ser resistente a ataques maliciosos.

**17. Cite e explique cada um dos requisitos de um Hash criptográfico.**

Além do determinismo, um hash criptográfico deve ter as seguintes propriedades de segurança:
* **Irreversibilidade (Função de mão única):** Deve ser computacionalmente inviável derivar a entrada original a partir do hash. Também conhecida como Resistência à 1ª inversão.
* **Resistência à 2ª inversão (Second Pre-image Resistance):** Dado um `x1`, deve ser computacionalmente inviável encontrar um `x2 ≠ x1` tal que `h(x1) = h(x2)`.
* **Resistência a colisões:** Deve ser computacionalmente inviável encontrar quaisquer dois valores `x1` e `x2` distintos tais que `h(x1) = h(x2)`.
* **Efeito Avalanche:** Uma pequena alteração na entrada deve causar uma mudança significativa e imprevisível na saída.

**18. Cite algumas aplicações de Hash.**

* **Integridade de dados**.
* **Assinatura digital**.
* **Proteção de senhas:** Armazena-se o hash da senha, e não a senha em si.
* **Autenticação de mensagens**.
* **Digital Timestamping:** A data e hora do documento entram no cálculo do hash para provar sua existência em um determinado momento.

**19. Por que em alguns sites que disponibilizam um determinado arquivo para download, também disponibilizam o hash do arquivo?**

Isso é feito para permitir a **verificação de integridade dos dados**. O usuário, após o download, pode calcular o hash do arquivo em sua máquina e comparar com o valor fornecido pelo site. Se os hashes forem idênticos, confirma-se que o arquivo não foi corrompido ou modificado durante a transferência. A avaliação da integridade é feita comparando os valores de hash, e não os documentos.

**20. O que é o ataque do aniversário, no contexto de hash? Quanto ele diminui a força (segurança) do hash?**

É um tipo de ataque que visa encontrar colisões em funções de hash. Baseia-se no paradoxo de que a probabilidade de duas pessoas em um grupo pequeno fazerem aniversário no mesmo dia é surpreendentemente alta. Para uma função de hash com saída de *n* bits, a força contra ataques de inversão é de 2^n, mas o ataque de aniversário reduz a força contra colisões para aproximadamente 2^(n/2) operações.

**21. Cite 3 exemplos de algoritmos de hash, apresentando o tamanho do bloco, do resumo e sua segurança (em bits).**

A tabela no documento "Criptografia Moderna  Hash Criptográfico.pdf" fornece as seguintes informações:
1.  **MD5:**
    * Tamanho do Bloco: 512 bits
    * Tamanho do Resumo: 128 bits
    * Segurança (contra colisão): 64 bits (considerado inseguro)
2.  **SHA-256:**
    * Tamanho do Bloco: 512 bits
    * Tamanho do Resumo: 256 bits
    * Segurança (contra colisão): 128 bits
3.  **SHA-512:**
    * Tamanho do Bloco: 1024 bits
    * Tamanho do Resumo: 512 bits
    * Segurança (contra colisão): 256 bits

**22. O que é HMAC? Apresente um exemplo de onde pode ser utilizado e qual o seu papel (função).**

**HMAC (Hash-based Message Authentication Code)** é uma técnica que utiliza uma função de hash criptográfico junto com uma chave secreta para criar um código de autenticação de mensagens (MAC). Seu papel é verificar tanto a **integridade** (se a mensagem foi alterada) quanto a **autenticidade** (se a mensagem veio de quem possui a chave) dos dados. É amplamente utilizado em protocolos de segurança como o TLS e em serviços de API.

**23. Faça um desenho esquemático para a geração e verificação de uma mensagem de autenticação utilizando HMAC.**

O processo, conforme descrito e ilustrado no documento "Criptografia Moderna  Hash Criptográfico.pdf" (páginas 23-24), é o seguinte:
* **1. Geração (Remetente):** O remetente combina a mensagem com uma chave secreta e aplica a função HMAC, gerando uma *tag* HMAC.
* **2. Envio:** O remetente envia a mensagem original junto com a *tag* HMAC.
* **3. Verificação (Destinatário):** O destinatário recebe a mensagem e a *tag*. Usando a mesma chave secreta, ele recalcula a *tag* HMAC a partir da mensagem recebida.
* **4. Comparação:** Ele compara a *tag* que calculou com a que recebeu. Se forem idênticas, a mensagem é considerada autêntica e íntegra.
