인공지능 R&D 챌린지 평가지표 AUROC 계산을 위한 소스코드
===================================================
 
 **이 소스코드는 인공지능 R&D 챌린지 2차 워크샵 및 본선 경연 시 평가지표 AUROC(Area Under Receiver Operating Characteristic) 계산 도구로 활용됩니다. 챌린저 여러분들은 이 평가도구를 활용하여 결과 값을 계산하길 권장 드립니다.** 아울러 소스코드의 오류를 검출하신 챌린저는 적극적으로 피드백 주시기 바랍니다.

- - -
**(2017.11.22. 수정사항)** 예측 값을 0 또는 1로 제출한 경우를 처리하기 위해, AUROC 계산시 ROC 곡선의 좌표 (0,0)과 (1,1)을 포함시켰습니다.

- - -

AUROC 소스코드는 python으로 작성됐으며, 객관성을 유지하기 위해 외부 라이브러리 사용은 최소화했습니다. AUROC를 계산하기 위한 방법은 입력 값에 따라 아래와 같이 두 가지 방법이 있습니다.

1. $ python ./main.py –p prediction_file.txt –l label_file.txt
  - 예측 값과 라벨 값을 담은 두 개의 텍스트 파일로부터 계산
  - (예측 값) prediction_file.txt는 챌린지에 공지했다시피 문제번호,확률 값 으로 작성
  - (라벨 값) label_file.txt는 문제번호,라벨 값 순으로 작성

2. $ python ./main.py –i merged_pl.txt
  - 예측 값과 라벨 값을 하나의 텍스트 파일에 작성한 경우를 계산
  - 문제번호, 예측 값, 라벨 값 순으로 작성

- - -

**아래는 AUROC를 계산하기 위한 가정사항입니다.**

1. 예측 값과 라벨 값의 차원은 같아야 한다. (line 수가 같다)
2. 예측 값과 라벨 값은 문제번호에 따라 오름차순으로 정렬되어야 한다.
3. 예측 값은 0과 1 사이의 실수 값, 라벨 값은 0 또는 1로 구성된다.
4. 가짜 뉴스의 라벨은 1, 진짜 뉴스의 라벨은 0이다.
5. ROC 곡선을 계산하는 cut-off 값은 예측 값을 활용한다. 
6. AUROC를 계산하는 방법은 사다리꼴 적분법(Trapezoidal Rule)을 활용했으며, 정밀도는 single precision(유효 숫자 7자리)을 사용한다.

- - -

[추가사항]

**ROC 곡선의 plotting 함수도 제공합니다.** 사용방법은 위에 공지한 바와 같고, 참고할 파일은 main_plot.py입니다.

<p align="center">
 <img src="https://raw.githubusercontent.com/hyoungseokchu/AUROC/master/plot_example.png" width="400">
</p>


**위 소스코드와 관련된 문의사항은 인공지능 R&D 챌린지 홈페이지에 게시해주시기 바랍니다.**

http://airndchallenge.com 
