import streamlit as st
import numpy as np

st.title("Калькулятор расчёта сделок на баскетбол")
age_columns = st.columns(2)
koef_1 = age_columns[0].slider("Коэффициент 1 четверти", min_value=1.01, max_value=3., step=0.01)
b_1 = age_columns[1].number_input("Первая ставка", value=35)
win_money = np.round(b_1 * (koef_1 - 1), 2)
st.write(f"Выигрыш в первой четверти: **{win_money}**")

age_columns_2 = st.columns(2)
koef_2 = age_columns_2[0].slider("Коэффициент 2 четверти", min_value=1.01, max_value=3., step=0.01)
b_2 = np.round((win_money + b_1) / (koef_2 - 1), 2)
age_columns_2[1].write(f"Размер ставки 2 четверть: **{b_2}**")

age_columns_3 = st.columns(2)
koef_3 = age_columns_3[0].slider("Коэффициент 3 четверти", min_value=1.01, max_value=3., step=0.01)
b_3 = np.round((win_money + b_2 + b_1) / (koef_3 - 1), 2)
age_columns_3[1].write(f"Размер ставки 3 четверть: **{b_3}**")

age_columns_4 = st.columns(2)
koef_4 = age_columns_4[0].slider("Коэффициент 4 четверти", min_value=1.01, max_value=3., step=0.01)
b_4 = np.round((win_money + b_3 + b_2 + b_1) / (koef_4 - 1), 2)
age_columns_4[1].write(f"Размер ставки 4 четверть: **{b_4}**")