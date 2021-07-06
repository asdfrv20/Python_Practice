# Tkinter로 승차권 예제를 GUI로 만들기 
## 작성 프로그램: 승차역별로 요금을 관리하는 프로그램 

# import Lib
from tkinter import Tk, ttk, Label, Button, Text, END

# stationfares 정보 
stationfares = [
    {'station': "청량리", 'fare': 1500},
    {'station': "성북", 'fare': 1800},
    {'station': "의정부", 'fare': 2000},
    {'station': "소요산", 'fare': 2500}
]

selected_index = 0     # selected_index: 선택하는 항목의 인덱스를 저장하는 전역변수(default:0) 

# 이벤트 함수들 정의 
def stationfares_selected(event):  
    # stationfares_selected는 이벤트에 대한 핸들 함수이므로, event를 입력으로 받아주어야 한다. 
    # tree에서 하나가 선택되면 해당 데이터가 station과 fare값이 stationfares[selected_index]에서 나누어지고
    # 이를 텍스트 형태로 입력창에 넣어주는 함수 
    # key point: 함수 내에서 selected_index의 "전역변수" 선언해주기()
    global selected_index   # (중요!) 이 함수안에서 설정된 selected_index가 전역변수임을 알려주어야한다.(만약 그렇지 않을 경우 함수 종료와 함께 값 없어짐)
    #print('.selection 정보 출력', treeStationfares.selection(), type(treeStationfares.selection()))
    for item in treeStationfares.selection():       # .selection: tree객체(ttk.Treeview 객체)에서 선택된 것들만 가져오는 내장함수
       #print('item 출력',item, type(item))
       selected_index = int(treeStationfares.item(item, "text"))       # treeStationfares의 item중에서 금방가져온 text를 가져오서 int로 변환->selected_index에 할당
       #print('.item 출력',treeStationfares.item(item, "text"), type(treeStationfares.item(item, "text")))
    stationfare = stationfares[selected_index]      # stationfares에서 선택된 인덱스의 fare(요금) 값을 가져온다. 
    station = stationfare['station']
    fare = str(stationfare['fare'])
    text_Station.delete("1.0",END)      # text_Station: station의 이름을 써주는 곳의 1.0~END까지를 전부 지우는 명령. 즉, 기존에 있던 내용들을 다 지우는 과정
    text_Station.insert("end", station) # "1.0": 첫번째 줄 첫번째(0번째)문자 // END: 텍스트의 마지막 문자 위치 (Tkinter.Text 문서의 '텍스트 마크' 참고, https://076923.github.io/posts/Python-tkinter-18/)
    text_Fare.delete("1.0", END)        # .delete(start_index, end_index): start_index부터 end_index까지의 문자열 삭제
    text_Fare.insert("end", fare)       # .index(index, "문자열"): 해당 index 위치에 문자열 삽입

def setTreeItems(): 
    # 현재 데이터의 정보를 tree에 보여주기위한 setting 함수 
    # 처음에 실행될 때 or 중간에 변화가 있을 때, stationfares의 값들을 tree에 넣어주는 함수. 즉, tree 내용을 setting 해주는 함수 
    # setTreeItems는 insert나 update, delete명령 실행 시, 그리고 window.mainloop() 바로 앞에 한 번 씩 실행해 주어야 함.(tree에 보이는 정보를 이벤트에 따라 지속적을 업데이트 해주는 것.)
    # 기존에 treeStationfares에 정보를 가져온 것이 있으면 모두 지워줌 & 다시 가져오기(Tip)
    treeStationfares.delete(*treeStationfares.get_children())   # *treeStationfares.get_children(): treeStationfares에 해당하는 주소값을 모두 가져와 지움.
                                                                # 이것들을 한 번에 확 지워주는 것이 여기 1줄 명령어(데이터가 계속 쌓이는 것을 방지)
    for idx, stationfare in enumerate(stationfares):    # 저장된 stationfares 가져오기 
        station = stationfare['station']                # statoinfares를 station과 fare로 나누기
        fare = stationfare['fare']
        treeStationfares.insert("", 'end', iid=None, text=str(idx), values=[station, fare]) # 위에서 가져온 station과 fare를 treeStationfares에 넣어주기
        # treeStationfares.insert(상위항목, 삽입위치, option)

def insert_content():
    # 새로운 데이터 추가를 위한 함수 
    station = text_Station.get("1.0",END)               # station과 fare 입력창의 입력값을 1.0~END까지 가져오기 
    fare = int(text_Fare.get("1.0",END))
    stationfare = { 'station': station, 'fare': fare }  # stationfare에 station과 fare값을 받아 [dic]형태로 저장
    stationfares.append(stationfare)                    # stationfares에 데이터 삽입하기 
    setTreeItems()      # tree의 정보 업데이트

def update_content():
    # 기존의 데이터를 수정하기 위한 함수
    global selected_index   # (중요!) 이 함수안에서 설정된 selecetd_index가 전역변수임을 알려주어야한다.(만약 그렇지 않을 경우 함수 종료와 함께 값 없어짐)
    station = text_Station.get("1.0",END)       # 입력창에서 station, fare값 읽어오기 
    fare = int(text_Fare.get("1.0",END))
    selectedItem = stationfares[selected_index] # tree에서 선택된 데이터의 index값 가져오기 
    selectedItem['station'] = station           # 해당 데이터의 station, fare값 수정 
    selectedItem['fare'] = fare
    setTreeItems()      # tree의 정보 update

def delete_content():
    global selected_index   # (중요!) 이 함수안에서 설정된 selecetd_index가 전역변수임을 알려주어야한다.(만약 그렇지 않을 경우 함수 종료와 함께 값 없어짐)
    stationfares.pop(selected_index)    # pop(): 지워주기 위한 명령어
    setTreeItems()


# 전체 화면의 틀 구성하기 
window = Tk()   # 화면 객체 생성   
window.title('Station Fare Management') # window의 제목(최상단에 표시될 프로그램 제목)
window.geometry("600x600")      # geometry("너비*높이+x좌표+y좌표"): 윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표,y좌표를 설정할 수 있다.
window.resizable(0,0)           # resizable(False,False): 화면의 크기를 조정할 수 있게 설정할지에 대한 내용.(True일 때, 조정 가능)
title = "정류장 요금관리"        # title: 화면에 출력될 제목 내용
lbl_title = Label(window, text=title, font=("돋움체",20))       #Label(대상객체, text='들어갈 내용', font=("글자체",폰트사아즈)): 화면에 이름을 써주는 tkinter 명령어
lbl_title.pack(padx=5, pady=15) # pack: 패딩값을 주는 것(x축 y축 여백)
        # 여기까지하고 화면 확인해보기 
        # 이제 여기에서부터 인형에 눈을 붙이듯이 하나씩 만들어 나갈 것임


# 트리구조 설정(목록 표 만들기)
# treeStationfares 생성 및 설정: 정류장 요금관리를 표시하는 treeStationsfares 생성
treeStationfares = ttk.Treeview(window)             # ttk.Treeview: 대상객체를 tree 형태로 보여주는 것
treeStationfares["columns"] = ("station", "fare")   # treeStationfares의 column(열) 설정
treeStationfares.column("#0", width=50)             # #0: 맨처음에 있는 것(빈칸), width=50: 크기를 50을 잡기
treeStationfares.column("station", width=200)       # station 항목의 너비: 200으로 주기
treeStationfares.column("fare", width=150)          # fare 항목의 너비: 150으로 주기 
# 헤더 설정: treeStationfares에는 순번, 정류장, 요금표시
treeStationfares.heading("#0", text="순번")         # #0(처음 앞에 있는 것): 순번 써주기
treeStationfares.heading("station", text="정류장")  # station에 '정류장' 넣기
treeStationfares.heading("fare", text="요금")       # fare에 '요금' 넣기 
treeStationfares.place(x=100, y=100, width=400, height=250)     # treeStationfares의 위치 설정: x=100,y100좌표에 width=400, height=250으로 잡아주기 
        # 여기까지 작성을 한 후 실행 해보기
        # 위와 달라진 점에 주목! 


# 검색한 정류장 요금을 선택하면 stationfares_selected를 실행함 
## tree를 누르면 실행이 되는 함수를 만들어기주기 
## 여기에서부터 이벤트에 해당하는 함수인 stationfares_selected, insert_content, update_content, delete_content는 우리가 만들어 주어야한다. 
## 이 함수들은 맨위에 초기 변수들이 선언된 곳에 만들어주자
treeStationfares.bind("<<TreeviewSelect>>", stationfares_selected)  # treeview가 selected 되었을 때, stationfares_selected(함수)라는 이벤트가 발생함

# 버튼 만들기 (Insert, Update, Delete 버튼 만들기 )
## Botton: tkinter에서 버튼을 생성하는 class
## Botton의 속성: Botton(대상객체, text="버튼글자", command=클릭시발생할이벤트, font=("글꼴",글자크기))
btn_Insert = Button(window, text="Insert", command=insert_content, font=("돋움체",14))
btn_Insert.place(x=100, y=400, width=100, height=30)

btn_Update = Button(window, text="Update", command=update_content, font=("돋움체",14))
btn_Update.place(x=250, y=400, width=100, height=30)

btn_Delete = Button(window, text="Delete", command=delete_content, font=("돋움체",14))
btn_Delete.place(x=400, y=400, width=100, height=30)


# 정류장, 요금에 대해 입력을 할 수 있는 부분
## (button들의 밑에) 정류장, 요금에 대한 Label만들기
## 이 항목의 옆에는 입력을 할 수 있는 창을 만들 것임 
labelStation = Label(window, text="정류장")
labelStation.place(x=100, y=450, width=50, height=25)
labelFare = Label(window, text="요금")
labelFare.place(x=100, y=500, width=50, height=25)
# 입력을 받을 입력창 만들기
## Text: tkinter에서 입력값을 넣는 엔트리, 즉 입력창
## Text의 속성: Text(대상객체, width=입력글자수, height=입력줄)
text_Station = Text(window, width=30, height=1)
text_Station.place(x=200, y=450)
text_Fare = Text(window, width=30, height=1)
text_Fare.place(x=200, y=500)


# treeStationfares 초기입력(처음에 비어있었던 tree를 초기값 설정으로 채워주기)
## setTreeItems: 초기값을 설정해주는 함수, 사용자 정의함수로 직접 설정해 줄 것임.(상단 함수 정의부분 참고) 
print('stationfares: ', stationfares)
setTreeItems()


window.mainloop()       # 실행 시, 그냥 꺼지는 것을 방지하기 위한 명령어 
