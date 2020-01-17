> 2020.01.17 금

# GIT

형상관리 tool



### 기본 환경 설정

사용자의 이름, 이메일 기본 설정으로 등록

```
$ git config --global user.name "사용자 이름"
$ git config --global user.email "사용자 이메일"
```

설정 값 확인

```
$ git config --global --list
```

기본 설정 값 변경

```
$ vi ~/.gitconfig
```

### 원격 저장소와 연결

```
$ git init
$ git remote add origin 저장소주소
```

현재 등록된 원격저장소의 상세 정보 확인

```
$ git remote -v
```

#### 변경된 코드 확인하기

`$ git diff`

### git log 명령어의 다양한 옵션

`$ git log -u` : 모든 커밋 변경점에 대해 더 자세히 볼 수 있음

` $ git log -1` : 가장 최신 커밋 1개 출력

`$ git log --name-only` : 커밋과 해당 커밋이 수정한 파일 함께 출력

`$ git log --oneline` : commit id, 내용 한줄로 보기

### commit message 수정

`$ git commit --amend` : 최신 커밋 메세지 변경

### 코드 원복하기

- 반영한 특정 코드(변경점)를 제거한다.
- 변경을 취소한다.
- 반영한 커밋을 되돌린다.
- 반영한 커밋을 revert 시킨다.

`$ git revert commitID `

### 브랜치

`$ git branch` : 현재 작업중인 브랜치 확인

`$ git branch 브랜치명` : 새로운 브랜치 생성 

`$ git checkout 브랜치명` : 브랜치 이동

`$ git checkout -b 브랜치명` : 새로운 브랜치 생성과 동시에 이동

`$ git branch -d 브랜치명` : 브랜치 삭제

`$ git merge 브랜치명 ` : 브랜치 병합하기

#### merge 충돌 해결

- 직접 merge 하기 
  - merge한 파일 열어서 충돌난 부분 합치기
- mergetool 사용
  - `$ git mergetool` 
  - `vimdiff` 입력
    - `The merge tool bc is not available as 'bcompare'` 메세지 발생하면 `$ git config merge.tool vimdiff` 설정 후 재시도
  - 1. 개발자의 의도대로 수정후
    2. Conflict 기호 제거(<<<<<<, =====, >>>>>>)
    3. 수정 완료되면 저장 후 종료 ([Esc] + :wq)
    4. 나머지 3-wqy 창은 수정 없이 종료 ([Esc] + :q) 
    5. 병합이 제대로 되었는지 확인 후, commit 생성

### Git 태그

- Lightweight 태그 : 버전명과 같은 태그명만 남기는 태그
- Annotated 태그 : Git 데이터베이스에 태그를 만든 사람의 이름, 이메일, 태그 생성 날짜, 태그 메시지 등을 저장한 태그

#### 태그 생성하기

- Lightweight 태그 생성 : `$ git tag [태그명]`
- Annotated 태그 생성 : `$ git tag -a [태그명] -m [태그메시지]`
  - `git tag -a v1.0 -m "Implemented login feature"`

#### 특정 시점의 커밋 태그하기

1. 태깅하고자 하는 커밋의 ID 값 확인 `$ git log --oneline `
2. 커밋 ID 값을 인자로 태깅하기 : `$ git tag -a [태그명] [커밋ID] -m [태그메시지]`
   - `$ git tag -a v0.1 b4cae7c -m "fix issue number-1"`
   - `$ git log --oneline` 으로 태그 생성된거 확인
3. 태그 정보 확인하기 `$ git show v0.1`

