from typing import TypedDict
from mistralai import Mistral
from models.redacao_models import Correcao, Redacao
import re

class Message(TypedDict):
    role: str
    content: str


class AvaliadorRedacao:
    START_PARAGRAPH_TOKEN='<START_PARAGRAPH>'
    END_PARAGRAPH_TOKEN='<END_PARAGRAPH>'

    @staticmethod
    def _generate(messages: list[Message]) -> Correcao:
        api_key = 'API_KEY'

        client = Mistral(api_key=api_key)

        chat_response = client.agents.complete(
            agent_id="AGENT_ID",
            messages=messages,
        )

        response: str = chat_response.choices[0].message.content

        print('Response:', response)

        return Correcao.from_json(response)

    def avaliar(self, tema: str, conteudo: str) -> str:
        normalized_content: str = ''.join([
            self.START_PARAGRAPH_TOKEN,
            re.sub(
                r'(\r?\n|\r)+',
                (self.START_PARAGRAPH_TOKEN + self.END_PARAGRAPH_TOKEN),
                conteudo
            ),
            self.END_PARAGRAPH_TOKEN,
        ])

        redacao = Redacao(tema=tema, conteudo=normalized_content)

        messages: list[Message] = [
            {"role": "user", "content": redacao.to_json()},
        ]

        return self._generate(messages).to_json()