from functools import wraps
from flask import request,request,make_response,jsonify,g

class JWTMiddleware:
    def confirm_token(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            token = request.headers.get("Bearer-Token")
            if not token or token!= "admin":
                return err_response("token required",400)
            
            g.token = "parse something from token" 
            return func(*args, **kwargs)
    
        return wrap

def err_response(err: str,code: int):
    return make_response(
            jsonify(
                {
                    "success":"false",
                    "message":err
                }
            ),
            code)
