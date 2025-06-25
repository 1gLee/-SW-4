import json
#https://github.com/python/cpython/tree/main/Lib/json
#https://abluesnake.tistory.com/107
#https://devpouch.tistory.com/33
#github 내에 있는 공식 파이썬 저장소에서 json라이브러리 사용법과 인터넷에 올라온 내용들 참고하여 파일 저장/불러오기 기능을 구현하였습니다

class Saram:
    def __init__(self, name, bunho):
        self.name = name
        self.bunho = bunho

    def info(self):
        return f"{self.name} / {self.bunho}"

    def __str__(self):
        return self.info()

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

class Gyosu(Saram):
    def __init__(self, name, bunho, salary=4000000):
        super().__init__(name, bunho)
        self.courses = set()
        self.salary = salary

    def add_course(self, subject):
        self.courses.add(subject)

    def info(self):
        listing = ", ".join(self.courses)
        return f"[교수] {self.name}({self.bunho}) 강의: [{listing}] | 월급: {self.salary}"

class Hakgwa:
    def __init__(self):
        self.students = []
        self.gyosus = []

    def add_student(self, name, bunho):
        s = Student(name, bunho)
        self.students.append(s)
        print("학생이 등록되었슴다.")

    def add_gyosu(self, name, bunho, salary=4000000):
        g = Gyosu(name, bunho, salary)
        self.gyosus.append(g)
        print("교수 한 명 넣었슴다.")

    def find_student(self, bunho):
        for s in self.students:
            if s.bunho == bunho:
                return s
        return None

    def find_gyosu(self, bunho):
        for g in self.gyosus:
            if g.bunho == bunho:
                return g
        return None

    def show_students(self):
        if not self.students:
            print("학생 없슴다.")
        for s in self.students:
            print(s.info())

    def show_gyosus(self):
        if not self.gyosus:
            print("교수 아무도 없음요.")
        for g in self.gyosus:
            print(g.info())

    def save(self, filename="db.json"):
        data = {
            "students": [
                {"name": s.name, "bunho": s.bunho, "grades": s.grades}
                for s in self.students
            ],
            "gyosus": [
                {"name": g.name, "bunho": g.bunho, "salary": g.salary, "courses": list(g.courses)}
                for g in self.gyosus
            ]
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("저장해뒀슴다.")

    def load(self, filename="db.json"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.students = []
            for d in data.get("students", []):
                s = Student(d["name"], d["bunho"])
                s.grades = d["grades"]
                self.students.append(s)
            self.gyosus = []
            for d in data.get("gyosus", []):
                g = Gyosu(d["name"], d["bunho"], d["salary"])
                g.courses = set(d["courses"])
                self.gyosus.append(g)
            print("불러왔슴다.")
        except FileNotFoundError:
            print("저장된 파일이 없슴다.")

def run():
    dept = Hakgwa()
    while True:
        print("\n[1] 학생추가 [2] 교수추가 [3] 성적입력 [4] 학생목록")
        print("[5] 강의과목 [6] 교수목록 [7] 저장 [8] 불러오기 [9] 끝내기")
        select = input("선택: ").strip()
        if select == '1':
            name = input("학생이름: ")
            bunho = input("학번: ")
            dept.add_student(name, bunho)
        elif select == '2':
            name = input("교수이름: ")
            bunho = input("교번: ")
            salary = input("월급(기본400만): ") or "4000000"
            dept.add_gyosu(name, bunho, int(salary))
        elif select == '3':
            bunho = input("학번: ")
            s = dept.find_student(bunho)
            if s:
                subject = input("과목명: ")
                score = float(input("점수: "))
                s.add_score(subject, score)
                print("성적이 입력됐슴다.")
            else:
                print("그 학생 못 찾겠슴다.")
        elif select == '4':
            dept.show_students()
        elif select == '5':
            bunho = input("교번: ")
            g = dept.find_gyosu(bunho)
            if g:
                subject = input("강의 과목명: ")
                g.add_course(subject)
                print("강의 지정 했슴다.")
            else:
                print("그 교수 못 찾겠슴다.")
        elif select == '6':
            dept.show_gyosus()
        elif select == '7':
            dept.save()
        elif select == '8':
            dept.load()
        elif select == '9':
            print("끝!")
            break
        else:
            print("잘못 고르셨슴다.")

if __name__ == "__main__":
    run()
