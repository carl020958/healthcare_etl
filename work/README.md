## 실행
* 각 폴더에 들어가면 각 task을 수행하는데 사용된 jupyter notebook이 존재합니다.
* Task7의 경우 RDBMS에서 SQL 스크립트를 실행한 후 jupyter notebook을 사용하였습니다.
* 만약 SQL 스크립트를 실행하고 싶은 경우 walker105로 접속 후 RDBMS에서 아래 명령어를 먼저 입력해주세요.
```bash
DROP TABLE condition_occurrence, drug_exposure, person, visit_occurrence;
```
---

### 실행시 참고사항
* db 연결을 위한 URL을 .credentials.json 파일에 두었습니다. 
* 아래 import와 with 문을 지워주시고 create_engine의 파라미터인 url 부분에 db 연결을 위한 url을 넣어야 합니다.
```python
import json

with open("/home/jovyan/work/.credentials.json", "r") as credential:
    credential = json.load(credential)
    url = credential["url"]

engine = create_engine(url, connect_args={'options': '-csearch_path={}'.format('de')})
```

### task4
* 5번쨰 셀의 url부분에 db 연결을 위한 url을 아래와 같이 넣어야 합니다.
```python
%sql postgresql://id:password@ip:port/db
```