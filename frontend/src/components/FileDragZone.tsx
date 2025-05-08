import {type Dispatch, type SetStateAction, useState} from "react";
import {useDropzone} from "react-dropzone";

type FileDragZoneProps = {
  fileState: [File | null, Dispatch<SetStateAction<File | null>>]
}

export function FileDragZone({
  fileState
}: FileDragZoneProps) {
  const [file, setFile] = fileState;
  const [preview, setPreview] = useState<string | null>(null);

  const { getRootProps, getInputProps } = useDropzone({
    accept: { 'image/*': ['.jpg', '.jpeg', '.png']},
    onDrop: acceptedFiles => {
      setFile(() => acceptedFiles[0]);
      if (file) setPreview(URL.createObjectURL(file));
    }
  })

  return (
    <div
      className='w-25 border p-4
        point text-white mx-auto'
      style={{ cursor: 'pointer', aspectRatio: '9/16', maxHeight: '27rem'}}
    >
      <div
        className='d-flex flex-column justify-content-center h-100 w-100'
        {...getRootProps()}
      >
        <input {...getInputProps()} />
        {!preview &&
          <p className='text-center my-auto'>
            Arraste ou clique para selecionar uma imagem
          </p>
        }
        {preview &&
          <img
            className='w-100 h-100 object-fit-contain'
            src={preview}
            alt="Preview"
          />
        }
      </div>
    </div>
  );
}