import hashlib

class Member:
    def __init__(self, name, username, password) :
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'회원 이름 : {self.name}, 회원 아이디 : {self.username}')

    def nm(self): #이름 리턴
        return self.name


class Post:
    def __init__(self, title, content, author) :
        self.title = title
        self.content = content
        self.author = author

    def search_user(self, user) : #검색된 유저이름과 작성자가 같으면 제목 출력
        if(user == self.author) :
            print(self.title)
        
    def search_kword(self, kword) : #검색된 키워드가 게시물에 존재하면 제목 출력
        if(kword in self.content) :
            print(self.title)

def name_list(list) : #회원 이름 리스트만들기
    name_list = []
    for name in list :
        name_list.append(name.nm())
    return name_list



members = []
posts = []

while(True) :
    num = 0
    while(True) :
        print('-------원하시는 항목의 번호를 입력해주세요-------.')
        num = int(input('[1]회원등록   [2]게시물작성   [3]회원정보   [4]게시글보기   [5]종료\n'))
        if(not num in [1,2,3,4,5]) :
            print('올바른 값을 입력해주세요\n')
        else :
            print('\n')
            break
    
    if(num==1) :
        user_name = input('등록하실 이름을 입력해주세요 : ')
        user_id = input('ID를 입력해주세요 : ')
        user_pwd = input('비밀번호를 입력해주세요 : ')
        print('\n')
        hashed_user_pwd = hashlib.sha256(user_pwd.encode())
        members.append(Member(user_name, user_id, hashed_user_pwd))
    elif(num==2) :
        title = input('제목 : ')
        content = input('내용 : ')
        while(True) :
            author = input('작성자 : ')
            if(not author in name_list(members)) :
                print('해당 작성자가 존재하지 않습니다')
            else :
                print('작성되었습니다.\n')
                posts.append(Post(title, content, author))
                break
    elif(num==3) :
        for member in members :
            member.display()
            print('\n')
    elif(num==4) :
        check = 0
        while(True) :
            print('검색하고싶은 게시물 필터의 번호를 입력하세요.')
            check = int(input('[1]유저 검색   [2]키워드 검색\n'))
            if(not check in [1,2]) :
                print('올바른 값을 입력해주세요\n')
            else :
                break
        
        if(check==1) :
            user = input('검색할 유저이름 : ')
            print('\n')
            for post in posts :
                post.search_user(user)
        else :
            kword = input('검색할 키워드 : ')
            print('\n')
            for post in posts :
                post.search_kword(kword)
        print('\n')
    else :
        break
