# 감소율 기준을 넘는 데이터와 넘지 않는 데이터를 비교

# 결과
- count_comment, 댓글 횟수와 구매 감소율과는 연관이 있다고 판단됨
    - 댓글 횟수가 많을수록 구매 감소율이 낮을 것으로 예상

- letter, 글자 수와 구매 감소율과는 연관이 없다고 판단됨

- purchase, 구매량 혹은 조회량은 구매 감소율에 연관되어 있음
    - 구매량이 높을 수록 구매 감소율은 감소할 것
    - 구매 감소율은 구매량에 의해 정의됨으로 당연함

- rate_change_purchase는 구매 감소율의 기준이 되는 값으로 의미 X

- rate_change_purchase_five, 즉 5화 전의 구매량과 현재 구매량의 변화율은 구매 감소율과 연관되어 있다고 판단됨
    - 즉, 변화율이 양의 방향으로 커진다면 구매 감소율은 감소될 것으로 예측
    - 구매량이 증가하는 추세였으니 감소율은 떨어짐

- rate_change_purchase_five_avg, 즉 5화 전부터 구매량의 변화율 평균은 구매 감소율과 연관되지 않음 

- rate_change_recommendation_five, 즉 5화전의 추천수와 현재의 추천수의 변화율은 구매 감소율과 연관되어 있음
    - 변화율이 양의 방향으로 커진다면 구매 감소율은 감소될 것
    - 추천수가 증가하는 추세였으면 감소율은 떨어짐

- rate_change_recommendation_five_avg는 구매 감소율에 연관되지 않음

- recommendation, 추천 수는 구매 감소율에 연관을 미침
    - 추천 수가 많다면 구매 감소율은 감소할 것이라 추측할 수 있음

# 정리
- 구매 감소율과 연관된 attribute는 count_comment, purchase, rate_change_purchase_five, rate_change_recommendation_five, recommendation임을 확인할 수 있음