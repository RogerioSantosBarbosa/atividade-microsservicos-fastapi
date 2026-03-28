Atividade: Comuniação Síncrona entre Microsserviços com FastAPI

Este repositório contém a implementação de dois microsserviços (Fazendas e Culturas) para demonstrar a comunicação síncrona entre eles via HTTP (REST), utilizando FastAPI e Docker Compose.

**Microsserviço 1 - Culturas**
- Endpoint: '/culturas/{id}'
- Retorna dados simulados sobre culturas agrícolas (ex: soja, milho)

**Microsserviço 2 - Fazendas**
- Endpoint: '/fazendas/{id}'
- Consome os dados do serviço de Culturas para compor as informações da fazenda atual

**COMO EXECUTAR O PROJETO**
1. Clone este repositório;
2. No terminal, acesse a pasta raiz do projeto;
3. Execute o comando para construir e subir os containers: `docker-compose up --build`;
4. Acesse no navegador: `http://localhost:8000/fazendas/1`.

**SIMULAÇÕES**
1. Funcionamento Integrado (Sucesso)
   
<img width="886" height="465" alt="image" src="https://github.com/user-attachments/assets/81e62211-b8d0-485c-accf-716ea9648af3" />

Quando ambos os serviços estão online, o serviço de Fazendas consegue buscar com sucesso os dados da cultura atual.


2. Simulação de falha na comunicação
   
<img width="886" height="542" alt="image" src="https://github.com/user-attachments/assets/ca22f4d2-ebdf-4eda-aa89-8c2f2cc54930" />

Derrubando o serviço de Culturas, o tratamento de erro do serviço de Fazendas entra em ação, exibindo uma mensagem amigável sem quebrar a aplicação (Erro 500).


4. Simulação de Timeout demorado
   
<img width="886" height="490" alt="image" src="https://github.com/user-attachments/assets/8273a0b7-3687-4fd4-a323-9c702772924d" />

Adicionando um atraso de 5 segundos no serviço de Culturas, o serviço de Fazendas atinge o seu limite de espera de 2 segundos e encerra a requisição antecipadamente, caindo na mesma tratativa de erro sem travar o usuário.


**ANÁLISE DE PROBLEMAS DA ARQUITETURA SÍNCRONA**
"Neste tipo de implementação, quais problemas podem ocorrer?"
Por haver uma forte dependência, o serviço de Fazendas só consegue funcionar com eficiência se o serviço de Culturas estiver online exatamente no mesmo momento. Ainda nesse sentido, o risco de falhas em cascata é real, pois se o serviço de Culturas travar e ficar muito tempo sem responder, o serviço de Fazenda irá travar também esperando a resposta, o mesmo ocorre se muitos usuários acessarem ao mesmo tempo. Por fim, aqui também se aplicam os conceitos de Overfetching e Underfetching, pois como apontado nos slides, o serviço de Fazendas pode precisar fazer várias requisições separadas para montar uma única tela ou receber dados demais que nem vai usar, desperdiçando banda. 
