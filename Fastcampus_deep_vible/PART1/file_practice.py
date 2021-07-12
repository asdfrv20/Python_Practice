# Overwatch 영웅들을 관리하는 GUI 프로그램 작성 
from tkinter import Tk, ttk, Button, Label, Text, END
import json

# 영웅과 class 데이터 입력(charaterclasses)
characterclasses = []
with open('characterclasses.json', 'r', encoding='UTF-8') as characterclasses_file:     # 저장된 파일 불러오기 
    characterclasses = json.load(characterclasses_file)

# tree에서 선택 전역변수
selected_index = 0

# 핸들 함수 정의
def characterclasses_selected(event):
    '''
    항목 선택 시, 입력창에 데이터 가져오기
    '''
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

def setTreecharacters():
    '''
    Treeview의 데이터 setting하기(추가, 수정, 삭제에 대한 내용 적용하는 setting 함수)
    '''
    treeCharacterclasses.delete(*treeCharacterclasses.get_children())
    for idx, characterclass in enumerate(characterclasses):
        character = characterclass['character']
        class_ = characterclass['class']
        treeCharacterclasses.insert("", 'end', iid=None, text=str(idx), value=[character, class_])

def insert_content():
    '''
    데이터 삽입(추가, Insert)를 수행하는 함수
    '''
    character = text_character.get('1.0',END)
    class_ = text_class.get('1.0', END)
    characterclass = {'character':character, 'class':class_}
    characterclasses.append(characterclass)
    setTreecharacters()
 
def update_content():
    '''
    데이터 수정(Update)를 수행하는 함수
    '''
    global selected_index
    character = text_character.get('1.0', END)
    class_ = text_class.get('1.0', END)
    selectedCharacter = characterclasses[selected_index]
    selectedCharacter['character'] = character
    selectedCharacter['class'] = class_
    setTreecharacters()

def delete_content():
    '''
    데이터를 삭제(Delete)를 수행하는 함수
    '''
    global selected_index
    characterclasses.pop(selected_index)
    setTreecharacters()

def save_content():
    '''
    데이터를 characterclasses.json에 저장하는 함수
    '''
    with open('characterclasses.json', 'w', encoding='UTF-8') as f:
        jsonString = json.dumps(characterclasses, ensure_ascii=False)
        f.write(jsonString)
    f.close()

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
btn_Insert.place(x=100, y=520, width=120, height=30)
btn_Update = Button(window, text='수정', command=update_content, takefocus=True, font=('koverwatch',16))
btn_Update.place(x=225, y=520, width=120, height=30)
btn_Delete = Button(window, text='삭제', command=delete_content,takefocus=True, font=('koverwatch',16))
btn_Delete.place(x=350, y=520, width=120, height=30)
btn_Save = Button(window, text="저장", command=save_content, takefocus=True, font=('koverwatch',16))
btn_Save.place(x=475, y=520, width=125, height=30)

## 입력창
labelCharacter = Label(window, text="영웅 이름", justify='left',font=('koverwatch',15))
labelCharacter.place(x=100, y=580, width=100, height=20)
labelClass = Label(window, text='분류', justify='left', font=('koverwatch', 15))
labelClass.place(x=100, y=620, width=100, height=20)
text_character = Text(window, takefocus=True)
text_character.place(x=220, y=580, width=320, height=20)
text_class = Text(window, takefocus=True)
text_class.place(x=220, y=620, width=320, height=20)


## tree 정보 update 
setTreecharacters()

window.mainloop()
