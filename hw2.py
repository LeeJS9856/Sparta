import random

wld_list = [0,0,0] #승/패/무 횟수담는 리스트

while(True) :
    random_number = random.randint(1, 3) #cpu가 낼 값 만들기, 1=바위, 2=가위, 3=보
    cpu_rsp = ''
    end_game = False

    if(random_number == 1) :
        cpu_rsp = '바위'
    elif(random_number == 2) :
        cpu_rsp = '가위'
    else :
        cpu_rsp = '보'

    while(True) :
        user_rsp = input('가위, 바위, 보 중 하나를 선택하세요 : ')
        if(user_rsp not in ['가위', '바위', '보']) :
            print('유효한 입력이 아닙니다')
        else :
            break

    print(f'사용자 : {user_rsp}, 컴퓨터 : {cpu_rsp}')
    if(user_rsp=='바위') :
        if(cpu_rsp=='바위') :
            print('비겼습니다')
            wld_list[2] += 1
        elif(cpu_rsp=='가위') :
            print('사용자 승리!')
            wld_list[0] += 1
        else :
            print('컴퓨터 승리!')
            wld_list[1] += 1
    elif(user_rsp=='가위') :
        if(cpu_rsp=='바위') :
            print('컴퓨터 승리!')
            wld_list[1] += 1
        elif(cpu_rsp=='가위') :
            print('비겼습니다')
            wld_list[2] += 1
        else :
            print('사용자 승리!')
            wld_list[0] += 1
    else :
        if(cpu_rsp=='바위') :
            print('사용자 승리!')
            wld_list[0] += 1
        elif(cpu_rsp=='가위') :
            print('컴퓨터 승리!')
            wld_list[1] += 1
        else :
            print('비겼습니다')
            wld_list[2] += 1

    while (True):
        input_yn = input('다시 하시겠습니까? (y/n): ')
        if (input_yn == 'y' or input_yn == 'Y'):
            break
        elif (input_yn == 'n' or input_yn == 'N'):
            end_game = True
            print('게임을 종료합니다')
            break
        else:
            print('올바른 값을 입력해주세요')

    if (end_game):
        break

print(f'승 : {wld_list[0]} 패 : {wld_list[1]} 무승부 : {wld_list[2]}')