from EmotionDetection import emotion_detector
import unittest
import json

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        # Caso de teste para sentimento positivo
        result_1 = json.loads( emotion_detector('I am glad this happened') )
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Caso de teste para sentimento negativo
        result_2 = json.loads( emotion_detector('I am really mad about this') )
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Caso de teste para sentimento neutro
        result_3 = json.loads( emotion_detector('I feel disgusted just hearing about this') )
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        result_4 = json.loads( emotion_detector('I am so sad about this') )
        self.assertEqual(result_4['dominant_emotion'], 'sadness')

        result_5 = json.loads( emotion_detector('I am really afraid that this will happen') )
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()