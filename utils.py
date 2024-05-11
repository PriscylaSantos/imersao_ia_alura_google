import base64


def encode_image_to_base64(image_bytes: bytes) -> str:
    """
    Codifica os bytes de uma imagem em uma string Base64.

    Esta função aceita um objeto bytes que representa uma imagem, codifica este objeto bytes em Base64 e então
    decodifica o resultado codificado para uma string em UTF-8.

    :param image_bytes: Os bytes da imagem a serem codificados. Deve ser do tipo bytes.

    :return: Uma string representando a imagem codificada em Base64. Retorna uma string UTF-8.
    """
    imagem_codificada: bytes = base64.b64encode(image_bytes)
    imagem_codificada_str: str = imagem_codificada.decode('utf-8')
    return imagem_codificada_str
