import base64
import os
import streamlit as st

from gemini import Gemini
import utils
import braille


def create_download_link(text: str, filename: str) -> None:
    """
    Cria um link de download para um texto fornecido, permitindo que o usuário baixe o texto como um arquivo.

    Esta função converte uma string em bytes UTF-8, codifica esses bytes em base64 e, então, cria um botão de download
    utilizando HTML e CSS que, quando clicado, baixa o arquivo com o conteúdo codificado. O link de download é embutido
    em uma página HTML que é renderizada na interface do usuário, tipicamente em um aplicativo web usando a biblioteca
    Streamlit.

    :param text: O texto que será convertido em arquivo para download. Este texto é codificado em UTF-8 e
                    convertido para base64 para o link de download.
    :param filename:  O nome do arquivo que será usado no download. Este nome é usado no atributo 'download' do
                        link gerado, especificando o nome do arquivo que será salvo no dispositivo do usuário.

    :return: Não retorna nenhum valor
    """
    text_bytes = text.encode('utf-8')

    b64 = base64.b64encode(text_bytes)

    html = """
        <style>
        .custom-button {
           background-color: #008080;
           color: white;
           padding: 14px 20px;
           margin: 8px 0;
           border: none;
           cursor: pointer;
           width: 30s%;
        }
        .custom-button:hover {
           opacity: 0.8;
        }
        </style>
        """
    html += (f'<a href="data:text/plain;base64,{b64.decode()}" download="{filename}">'
             f'<button class="custom-button">Baixar descrição</button></a>')
    st.markdown(html, unsafe_allow_html=True)


if __name__ == '__main__':
    gemini = Gemini()

    st.header("Olá, vou te ajudar a descrever imagens!")

    uploaded_files: list = st.file_uploader(
        "Insira suas imagens", type=['png', 'jpg'], accept_multiple_files=True, key=str, disabled=False,
        label_visibility="visible"
    )

    if uploaded_files:

        for num, uploaded_file in enumerate(uploaded_files, start=1):

            image_name: str = uploaded_file.name
            download_name, _ = os.path.splitext(image_name)
            mime_type: str = uploaded_file.type

            st.subheader(f"{num}) Processando o arquivo {image_name}", divider='rainbow')

            data_bytes: bytes = uploaded_file.read()
            st.image(data_bytes, width=300)  # Exibe a imagem
            image_string: str = utils.encode_image_to_base64(image_bytes=data_bytes)

            description: str = gemini.image_description(image=image_string, mime_type=mime_type)
            st.write("**Descrição original**")
            st.write(description)
            create_download_link(description, f"{download_name}_en.txt")

            translated_description: str = gemini.text_translation_portuguese(description)
            st.write("**Tradução para pt-br**")
            st.write(translated_description)
            create_download_link(translated_description, f"{download_name}_pt-br.txt")

            description_braille: str = braille.text_to_braille(translated_description)
            st.write("**Texto do pt-br para Braille**")
            st.write(description_braille)
            create_download_link(description_braille, f"{download_name}_braille.txt")

            st.subheader("", divider='rainbow')

