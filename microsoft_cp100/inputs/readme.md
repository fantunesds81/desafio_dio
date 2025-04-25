# Azure AI Foundry - Playground de Chat

## Visão Geral

Este ambiente é parte da plataforma **Azure AI Foundry**, especificamente o **Playground de Chat**, utilizado para testar e construir aplicações com modelos de linguagem baseados em IA, como GPT.

A imagem mostra uma sessão em andamento, onde o usuário utiliza dados personalizados para realizar consultas inteligentes com base em PDFs enviados.

---

## Processo Demonstrado

1. **Fonte de Dados Personalizada**:
   - O usuário adicionou uma fonte de dados personalizada com o índice: `strong-caravan-lnzf7rdq6f`.
   - O tipo de pesquisa selecionado é "Palavra-chave", o que indica que o modelo busca as informações a partir de termos-chave presentes nos documentos carregados.

2. **Histórico de Chats**:
   - À direita, é possível ver uma resposta gerada pelo modelo, baseada em três documentos PDF:
     1. `Python+Direto+ao+Ponto+-+Estevao+Paiva+Fonseca.pdf`
     2. `Livro de Python (Automatize tarefas maçantes).pdf`
     3. `Luiz Eduardo Borges ...ores - 2ª Edição.pdf`

   - O modelo foi questionado sobre a origem do nome "Python", e respondeu utilizando referências nos documentos adicionados.

3. **Funcionalidades Utilizadas**:
   - Exibição do código (possivelmente para fins de auditoria ou exportação).
   - Formato de resposta em **Texto**, com a possibilidade de alterar para outras visualizações.
   - Parâmetros e configurações avançadas disponíveis, embora não detalhados na imagem.

---

## Insights

- A plataforma permite criar experiências de chat com IA usando **documentos próprios como base de conhecimento**.
- A capacidade de importar e pesquisar documentos por palavra-chave é útil para cenários como **assistentes personalizados, chatbots com conhecimento de domínio**, ou ferramentas de suporte técnico.
- As referências numeradas no corpo da resposta do modelo facilitam a **auditoria e validação da informação**.

---

## Potenciais Aplicações

- Suporte técnico automatizado com base em manuais e guias internos.
- Assistentes de estudo com base em livros e apostilas.
- Bots corporativos para políticas e procedimentos internos.

---

## Conclusão

A interface do Playground do Azure AI Foundry demonstra um ambiente poderoso para testar aplicações de IA generativa com dados personalizados, unindo flexibilidade, rastreabilidade e integração com serviços do Azure.
