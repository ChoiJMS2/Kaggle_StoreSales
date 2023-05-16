# Kaggle_Competition
## Store Sales - Time Series Forecasting

[Streamlit 링크](https://choijms2-kaggle-storesales-app-a383bo.streamlit.app/) <br/><br/>
[발표 영상]() <br/><br/>
[데모 시연]() <br/><br/>
[포트 폴리오]() <br/><br/>
![screensh](img/홈페이지.png)

### 1.프로젝트의 시작 (2023.04.20 ~ 2023.05.17)
- Kaggle Competition : Store Sales - Time Series Forecasting ( Use machine learning to predict grocery sales )
- 링크 : [Kaggle page](https://www.kaggle.com/c/store-sales-time-series-forecasting)
 
### 2. 대회 목표 : 식료품 소매업체의 데이터로 매장 매출을 예측 ( 시계열 예측)
- 여러 매장에서 판매되는 수천 가지 품목의 판매 단가를 더 정확하게 예측하는 모델을 구축
- 날짜, 매장 및 품목 정보, 프로모션, 판매 단가로 구성된 접근하기 쉬운 학습 데이터 세트를 통해 머신 러닝 기술을 연습
- 
### 3. 참여 목적 :
- Python에 대해 공부한 내용을 바탕으로 머신러닝 실습 및 실력향상
- 대시보드 생성능력 향상.
- 시계열 분석 및 회귀 분석 등 통계 지식 향상

### 4. ERD (개체 관계 모델)
![screensh](img/erd.jpg)

### 5. 팀 구성
- 사용언어 : Python : 3.9.13v
- 작업툴 : Pycharm
- 인원 : 4명
- 주요 업무 : Streamlit 라이브러리를 이용한 웹개발 구현 코드 작성 및 머신러닝을 활용한 매장 매출 예측
- 기간 : 2023.04.20 ~ 2023.05.17
***

### 6. 주요 기능
- 
    + ㅇㄹ
### 7. 설치 방법
#### Windows
+ 버전 확인
    - vscode : 1.74.1
    - python : 3.9.13
    - 라이브러리 :  pandas (1.5.3), numpy (1.24.1), plotly (5.13.0), matplotlib (3.6.3), streamlit (1.17.0), streamlit-option-menu (0.3.2), geopandas (0.12.2), pandas-gbq (0.19.1), pydeck (0.8.0), stqdm (0.0.5), prophet (1.1.2), seaborn (0.12.2), openai (0.26.5), streamlit_chat (0.0.2.1), requests (2.28.2v), tensorflow(2.9.0), scikit-learn(1.2.1)

- 프로젝트 파일을 다운로드 받습니다. 

```bash
git clone https://github.com/ChoiJMS2/Kaggle_StoreSales.git
```

- 프로젝트 경로에서 가상환경 설치 후 접속합니다. (Windows 10 기준)
```bash
virtualenv venv
source venv/Scripts/activate
```

- 라이브러리를 설치합니다. 
```bash
pip install -r requirements.txt
```

- streamlit 명령어를 실행합니다. 
```bash
streamlit run app.py
```