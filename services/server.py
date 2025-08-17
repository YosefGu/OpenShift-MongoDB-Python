from fastapi import FastAPI
from .dataloader import DataLoader

app = FastAPI()
data_loader = DataLoader()


@app.get("/data")
def get_data():
    return data_loader.get_data()

