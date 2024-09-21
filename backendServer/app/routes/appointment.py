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


# 模拟排班数据模型
class Schedule(BaseModel):
    doctor_id: int
    date: str
    timeSlot: str
    status: str  # 可预约、已满、停诊


# 模拟预约数据模型
class Appointment(BaseModel):
    doctorId: int
    date: str
    timeSlot: str
    name: str
    phone: str


# 返回预约响应
class AppointmentResponse(BaseModel):
    success: bool
    message: Optional[str] = None


# 模拟数据库 - 医生和排班数据
doctors_db = [
    {"id": 1, "name": "张医生", "title": "主任医师", "specialty": "心脏内科"},
    {"id": 2, "name": "李医生", "title": "副主任医师", "specialty": "消化内科"},
]

schedule_db = [
    {"doctor_id": 1, "date": "2024-09-23", "timeSlot": "上午", "status": "可预约"},
    {"doctor_id": 1, "date": "2024-09-23", "timeSlot": "下午", "status": "已满"},
    {"doctor_id": 2, "date": "2024-09-23", "timeSlot": "上午", "status": "可预约"},
    {"doctor_id": 2, "date": "2024-09-23", "timeSlot": "下午", "status": "停诊"},
]


departments = [
    {"id": 1, "name": "心脏内科"},
    {"id": 2, "name": "消化内科"},
]


# 模拟数据库 - 已预约的记录
appointments_db = []


# API 路由

# 获取医生列表
@router.get("/api/doctors", response_model=List[Doctor])
async def get_doctors():
    return doctors_db


# 获取特定医生的详细信息
@router.get("/doctor/{doctor_id}", response_model=Doctor)
async def get_doctor(doctor_id: int):
    for doctor in doctors_db:
        if doctor["id"] == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="医生未找到")


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
                schedule["date"] == appointment.date and
                schedule["timeSlot"] == appointment.timeSlot):

            if schedule["status"] == "可预约":
                # 添加预约记录到模拟数据库
                appointments_db.append(appointment.dict())

                # 更新排班状态为"已满"
                schedule["status"] = "已满"

                return AppointmentResponse(success=True, message="预约成功")

            elif schedule["status"] == "已满":
                return AppointmentResponse(success=False, message="该时间段已满")

            elif schedule["status"] == "停诊":
                return AppointmentResponse(success=False, message="该时间段已停诊")

    raise HTTPException(status_code=400, detail="无效的预约请求")


# 获取所有预约记录（仅供调试）
@router.get("/appointments", response_model=List[Appointment])
async def get_appointments():
    return appointments_db


@router.get("/api/departments")
async def get_departments():
    return departments