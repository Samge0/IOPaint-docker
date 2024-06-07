# set base mirror
FROM samge/ai-env:cuda11.8.0-cudnn8-runtime-ubuntu22.04-python3.8.18-torch2.2.0 as base

ARG PROXY
ENV http_proxy=${PROXY} https_proxy=${PROXY}

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 重置代理配置
ENV http_proxy= https_proxy=


FROM base as prod

WORKDIR /app
COPY . .

EXPOSE 8080

VOLUME ["/root/.cache"]

CMD ["python", "iopaint_server.py", "--device=cuda"]