## API "Fastapi"


from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
async def root(): 

    return {"message" : "Hello World this is your Tuberculosis Detection AOOOOOOOOOOOOOOOOOOOOOOOOO"}

@app.get("/predict")

async def predict():
    # Placeholder for the model prediction logic
    return {"result": "Prediction placeholder", 
            "message": "placeholder ? ?"}


