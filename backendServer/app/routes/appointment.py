from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

router = APIRouter()

class Doctor(BaseModel):
    id: int
    name: str
    title: str
    specialty: str
    department_id: int

# 模拟排班数据模型
class Schedule(BaseModel):
    doctor_id: int
    date: date
    timeSlot: str
    status: str  # 可预约、已满、停诊
    remaining: int  # 剩余预约名额
    fee:int

# 模拟预约数据模型
class Appointment(BaseModel):
    doctorId: int
    date: date
    timeSlot: str
    name: str
    phone: str

# 返回预约响应
class AppointmentResponse(BaseModel):
    success: bool
    message: Optional[str] = None
    remaining: Optional[int] = None  # 返回剩余预约名额

# 模拟数据库 - 医生和排班数据
doctors_db = [
    {"id": 1, "name": "张医生", "title": "主任医师", "specialty": "心脏内科", "department_id": 1},
    {"id": 2, "name": "李医生", "title": "副主任医师", "specialty": "消化内科", "department_id": 2},
]

schedule_db = [
    {"doctor_id": 1, "date": "2024-09-23", "timeSlot": "上午", "status": "可预约", "remaining": 24, "fee": 50},
    {"doctor_id": 1, "date": "2024-09-23", "timeSlot": "下午", "status": "已满", "remaining": 0, "fee": 50},
    {"doctor_id": 2, "date": "2024-09-23", "timeSlot": "上午", "status": "可预约", "remaining": 15, "fee": 40},
    {"doctor_id": 2, "date": "2024-09-23", "timeSlot": "下午", "status": "停诊", "remaining": 0, "fee": 40},
]

departments = [
    {"id": 1, "name": "心脏内科"},
    {"id": 2, "name": "消化内科"},
]

# 模拟数据库 - 已预约的记录
appointments_db = []

# API 路由

#获取医生列表
@router.get("/doctors", response_model=List[Doctor])
async def get_doctors():
    return doctors_db
# 获取科室列表
@router.get("/departments", response_model=List[dict])
async def get_departments():
    return departments

# 获取特定科室的医生列表
@router.get("/department/{department_id}/doctors", response_model=List[Doctor])
async def get_doctors_by_department(department_id: int):
    doctors = [doctor for doctor in doctors_db if doctor["department_id"] == department_id]
    if not doctors:
        raise HTTPException(status_code=404, detail="该科室没有医生")
    return doctors

#获取特定医生信息
@router.get("/doctor/{doctor_id}", response_model=Doctor)
async def get_doctor(doctor_id: int):
    for doctor in doctors_db:
        if doctor["id"] == doctor_id:
            return doctor


# 获取特定医生的排班信息
@router.get("/schedule/{doctor_id}", response_model=List[Schedule])
async def get_schedule(doctor_id: int):
    return [s for s in schedule_db if s["doctor_id"] == doctor_id]

# 提交预约信息
@router.post("/appointments", response_model=AppointmentResponse)
async def create_appointment(appointment: Appointment):
    # 检查医生排班，确保选择的时间段可预约
    for schedule in schedule_db:
        if (schedule["doctor_id"] == appointment.doctorId and
                schedule["date"] == str(appointment.date) and
                schedule["timeSlot"] == appointment.timeSlot):

            if schedule["status"] == "可预约" and schedule["remaining"] > 0:
                # 添加预约记录到模拟数据库
                appointments_db.append(appointment.dict())

                # 减少剩余预约名额
                schedule["remaining"] -= 1
                if schedule["remaining"] == 0:
                    schedule["status"] = "已满"

                return AppointmentResponse(success=True, message="预约成功", remaining=schedule["remaining"])

            elif schedule["status"] == "已满" or schedule["remaining"] == 0:
                return AppointmentResponse(success=False, message="该时间段已满", remaining=0)

            elif schedule["status"] == "停诊":
                return AppointmentResponse(success=False, message="该时间段已停诊", remaining=0)

    raise HTTPException(status_code=400, detail="无效的预约请求")

# 获取所有预约记录（仅供调试）
@router.get("/appointments", response_model=List[Appointment])
async def get_appointments():
    return appointments_db
