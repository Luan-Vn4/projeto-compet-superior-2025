# Projeto: CorretorAI

## Visão Geral

Este projeto tem como objetivo automatizar a correção de redações do ENEM. A proposta é utilizar técnicas de OCR (Reconhecimento Óptico de Caracteres) combinadas com um modelo de linguagem (LLM) para extrair o texto da redação manuscrita e avaliá-lo com base nos critérios utilizados pelo ENEM.

O sistema é composto por uma **arquitetura distribuída** com múltiplas APIs que se comunicam entre si para realizar todo o processo — desde a recepção da imagem até o retorno da correção.

---

# Como rodar:

Claro! Aqui está uma seção **"Como rodar o projeto"** que você pode adicionar ao seu `README.md`, seguindo os padrões mais comuns usados no GitHub para projetos Python com múltiplas APIs e um frontend React:

---

## Como rodar o projeto

Para executar o projeto localmente, você precisará ter o **Python 3.10+** e o **Node.js 21.6.2+** instalados em sua máquina.

A aplicação é composta por três APIs (OCR e LLM) escritas em Python, e um frontend desenvolvido em React.

### Estrutura de pastas esperada

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-enem.git
cd projeto-enem
```

### 2. Configure os ambientes Python para as APIs

Você pode usar `venv` ou `conda`. Abaixo um exemplo com `venv`.

#### Para cada API, faça:

```bash
cd nome-da-api 
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Repita o processo acima para as três APIs: `ocr-api`, `llm-api`.

### 3. Rode as APIs simultaneamente

Cada API deve rodar em uma porta diferente. Você pode iniciar cada uma em um terminal separado:

```bash
cd ocr
uvicorn main:app --reload

cd llm
uvicorn main:app --reload
```

### 4. Rode o frontend React

```bash
cd frontend
npm install
npm run dev
```

A aplicação React deve estar disponível em `http://localhost:5173` ou a porta definida pelo Vite.

---

## Componentes da Arquitetura

A arquitetura do sistema é composta pelos seguintes serviços:

### 1. **Frontend**

* Permite que o usuário envie uma imagem contendo a redação escrita à mão.
* Recebe a avaliação final da redação.

### 2. **Gateway API**

* Responsável por coordenar o fluxo entre os serviços.
* Recebe a imagem enviada pelo frontend.
* Encaminha a imagem para a API OCR.
* Recebe o texto extraído da imagem.
* Envia o texto para a API LLM.
* Recebe a avaliação da redação e retorna ao frontend.

### 3. **OCR API**

* API responsável por realizar o reconhecimento de caracteres (OCR) na imagem.
* Encapsula um OCR instalado em um servidor específico.
* Retorna o texto extraído da imagem para a API Gateway.

### 4. **LLM API**

* Recebe o texto extraído da redação e aplica critérios de correção baseados no ENEM.
* Utiliza um modelo de linguagem (LLM) para:

  * Corrigir ortografia e gramática.
  * Avaliar a coesão, argumentação e estrutura textual.
  * Classificar a redação com base nas **cinco competências** do ENEM.
* Retorna a correção detalhada para a API Gateway.

---

## Correção com Base no ENEM

O modelo de linguagem utilizado na API LLM foi ajustado para seguir os critérios oficiais do ENEM, que incluem:

1. **Domínio da norma culta da língua portuguesa.**
2. **Compreensão da proposta de redação.**
3. **Capacidade de selecionar, relacionar, organizar e interpretar informações.**
4. **Demonstração de conhecimento da língua necessária para argumentação.**
5. **Elaboração de proposta de intervenção para o problema abordado.**

A correção retornada inclui feedback textual e notas (simuladas) para cada uma dessas competências.

---

## Exemplo de Fluxo

1. Usuário envia imagem da redação → **Frontend**
2. Imagem é enviada para → **Gateway API**
3. Gateway envia imagem para → **OCR API**
4. Texto extraído é enviado para → **LLM API**
5. Avaliação completa é retornada ao usuário via → **Gateway → Frontend**

---

## Tecnologias Utilizadas

* Python / FastAPI
* EasyOCR
* Mistral NeMo
---

## Objetivo Educacional

Este projeto tem como foco auxiliar estudantes que se preparam para o ENEM, oferecendo uma forma prática e automatizada de receber feedback sobre suas redações, a partir de imagens capturadas com o celular ou digitalizações.
