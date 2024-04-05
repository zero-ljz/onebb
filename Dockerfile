# 如需更多资料，请参阅 https://aka.ms/vscode-docker-python
FROM python:3.10-slim

EXPOSE 8000

# 防止Python在容器中生成.pyc文件
ENV PYTHONDONTWRITEBYTECODE=1

# 关闭缓冲以便更容易地记录容器日志
ENV PYTHONUNBUFFERED=1

# 安装 pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# 创建具有显式 UID 的非root用户并添加访问 /app 文件夹的权限
# 如需更多资料，请参阅 https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# 在调试期间，这个入口点将被覆盖。 如需更多资料，请参阅 https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "onebb.wsgi"]
