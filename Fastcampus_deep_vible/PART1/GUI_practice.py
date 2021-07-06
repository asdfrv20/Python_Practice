# Overwatch 영웅들을 관리하는 GUI 프로그램 작성 
from tkinter import Tk, ttk, Button, Label, Text, END

# 영웅과 class 데이터 입력(charaterclasses)
characterclasses = [
    {'character': '겐지', 'class': '공격(Damage)'},
    {'character': '리퍼', 'class': '공격(Damage)'},
    {'character': '맥크리', 'class': '공격(Damage)'},
    {'character': '메이', 'class': '공격(Damage)'},
    {'character': '바스티온', 'class': '공격(Damage)'},
    {'character': '솔저:76', 'class': '공격(Damage)'},
    {'character': '시메트라', 'class': '공격(Damage)'},
    {'character': '위도우메이커', 'class': '공격(Damage)'},
    {'character': '정크랫', 'class': '공격(Damage)'},
    {'character': '토르비욘', 'class': '공격(Damage)'},
    {'character': '트레이서', 'class': '공격(Damage)'},
    {'character': '파라', 'class': '공격(Damage)'},
    {'character': '한조', 'class': '공격(Damage)'},
    {'character': 'D.va', 'class': '돌격(Tank)'},
    {'character': '라인하르트', 'class': '돌격(Tank)'},
    {'character': '레킹볼', 'class': '돌격(Tank)'},
    {'character': '로드호그', 'class': '돌격(Tank)'},
    {'character': '윈스턴', 'class': '돌격(Tank)'},
    {'character': '자리야', 'class': '돌격(Tank)'},
    {'character': '루시우', 'class': '지원(Surport)'},
    {'character': '메르시', 'class': '지원(Surport)'},
    {'character': '젠야타', 'class': '지원(Surport)'}
]

# tree에서 선택 전역변수
selected_index = 0

# 핸들 함수 정의
## 항목 선택 시, 입력창에 데이터 가져오기 
def characterclasses_selected(event):
    global selected_index
    for item in treeCharacterclasses.selection():
        selected_index = int(treeCharacterclasses.item(item,'text'))
    characterclass = characterclasses[selected_index]
    character = characterclass['character']
    class_ = characterclass['class']
    text_character.delete('1.0',END)
    text_character.insert('end',character)
    text_class.delete('1.0',END)
    text_class.insert('end',class_)

## Treeview의 데이터 setting하기(추가, 수정, 삭제에 대한 내용 적용하는 setting 함수)
def setTreecharacters():
    treeCharacterclasses.delete(*treeCharacterclasses.get_children())
    for idx, characterclass in enumerate(characterclasses):
        character = characterclass['character']
        class_ = characterclass['class']
        treeCharacterclasses.insert("", 'end', iid=None, text=str(idx), value=[character, class_])

# 데이터 삽입(추가, Insert)를 수행하는 함수
def insert_content():
    character = text_character.get('1.0',END)
    class_ = text_class.get('1.0', END)
    characterclass = {'character':character, 'class':class_}
    characterclasses.append(characterclass)
    setTreecharacters()

# 데이터 수정(Update)를 수행하는 함수 
def update_content():
    global selected_index
    character = text_character.get('1.0', END)
    class_ = text_class.get('1.0', END)
    selectedCharacter = characterclasses[selected_index]
    selectedCharacter['character'] = character
    selectedCharacter['class'] = class_
    setTreecharacters()

# 데이터를 삭제(Delete)를 수행하는 함수
def delete_content():
    global selected_index
    characterclasses.pop(selected_index)
    setTreecharacters()

# GUI 창 설정 
## window 생성 및 제목 label 생성
window = Tk()
window.title('Overwatch Character Manager')
window.geometry('700x700+50+50')
window.resizable(0,0)
title = "Overwatch 캐릭터 종류, class 관리 프로그램"
lbl_title = Label(window, text=title, font=('koverwatch', 30))
lbl_title.pack(padx=5 ,pady=25)

## tree 생성
treeCharacterclasses = ttk.Treeview(window)
treeCharacterclasses['columns'] = ('character', 'class')
treeCharacterclasses.column('#0', width=50)
treeCharacterclasses.heading('#0', text='순번')
treeCharacterclasses.column('character', width=200)
treeCharacterclasses.heading('character', text='영웅')
treeCharacterclasses.column('class', width=200)
treeCharacterclasses.heading('class', text='분류')
treeCharacterclasses.place(x=100, y=100, width=500, height=400)

treeCharacterclasses.bind('<<TreeviewSelect>>', characterclasses_selected)

## 버튼 생성: 추가(Insert), 수정(Update), 삭제(Delete) 
btn_Insert = Button(window, text="추가", command=insert_content, takefocus=True ,font=('koverwatch',16))
btn_Insert.place(x=100, y=520, width=150, height=30)
btn_Update = Button(window, text='수정', command=update_content, takefocus=True, font=('koverwatch',16))
btn_Update.place(x=275, y=520, width=150, height=30)
btn_Delete = Button(window, text='삭제', command=delete_content,takefocus=True, font=('koverwatch',16))
btn_Delete.place(x=450, y=520, width=150, height=30)

## 입력창
labelCharacter = Label(window, text="영웅 이름", justify='left',font=('koverwatch',15))
labelCharacter.place(x=100, y=580, width=100, height=20)
labelClass = Label(window, text='분류', justify='left', font=('koverwatch', 15))
labelClass.place(x=100, y=620, width=100, height=20)
text_character = Text(window, )
text_character.place(x=220, y=580, width=320, height=20)
text_class = Text(window, )
text_class.place(x=220, y=620, width=320, height=20)


## tree 정보 update 
setTreecharacters()

window.mainloop()
