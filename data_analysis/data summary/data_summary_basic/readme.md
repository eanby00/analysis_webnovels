### data_summary_novel_list.hql의 결과
#### 분석에 적합한 attribute: avg_serial_week, favorite, recommendation
- 이외의 attribute의 경우에는 데이터의 최대값보다 최소값, 평균이 높게 나오거나 이유를 알 수 없는 음수로 표현되어 분석 대상에서 제외됨
#### 해당 attribute들을 이용하는 것은 불가능한 것으로 판단됨
- avg_serial_week: 대다수의 데이터가 해당 데이터에 대해 값이 존재하지 않음
- favorite: 가장 최근 선호 인원을 기록하기 때문에 조회, 판매량이 떨어지는 지점에서의 선호 인원을 제대로 반영하지 못함
- recommendation: 가장 최근 추천수를 기록하기 때문에 조회, 판매량이 떨어지는 지점에서의 추천수를 제대로 반영하지 못함

### data_summary_novel_unit_list.hql의 결과
#### 모든 attribute가 비교적 정상적인 값을 가지고 있음
#### letter의 경우 모든 데이터의 평균값이 약 12쪽으로 일정함
#### rate_change_purchase, rate_change_purchase_five_avg,rate_change_recommendation_five_avg의 경우 모든 데이터의 평균값이 약 0으로 일정함

### data_summary_check_standard.hql
#### 기준 설정을 위한 hql 코드
#### 반복문에 대해 알지 못해 0 ~ -0.95까지 일일이 테스팅하기 때문에 양이 많아 따로 분리함
#### 결과 기준을 10%로 결정함, 10%일 때 한 버전에서 약 60000개의 데이터가 걸려 충분히 많은 양의 데이터를 줄였다고 판단함