from typing import TypedDict
from mistralai import Mistral
from models.redacao_models import Correcao, Redacao
import re
import os

class _Message(TypedDict):
    role: str
    content: str


class RedacaoEvaluatorService:
    START_PARAGRAPH_TOKEN='<START_PARAGRAPH>'
    END_PARAGRAPH_TOKEN='<END_PARAGRAPH>'

    def __init__(self):
        api_key: str = os.getenv('MISTRAL_API_KEY')
        self._client = Mistral(api_key=api_key)

    def _generate_correcao(self, messages: list[_Message]) -> Correcao:
        mistral_agent_id = os.getenv('MISTRAL_AGENT_ID')

        chat_response = self._client.agents.complete(
            agent_id=mistral_agent_id,
            messages=messages,
        )

        response: str = chat_response.choices[0].message.content

        return Correcao.model_validate_json(response)

    def evaluate(self, redacao: Redacao) -> Correcao:
        normalized_content: str = ''.join([
            self.START_PARAGRAPH_TOKEN,
            re.sub(
                r'(\r?\n|\r)+',
                (self.START_PARAGRAPH_TOKEN + self.END_PARAGRAPH_TOKEN),
                redacao.conteudo
            ),
            self.END_PARAGRAPH_TOKEN,
        ])

        normalized_redacao = Redacao(
            tema=redacao.tema,
            conteudo=normalized_content,
        )

        messages: list[_Message] = [
            {"role": "user", "content": normalized_redacao.model_dump_json()},
        ]

        return self._generate_correcao(messages)