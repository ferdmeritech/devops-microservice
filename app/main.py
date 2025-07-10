from fastapi import FastAPI, Request, Header, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
import jwt

app = FastAPI()

API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
JWT_SECRET = "tu_secreto_muy_seguro"  # Usa el mismo secreto que usas para generar el JWT

@app.api_route("/DevOps", methods=["POST", "GET", "PUT", "DELETE", "PATCH"])
async def devops_endpoint(
    request: Request, 
    x_parse_rest_api_key: str = Header(None), 
    x_jwt_kwy: str = Header(None)
):
    # Validar API Key
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    # Validar JWT
    try:
        jwt.decode(x_jwt_kwy, JWT_SECRET, algorithms=["HS256"])
    except Exception:
        return JSONResponse(status_code=401, content={"error": "Invalid JWT"})

    # Solo aceptar método POST
    if request.method != "POST":
        # Responder con texto plano "ERROR" entre comillas para que coincida con el test
        return PlainTextResponse('"ERROR"', status_code=400)

    data = await request.json()
    # Validar campos básicos del JSON
    if not all(k in data for k in ("message", "to", "from", "timeToLifeSec")):
        raise HTTPException(status_code=400, detail="Invalid payload")

    to_user = data["to"]

    response = {"message": f"Hello {to_user} your message will be send"}
    return JSONResponse(content=response)