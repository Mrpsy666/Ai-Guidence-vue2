from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

# 定义请求体
class SymptomRequest(BaseModel):
    symptoms: List[str]  # 接受一个症状列表

# 科室推荐数据库，键值全为中文，附带建议
symptom_to_department = {
    # 消化系统
    "腹胀": {"department": "消化科", "advice": "建议前往消化科进行相关检查。"},
    "腹痛": {"department": "消化科", "advice": "建议前往消化科检查胃肠道健康。"},
    "腹泻": {"department": "消化科", "advice": "建议前往消化科检查消化系统。"},
    "便秘": {"department": "消化科", "advice": "建议前往消化科排查便秘原因。"},
    "呕吐": {"department": "消化科", "advice": "建议前往消化科检查胃部或肠道。"},
    "消化不良": {"department": "消化科", "advice": "建议前往消化科进行消化道检查。"},

    # 呼吸系统
    "咳嗽": {"department": "呼吸科", "advice": "建议前往呼吸科检查肺部或呼吸道。"},
    "咳痰": {"department": "呼吸科", "advice": "建议前往呼吸科检查是否有感染。"},
    "呼吸困难": {"department": "呼吸科", "advice": "建议前往呼吸科检查呼吸功能。"},
    "胸痛": {"department": "呼吸科", "advice": "建议前往呼吸科排查胸部疾病。"},
    "发热": {"department": "感染科", "advice": "建议前往感染科进行感染排查。"},

    # 心血管系统
    "心悸": {"department": "心内科", "advice": "建议前往心内科检查心脏功能。"},
    "胸闷": {"department": "心内科", "advice": "建议前往心内科进行心脏检查。"},
    "乏力": {"department": "心内科", "advice": "建议前往心内科检查心脏和血液循环系统。"},
    "浮肿": {"department": "心内科", "advice": "建议前往心内科进行水肿原因检查。"},
    "头晕": {"department": "心内科", "advice": "建议前往心内科检查血压或心脏。"},

    # 神经系统
    "头痛": {"department": "神经科", "advice": "建议前往神经科进行脑部检查。"},
    "眩晕": {"department": "神经科", "advice": "建议前往神经科检查平衡系统。"},
    "记忆力减退": {"department": "神经科", "advice": "建议前往神经科排查大脑功能问题。"},
    "面瘫": {"department": "神经科", "advice": "建议前往神经科检查面部神经系统。"},
    "失眠": {"department": "神经科", "advice": "建议前往神经科检查睡眠障碍。"},

    # 泌尿系统
    "尿频": {"department": "泌尿外科", "advice": "建议前往泌尿外科检查泌尿系统。"},
    "尿急": {"department": "泌尿外科", "advice": "建议前往泌尿外科进行泌尿道检查。"},
    "尿痛": {"department": "泌尿外科", "advice": "建议前往泌尿外科检查泌尿道感染。"},
    "血尿": {"department": "泌尿外科", "advice": "建议前往泌尿外科排查泌尿系统病变。"},
    "腰痛": {"department": "泌尿外科", "advice": "建议前往泌尿外科检查肾脏。"},

    # 内分泌系统
    "多饮": {"department": "内分泌科", "advice": "建议前往内分泌科检查血糖和激素水平。"},
    "多食": {"department": "内分泌科", "advice": "建议前往内分泌科排查糖尿病或内分泌失调。"},
    "多尿": {"department": "内分泌科", "advice": "建议前往内分泌科进行尿频原因检查。"},
    "体重增加": {"department": "内分泌科", "advice": "建议前往内分泌科检查体重异常增加的原因。"},
    "手脚发麻": {"department": "内分泌科", "advice": "建议前往内分泌科检查神经和血糖水平。"},

    # 骨科
    "关节疼痛": {"department": "骨科", "advice": "建议前往骨科进行关节健康检查。"},
    "骨折": {"department": "骨科", "advice": "建议前往骨科处理骨折及进行相关治疗。"},
    "腰背痛": {"department": "骨科", "advice": "建议前往骨科检查脊柱和肌肉健康。"},
    "肿胀": {"department": "骨科", "advice": "建议前往骨科检查骨骼和关节健康。"},
    "活动受限": {"department": "骨科", "advice": "建议前往骨科检查关节活动范围问题。"},

    # 皮肤科
    "皮肤瘙痒": {"department": "皮肤科", "advice": "建议前往皮肤科进行过敏和皮肤病检查。"},
    "皮疹": {"department": "皮肤科", "advice": "建议前往皮肤科检查皮疹和炎症原因。"},
    "红肿": {"department": "皮肤科", "advice": "建议前往皮肤科检查皮肤健康。"},
    "脱皮": {"department": "皮肤科", "advice": "建议前往皮肤科检查脱皮原因，可能与过敏或感染有关。"},
    "色素沉着": {"department": "皮肤科", "advice": "建议前往皮肤科排查色素异常沉着的原因。"},

    "胃痛": {"department": "胃肠外科", "advice": "建议前往胃肠外科检查胃部或肠道问题。"},
    "乳房肿块": {"department": "乳腺外科", "advice": "建议前往乳腺外科检查乳房健康，排查肿瘤或其他病变。"},
    "体重变化": {"department": "内分泌代谢科","advice": "建议前往内分泌代谢科检查体重异常变化的原因，如代谢或激素问题。"},
    "尿频": {"department": "泌尿外科", "advice": "建议前往泌尿外科检查泌尿系统健康，排查感染或其他问题。"},
    "视力下降": {"department": "眼科", "advice": "建议前往眼科检查视力问题，如屈光不正或眼部病变。"},
    "咳嗽": {"department": "呼吸内科", "advice": "建议前往呼吸内科检查呼吸道健康，排查感染或其他问题。"},
    "心悸": {"department": "心脏内科", "advice": "建议前往心脏内科检查心脏功能，排查心律不齐等问题。"},
    "耳鸣": {"department": "耳鼻咽喉头颈外科", "advice": "建议前往耳鼻喉科检查耳部健康，排查听力问题或耳部感染。"},
    "骨折": {"department": "骨科", "advice": "建议前往骨科进行骨折处理和相关检查。"},
    "头晕": {"department": "神经内科", "advice": "建议前往神经内科检查神经系统，排查脑供血不足等问题。"},
    "消化不良": {"department": "消化内科", "advice": "建议前往消化内科检查胃肠道功能，排查消化系统疾病。"},
    "心理问题": {"department": "心理卫生中心", "advice": "建议前往心理卫生中心寻求专业心理咨询和治疗。"},
    "皮肤瘙痒": {"department": "皮肤性病科", "advice": "建议前往皮肤性病科检查皮肤问题，排查过敏或性病相关症状。"}
}


@router.post("/recommend")
async def recommend_department(request: SymptomRequest):
    """
    根据用户选择的多个症状推荐合适的科室和建议
    """
    departments = {}  # 使用字典存储科室和建议，避免重复

    # 检查是否有传入的症状列表
    if not request.symptoms:
        raise HTTPException(status_code=400, detail="症状列表不能为空")

    # 遍历症状，获取对应的科室和建议
    for symptom in request.symptoms:
        department_info = symptom_to_department.get(symptom)
        if department_info:
            departments[department_info["department"]] = department_info["advice"]

    # 如果没有找到匹配的科室，返回404
    if not departments:
        raise HTTPException(status_code=404, detail="未找到匹配的科室")

    # 返回多个科室及建议
    return {"departments": [{"department": dept, "advice": advice} for dept, advice in departments.items()]}
