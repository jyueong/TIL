# git
## local에서 git 기록 하는법
- `git init` >> 디렉토리를 깃 레포지토리로 지정
- 세가지 상태(working directory(작업하는곳) / staging area(임시공간) / commits)
  - `git status` 로 확인
    - git add 전에는 untracted files
    - staging area에 있으면 changes to be committed
    - commit 하면 nothing to commit
    - 파일 수정하면 modified
      - working directory에 있던 애가 수정됨 >> commits 에 있는 애랑 다름 >> git status 해보면 modified 로 나옴
      - `git restore` 혹은 (`git add` >> `git commit`)

- `git add {file_name}`
  - 파일을 staging area에 추가(자연스럽게 working directory에도 추가)
  - 폴더에 있는 파일들 싹 다 올려줘(변경사항 있는 경우에만) >> `git add .`
  - 
- `git commit -m 'commit message'`
  - 커밋(버전기록 남기기)
    - 'commit message'는 필수, 내용은 변경가능 >> 어떤게 변경되었는지 내용 적어주기
      - 남이 봐도 알 수 있게 >> 협업에 유용
      - 정보 중심
    - 커밋하면 staging area에서는 없어짐
- 초기설정
  - `git config --global user.name {username}`
  - `git config --global user.email {useremail}`
  - `git config --global -l` : 현재 어떻게 설정되어있는지 확인
  - 변경 하고 싶으면 그냥 다시 입력 >> 덮어씌워짐
  - `git config --local user.name {}` 을 알려주셨는데... 뭔 말이지...?
  - `git log` : 남긴 commit에 대한 기록 조회
  - ```python
    $ git log
    commit ff10b0804ce5822304bf4a5f2f39ae3106b41a95 (HEAD -> master)
    Author: jyueong <uj9125@gmail.com>
    Date:   Fri Jul 15 12:59:45 2022 +0900
    
        change a.txt
    
    commit 4c0c8ce90ba41e87fa132d7cf11bc451cb704fb1
    Author: jyueong <uj9125@gmail.com>
    Date:   Fri Jul 15 12:44:25 2022 +0900
    
        commit message
    ```

  - commit 뒤에 있는건 commit 아이디, 커밋별로 다 다름, 앞에 4자로 구분

  - HEAD? branch(작업공간) 중 어디에 있는지?

  - `git log --oneline` : 짧게 보여줘

    - ```python
      $ git log --oneline
      8fda4d7 (HEAD -> master) change a.txt again, add b.txt
      ff10b08 change a.txt
      4c0c8ce commit message
      ```

  - `git log -n` : n개만 보여줘 (최신부터인듯?)
  - `git log --graph` 뭔가... 노선도가 보임...
  - `git log -n --oneline`
   : n개만 짧게 보여줘

- *git 관리 끝내려면?* .git 폴더 없애기
  - `rm -r .git`
- git commit 만 쓰고 엔터치면 VI 에디터(태초에 이런 메모장이 있었다... 마우스 못 씀...)
  - I 누르면 insert모드 커밋 메세지 쓸 수 있음
    - 윗줄에는 header 제목
    - 이후로는 content 내용 여러줄 가능 << git log --oneline 으로 보면 안 나옴
  - esc 눌러서 인서트모드 해제
  - `:wq` >> 적었고 이제 나갈게
- git 명령어? 알고 싶으면
  - https://git-scm.com/doc
- git으로 이미 관리되고 있는 폴더 안에 있는 하위폴더에서는 `git init` 하지말기
- 실제 폴더에는 있지만 git에 올라가지 마(비밀번호 등)
  - `.gitignore` 파일 만들기
  - 메모장으로 파일 열고 안에 숨기고 싶은 파일(a.txt) 적기, 엔터로 구분
  - 커밋한 이후에 b.txt에 변경사항, 추가로 숨기고 싶어서 .gitignore에 적어도 무시불가.. 첨부터 무시해야됨
  - add, commit 하기 전에 `gitignore.io` 가서 python, windows, visualstudiocode 등 환경 선택해서 필요없는 애들 생성해서 전체 복사해서 .gitignore 파일에 넣어주기
  - 디렉토리 무시하고 싶으면 / 까지 입력
  - *.확장자 쓰면 해당 확장자 다 무시

# github

- url에 쓸때는 하이픈(-) 쓰자 << 링크 복사하면 밑줄이 생김.... 언더바는 안 보여....
- 기본 브랜치 이름 변경
  - profile >> setting >> repositories
- `git remote add xxx url주소` : 깃이랑 깃허브랑 연동, 이 주소(원격저장소)의 별명이 xxx임
- `git remote remove xxx` : 연동 끊기
- `git push {remote 이름} {branch 이름}`
  - `git push xxx main`
  - main을 안 써도 올라가는데 하위 브랜치가 있으면 얘기가 달라지는가....
- `git remote -v` 연동되어있는 원격저장소 별명&주소 보기
- `-u`
  - `--set-upstream` 의 줄임?
  - 처음에 push할때 `git push -u origin main` 으로 입력하면 다음부터는 `git push` 만 써도 됨
- git 하나에 github 레포 여러개 가능
- github 레포 하나에 git 여러개 불가능
## 다운로드
- `git clone (연동할 github 레포 url 주소)` 점 안 찍으면 하위폴더 만들면서 다운로드 
- `git clone url주소 .` 으로 맨 뒤에 점 찍어주면 그 폴더에 다운로드
- ls로 확인
- 나는 이게 최신인지 몰라... push한 쪽도 알고 github도 아는데 나만 몰라..
- 이미 연동되어있으면 `git pull`

## git conflict
- 이쁜 상황(3-way merge)
  - 1에는 a,b,c 깃허브에는 a,b,c 2에는 a,b,d 인 상황에서 2가 push 하면?
    - rejected 당하고 git pull 하라고 힌트줌
    - 휴 다행..
- 정신나간상황
  - 1,2 둘다 a를 건드려버린거임
  - git pull 하면 conflict 나오고 merging 상태가 됨
  - vscode에서 열기(code . 아니면 폴더 가서 우클릭 code로 열기) >> 뭐 어케 할건지 고르기 (안 해도 됨) >> add, commit, push
- 오늘의 교훈 : `git pull`을 일단 외치고 시작하자

## 마지막 희희
- handsout_NOTPUSH/ : clone, pull 만 하면됨
- handsout_MINE/ : ?
- live_NOTPUSH/ : clone, pull 만
-  gitlab과 github 아이디가 달라요... 해결 안 되면 걍 네이버로 깃허브 다시 만들기...ㅎㅎ...

# 주명령어
- `add`
- `commit`
- `push`
- `clone`
- `pull`
