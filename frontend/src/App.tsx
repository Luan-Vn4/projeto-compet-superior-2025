import './App.css'
import './components/FileDragZone.tsx'
import {type FormEvent, useRef, useState} from "react";
import {FileDragZone} from "./components/FileDragZone.tsx";
import type {Correcao} from "./models/Correcao.ts";

const API_ENDPOINT = 'http://localhost:8000';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const themeInputRef = useRef<HTMLInputElement>(null);
  const [correcao, setCorrecao] = useState<Correcao | null>(null);

  const onSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!file) return;
    if (!themeInputRef.current?.value) return;

    const formData = new FormData();
    formData.append('theme', themeInputRef.current.value);
    formData.append('file', file);

    const response = await fetch(`${API_ENDPOINT}/correcao`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json() as Correcao;

    setCorrecao(data);
  }

  return (
    <>
      <nav className='navbar navbar-dark bg-primary'>
        <a
          className='navbar-brand'
          style={{
            fontSize: '1.5rem',
            padding: '0.5rem 1rem'
          }}
        >
          Projeto Compet Superior
        </a>
      </nav>
      <h1 className='text-white mx-auto text-center my-4'>
        Corretor de Redações
      </h1>
      <form
        className='d-flex flex-column gap-4'
        method="post"
        encType="multipart/form-data"
        onSubmit={onSubmit}
      >
        <FileDragZone fileState={[file, setFile]} />
        <div className='w-25 mx-auto'>
          <label
            htmlFor={'theme'}
            className='text-white'
          >
            Tema:
          </label>
          <input
            id={'theme'}
            ref={themeInputRef}
            type="text"
            className='form-control'
            placeholder='Insira o tema da redação...'
          />
        </div>
        <button
          className='btn btn-primary w-25 mx-auto'
          type="submit"
        >
          Enviar
        </button>
      </form>
      {correcao && <CorrecaoDisplay correcao={correcao!} />}
    </>
  )
}

function CorrecaoDisplay({
  correcao
}: { correcao: Correcao }) {

  const competencias = [
      correcao.competencia1,
      correcao.competencia2,
      correcao.competencia3,
      correcao.competencia4,
      correcao.competencia5,
  ];

  const competencia = (i: number) => (
    <div key={i}>
      <h1>Competência {i}</h1>
      <h2>Nota: </h2>
      <p>{competencias[i-1].nota}</p>
      <h2>Comentário </h2>
      <p>{competencias[i-1].comentario}</p>
    </div>
  )

  return (
    <section
        className='text-white'
        id='correcoes'
    >
      <h1>Tema:</h1>
      <p>{correcao.tema}</p>
      {
        competencias.map((_, i) => {
          return competencia(i+1)
        })
      }
    </section>
  )
}

export default App
