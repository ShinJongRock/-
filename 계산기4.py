from tkinter import *  # Tkinter 모듈 가져오기

# 버튼 클릭 이벤트 함수
def button_click(value):
    """
    숫자 또는 연산자를 입력창에 추가하는 함수.
    :param value: 버튼 클릭 시의 값 (문자열)
    """
    current = ent.get()  # 현재 입력창의 값을 가져오기
    ent.delete(0, END)  # 입력창 초기화
    ent.insert(0, current + value)  # 기존 값에 클릭한 값을 추가하여 입력창에 다시 삽입

# "=" 버튼 클릭 시 계산 수행
def calculate():
    try:
        result = eval(ent.get())  # 입력된 수식을 계산
        ent.delete(0, END)  # 입력창 초기화
        ent.insert(0, str(result))  # 계산 결과를 입력창에 삽입
    except Exception as e:  # 계산 중 에러 발생 시 처리
        ent.delete(0, END)  # 입력창 초기화
        ent.insert(0, "Error")  # "Error" 메시지 표시

# "C" 버튼 클릭 시 입력 초기화
def clear():
    ent.delete(0, END)  # 입력창 초기화

# 백스페이스 버튼 클릭 시 한 글자 삭제
def backspace():
    current = ent.get()  # 현재 입력창의 값을 가져오기
    ent.delete(len(current)-1, END)  # 마지막 글자 삭제

# Tkinter 창 설정
win = Tk()  # Tkinter 기본 창 생성
win.title("계산기")  # 창 제목 설정
win.geometry("360x420")  # 창 크기 설정

# 입력창
ent = Entry(
    win,  # 부모 윈도우
    width=20,  # 입력창 너비
    font=("돋움", 18),  # 입력창 폰트와 크기
    borderwidth=2,  # 테두리 두께
    relief="solid",  # 테두리 스타일
    justify="right",  # 텍스트를 오른쪽 정렬
    bg="#ffffff",  # 배경색
)
ent.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # 그리드 배치

# 버튼 레이아웃 정의
btn_num = [
    'C', "⌫", "%", "/",  # 첫 번째 줄
    '7', '8', '9', '*',  # 두 번째 줄
    '4', '5', '6', '-',  # 세 번째 줄
    '1', '2', '3', '+',  # 네 번째 줄
    '±', '0', '.', '='  # 마지막 줄
]

# 버튼 생성 및 배치
row_val = 1  # 그리드의 행 초기값
col_val = 0  # 그리드의 열 초기값

for i in btn_num:  # 버튼 리스트를 순회
    if i == "=":  # "=" 버튼의 경우 계산 함수 연결
        btn = Button(win, text=i, width=5, height=2, command=calculate, font=("돋움", 16, "bold"), relief="raised", bg="#0000FF", fg="#FFFFFF")
    elif i == "C":  # "C" 버튼의 경우 초기화 함수 연결
        btn = Button(win, text=i, width=5, height=2, command=clear, font=("돋움", 16, "bold"), relief="raised", bg="#ff6347", fg="#ffffff")
    elif i == "⌫":  # 백스페이스 버튼의 경우 삭제 함수 연결
        btn = Button(win, text=i, width=5, height=2, command=backspace, font=("돋움", 16, "bold"), relief="raised", bg="#e0e0e0", fg="#000000")
    else:  # 숫자 또는 연산자 버튼의 경우 클릭 함수 연결
        btn = Button(win, text=i, width=5, height=2, command=lambda b=i: button_click(b), font=("돋움", 16, "bold"), relief="flat", bg="#ffffff", fg="#000000")
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)  # 버튼 배치
    col_val += 1  # 다음 열로 이동
    if col_val > 3:  # 열 값이 3보다 크면 다음 행으로 이동
        col_val = 0
        row_val += 1

win.mainloop()  # GUI 이벤트 루프 시작
