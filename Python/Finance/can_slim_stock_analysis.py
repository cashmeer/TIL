# let's make CAN SLIM Stock Analysis William O'Neil
"""
C (Current Earnings): 현재 주당 분기 순이익
분기 순이익 증가율이 25% 이상인 기업에 투자합니다.
A (Annual Earnings) : 연간 순이익
연간 순이익 증가율이 25% 이상, 3년 순이익 증가율이 안정적인 기업, 자기자본이익률이 17% 이상인 기업에 투자합니다.
N (New) : 신제품, 경영혁신, 신고가
신제품, 신경영, 신고가를 형성하는 기업에 투자합니다.
S (Supply and Demand) : 수요와 공급
유동주식수가 적은 종목을 공략합니다. (많은 종목이 아닙니다!)
유동주식수가 적은 종목이 향후 큰 시세를 준다고 믿고 있기 때문이죠.
L (Leader or Laggard) : 주도주와 소외주
시장 주도주를 사고 소외주를 피합니다.
I (Institutional Sponsorship) : 기관 관심주
기관이 관심을 맞는 종목에 투자를 합니다.
M (Market Direction) : 시장의 방향
보조지표나 시장속보 등 전문가의 견해를 의지하는 것 보다는 매일 종합주가지수의 움직임을 체크하며 자신만의 노하우로 시장 움직임을 파악하는 것이 중요합니다.
"""

EPS = 1044