import streamlit as st
from streamlit_dragboard import Dragboard

# Configuração da página
st.set_page_config(page_title="Kanban Board", layout="wide")

# Estado inicial das colunas do Kanban
if "kanban_data" not in st.session_state:
    st.session_state.kanban_data = {
        "To Do": ["Tarefa 1", "Tarefa 2"],
        "In Progress": ["Tarefa 3"],
        "Done": ["Tarefa 4"],
    }

# Criando colunas
columns = list(st.session_state.kanban_data.keys())

# Layout do Kanban
st.title("📌 Kanban Board")
st.write("Arraste os cartões entre as colunas!")

# Criando colunas no Streamlit
cols = st.columns(len(columns))

# Criando o Dragboard (área arrastável) para cada coluna
for i, col_name in enumerate(columns):
    with cols[i]:
        st.subheader(col_name)

        # Criando o Dragboard para a coluna atual
        dragboard = Dragboard(col_name)
        for item in st.session_state.kanban_data[col_name]:
            dragboard.add_block(item)

        # Salvando nova posição dos itens ao mover
        result = dragboard.display()
        st.session_state.kanban_data[col_name] = [block["text"] for block in result]

# Adicionando novas tarefas
st.sidebar.header("➕ Adicionar Tarefa")
new_task = st.sidebar.text_input("Nome da Tarefa")
col_select = st.sidebar.selectbox("Coluna", columns)

if st.sidebar.button("Adicionar"):
    if new_task:
        st.session_state.kanban_data[col_select].append(new_task)
        st.rerun()

