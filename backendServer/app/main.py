# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routes import chat
from routes import disease, fastDiagnosis, appointment

app = FastAPI(title="智能导诊和疾病自查 API")

# 设置CORS
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
# app.include_router(chat.router, prefix="/chat", tags=["智能导诊"])
app.include_router(disease.router, prefix="/disease", tags=["疾病自查"])
app.include_router(fastDiagnosis.router, prefix="/fast", tags=['快捷分诊'])
app.include_router(appointment.router, prefix="/appoint", tags=['预约挂号'])

# 启动应用
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
