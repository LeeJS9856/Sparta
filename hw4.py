from flask import Flask, render_template, request
import random

app = Flask(__name__)

count_list = [0, 0, 0]  # 횟수 카운트 리스트 [승/무/패]
game_list = []  # 게임 내역 리스트
game_cnt = 0

@app.route("/", methods=['GET', 'POST'])
def hw():
    def cpu_random():
        random_number = random.randint(1, 3)  # cpu가 낼 값 만들기, 1=바위, 2=가위, 3=보
        cpu_rsp = ''
        if (random_number == 1):
            cpu_rsp = '바위'
        elif (random_number == 2):
            cpu_rsp = '가위'
        else:
            cpu_rsp = '보'
        return cpu_rsp

    def rsp(user_rsp, cpu_rsp, cnt):  # 가위바위보 결과 출력
        if (user_rsp == '바위'):
            if (cpu_rsp == '바위'):
                cnt[1] += 1
                return "비겼습니다."
            elif (cpu_rsp == '가위'):
                cnt[0] += 1
                return "이겼습니다."
            else:
                cnt[2] += 1
                return "졌습니다."
        elif (user_rsp == '가위'):
            if (cpu_rsp == '바위'):
                cnt[2] += 1
                return "졌습니다."
            elif (cpu_rsp == '가위'):
                cnt[1] += 1
                return "비겼습니다."
            else:
                cnt[0] += 1
                return "이겼습니다."
        else:
            if (cpu_rsp == '바위'):
                cnt[0] += 1
                return "이겼습니다."
            elif (cpu_rsp == '가위'):
                cnt[2] += 1
                return "졌습니다."
            else:
                cnt[1] += 1
                return "비겼습니다."

    def change_emo(rsp):  # 가위바위보를 이모티콘으로 변경
        if (rsp == "바위"):
            return "✊"
        elif (rsp == "보"):
            return "🤚"
        elif (rsp == "가위"):
            return "✌"
        else:
            return "오류"
        
    global count_list, game_list, game_cnt

    if request.method == "POST":
        user_rsp = request.form.get("choices")  # 사용자 값 가져오기
        cpu_rsp = cpu_random()  # 컴퓨터 값 생성하기

        result = rsp(user_rsp, cpu_rsp, count_list)  # 가위바위보 시도하기
        game_cnt += 1  # 게임횟수 + 1

        new_user_rsp = change_emo(user_rsp)
        new_cpu_rsp = change_emo(cpu_rsp)
        game_result = [game_cnt, new_cpu_rsp, new_user_rsp, result]
        game_list.append(game_result)  # 현재 게임 결과를 게임 내역 리스트에 추가

        context = {
            "user_rsp": new_user_rsp,
            "cpu_rsp": new_cpu_rsp,
            "result": result,
            "count": count_list,
            "game_list": game_list,
        }
        return render_template('hw4.html', data=context)
    else:
        context = {
            "user_rsp": "🤚",
            "cpu_rsp": "🤚",
            "result": "게임을 시작합니다.",
            "count": count_list,
            "game_list": game_list,
        }
        return render_template('hw4.html', data=context)


if __name__ == '__main__':
    app.run(debug=True)
