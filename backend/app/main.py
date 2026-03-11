from fastapi import FastAPI
from app.routers.health_router import router
from app.routers.product_router import router as product_router
from app.routers.user_router import router as user_router 

app= FastAPI(title="Voice Interview Assistant ")

app.include_router(router)
app.include_router(product_router)
app.include_router(user_router)

@app.get("/")
def root():
    return{"message":"Interview  backend running successfully!"}


@app.get("/items/{item_id}")
def read_item(item_id :int ):
    return {"item_id": item_id}


@app.get("/items/")
def read_items(skip: int =0, limit :int =10):
    return {
        "skip": skip,
        "limit": limit
        }


@app.get("/users/{user_id}")
def get_user(user_id : int, active :bool = True):
    return{
        "user_id": user_id,
        "active": active
    }
    
@app.get("/products/{product_id}")
def  get_product(product_id :int ):
    return {
            "product_id": product_id
        }
        
@app.get("/search/")
def search_items(keyword:str, page:int =1):
    return{
        "keyword": keyword,
        "page" :page 
    }        


@app.get("/orders/{order_id}")
def get_order(order_id :int, status:str="in progress"):
    return{
        "order_id":order_id,
        "status":status
    }