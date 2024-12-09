

# from fastapi import FastAPI, Header, HTTPException

# app = FastAPI()

# @app.get("/secure-data/")
# async def secure_data(authorization: str = Header(None)):
#     if authorization is None:
#         raise HTTPException(status_code=401, detail="Authorization header missing")
#     return {
#         "message": "Access granted",
#         "Authorization": authorization
#         }


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/user")
# async def get_user():
#     return {
#         "id": 1,
#         "name": 10,
#         "email": "johndoe@example.com"
#     }



# from fastapi import FastAPI, Query

# app = FastAPI()

# # Sample data
# data = [{"id": i, "name": f"Item {i}"} for i in range(1, 101)]  # 100 items

# @app.get("/items")
# async def get_items(page: int = Query(1, ge=1), per_page: int = Query(8, ge=1, le=50)):
#     start = (page - 1) * per_page
#     end = start + per_page
#     return {
#         "page": page,
#         "per_page": per_page,
#         "total_items": len(data),
#         "items": data[start:end]
#     }





# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/user")
# async def get_user():
#     return {
#         "id": 123, 
#         "name": "John Doe", 
#         "email": "johndoe@example.com"
#         }




from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class InputModel(BaseModel):
    number: int

@app.post("/validate")
async def validate_input(data: InputModel):
    if data.number < 0:
        raise HTTPException(status_code=400, detail={"error": "Number must be non-negative"})
    return {
            "message": "Input is valid",
            "number" : data.number
            }



