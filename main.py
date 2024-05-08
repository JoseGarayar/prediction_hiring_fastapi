from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import pickle

# Importar los modelos
model = pickle.load(open('pickle_files/model.pkl', 'rb'))

# crear la aplicación FastAPI
app = FastAPI()

def predict(gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p):
    gender = 0 if gender == "F" else 1
    workex = 1 if workex == "Yes" else 0
    specialisation = 0 if specialisation == "Mkt&Fin" else 1
    data = [[gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p]]
    prediction = model.predict(data)
    return prediction[0]

@app.get("/")
def index():
    return {"message": "Welcome to the predictor API."}

@app.post("/predict")
async def predict_endpoint(gender: str = Form(...), ssc_p: float = Form(...), hsc_p: float = Form(...),
                           degree_p: float = Form(...), workex: str = Form(...), etest_p: float = Form(...),
                           specialisation: str = Form(...), mba_p: float = Form(...)):
    prediction = predict(gender, ssc_p, hsc_p, degree_p, workex, etest_p, specialisation, mba_p)
    if prediction == 1:
        result = 'Contratado'
    else:
        result = 'No Contratado'
    return JSONResponse(content={"result": result})

# python main
if __name__ == "__main__":
    import uvicorn
    # uvicorn.run(app, host='0.0.0.0', port=5000, debug=True)
    uvicorn.run(app, host='0.0.0.0', port=8000)
