<img width="797" alt="image" src="https://user-images.githubusercontent.com/117002193/224116465-2d81cbc4-c2de-4257-9010-815f02ce389a.png">


<h1>🚘  &nbsp Final-Project  &nbsp 🚘</h1>

연산기 센서 데이터 및 MES 분석을 통한 연삭 휠 수명관리 및 예측 솔루션

연삭지 잔량, 교체 시기 예측 

부서간 협력 툴 <hr>

<h2>💻 &nbsp 개발환경 &nbsp 💻</h2>

- Colab    (개발툴)

- VSCode   (개발툴)
 
- Grafana  (시각화)

- Arima    (시계열)

- Django   (웹) <hr>



<h2>🫧 &nbsp 전처리 및 알고리즘 사용 프로세스 요약 &nbsp 🫧</h2>

date_range를 통해 ‘time’열의 결측값을 채워줌

휠을 교체했을 때의 초기두께를 알아낸 후 전체 그래프에서 데이터가 사라지기 전까지의 데이터의 기울기를 얻음

기울기를 통해 0이 될 때까지의 기간을 구하고 교체 시점 예측 후 초기 두께인 60mm 입력

남은 결측치 선형 보간법을 통해 보간

auto arima를 통해 베스트 모델 채택 (ARIMA 차수 p,d,q 구함)

ARIMA 사용 후 예측 결과 도출 (7일 학습, 1일 예측)


