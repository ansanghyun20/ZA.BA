# ZA.BA 
자바 : 자세를 바르게
 
### 헬스 자세교정 플랫폼
 
## 시연 영상 링크

1. 서비스  -  https://youtu.be/G40ThETazsk
2. 대시보드  -  https://youtu.be/GjyRyMhT6oQ
3. 트레이너인증  -  https://youtu.be/gLuK0BR-Yfg
4. 스쿼트 시연  -  https://youtu.be/oBK45VmUOoA
5. 플랭크 시연  -  https://youtu.be/hppbg2swK8c
6. 런지 시연  -  https://youtu.be/s9f7PsMZHMw

#

### 팀원 소개 및 역할

![image](https://user-images.githubusercontent.com/62547169/138979253-109f0c6b-8f13-472e-8b69-6699bdca0d9b.png)

#

### 프로젝트 제작 동기


#### 1) 왜 홈 트레이닝인가?

   - 코로나19로 인한 건강 문제 발생 : 신체활동 감소, 흡연 증가 등으로 인한 체중 증가 및 건강상태 악화
   - 코로나 시대에 따른 사회 변화 : 코로나 대유행 때마다 ‘홈트레이닝’언급량 증가
   - 트레이너가 겪는 어려움 : 코로나 영향 및 유튜브 시장 등으로 인해 대면 트레이닝에 어려움 발생
   - 올바른 자세의 중요성 : 정확하고 올바른 자세가 트레이닝에 있어서 가장 중요

 `→ 이를 모두 고려한 트레이닝 플랫폼에 대한 개발 필요성 대두`
 
 #### 2) 왜 ZA.BA.인가?
 
   - 차별성 : 전문 트레이너의 피드백을 받을 수 없는 단순 AI 트레이닝 플랫폼과 차별화
   - 기획의도
    ◦ 트레이너에게 받을 수 있는 실시간 자세 피드백
    ◦ 줌과 같은 인터넷 서버와 인공지능 기술을 결합한 웹 사이트 개발
   - 개발 목적
    ◦ 트레이너의 전문적 코칭
    ◦ 정확한 자세를 측정하는 AI
    ◦ 운동량 측정 데이터 제공
    

#

### 서비스 및 구조 설명


#### 1) 프로젝트 설계

- 일정 : 구글 스프레드시트, 트렐로 등을 활용한 의사소통 및 협업 수행

![image](https://user-images.githubusercontent.com/62547169/138979400-aa1f8aee-5e9d-4ebb-94fc-c9a055483f1c.png)

#


- 유스케이스 : 운동 선택, 화상 채팅 등 사용자 입장에서 설계한 유스케이스

![image](https://user-images.githubusercontent.com/62547169/138979443-93d58703-a5c9-4fcc-a756-f8157d33b893.png)

#

- 테이블 : 회원정보, 트레이너 정보, 운동량을 반영할 수 있는 테이블 설계

![image](https://user-images.githubusercontent.com/62547169/138979460-652045c6-047f-4bad-9ce8-89deaa2eb462.png)

#

- 인공지능 모델 : 수집, 훈련, 테스트 3단계를 거친 운동별 인공지능 모델 개발

![image](https://user-images.githubusercontent.com/62547169/138979486-166342ad-6348-4be0-88ec-c835ea723f29.png)


#

### 서버 및 인공지능 모델 구조

#### 1) 서버 구조

![image](https://user-images.githubusercontent.com/62547169/138979554-e6312396-2161-4251-ba94-0ec70fc70ae6.png)


#

#### 2) 인공지능 모델 구조

- 데이터 수집

![image](https://user-images.githubusercontent.com/62547169/138979570-9deb3c22-27f3-4638-a40d-8f763fcbd6d4.png)

#

- 모델 훈련 및 테스트 : CSV 파일을 활용하여 데이터 수집 후 운동별 모델 훈련, 시각화 및 테스트

![image](https://user-images.githubusercontent.com/62547169/138979596-510af02e-5317-418d-8a45-9d388816aa28.png)

#

- 테스트 과정 : 훈련한 모델을 기반으로 하여 실제 테스트 수행

![image](https://user-images.githubusercontent.com/62547169/138979617-c48be645-408d-4e61-aa18-0af2c2f96cbd.png)


#

### 주요 제공 서비스

- 서비스 안내 페이지 : 스쿼트, 런지, 플랭크 등 5개의 맨몸 운동 제공

![image](https://user-images.githubusercontent.com/62547169/138979661-96a49d5f-a4dc-40a6-a8f8-98d2c0a10e8d.png)

#

- 트레이너 선택 페이지 : 원하는 트레이너를 선택하여 방에 입실

![image](https://user-images.githubusercontent.com/62547169/138979681-c453a6b6-8f98-44a7-bd84-cc612fe7ec3e.png)

#

- 실제 운동 페이지 : 트레이너와 사용자들이 한 화면에서 트레이닝 실시

![image](https://user-images.githubusercontent.com/62547169/138979686-eb5eadec-9409-40b9-9104-8b5dbd555b4c.png)

#

- 대시보드 페이지 : 사용자 개인과 전체 사용자의 운동 결과 표시

![image](https://user-images.githubusercontent.com/62547169/138979703-35d6a22d-f633-4f9d-8f3e-469f025a76b8.png)

#

- 대시보드 1 : 사용자 개인의 오늘 운동량과 사용자 전원의 오늘 운동량 산출

![image](https://user-images.githubusercontent.com/62547169/138979719-a3550c63-1b50-46c6-b91f-ae3c5c57df11.png)

#

- 대시보드 2 : 운동 횟수에 따른 목표 수치 및 등급 제공

![image](https://user-images.githubusercontent.com/62547169/138979739-749b1aa9-3434-472b-be83-a72ad8adc6cf.png)

#

- 대시보드 3 : 스쿼트 운동 횟수에 대한 사용자 순위와 인공지능 모델의 정확도 제공

![image](https://user-images.githubusercontent.com/62547169/138979747-aff95035-47e5-4dd3-b082-abc645df95a2.png)

#

- 대시보드 4 : 시용자의 날짜별 운동량 제공

![image](https://user-images.githubusercontent.com/62547169/138979764-8a0e3685-4cc4-43f2-a7f1-fa6a9c2a6759.png)

#

- 고객센터 페이지 : 문의사항과 의견을 메일로 보내는 기능

![image](https://user-images.githubusercontent.com/62547169/138979780-c858e77d-218d-492a-8bbb-966c2ef72537.png)


#
