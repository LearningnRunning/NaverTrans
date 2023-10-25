import unittest
from navertrans import navertrans

class TranslatorTests(unittest.TestCase):
    def test_basic_check(self):
        # Test translation from Korean to English
        result = navertrans.translate(u'안녕하세요. 저는 한국인 입니다. 이 문장은 한글로 작성되었습니다.', src_lan='ko', tar_lan='en')
        
        # Verify that the result is a string
        self.assertIsInstance(result, str)

        # Verify that the translation is not empty
        self.assertTrue(result.strip())

if __name__ == '__main__':
    unittest.main()
