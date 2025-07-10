import jwt
import datetime
import uuid

SECRET_KEY = "tu_secreto_muy_seguro"

def generate_jwt():
    payload = {
        "jti": str(uuid.uuid4()),  # JWT ID único
        "iat": datetime.datetime.utcnow(),  # Issued At (fecha emisión)
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60)  # Expiración (1 min)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

if __name__ == "__main__":
    token = generate_jwt()
    print(f"JWT generado:\n{token}")