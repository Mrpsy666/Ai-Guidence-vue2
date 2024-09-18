# disease.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# 创建路由对象
router = APIRouter()

# 模拟的疾病数据库
diseases_db = [
    {
        "id": "1",
        "name": "感冒",
        "overview": "感冒是由病毒引起的上呼吸道感染。",
        "symptoms": ["发烧", "咳嗽", "喉咙痛", "流鼻涕", "鼻塞"],
        "causes": ["病毒感染", "天气变化"],
        "tests": ["血常规"],
        "treatments": ["多喝水", "休息"],
        "medications": ["对乙酰氨基酚", "布洛芬"],
        "prognosis": "良好，通常在7-10天内自愈",
        "care": "注意休息，保持空气湿润",
        "prevention": "勤洗手，避免接触感冒患者",
        "transmission": "空气传播，接触传播"
    },
    {
        "id": "2",
        "name": "肺炎",
        "overview": "肺炎是由细菌、病毒或真菌引起的肺部严重感染。",
        "symptoms": ["发热", "咳嗽", "呼吸困难", "胸痛", "寒战"],
        "causes": ["细菌感染", "病毒感染", "真菌感染"],
        "tests": ["胸片", "血液检查", "痰液培养"],
        "treatments": ["抗生素", "吸氧", "支持疗法"],
        "medications": ["阿莫西林", "阿奇霉素", "头孢类抗生素"],
        "prognosis": "病情取决于病因及患者体质，重症者可能需住院",
        "care": "卧床休息，定期复查",
        "prevention": "注射肺炎疫苗，避免吸烟",
        "transmission": "飞沫传播"
    },
    {
        "id": "3",
        "name": "糖尿病",
        "overview": "糖尿病是一种由于胰岛素分泌不足或机体对胰岛素反应异常引起的慢性代谢性疾病。",
        "symptoms": ["多尿", "口渴", "乏力", "体重下降", "视力模糊"],
        "causes": ["胰岛素分泌不足", "胰岛素抵抗"],
        "tests": ["空腹血糖", "糖化血红蛋白"],
        "treatments": ["饮食控制", "运动", "药物治疗"],
        "medications": ["胰岛素", "二甲双胍", "格列齐特"],
        "prognosis": "需长期管理，可能出现并发症",
        "care": "监控血糖水平，定期检查眼睛、肾脏、心血管健康",
        "prevention": "健康饮食，定期运动，维持健康体重",
        "transmission": "不传染"
    },
    {
        "id": "4",
        "name": "高血压",
        "overview": "高血压是指动脉血压持续升高的慢性疾病，可能导致心血管疾病。",
        "symptoms": ["头痛", "眩晕", "心悸", "鼻出血"],
        "causes": ["遗传", "饮食高盐", "肥胖", "压力"],
        "tests": ["血压测量"],
        "treatments": ["饮食调整", "运动", "药物治疗"],
        "medications": ["硝苯地平", "拉贝洛尔", "利尿剂"],
        "prognosis": "长期管理，控制血压可减少并发症",
        "care": "定期测量血压，健康饮食，戒烟限酒",
        "prevention": "低盐饮食，保持健康体重，减少压力",
        "transmission": "不传染"
    },
    {
        "id": "5",
        "name": "心肌梗死",
        "overview": "心肌梗死是由于心脏供血突然中断，导致部分心肌坏死的急性情况，通常称为心脏病发作。",
        "symptoms": ["胸痛", "呼吸急促", "恶心", "出冷汗", "左臂或下巴放射性疼痛"],
        "causes": ["冠状动脉阻塞", "动脉粥样硬化"],
        "tests": ["心电图", "心脏标志物血液检测", "冠状动脉造影"],
        "treatments": ["紧急支架植入", "溶栓治疗", "冠状动脉旁路移植术"],
        "medications": ["阿司匹林", "氯吡格雷", "β受体阻滞剂"],
        "prognosis": "早期治疗可大幅提高存活率，但需长期心脏康复管理",
        "care": "心脏康复，健康生活方式",
        "prevention": "控制血压和血脂，避免吸烟，保持健康体重",
        "transmission": "不传染"
    },
    {
        "id": "6",
        "name": "抑郁症",
        "overview": "抑郁症是一种常见的情绪障碍，特征是持续的悲伤和失去兴趣。",
        "symptoms": ["情绪低落", "失眠", "食欲不振", "注意力难以集中", "自杀念头"],
        "causes": ["遗传因素", "压力", "神经化学失衡"],
        "tests": ["心理评估", "抑郁症筛查量表"],
        "treatments": ["心理治疗", "药物治疗"],
        "medications": ["选择性5-羟色胺再摄取抑制剂（SSRIs）", "5-羟色胺和去甲肾上腺素再摄取抑制剂（SNRIs）"],
        "prognosis": "多数患者通过治疗可缓解症状，但需长期管理",
        "care": "建立支持系统，按时复诊，保持规律生活",
        "prevention": "保持心理健康，学习应对压力的技巧",
        "transmission": "不传染"
    },
    {
        "id": "7",
        "name": "哮喘",
        "overview": "哮喘是一种慢性呼吸道炎症性疾病，导致气道收缩，呼吸困难。",
        "symptoms": ["咳嗽", "喘息", "呼吸急促", "胸闷"],
        "causes": ["过敏反应", "吸入刺激物", "遗传因素"],
        "tests": ["肺功能测试", "支气管激发试验"],
        "treatments": ["吸入类固醇", "支气管扩张剂"],
        "medications": ["沙丁胺醇", "布地奈德", "孟鲁司特"],
        "prognosis": "哮喘无法治愈，但可以通过药物控制症状",
        "care": "避免诱发因素，定期使用控制药物",
        "prevention": "避免过敏原，保持室内空气清洁",
        "transmission": "不传染"
    },
    {
        "id": "8",
        "name": "阿尔茨海默病",
        "overview": "阿尔茨海默病是一种进行性的神经退行性疾病，导致记忆丧失和认知功能下降。",
        "symptoms": ["记忆力减退", "语言障碍", "混乱", "判断力差", "行为改变"],
        "causes": ["未知，但遗传和环境因素可能有影响"],
        "tests": ["认知功能测试", "脑成像", "遗传检测"],
        "treatments": ["药物治疗", "认知行为疗法"],
        "medications": ["多奈哌齐", "美金刚", "加兰他敏"],
        "prognosis": "病情逐步加重，目前无治愈方法",
        "care": "支持性护理，家庭支持",
        "prevention": "保持脑部活跃，定期体检，健康饮食",
        "transmission": "不传染"
    },
    {
        "id": "9",
        "name": "中风",
        "overview": "中风是脑部血液供应中断导致的严重神经系统疾病。",
        "symptoms": ["突然的肢体无力", "言语不清", "面部偏瘫", "视力模糊", "头晕"],
        "causes": ["脑血管阻塞", "脑出血"],
        "tests": ["脑CT", "脑MRI", "血液检查"],
        "treatments": ["溶栓治疗", "血管内治疗", "康复治疗"],
        "medications": ["阿司匹林", "华法林", "抗凝剂"],
        "prognosis": "严重中风可能导致永久性残疾，早期治疗可改善预后",
        "care": "康复训练，预防并发症",
        "prevention": "控制高血压，戒烟，保持健康饮食",
        "transmission": "不传染"
    }
]
diseases_db += [
    {
        "id": "10",
        "name": "胃溃疡",
        "overview": "胃溃疡是胃内壁的一种溃疡，通常由于胃酸和消化酶侵蚀引起。",
        "symptoms": ["胃痛", "恶心", "呕吐", "腹胀", "消化不良"],
        "causes": ["幽门螺杆菌感染", "非甾体抗炎药的使用", "吸烟", "饮酒"],
        "tests": ["胃镜检查", "幽门螺杆菌检测", "血液检查"],
        "treatments": ["抑制胃酸药物", "抗生素", "胃保护剂"],
        "medications": ["奥美拉唑", "克拉霉素", "阿莫西林"],
        "prognosis": "通过治疗多数溃疡可以愈合，但可能复发",
        "care": "避免使用非甾体抗炎药，少食多餐，避免辛辣食物",
        "prevention": "预防感染幽门螺杆菌，合理使用药物",
        "transmission": "幽门螺杆菌可以通过口-口传播"
    },
    {
        "id": "11",
        "name": "急性阑尾炎",
        "overview": "急性阑尾炎是阑尾发炎的一种急性疾病，常导致剧烈的腹痛。",
        "symptoms": ["右下腹剧痛", "恶心", "呕吐", "发热", "食欲不振"],
        "causes": ["阑尾阻塞", "细菌感染"],
        "tests": ["腹部超声", "CT扫描", "血常规"],
        "treatments": ["手术切除阑尾", "抗生素治疗"],
        "medications": ["头孢菌素", "甲硝唑"],
        "prognosis": "手术治疗后通常预后良好",
        "care": "术后避免剧烈运动，注意恢复",
        "prevention": "无法预防，健康饮食可能有助于降低风险",
        "transmission": "不传染"
    },
    {
        "id": "12",
        "name": "荨麻疹",
        "overview": "荨麻疹是一种常见的皮肤疾病，特点是皮肤上出现红色的瘙痒性斑块。",
        "symptoms": ["皮肤瘙痒", "红色风团", "皮肤肿胀"],
        "causes": ["过敏反应", "药物反应", "感染"],
        "tests": ["皮肤过敏测试", "血液检查"],
        "treatments": ["抗组胺药", "避免过敏原"],
        "medications": ["西替利嗪", "氯雷他定", "地塞米松"],
        "prognosis": "通常为短期，治疗后迅速恢复",
        "care": "避免过敏原，使用润肤霜",
        "prevention": "避免已知的过敏源，保持皮肤清洁",
        "transmission": "不传染"
    },
    {
        "id": "13",
        "name": "带状疱疹",
        "overview": "带状疱疹是由水痘-带状疱疹病毒引起的皮肤感染，表现为疼痛性皮疹。",
        "symptoms": ["局部皮肤疼痛", "水疱样皮疹", "发热", "乏力"],
        "causes": ["水痘-带状疱疹病毒的重新激活"],
        "tests": ["病毒检测", "血液检查"],
        "treatments": ["抗病毒药物", "止痛药"],
        "medications": ["阿昔洛韦", "伐昔洛韦", "伽马氨基丁酸类似物"],
        "prognosis": "多数患者可恢复，但可能有长期疼痛（带状疱疹后神经痛）",
        "care": "保持皮肤干燥，避免水疱破裂感染",
        "prevention": "接种水痘疫苗或带状疱疹疫苗",
        "transmission": "与带状疱疹患者接触可能导致易感者感染水痘"
    },
    {
        "id": "14",
        "name": "慢性阻塞性肺疾病（COPD）",
        "overview": "慢性阻塞性肺疾病是一种慢性肺部疾病，常见于吸烟者，特征是呼吸困难和慢性咳嗽。",
        "symptoms": ["慢性咳嗽", "呼吸急促", "胸闷", "痰多"],
        "causes": ["长期吸烟", "空气污染", "职业性粉尘暴露"],
        "tests": ["肺功能测试", "胸部X光片"],
        "treatments": ["戒烟", "肺康复治疗", "氧疗"],
        "medications": ["沙丁胺醇", "噻托溴铵", "布地奈德"],
        "prognosis": "无法治愈，但可以通过治疗缓解症状",
        "care": "避免空气污染，定期复查",
        "prevention": "戒烟，避免职业性粉尘暴露，减少空气污染接触",
        "transmission": "不传染"
    },
    {
        "id": "15",
        "name": "骨质疏松症",
        "overview": "骨质疏松症是指骨密度降低，骨折风险增加的一种疾病，常见于老年人和女性。",
        "symptoms": ["背痛", "身高下降", "骨折风险增加"],
        "causes": ["钙和维生素D不足", "激素变化", "遗传因素"],
        "tests": ["骨密度检测", "血钙水平测试"],
        "treatments": ["补充钙和维生素D", "抗骨质疏松药物"],
        "medications": ["阿仑膦酸钠", "降钙素", "维生素D"],
        "prognosis": "需要长期治疗和管理，可能减缓病情进展",
        "care": "饮食中补充足够的钙和维生素D，保持适当的运动",
        "prevention": "早期补钙和维生素D，适度运动，避免过度饮酒和吸烟",
        "transmission": "不传染"
    },
    {
        "id": "16",
        "name": "肾结石",
        "overview": "肾结石是指矿物质在肾脏中沉淀形成固体结石，可能引发严重的疼痛。",
        "symptoms": ["腰部剧痛", "血尿", "恶心", "呕吐", "排尿困难"],
        "causes": ["脱水", "饮食中高钙或草酸含量", "家族史"],
        "tests": ["腹部X光", "CT扫描", "尿液检查"],
        "treatments": ["大量饮水", "疼痛管理", "体外震波碎石术", "手术取石"],
        "medications": ["镇痛药", "α受体阻滞剂"],
        "prognosis": "多数结石可以通过非手术方式排出，但复发率较高",
        "care": "多喝水，避免高草酸、高钙的食物",
        "prevention": "保持充足水分摄入，避免过多摄入钙和草酸含量高的食物",
        "transmission": "不传染"
    },
    {
        "id": "17",
        "name": "痛风",
        "overview": "痛风是一种由于尿酸盐结晶沉积在关节中引起的关节炎，导致剧烈的疼痛和红肿。",
        "symptoms": ["关节剧痛", "红肿", "发热", "皮肤发热"],
        "causes": ["高尿酸水平", "遗传因素", "饮食高嘌呤"],
        "tests": ["血尿酸水平测试", "关节液分析"],
        "treatments": ["低嘌呤饮食", "药物降低尿酸水平"],
        "medications": ["别嘌呤醇", "秋水仙碱", "非甾体抗炎药"],
        "prognosis": "通过长期治疗可减少发作次数，但需持续管理",
        "care": "控制饮食，定期监测尿酸水平",
        "prevention": "避免高嘌呤食物，如红肉、酒精等，保持健康体重",
        "transmission": "不传染"
    },
    {
        "id": "18",
        "name": "银屑病",
        "overview": "银屑病是一种慢性皮肤病，导致皮肤上出现鳞屑状红斑。",
        "symptoms": ["皮肤红斑", "瘙痒", "鳞屑状皮疹", "皮肤干燥"],
        "causes": ["免疫系统异常", "遗传因素", "环境触发因素"],
        "tests": ["皮肤活检", "血液检查"],
        "treatments": ["局部治疗", "光疗", "系统性药物治疗"],
        "medications": ["类固醇软膏", "维A酸", "免疫抑制剂"],
        "prognosis": "无法治愈，但可以通过治疗控制症状",
        "care": "保持皮肤湿润，避免触发因素",
        "prevention": "无法预防，保持健康生活方式可以减少发作",
        "transmission": "不传染"
    },
    {
        "id": "19",
        "name": "甲状腺功能亢进（甲亢）",
        "overview": "甲状腺功能亢进是一种甲状腺产生过多甲状腺激素的疾病，导致新陈代谢过快。",
        "symptoms": ["体重减轻", "心悸", "手抖", "多汗", "焦虑"],
        "causes": ["格雷夫斯病", "甲状腺结节", "过量碘摄入"],
        "tests": ["血清甲状腺激素水平检测", "甲状腺功能检查"],
        "treatments": ["抗甲状腺药物", "碘治疗", "手术切除甲状腺"],
        "medications": ["甲巯咪唑", "丙硫氧嘧啶", "β受体阻滞剂"],
        "prognosis": "通过治疗多数患者可以恢复正常甲状腺功能",
        "care": "定期复查甲状腺功能，避免过量碘摄入",
        "prevention": "无法预防，控制碘摄入可以减少风险",
        "transmission": "不传染"
    }
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
