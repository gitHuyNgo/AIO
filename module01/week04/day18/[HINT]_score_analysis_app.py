import io
import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
from PIL import Image  

# Tiêu đề ứng dụng
st.title("Phân tích dữ liệu điểm số học sinh")

# Upload file
uploaded_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')", type=["xlsx"])

# Hàm tính điểm trung bình
def calculate_average(scores):
    """ Hàm tính điểm trung bình """
    ### Your code here

# Hàm phân loại điểm số
def percentage_distribution(scores):
    """ Hàm phân loại điểm số """
    bins = {'90-100': 0, '80-89': 0, '70-79': 0, '60-69': 0, '<60': 0}
    ### Your code here
    return bins

# Khi có file
def main():
    """ Hàm xử lý tải file lên và tính điểm """
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        scores = df["Điểm số"].dropna().astype(float).tolist()
    
        if scores:
            st.write("Tổng số học sinh:", len(scores), "Điểm trung bình:", round(calculate_average(scores), 2))
            # Phân loại điểm
            dist = percentage_distribution(scores)
            labels = list(dist.keys())
            values = list(dist.values())
        
            fig, ax = plt.subplots(figsize=(1, 1))  
            ax.pie(
                values, 
                labels=labels, 
                autopct='%1.1f%%', 
                textprops={'fontsize': 3.5}, 
            )
            ax.axis("equal")
            plt.tight_layout(pad=0.1) 
            
            buf = io.BytesIO()
            fig.savefig(buf, format='png', dpi=300) 
            buf.seek(0) 
            st.markdown("Biểu đồ phân bố điểm số.")  
            img = Image.open(buf) 
    
            col1, col2, col3 = st.columns([1, 2, 1])  # Tạo ba cột, cột giữa rộng hơn
            with col2:
                st.image(img, width=300)  # Hiển thị biểu đồ ở cột giữa
                st.markdown("Biểu đồ phân bố điểm số.")
if __name__ == "__main__":
    main()