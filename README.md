# caseHeinz

![logogs-removebg-preview](https://github.com/Rodrigo-Brasileiro/caseHeinz/assets/126472820/2cd126f6-513e-4762-bfc2-2e14e4d12019)

<h2>Problema:</h2>
  <p> A geração dos boomers é uma parcela da população nascida durante o período chamado baby boom, evento muito significativo que marca o fim da Segunda Guerra Mundial, com soldados retornando as suas famílias e consequentemente aumentando a natalidade. Essa linhagem abrange final da década de 40 até começo de 60. Assim, dados da ONU dizem que a população de 1950 era de 2,5 bilhões de habitantes, hoje passando de 8 bilhões, não atoa, muitas temáticas entraram em discussão pelo aumento populacional que passam por segurança social, sistemas de saúde, política e talvez o mais discutido, alimentação. </p>
  <p> O tema se tornou altamente disseminado em virtude de desempenhar um papel fundamental na saúde, bem-estar e qualidade de vida das pessoas. Desse modo, o que comemos afeta diretamente nosso corpo e mente, influenciando nosso desempenho físico, cognitivo e emocional, de modo que nesses debates são intrínsecos tópicos como sustentabilidade, segurança alimentar e novas tendências alimentares. Nessa linha de raciocínio que a empresa HEINZ nos contratou, buscar inovações por meio de tecnologia para aspectos alimentícios, nós somos o grupo Tech Pulse Global Network e buscamos por meio da ciência programacional melhorar o processo de produção alimentícia relacionado a agricultura vertical.</p>

  <p> Primeiramente, a agricultura vertical é um método de plantação, o qual são construídas prateleiras com diversas lavras a serem cultivadas em ambientes controlados, o que a beneficia ao ponto ser plantada em grandes centros urbanos como prédios ou galpões e, o mais importante longe de pragas. Nesse sistema, a luz LED é usada em substituição do Sol, trazendo a vantagem de ser volátil e adaptável as diversas fases de crescimento, desde semente ao amadurecimento da planta. Por essas razões o vegetal cresce mais rápido e saudável, fazendo-a chegar na mesa da população em menor tempo, gerando mais comida em menos tempo.</p>
  
  <h2>Solução:</h2>
  Nossa solução abrange dois tópicos, a primeira é a solução de um programa em python que visa ajudar os produtores de alimentos a saber a margem de ganhos que eles terão com suas plantações e a outra é a solução prática(circuito eletrônico com foco no arduino uno r3 que tem como foco monitorar as lavras), assim cada um será descrita a seguir.</h2>
  <h3> Sistema python</h3>
  <p> O desenvolvimento da plataforma foi criada para auxiliar os produtores de agricultura vertical, os requisitos até o momento por limitações são que o produto a ser calculado deve ser entre soja, tomate e morango.</p>
 <h4>Como usar o programa?</h4>
 <p> Para o uso do programa o usuário existem alguns requisitos, além de sua plantação ser de um dos alimentos citados anteriormente, são eles: tem que estar com um aplicativo que seja compatível com a linguagem python e estar com o código do trabalho, só então poderá usufruir dos benefícios dele.</p>
<p>  OBS: Vale ressaltar que o projeto está em seu início e atualizações podem ocorrer para que novos alimentos sejam adicionados para auxiliar agricultores na tarefa de prever as variáveis das plantações.</p>

<h3>Solução prática:</h3>
  <p> Para o monitoramento desse tipo de cultivo, implementamos diversos sensores e atuadores que ficarão na estufa de produção, são eles:</p>
    <li>O sensor de luminosidade(LDR) que verifica a quantidade luminosa, se está de acordo com a fase atual da planta;</li>
    <li>Sensor de temperatura e umidade do ar DHT-11, para verificar se precisam ser alteradas;</li>
    <li>Sensor de umidade do solo;</li>
    <li>Bomba d'água com motor, caso o solo precise ser regado, após receber dados do sensor de umidade do solo;</li>
    <li>Lâmpada Led regulável, de acordo com a luminosidade apontada pelo LDR;</li>
    <li>Display tela LCD 16x2, o qual mostrará as informações dos sensores em sua tela por 5 segundos, deixando inteirado os produtores sobre a qualidade do ambiente;</li>
    <li>Tudo agregado a uma placa de prototipação Arduino uno R3.</li>
  <p>O projeto funciona com os sensores captando informações e regulando conforme a necessidade nas estações da planta, de forma que que deve funcionar sem interferência humana.</p>
  <p>Além dos componentes citados acima, estão presentes dois resistores de 220ohms e um resistor de 1k, ademais diversos jumpers (macho-macho, macho-fêmea e fêmea-fêmea). </p>

 
<h4>Observações:</h4>
  <li>O ideal é o projeto ter uma shield ethernet uno para mandar os dados à nuvem, a qual por falta de conhecimentos técnicos e ausência no Tinkercad, não é possível sua presença;</li>
  <li>Além de um circuito com bateria de 9v integrada para ficar ligado continuamente sem riscos;</li>
  <li> O tinkercad não possui o sensor de umidade e temperatura DHT-11, desse modo precisa-se baixar sua biblioteca externa e a inserir no aplicativo do arduino;</p>
  <li> O nosso sistema no tinkercad possui algumas limitações, de modo que a implementação do projeto não é possível, as limitações são:
    <ol> lâmpada LED, que é representada por um simples LED amarelo e um potenciômetro que altera sua intensidade luminosa;</ol>
    <ol> O Próprio sensor DHT-11, como ele não existe no tinkercad, colocamos um simulador dele com o sensor de temperatura com potenciômetro, em vista disso o código apresentado é diferente do tinkercad, ou seja, ao ser utilizado para o aplicativo arduino não precisa de alteração, somente a biblioteca externa.</ol>

<h2>Tecnologia usada:</h2>
  Durante as implementações do programa de cálculo, utilizamos o aplicativo Visual Studio Code com um arquivo na linguagem Python. Para experimentos virtuais do circuito, usamos o Tinkercad com a linguagem C++.
  Link da Simulação Público Tinkercad:
  https://www.tinkercad.com/things/kgafd58xMyU  

Para a utilização do DHT11, utilizamos uma biblioteca externa do site:

https://blogmasterwalkershop.com.br/arduino/como-usar-com-arduino-sensor-de-umidade-e-temperatura-dht11 </p>

<h2>Integrantes do grupo</h2>
<p>GUILHERME ROCHA BIANCHINI - RM: 97974</p>
<p>NIKOLAS RODRIGUES MOURA DOS SANTOS - RM: 551566</p>
<p>PEDRO HENRIQUE PEDROSA TAVARES - RM:97877</p>
<p>RODRIGO BRASILEIRO - RM:98952</p>
<p>THIAGO JARDIM DE OLIVEIRA - RM:551624</p>
