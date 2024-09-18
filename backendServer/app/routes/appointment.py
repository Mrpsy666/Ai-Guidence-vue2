from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

router = APIRouter()

# 模拟数据库 - 已预约的记录
appointments_db = []

# 预约请求体数据模型
class Appointment(BaseModel):
    department: str
    date: date
    timeSlot: str
    name: str
    phone: str

# 预约响应数据模型
class AppointmentResponse(BaseModel):
    success: bool
    message: Optional[str] = None

# 可预约的科室
available_departments = ["心脏内科", "呼吸内科", "泌尿外科", "消化内科", "骨科"]

# 可用的时间段
available_time_slots = ["上午", "下午"]

# POST请求：提交预约信息
@router.post("/appointments", response_model=AppointmentResponse)
async def create_appointment(appointment: Appointment):
    # 检查科室是否有效
    if appointment.department not in available_departments:
        raise HTTPException(status_code=400, detail="无效的科室")

    # 检查时间段是否有效
    if appointment.timeSlot not in available_time_slots:
        raise HTTPException(status_code=400, detail="无效的时间段")

    # 检查是否已有相同时间段的预约
    for appt in appointments_db:
        if (appt["department"] == appointment.department and
            appt["date"] == appointment.date and
            appt["timeSlot"] == appointment.timeSlot):
            return AppointmentResponse(success=False, message="该时间段已被预约")

    # 添加到模拟数据库中
    appointments_db.append(appointment.dict())

    return AppointmentResponse(success=True, message="预约成功")

# 获取所有预约记录（仅供调试）
@router.get("/appointments", response_model=List[Appointment])
async def get_appointments():
    return appointments_db
