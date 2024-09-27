# chat.py
import time
import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
from modelscope import AutoModelForCausalLM, AutoTokenizer
from modelscope import GenerationConfig

# 创建路由对象
router = APIRouter()

# 加载模型
try:
    tokenizer = AutoTokenizer.from_pretrained("E:/LLM/qwen2/qwen/Qwen-1_8B-Chat", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        "E:/LLM/qwen2/qwen/Qwen-1_8B-Chat",
        device_map="auto",
        trust_remote_code=True,
        fp16=True
    ).eval()
    model.generation_config = GenerationConfig.from_pretrained(
        "E:/LLM/qwen2/qwen/Qwen-1_8B-Chat",
        trust_remote_code=True
    )
except Exception as e:
    print(f"模型加载失败: {e}")
    raise e

# 存储会话历史
sessions: Dict[str, List[str]] = {}

# 请求模型并生成响应的函数
def chat_with_timing(model, tokenizer, prompt, history=None):
    start_time = time.time()
    try:
        response, history = model.chat(tokenizer, prompt, history=history)
    except Exception as e:
        raise e
    end_time = time.time()
    elapsed_time = end_time - start_time
    return response, history, elapsed_time

# 请求体模型
class ChatRequest(BaseModel):
    session_id: Optional[str] = None  # 可选的会话 ID
    prompt: str  # 用户输入的症状

# 响应体模型
class ChatResponse(BaseModel):
    session_id: str  # 会话 ID
    response: str  # 模型生成的响应
    time_taken: float  # 模型响应时间

class RecommendResponse(BaseModel):
    department: str
    advice: str

# 聊天接口，处理智能导诊请求
@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    prompt = request.prompt
    session_id = request.session_id

    # 创建新的会话
    if not session_id:
        session_id = str(uuid.uuid4())
        sessions[session_id] =[('我要去医院看病，但是不知道挂什么科，请你作为一个医生询问我几个问题来了解我的病情', '当然可以。接下去我会问你几个问题以了解你的病症')]


    history = sessions.get(session_id, [])
    print(history)
    try:
        response, updated_history, elapsed_time = chat_with_timing(model, tokenizer, prompt, history)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"模型处理失败: {e}")

    # 更新会话历史
    sessions[session_id] = updated_history

    return ChatResponse(
        session_id=session_id,
        response=response,c
        time_taken=round(elapsed_time, 2)
    )


@router.get("/getRecommend", response_model=RecommendResponse)
def recommend_response():
    return RecommendResponse(
        department="心脏内科",
        advice = "请尽早处理"
    )

# 清理会话接口
@router.delete("/session/{session_id}", status_code=204)
def delete_session(session_id: str):
    if session_id in sessions:
        del sessions[session_id]
    return
