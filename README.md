# DRF-session

## DB 설계서

### 1. Memo  
  - title : 노래 제목, char형(max_length=512)
  - singer : 가수 이름 char형(max_length=256)
  - date : 메모 작성 날짜, date형, 자동 등록
  - likes : 좋아요 수, 양수형(positiveinteger)
  - content : text 형, 메모 내용 입력
  - genre : 미리 정해두었던 genre_choice 목록에서 선택 가능
    - genre_choice : 발라드, 댄스, 록, ost, 인디, pop, 클래식, 재즈, kpop, ccm, 힙합, 블루스
  - author : 고유값
  - nickname : 작성자의 닉네임 char형
  - id : 메모장의 번호, integer형

### 2. Comment
  - comment : text형, 댓글 내용 입력
  - date : 댓글 작성 날자, datetime형, 자동 등록
  - memo : fk, 메모 본글, 고유값
  - nickname : 작성자의 닉네임 char형




## SERIALIZER

### 1. MemoSerializer
  - 메모 작성 serializer
  - fields = ['nickname', 'title', singer', 'date', 'likes', 'content', 'genre', 'memo_id']


### 2. CommentSerializer
  - 댓글 작성 serializer
  - fields = ['comment', 'date', 'memo', 'nickname']



## APIView
- viewset 사용
  ### 1. MemoViewSet
    - create 기능, 포스트 작성
  
  ### 2. CommentViewSet
    - 댓글 작성 기능




## URL
  - memos/ : 메모 포스트 작성 및 메모글 전체 조회
  - memos/int:pk : 작성한 메모 하나씩 조회, 수정, 삭제


