import google.generativeai as genai

from config import GENERATION_CONFIG, SAFETY_SETTINGS, GOOGLE_API_KEY


class Gemini:
    def __init__(self, model_name="gemini-1.5-pro-latest"):

        self.model_name = model_name
        genai.configure(api_key=GOOGLE_API_KEY)

    def image_description(self, image: str, mime_type: str) -> str:
        """
        Este método utiliza um modelo de IA para gerar descrições detalhadas e acessíveis de uma imagem, especialmente
        projetadas para indivíduos com deficiência visual. O método se concentra em identificar e descrever cada objeto
        na imagem com alta precisão, enfatizando formas, cores e a disposição espacial dos elementos.

        :param image: Os dados da imagem em bytes que precisam ser descritos. Deve corresponder ao tipo MIME
        especificado.
        :param mime_type: O tipo MIME da imagem (por exemplo, 'image/jpeg', 'image/png'). Isso ajuda o modelo
                         a entender o formato dos dados da imagem recebidos.

        :return: Uma string de texto contendo a descrição detalhada da imagem. Esta descrição visa fornecer um
             entendimento visual por meio de palavras, tornando o conteúdo da imagem acessível para usuários com
             deficiência visual.
        """

        prompt: str = """ 
           Create a detailed and accessible description of an image for visually impaired individuals, identifying and 
           describing each object present in minute detail. Emphasize the shapes, colors, and spatial arrangement of the 
           elements in the scene to provide a visual understanding through words. Descriptions should be clear and 
           precise to allow the user to form a vivid and complete mental image of what is being described.
        """

        model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS,
            system_instruction=prompt
        )

        cookie_picture: list = [{
            'mime_type': mime_type,
            'data': image
        }]

        response = model.generate_content(cookie_picture)
        return response.text

    def text_translation_portuguese(self, text: str) -> str:
        """
        Traduz um texto do idioma original para o português do Brasil utilizando um modelo de IA avançado.

        :param text: O texto a ser traduzido para o português. Esse texto pode estar em qualquer idioma que o modelo
        de IA suporte e seja capaz de reconhecer e traduzir.

        :return: O texto traduzido para o português do Brasil.
        """

        model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=GENERATION_CONFIG,
            safety_settings=SAFETY_SETTINGS
        )

        response = model.generate_content(f"Translate the text into Brazilian Portuguese: {text}")
        return response.text
