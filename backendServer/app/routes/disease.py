# disease.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# 创建路由对象
router = APIRouter()

# 模拟的疾病数据库
diseases_db = [
    {"id": "1", "name": "感冒", "overview": "感冒是由病毒引起的上呼吸道感染。", "symptoms": ["发烧", "咳嗽"], "causes": ["病毒感染"], "tests": ["血常规"], "treatments": ["多喝水", "休息"], "medications": ["对乙酰氨基酚"], "prognosis": "良好", "care": "注意休息", "prevention": "勤洗手", "transmission": "空气传播"},
    {"id": "2", "name": "肺炎", "overview": "肺炎是肺部的严重感染。", "symptoms": ["发热", "呼吸困难"], "causes": ["细菌感染"], "tests": ["胸片"], "treatments": ["抗生素"], "medications": ["阿莫西林"], "prognosis": "中等", "care": "卧床休息", "prevention": "注射疫苗", "transmission": "飞沫传播"},
    # 更多疾病
]

# 疾病模型
class Disease(BaseModel):
    id: str
    name: str
    overview: str
    symptoms: List[str]
    causes: List[str]
    tests: List[str]
    treatments: List[str]
    medications: List[str]
    prognosis: str
    care: str
    prevention: str
    transmission: str

# 根据名称或字母查询疾病
@router.get("/search", response_model=List[Disease])
def search_diseases(query: Optional[str] = None):
    if query:
        result = [d for d in diseases_db if query in d["name"]]
    else:
        result = []
    return result

# 获取疾病详细信息
@router.get("/{disease_id}", response_model=Disease)
def get_disease_detail(disease_id: str):
    disease = next((d for d in diseases_db if d["id"] == disease_id), None)
    if not disease:
        raise HTTPException(status_code=404, detail="疾病未找到")
    return disease
