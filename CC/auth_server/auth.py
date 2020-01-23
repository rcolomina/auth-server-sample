import cryptography
from jwt import (
  JWT,
  jwk_from_dict,
  jwk_from_pem)

import time

jwt = JWT()

ISSUER = 'sample-auth-server'
LIFE_SPAN = 1800

with open('private.pem', 'rb') as f:
  private_key = jwk_from_pem(f.read())

def authenticate_client(client_id, client_secret):
  return True

def generate_access_token():
  payload = {
    "iss": ISSUER,
    "exp": time.time() + LIFE_SPAN,
  }
  print(private_key)

  
  compact_jwt = jwt.encode(payload, private_key, 'RS256') #.decode()
  access_token = compact_jwt
    
  return access_token
