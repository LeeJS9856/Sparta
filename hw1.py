import random


min_count = 0  # 최소 시도횟수
game_count = 1  # 게임 횟수

while (True):
    random_number = random.randint(1, 100)
    count = 0  # 시도횟수
    end_game = False
    while (True):
        try:
            input_num = int(input('숫자를 입력하세요 : '))
            if (input_num > random_number):
                print('다운')
                count += 1
            elif (input_num < random_number):
                print('업')
                count += 1
            else:
                count += 1
                print('맞았습니다')
                break
        except ValueError:
            print('유효한 범위 내의 숫자를 입력하세요')

    print(f'시도한 횟수 : {count}')
    if (game_count == 1 or min_count > count): #기록 갱신하거나, 첫 게임일때 최소 시도횟수 갱신
        min_count = count
    game_count += 1

    while (True):
        input_yn = input('다시 하시겠습니까? (y/n): ')
        if (input_yn == 'y' or input_yn == 'Y'):
            print(f'이전 게임 플레이어 최소 시도 횟수 : {min_count}')
            break
        elif (input_yn == 'n' or input_yn == 'N'):
            end_game = True
            print('게임을 종료합니다')
            break
        else:
            print('올바른 값을 입력해주세요')

    if (end_game):
        break
