# DevOps Microservice

Este microservicio fue desarrollado usando **FastAPI** y se encuentra contenerizado con **Docker** y **docker-compose**.

## Endpoints

- `POST /DevOps`: Envía un mensaje con JWT y API Key.
- Solo se permite método `POST`.
- Headers requeridos:
  - `X-Parse-REST-API-Key`: API Key
  - `X-JWT-KWY`: JWT válido

## Autenticación

- Se valida una API Key fija: `2f5ae96c-b558-4c7b-a590-a501ae1c3f6c`
- Se valida un JWT firmado con el secreto: `tu_secreto_muy_seguro`

Puedes generar un token JWT ejecutando:

```bash
python app/generate_jwt.py
