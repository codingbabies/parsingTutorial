# 알고 있으면 좋은 거

## IDE
- [VSCode](https://code.visualstudio.com/)(Visual Studio Code)
    - MS에서 만든 코드 에디터로, 거의 모든 환경을 대체 가능한 막강한 툴
    - Python, JS, C, Golang 등 대부분의 언어 개발에 이용 가능함
    - 크로스 플랫폼 지원으로 대부분의 모든 OS에서 지원함
- [Pycharm](https://www.jetbrains.com/ko-kr/pycharm/)
    - 파이썬 코딩러들의 영원한 IDE 파이참
    - 파이썬에 특화된 막강한 기능을 지원함
    - 자바로 만들어졌으며, 마찬가지로 거의 모든 OS에서 지원함
    - 커뮤니티 버전은 무료로 이용 가능, 유료버전을 이용할 경우 신기하고 많은 기능 이용 가능

## pip? pypi?
- pip(package installer for Python)
    - 대부분의 언어는 패키지 관리 툴이 존재함
    - 파이썬은 pip라는 패키지 관리 툴을 이용함
    - `pip install xxx` 형식으로 패키지를 다운 받을 수 있고, 이후에 `import`하여 사용 가능
    - `pip freeze` 명령을 통해 현재 설치된 패키지 목록을 얻을 수 있음
    - 일반적으로 `pip freeze > requirements.txt`로 dependency list 같이 배포
- [pypi](https://pypi.org/)(The Python Package Index)
    - pip로 설치할 때 실제로 해당 파일을 가져오는 저장소로, 각종 패키지를 검색해 볼 수 있음
    - 버전 및 설명 등이 자세히 써있으며, 없는 경우 일반적으로 github 링크 제공하는 것 같음

## [Jupyter Notebook](https://jupyter.org/)
- 파이썬은 여러가지 방법으로 개발이 가능한데, jupyter notebook은 좋은 방법 중 하나
- 일반적으로 로컬 혹은 서버로 웹앱을 띄운 뒤 개발하는 방식으로, 인터프리터의 특성에 맞게 라인별 실행이 가능
- 각 실행에 대한 결과를 즉각 확인 가능하며, 해당 결과는 저장되어 나중에 다시 열어도 남아있음
- 학습, 스터디, 교육용 등으로 적합함
- MarkDown(본 문서도 md임)을 자체 지원하기 때문에 문서 작성과 코딩을 동시에 할 수 있음
- 추가로 링크나 이미지 등도 삽입이 가능하기 때문에 매우 실용적임