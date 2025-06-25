# -SW-4
학생&교수 정보 관리 프로그램입니다.

---

## 주요 기능들

- 학생 등록, 교수 등록
- 학생별 과목별 점수 입력, 평균 계산
- 교수별 강의과목 입력/관리
- 정보 파일로 저장/불러오기(json)
- 메뉴 기반 입력/출력

---

## 코드 주요 부분

이 코드는 학생, 교수의 정보와 학과 전체 관리를 위한 클래스를 사용한다.

- **Saram 클래스**  
  인물 객체의 기본 정보. 이름과 번호를 저장하고 문자열로 정보 출력

- **Student 클래스 (Saram 상속)**  
  학생의 정보를 관리  
  - 각 과목(subject)별 점수(score)를 `grades` 딕셔너리에 저장  
  - `add_score()`로 점수 추가  
  - `get_average()`로 평균 계산  
  - `info()`로 전체 성적 출력

- **Gyosu 클래스 (Saram 상속)**  
  교수의 정보를 관리  
  - 강의하는 과목 목록은 `courses` 집합으로 저장  
  - `add_course()`로 강의 과목 추가  
  - `info()`로 담당 강의와 월급 표시

- **Hakgwa 클래스**  
  학생/교수 전체 목록을 관리
  - 학생 추가/검색/목록 출력  
  - 교수 추가/검색/목록 출력  
  - 파일로 저장 및 불러오기
  
- **파일 저장/불러오기**  
  파이썬 json 라이브러리로 정보를 저장하고 불러옴  
  참고 사이트들  
  (https://github.com/python/cpython/tree/main/Lib/json)  
  (https://abluesnake.tistory.com/107)  
  (https://devpouch.tistory.com/33)

- **메인 루프(run 함수)**  
  메뉴를 출력하고 입력에 따라 각 기능(등록, 조회, 저장 등)을 실행  
 

---

**예시 코드 일부**

```
class Student(Saram):
    def __init__(self, name, bunho):
        super().__init__(name, bunho)
        self.grades = {}

    def add_score(self, subject, score):
        self.grades[subject] = score

    def get_average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0

    def info(self):
        summary = ", ".join([f"{sub}:{val}" for sub, val in self.grades.items()])
        return f"[학생] {self.name}({self.bunho}) 성적: [{summary}] | 평균: {self.get_average():.1f}"
```
---

작성자: 이원겸/20255563
과제명: 오픈소스SW와 파이썬프로그래밍 과제4
