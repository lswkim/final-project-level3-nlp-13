from typing import *
from transformers import AutoModelForSequenceClassification, AutoTokenizer

def get_model(
        model_name: str,
        model_type: str = 'huggingface',
    ):
    '''
        arguments
            model_name : str
                모델의 이름을 반환 허깅페이스의 경우 pretrained 모델의 이름
                커스텀 모델의 경우 클래스 이름
            model_type : str
                huggingface or custom

        return
            torch.nn.module

        summary
            모델의 이름과 타입에 따라 학습 및 추론에 사용할 모델 반환
    '''

    if model_type == 'huggingface':
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
    elif model_type == 'custom':
        print(model_name)

    return model

def get_tokenizer(
        tokenizer_name: str,
        tokenizer_type: str = 'huggingface',
    ):
    '''
        arguments
            tokenizer_name : str
                토크나이저의 이름을 반환 허깅페이스의 경우 pretrained 모델의 이름
                커스텀 토크나이저의 경우 클래스 이름
            tokenizer_type : str
                huggingface or custom

        return
            AutoTokenizer

        summary
            토크나이저의 이름과 타입에 따라 학습 및 추론에 사용할 모델 반환
    '''

    if tokenizer_type == 'huggingface':
        tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    elif tokenizer_type == 'custom':
        print(tokenizer_name)

    return tokenizer

def get_optimizer(
        optimizer_name:str
    ):
    '''
        arguments
            optimizer_name : str
                학습에 사용할 옵티마이저 이름

        return
            Optimizer

        summary
            옵티마이저 반환
    '''
    print('아직 미사용')