## healthcare_etl
### Local 환경 구성
* 적당한 디렉토리에 들어간 후 git clone을 해주세요.
* 파이썬 가상환경에 아래의 라이브러리가 설치되어 있다면 모든 주피터 노트북 스크립트가 실행 가능합니다.
* work 디렉토리 내의 task1부터 task7 폴더에 들어가서 각각의 스크립트를 실행해 볼 수 있습니다.
```bash
git clone https://github.com/carl020958/healthcare_etl.git

# 가상환경 구성
pip3 install -y pandas \
notebook \
sqlalchemy \
psycopg2 \
ipython-sql
```

---

### Docker 환경 구성
* 환경 구성이 안되어 있고 Docker가 설치되어 있다면 Docker을 이용해볼 수 있습니다.
* 먼저 Docker을 실행해주세요.
* 적당한 디렉토리에 들어가주신 후 git clone을 해주세요.
```bash
git clone https://github.com/carl020958/healthcare_etl.git
```

* 이후, 해당 프로젝트의 work 폴더에 들어가주세요.
```bash
cd healthcare_etl/work
```

* work 폴더에 들어가 시스템에 따라 아래 명령어 중 하나를 입력해주세요.
* 만약 arm64 아키텍처를 사용하는 경우 amd64 대신 arm64를 입력해주세요
```bash
# 만약 8877포트가 현재 사용중이라면 다른 포트로 바꿔주세요
docker container run \
-it \
-d \
-p 8877:8888 \
--name walker105 \
-v $(pwd):/home/jovyan/work \
zsu58/healthcare:amd64
```

* 웹 브라우저에 localhost:8877(포트를 바꿨다면 8877 대신 입력한 포트를 입력해주세요)을 입력하면 주피터가 나옵니다.
* 토큰을 받아야 하는 경우 아래 명령어를 통해 도커 컨테이너에 들어가주세요.
```bash
docker container exec -it walker105 bash
```

* 해당 컨테이너에서 아래 명령어를 입력하여 토큰을 받아주세요.
```bash
jupyter server list
# 아래와 같은 토큰이 주어집니다.
# http://43fad8b096d5:8888/?token=2951f55734cdb334413c561a808962f549b7457f56cc8adf :: /home/jovyan
```
* 위의 주석과 같은 토큰이 나오면 "token=" 뒤의 숫자를 웹 브라우저의 password or token에 입력해주세요.
* 웹 주소창에 http://localhost:8877/tree/work을 입력하면 각 task 별 폴더가 나옵니다.
* 각 폴더에 들어가면 각 task를 수행한 jupyter notebook이 존재합니다.
