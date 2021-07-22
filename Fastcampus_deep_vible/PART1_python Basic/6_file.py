# 승차권 GUI + 파일 읽고 쓰기 기능 추가

# import Lib
from tkinter import Tk, ttk, Label, Button, Text, END
import json     # json 파일을 불러오기 및 저장하기 위해 import 

# stationfares 정보 : 휘발성, 프로그램 실행 중에 아무리 수정하고 지우고 삭제해도 이 부분은 바뀌지 않는다. 
stationfares = []       # 빈 stationfares 리스트 생성 
with open("stationfares.json", "r", encoding='UTF-8') as stationfares_file:    # 생성한 stationfares.json 파일에 저장된 내용 불러오기('r'), 파일 경로 주의!(설정떄문인지 지금은 python_practice 파일 바로 아래에 .json 파일이 있어야 열림)
    stationfares = json.load(stationfares_file)                                # 강의에는 없지만 open()부분의 encoding='UTF-8' 추가해주기 ('UnicodeDecodeError: 'cp949' codec can't decode byte 0xad in position 21: illegal multibyte sequence' 오류 해결)

selected_index = 0     # selected_index: 선택하는 항목의 인덱스를 저장하는 전역변수(default:0) 

# 이벤트 함수들 정의 
def stationfares_selected(event):
    '''
    treeview에서 선택한 내용을 입력창(text_Station, text_Fare)에 그대로 가져오는 함수
    '''
    global selected_index   
    for item in treeStationfares.selection():
       selected_index = int(treeStationfares.item(item, "text"))
    stationfare = stationfares[selected_index]
    station = stationfare['station']
    fare = str(stationfare['fare'])
    text_Station.delete("1.0",END)
    text_Station.insert("end", station)
    text_Fare.delete("1.0", END)
    text_Fare.insert("end", fare)

def setTreeItems(): 
    '''
    treeview에 현재 stationfares의 내용을 setting 해주는 함수 
    '''
    treeStationfares.delete(*treeStationfares.get_children())
    for idx, stationfare in enumerate(stationfares):   
        station = stationfare['station']               
        fare = stationfare['fare']
        treeStationfares.insert("", 'end', iid=None, text=str(idx), values=[station, fare])

def insert_content():
    '''
    새로운 데이터 추가(Insert)를 위한 함수 
    '''
    station = text_Station.get("1.0",END)
    fare = int(text_Fare.get("1.0",END))
    stationfare = { 'station': station.rstrip(), 'fare': fare } # # .rstrip() 실행
    stationfares.append(stationfare)
    setTreeItems() 

def update_content():
    '''
    기존의 데이터를 수정(Update)하기 위한 함수
    '''
    global selected_index   
    station = text_Station.get("1.0",END)       
    fare = int(text_Fare.get("1.0",END))
    selectedItem = stationfares[selected_index] 
    selectedItem['station'] = station.rstrip()      # .rstrip() 실행: 수정시, 개행문자(\n)이 들어가는 것을 방지하는 명령어
    selectedItem['fare'] = fare
    setTreeItems()     

def delete_content():
    '''
    데이터를 삭제하기 위한 함수
    '''
    global selected_index   
    stationfares.pop(selected_index)
    setTreeItems()

# 이 파일 핵심내용: save_content
def save_content():
    '''
    stationfares.json 파일에 현재 stationfares의 데이터를 저장(Save)하는 함수 
    '''                                                               
    with open('stationfares.json', 'w', encoding='UTF-8') as f:       # encoding='UTF-8'을 안써주면 한글이 깨질 수 있음(UTF-8: 유니코드를 위한 가변길이 인코딩 방식)
        jsonString = json.dumps(stationfares, ensure_ascii=False)     # with open("열 파일 이름", '모드', encoding='방식') as 파일객체명:   <- with문을 활용한 파일 열기
        f.write(jsonString)                                           # json.dumps(저장할 객체[obj], ensure_ascii=False): obj를 json형식의 str로 직렬화하는 것. ensure_ascii=False는 그 문자들을 그대로 출력하도록 설정하는 것(ASCII 문자 이스케이프 X) 
    f.close()                                                         # ensure_ascii=False: ASCII를 사용하지 못하도록 만드는 것


# 전체 화면의 틀 구성하기 
window = Tk()   # 화면 객체 생성   
window.title('Station Fare Management') 
window.geometry("600x600")
window.resizable(0,0)
title = "정류장 요금관리"
lbl_title = Label(window, text=title, font=("돋움체",20))       #Label(대상객체, text='들어갈 내용', font=("글자체",폰트사아즈)): 화면에 이름을 써주는 tkinter 명령어
lbl_title.pack(padx=5, pady=15)

# 트리구조 설정(목록 표 만들기)
# treeStationfares 생성 및 설정: 정류장 요금관리를 표시하는 treeStationsfares 생성
treeStationfares = ttk.Treeview(window)             
treeStationfares["columns"] = ("station", "fare")  
treeStationfares.column("#0", width=50)             
treeStationfares.column("station", width=200)       
treeStationfares.column("fare", width=150)         
# 헤더 설정: treeStationfares에는 순번, 정류장, 요금표시
treeStationfares.heading("#0", text="순번")         
treeStationfares.heading("station", text="정류장")  
treeStationfares.heading("fare", text="요금")      
treeStationfares.place(x=100, y=100, width=400, height=250)      

# 검색한 정류장 요금을 선택하면 stationfares_selected를 실행함, tree를 누르면 실행이 되는 함수를 만들어기주기 
treeStationfares.bind("<<TreeviewSelect>>", stationfares_selected)  

# 버튼 만들기 (Insert, Update, Delete 버튼 만들기 )
btn_Insert = Button(window, text="Insert", command=insert_content, font=("돋움체",14))
btn_Insert.place(x=100, y=400, width=100, height=30)

btn_Update = Button(window, text="Update", command=update_content, font=("돋움체",14))
btn_Update.place(x=200, y=400, width=100, height=30)

btn_Delete = Button(window, text="Delete", command=delete_content, font=("돋움체",14))
btn_Delete.place(x=300, y=400, width=100, height=30)

btn_Save = Button(window, text="Save", command=save_content, font=("돋움체",14))
btn_Save.place(x=400, y=400, width=100, height=30)

# 정류장, 요금에 대해 입력을 할 수 있는 부분
## (button들의 밑에) 정류장, 요금에 대한 Label만들기
labelStation = Label(window, text="정류장")
labelStation.place(x=100, y=450, width=50, height=25)
labelFare = Label(window, text="요금")
labelFare.place(x=100, y=500, width=50, height=25)
# 입력을 받을 입력창 만들기
## Text: tkinter에서 입력값을 넣는 엔트리, 즉 입력창
text_Station = Text(window, width=30, height=1)
text_Station.place(x=200, y=450)
text_Fare = Text(window, width=30, height=1)
text_Fare.place(x=200, y=500)

# treeStationfares 초기입력(처음에 비어있었던 tree를 초기값 설정으로 채워주기)
## setTreeItems: 초기값을 설정해주는 함수, 사용자 정의함수로 직접 설정해 줄 것임.(상단 함수 정의부분 참고) 
print('stationfares: ', stationfares)
setTreeItems()

window.mainloop()   
