from fastapi import FastAPI 
app = FastAPI()

@app.get('/') #decorador en python, tipo de acceso
def Hola_Mundo():
    return{ " Hola ": " Mundo " }
