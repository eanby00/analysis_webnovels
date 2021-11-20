# 합쳐진 csv 파일을 생성하기 위한 테이블 생성

# version 별로 정리하여 maria_dev/analysis_webnovels/preprocessing/novel_list or novel_unit_list에 csv로 저장
- 기존의 크롤링 오류 + 기존의 데이터는 데이터가 csv로 분리되어 저장되어 있어 excel과 같은 외부 프로그램으로 한 번에 확인하기 어려운 문제가 있음
- 형식: novel_list_[version].csv, novel_unit_list_[version].csv


# 작동 순서
- version1의 경우: source와 ending이 포함되지 않음
    - solve_error/make_table_solve_error를 hive에서 실행: 문제가 되는 version1의 novel_unit_list를 폴더별로 가져와서 테이블을 분리
    - solve_error/make_table_with_cols를 hive에서 실행: 각 테이블에 맞는 source와 ending을 추가한 select문을 기반으로 테이블 생성 후 해당 열의 이름을 source와 ending으로 변경
    - solve_error/save_csv의 결과물을 hive 기능을 이용해 csv로 다운 후 maria_dev/analysis_webnovels/preprocessing/novel_unit_list에 저장
    - make_table 실행 후 select * from novel_list where version = 1;의 결과물을 csv로 다운 후 preprocessing/novel_list에 저장

- 그 이외의 경우: version에 따라 where 변경
    - make_table 실행
    - select * from novel_list where version = 2...;
    - select * from novel_unit_list where version = 2...;
    - 각 결과물을 preprocessing/novel_list or novel_unit_list 아래에 저장
    