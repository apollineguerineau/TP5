from fastapi import FastAPI
import requests
import uvicorn
app = FastAPI()

@app.get("/")
async def get_product():
    req=requests.get("https://world.openfoodfacts.org/api/v0/product/3033491270864.json")
    if req.status_code==200:
        res=req.json()
        return(res)

if __name__=='__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)