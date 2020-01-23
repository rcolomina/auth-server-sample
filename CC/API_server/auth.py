import cryptography

from jwt import (
  JWT,
  jwk_from_dict,
  jwk_from_pem
)

from jwt import exceptions as e

jwt = JWT()

ISSUER = 'sample-auth-server'

def verify_access_token(access_token):
  with open('public.pem', 'rb') as f:
    public_key = jwk_from_pem(f.read())
  #pk = jwk_from_pen(open('/home/rcolomina/public.pem','rb').read())

  try:
    #print(access_token)
    #print(public_key)
    print("type of access_token:",type(access_token))
    pk = jwk_from_pem(open('/home/rcolomina/public.pem','rb').read())
    
    decoded_token = jwt.decode(access_token,pk, algorithms='RS256')
        
    print(decoded_token)
    return True
  except (e.JWSEncodeError,
          e.JWSDecodeError):
    print("Exception happened")
    return False
  
#def verify_access_token(access_token):
#  try:
#    print(access_token)
#    print(public_key)
#    decoded_token = jwt.decode(access_token, public_key, algorithms='RS256')
    
#    print(decoded_token)
#  return True

    #print(jwt.decode(access_token, public_key))
    #decoded_token = jwt.decode(access_token.encode(), public_key,
    #                           issuer = ISSUER,
    #                           algorithm = 'RS256')        
  #except (jwt.exceptions.InvalidTokenError,
  #        jwt.exceptions.InvalidSignatureError,
  #        jwt.exceptions.InvalidIssuerError,
  #        jwt.exceptions.ExpiredSignatureError):
  #  return False

