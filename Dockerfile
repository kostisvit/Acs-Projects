FROM python:3.11
ENV PATH="/scripts:${PATH}"
# Diasbles generation of pyc files
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /acs_projects
COPY . /acs_projects
WORKDIR /acs_projects
COPY requirements.txt /acs_projects/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /vol/acs_projects/media
RUN mkdir -p /vol/acs_projects/static

RUN useradd -ms /bin/bash user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/acs_projects
RUN chmod -R 755 /acs_projects
USER user