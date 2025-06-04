import requests
import json

def emotion_detector( text_to_analyse ):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL do serviço de análise de sentimentos
    myobj = { "raw_document": { "text": text_to_analyse } }  # Cria um dicionário com o texto a ser analisado
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Define os cabeçalhos necessários para a requisição da API
    response = requests.post(url, json = myobj, headers=header)  # Envia uma requisição POST para a API com o texto e os cabeçalhos
    
    if( response.status_code != 200 ):
        return None

    formatted_response = json.loads( response.text )

    emotions = formatted_response[ 'emotionPredictions'] [ 0 ] ['emotion']
    # Encontrar a emoção dominante
    dominant_emotion = max(emotions, key=emotions.get)

    # Adicionar ao dicionário
    emotions["dominant_emotion"] = dominant_emotion

    return json.dumps(emotions, indent=4)  # Retorna o texto da resposta da API