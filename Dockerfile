FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install git+https://github.com/huggingface/transformers.git@main
RUN pip3 install torch
RUN pip3 install open_clip_torch
RUN pip3 install accelerate
RUN pip3 install bitsandbytes

RUN pip3 install git+https://github.com/openai/clip
RUN pip3 install ftfy
RUN pip3 install regex
RUN pip3 install tqdm
RUN pip3 install pillow
RUN pip3 install torchvision

RUN pip3 install fastapi uvicorn[standard]

WORKDIR /app