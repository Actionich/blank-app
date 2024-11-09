import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="상세페이지 예시", layout="centered")

# 히어로 섹션
st.image("product-image.jpg", use_column_width=True, caption="제품 이미지")
st.markdown("<h1 style='text-align: center; color: #333;'>더 나은 삶을 위한 완벽한 선택</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>고객의 편안함을 위해 디자인된 혁신적인 기술</p>", unsafe_allow_html=True)
st.markdown("<ul style='text-align: center; list-style-type: none; padding: 0;'>"
            "<li>빠른 충전</li><li>경량 디자인</li><li>긴 배터리 수명</li></ul>", unsafe_allow_html=True)
if st.button("지금 구매하기"):
    st.write("구매하기 버튼이 클릭되었습니다.")

# 제품 상세 설명 및 혜택
st.markdown("---")
st.header("제품 설명")
st.write("여기에서 제품의 구체적인 사양과 혜택에 대해 설명합니다.")
st.image(["feature1.jpg", "feature2.jpg"], width=150, caption=["경량 설계", "무소음 작동"])

# 신뢰 요소
st.markdown("---")
st.header("고객 리뷰")
st.write("★★★★★ 4.8/5점")
st.markdown("<blockquote style='font-style: italic;'>\"제품 품질이 매우 뛰어납니다!\" - 고객 A</blockquote>", unsafe_allow_html=True)
st.write("30일 무료 반품 보장, 1년 보증 서비스 제공")

# 추가 정보
st.markdown("---")
st.header("추가 정보")
st.write("무료 배송 제공, 30일 내 반품 가능")
st.subheader("자주 묻는 질문(FAQ)")
st.write("**충전 시간은 얼마나 걸리나요?** 약 2시간 소요됩니다.")

# 마지막 CTA
st.markdown("---")
st.markdown("<div style='background-color: #ff5a5f; padding: 2em; text-align: center;'>"
            "<p style='color: #fff; font-size: 1.2em;'>지금 구매 시 특별 할인 제공</p></div>", unsafe_allow_html=True)
if st.button("장바구니에 담기"):
    st.write("장바구니에 담기 버튼이 클릭되었습니다.")
