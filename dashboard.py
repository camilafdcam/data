import pandas as pd
import streamlit as st
from streamlit_sortables import sort_items
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Controle interno",
    page_icon="bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded")



st.sidebar.image("./images/logo.png", width=300)  # Certifique-se de que o caminho da logo está correto


with st.sidebar:
    menu = option_menu(
        menu_title="Menu",  # Título do menu
        options=["Home", "INDICADORES", "EQUIPAMENTOS", "BACKLOG"],  # Opções do menu
        icons=["house", "journal-check", "truck-flatbed", "card-checklist"],  # Ícones das opções
        menu_icon="cast",  # Ícone principal do menu
        default_index=0,  # Primeira opção selecionada por padrão
        orientation="vertical",  # Menu vertical
        styles={  # Customização do estilo do menu
            "container": {"padding": "5px", "background-color": "#777777"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#5b5b5b"},
            "nav-link-selected": {"background-color": "#5972F1"},
        }
    )
    








 
if menu == 'Home':
    
    
    st.markdown(
        """
        <div style="text-align: center;">
            <h2>CONTROLE INTERNO</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
        # Configurações da página

    # Retângulos superiores para indicadores
    html_code = """
    <style>
    /* Container principal para os indicadores */
    .indicadores-container {
        display: flex;
        justify-content: space-around; /* Espaçamento uniforme */
        align-items: center;
        flex-wrap: wrap; /* Permite que os elementos quebrem linha */
        gap: 5px; /* Espaçamento entre os retângulos */
        padding: 20px;
        border-radius: 10px;
    }

    /* Estilo para cada retângulo */
    .indicador-box {
        background: linear-gradient(135deg, #686767, #686767); /* Gradiente de cor */
        color: white; /* Cor do texto */
        text-align: center;
        padding: 20px;
        width: 160px; /* Largura fixa */
        height: 90px; /* Altura fixa */
        border-radius: 3px; /* Bordas arredondadas */
        box-shadow: 0 4px 8px rgb(0, 0, 0); /* Sombra */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        font-family: Arial, sans-serif;
        font-size: 18px;
        font-weight: bold;
        transition: transform 0.3s ease-in-out; /* Animação ao passar o mouse */
    }

    /* Efeito hover nos retângulos */
    .indicador-box:hover {
        transform: scale(1.05); /* Leve aumento no tamanho */
        cursor: pointer; /* Muda o cursor */
    }
    </style>

    <!-- Estrutura dos Retângulos -->
    <div class="indicadores-container">
        <div class="indicador-box">
            Finalizada<br>
            <span style="font-size: 20px;">15</span>
        </div>
        <div class="indicador-box">
            Em Andamento<br>
            <span style="font-size: 20px;">7</span>
        </div>
        <div class="indicador-box">
            Aberta<br>
            <span style="font-size: 20px;">5</span>
        </div>
        <div class="indicador-box">
            Cancelada<br>
            <span style="font-size: 20px;">30%</span>
        </div> 
        <div class="indicador-box">
            Indicador 4<br>
            <span style="font-size: 20px;">30%</span>
        </div>
        <div class="indicador-box">
            Indicador 4<br>
            <span style="font-size: 20px;">30%</span>
        </div>

    </div>
    """

    # Inserir HTML no Streamlit
    st.markdown(html_code, unsafe_allow_html=True)

   

    import pandas as pd
    import plotly.express as px
    import streamlit as st

    # Leitura do arquivo Excel
    df_geral = pd.read_excel(
        io='data.xlsx',  # endereço do arquivo
        index_col=2,  # referência inicial para contagem de coluna
        dtype=str,  # tipo de leitura de dados str
        engine='openpyxl',  # biblioteca para leitura Excel
        sheet_name='Planilha1',
        usecols='A:W',  # delimitação de colunas
        nrows=4400  # delimitação de linhas
    )

    # Filtrando as colunas que precisamos
    df_filtered = df_geral[['EQUIPAMENTO', 'STATUS']].dropna()

    # Criando o multiselect para selecionar os equipamentos
    equipamentos_unicos = df_filtered['EQUIPAMENTO'].unique()
    equipamentos_selecionados = st.multiselect(
        'Selecione os equipamentos:', 
        options=equipamentos_unicos, 
        default=equipamentos_unicos.tolist()  # Definir todos como padrão
    )

    # Filtrando os dados com base nos equipamentos selecionados
    df_filtrado_equipamentos = df_filtered[df_filtered['EQUIPAMENTO'].isin(equipamentos_selecionados)]

    # Contagem dos status para os equipamentos selecionados
    contagem_status = df_filtrado_equipamentos.groupby('STATUS').size().reset_index(name='Count')

    # Gráfico de barras usando Plotly
    fig_bar = px.bar(contagem_status, 
                    x='STATUS', 
                    y='Count', 
                    title=f'Distribuição de Status para Equipamentos Selecionados', 
                    labels={'STATUS': 'Tipo de Status', 'Count': 'Quantidade'},
                    color='STATUS', 
                    color_discrete_sequence=['#B11515', '#4473C5', '#9DC3E7', 'grey']
                    )

    # Adicionar rótulos diretamente no topo das barras
    fig_bar.update_traces(
        text=contagem_status['Count'].astype(str),  # Passar a contagem diretamente nos rótulos
        textposition='outside',  # Coloca o texto fora da barra
        texttemplate='%{text}',   # Exibe o valor de contagem no rótulo
        showlegend=True
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig_bar)

    
    # Gráfico de pizza

    # Exibir os gráficos no Streamlit
    #st.plotly_chart(fig_bar)
    #st.plotly_chart(fig_pie)
    
    
   # Ler dados do Excel
df_geral = pd.read_excel(
    io='data.xlsx',  # endereço do arquivo
    index_col=2,  # Referência inicial para contagem de coluna
    dtype=str,  # Tipo de leitura de dados como string
    engine='openpyxl',  # Biblioteca para leitura Excel
    sheet_name='Planilha1',
    usecols='A:W',  # Delimitação de colunas
    nrows=4400  # Delimitação de linhas
)

# Filtrar dados e contar tipos de manutenção
df_filtered = df_geral[['TIPO DE MANUTENÇÃO']].dropna()  # Remove as linhas com valores ausentes
count_adequacao = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Adequação de Segurança'].shape[0]
count_corretiva = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Corretiva'].shape[0]
count_fabricacao = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Fabricação'].shape[0]
count_melhoria = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Melhoria'].shape[0]
count_pintura = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Pintura'].shape[0]
count_preventiva = df_filtered[df_filtered['TIPO DE MANUTENÇÃO'] == 'Preventiva'].shape[0]

# Criar um DataFrame para os gráficos
status_data = {
    'TIPO DE MANUTENÇÃO': ['Adequação de Segurança', 'Corretiva', 'Fabricação', 'Melhoria', 'Pintura', 'Preventiva'],
    'Count': [count_adequacao, count_corretiva, count_fabricacao, count_melhoria, count_pintura, count_preventiva]
}
df_status = pd.DataFrame(status_data)

# Gráfico de barras
fig_bar = px.bar(
    df_status,
    x='TIPO DE MANUTENÇÃO',
    y='Count',
    title='Distribuição de Tipos de Manutenção',
    labels={'TIPO DE MANUTENÇÃO': 'Tipo de Manutenção', 'Count': 'Quantidade'},
    color='TIPO DE MANUTENÇÃO',
    color_discrete_sequence= ['#B11515','#4473C5','#9DC3E7','grey', '#E1E6E3','#800000'] #cores personalizadas 
)

# Adicionar rótulos no topo das barras
fig_bar.update_traces(
    text=df_status['Count'],  # Rótulo correto para cada barra
    textposition='outside',  # Coloca o texto fora da barra
    texttemplate='%{text}',  # Exibe o valor de contagem no rótulo
    showlegend=False  # Remove legenda desnecessária
)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig_bar)

#if menu == 'Requisições':
    
    #df_req = pd.read_excel(
    #io = 'dados.xlsx', # endereço do arquivo
    #index_col=0, # referência inicial para contagem de coluna 
    #dtype= str, # tipo de leitura de dados str
    #engine='openpyxl', # biblioteca para leitura excel
    #sheet_name='REQUISIÇÃO',
    #usecols='A:F', # delimitação de colunas
    #nrows=4400 # delimitação de linhas
    #)
    
    #df_req

# Verifica se a planta selecionada é "Carajás"
if menu == 'DISPONIBILIDADE':
        
    # Leitura do arquivo Excel
    df_log = pd.read_excel(
        io='data.xlsx',  # endereço do arquivo
        index_col=0,  # referência inicial para contagem de coluna 
        dtype=str,  # tipo de leitura de dados str
        engine='openpyxl',  # biblioteca para leitura excel
        sheet_name='DISPONIBILIDADE',  # aba a ser lida
        usecols='A:D',  # delimitação de colunas
        nrows=4400  # delimitação de linhas
    )

   

