import os 
import csv
from post import Post

# @ - 게시글 로딩하기
# 파일 경로
file_path = "./Fastcampus_python_web/Chapter12/data.csv"

# post 객체를 저장할 리스트 
post_list = []

# data.csv 파일이 있다면, 
if os.path.exists(file_path):       # os.path.exists: 이 path에 해당 파일이 있는지 확인하는 명령어, 결과:True/False
    # 게시글 로딩
    print("게시글 로딩중...")
    f = open(file_path, "r", encoding="utf-8")
    reader = csv.reader(f)
    for data in reader:
        # Post 인스턴스 생성하기 
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)
    f.close()

# data.csv 파일이 없다면,
else:
    # 파일 생성하기 
    f = open(file_path, "w", encoding="utf-8", newline="")
    f.close()

print(post_list[0].get_title())


# @ - 게시글 쓰기
def write_post():
    """게시글 쓰기 함수"""
    print("\n\n- 게시글 쓰기 -")
    title = input("제목을 입력해 주세요\n>>>")
    content = input("내용을 입력해 주세요\n>>>")
    # 글번호
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    print("# 게시글이 등록되었습니다.")


# @ - 게시글 목록 
def list_post():
    """게시글 목록 함수"""
    # 글번호 선택
    # 현재 게시글 목록 출력 
    print("\n\n- 게시글 목록 -")
    id_list = []
    for post in post_list:
        print("번호 :", post.get_id())
        print("제목 :", post.get_title())
        print("조회수 :", post.get_view_counts(), "\n")
        id_list.append(post.get_id())

    while True:
        try:
            id = int(input("Q) 글 번호를 선택해 주세요 (메뉴로 돌아가려면 -1을 입력)\n>>> "))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                print("메뉴로 돌아갑니다")
                break
            else:
                print("없는 글 번호입니다.")
        except ValueError:
            print("숫자를 입력해주세요")


# @ - 게시글 상세페이지 확인
def detail_post(id):
    """ 게시글 상세 보기 함수 """
    print("\n\n- 게시글 상세 -")

    for post in post_list:
        if post.get_id() == id:
            # 조회수 1증가
            post.add_view_count()
            print("번호 : ", post.get_id())
            print("제목 : ", post.get_title())
            print("본문 : ", post.get_content())
            print("조회수 : ", post.get_view_counts())
            targetpost = post

    while True:
        print("Q) 수정: 1 삭제:2 (메뉴로 돌아가려면 -1을 입력)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                updata_post(targetpost)
                break
            elif choice == 2:
                delete_post(targetpost)
                break
            elif choice == -1:
                break
            else:
                print("잘못 입력하였습니다.")
        except ValueError:
            print("숫자를 입력해 주세요.")

# @ - 게시글 수정 
def update_post(targetpost):
    """게시글 수정 함수"""
    print("\n\n- 게시글 수정 -")
    title = input(f"제목을 입력해 주세요>>> ")
    for post in post_list:


# @ - 게시글 삭제
def delete_post(targetpost):
    """게시글 삭제 함수"""
    



# @ - 메뉴 출력하기 
while True:
    print("\n\n- FASTCAMPUS BLOG -")
    print("- 메뉴를 선택해 주세요 -")
    print("1. 게시글 쓰기")
    print("2. 게시글 목록")
    print("3. 프로그램 종료")
    try:
        select = int(input(">>>"))
    except ValueError:
        print("잘못된 입력입니다. 숫자를 입력해주세요.")
    if select == 1:
        # @ - 게시글 쓰기(함수 - "write_post"의 내용 참고)
        write_post()
    elif select == 2:
        # @ - 게시글 목록(함수 - "list_pose"의 내용 참고)
        list_post()
    elif select == 3:
        print("[프로그램 종료]")
        break




