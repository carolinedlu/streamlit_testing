import streamlit as st

def gera_tabela(df, label):
    df.index = [" "] * len(df)


    df['na_terra'] = " "
    df['na_cesta'] = " "
    df['  '] =  " "
    df.rename({'produto':label,'na_terra': '   ', 'na_cesta':' '}, axis='columns', inplace=True)
    st.table(df[[label, '   ', '  ',' ']])

 if st.checkbox(f"Na cesta em {data}",value=False):
    st.image("src/na_cesta.jpg",use_column_width=True)
    na_cesta = dados_csa.query("na_cesta == 'x'")
    gera_tabela(na_cesta, f'--provável cesta em {data} (sujeito à adições)--')
    

st.write("-------------------------------------------")
