## 실행
* 각 폴더에 들어가면 각 task을 수행하는데 사용된 jupyter notebook이 존재합니다.
* Task7의 경우 RDBMS에서 SQL 스크립트를 실행한 후 jupyter notebook을 사용하였습니다.
* 만약 SQL 스크립트를 실행하고 싶은 경우 walker105로 접속 후 RDBMS에서 아래 명령어를 먼저 입력해주세요.
```bash
DROP TABLE condition_occurrence, drug_exposure, person, visit_occurrence;
```
---

### Task4
* Task4의 경우 ipython-sql을 사용하는데, 현재 db에 drug_exposure table이 2개가 존재해 아래 코드가 정상 실행되지 않은 점 참고 부탁드립니다.
```sql
drug_exposure_sql = %sql select distinct drug_concept_id, concept_name, count(*) as cnt from drug_exposure de join concept on drug_concept_id = concept_id where concept_id in ( 40213154,19078106,19009384,40224172,19127663,1511248,40169216,1539463, 19126352,1539411,1332419,40163924,19030765,19106768,19075601) group by drug_concept_id, concept_name order by count(*) desc
```