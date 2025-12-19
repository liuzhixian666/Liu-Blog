from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="个人博客后端 API")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174"],  # 允许前端访问
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 数据模型
class Message(BaseModel):
    id: Optional[int] = None
    name: str
    content: str
    created_at: Optional[str] = None

class Project(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    image_url: Optional[str] = None
    created_at: Optional[str] = None

class Footprint(BaseModel):
    id: Optional[int] = None
    count: int = 0
    last_updated: Optional[str] = None

# 内存存储
messages: List[Message] = []
projects: List[Project] = []
footprint: Footprint = Footprint(id=1, count=0, last_updated="2025-12-19 12:00:00")

# 初始化一些示例数据
messages.append(Message(id=1, name="张三", content="这是第一个留言！", created_at="2025-12-19 10:00:00"))
messages.append(Message(id=2, name="李四", content="博客看起来很棒！", created_at="2025-12-19 10:30:00"))

projects.append(Project(id=1, title="项目 1", description="这是我的第一个项目", image_url="https://via.placeholder.com/300", created_at="2025-12-19 11:00:00"))
projects.append(Project(id=2, title="项目 2", description="这是我的第二个项目", image_url="https://via.placeholder.com/300", created_at="2025-12-19 11:30:00"))

# 留言板接口
@app.get("/messages", response_model=List[Message])
async def get_messages():
    return messages

@app.post("/messages", response_model=Message)
async def create_message(message: Message):
    message.id = len(messages) + 1
    message.created_at = "2025-12-19 12:00:00"  # 简化处理，实际应使用当前时间
    messages.append(message)
    return message

@app.delete("/messages/{message_id}")
async def delete_message(message_id: int):
    for i, message in enumerate(messages):
        if message.id == message_id:
            messages.pop(i)
            return {"message": "留言已删除"}
    raise HTTPException(status_code=404, detail="留言不存在")

# 展示柜接口
@app.get("/projects", response_model=List[Project])
async def get_projects():
    return projects

@app.post("/projects", response_model=Project)
async def create_project(project: Project):
    project.id = len(projects) + 1
    project.created_at = "2025-12-19 12:00:00"  # 简化处理，实际应使用当前时间
    projects.append(project)
    return project

@app.delete("/projects/{project_id}")
async def delete_project(project_id: int):
    for i, project in enumerate(projects):
        if project.id == project_id:
            projects.pop(i)
            return {"message": "项目已删除"}
    raise HTTPException(status_code=404, detail="项目不存在")

# 点亮足迹接口
@app.get("/footprint", response_model=Footprint)
async def get_footprint():
    return footprint

@app.post("/footprint/like", response_model=Footprint)
async def add_like():
    footprint.count += 1
    footprint.last_updated = "2025-12-19 12:00:00"  # 简化处理，实际应使用当前时间
    return footprint

# 根路径
@app.get("/")
async def root():
    return {"message": "欢迎使用个人博客 API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
