from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='deepseek-ai/DeepSeek-V4-Flash',
    provider='novita',
    temperature=0.8
)

model = ChatHuggingFace(
    llm=llm
)

class AdCopy(BaseModel):
    social_media_caption: str = Field(description='An engaging social media caption')
    ad_headline: str = Field(description='A short and catchy advertisement headline')
    call_to_action: str = Field(description='Motivating call to action')

parser = PydanticOutputParser(pydantic_object=AdCopy)

template = '''You are an expert advertising copywriter. You have been provided with:

product name = {product_name}
target audience = {target_audience}

Your task is to generate:
1. A social media caption
2. An ad headline
3. A call to action

Guidelines:
1. Social media caption should be captivating and participatory, and it should be within 150 characters
2. Ad headline should be simple, memorable, focusing on the value the customer will get, and it should be within 60 characters
3. CTA should be clear and rewarding, and it should be within 4 to 7 words
4. Adjust your tone according to the target audience.
5. Avoid overly generic marketing phrases.

The output must follow the specified formatting instructions:
format instructions = {format_instructions}'''

prompt = PromptTemplate.from_template(template=template,
                                      partial_variables={'format_instructions':parser.get_format_instructions()})

chain = prompt | model | parser

def generate_ad_content(product_name, target_audience):
    try:
        result = chain.invoke(input={'product_name': product_name, 'target_audience': target_audience})
        formatted_result = result.model_dump_json(indent=4)
        print(formatted_result)

        with open('sample_output.json', 'w', encoding='utf-8') as f:
            f.write(formatted_result)

    except Exception as e:
        print(f'The following error occured: {e}')

if __name__=='__main__':
    product_name = input('Enter product name: ')
    target_audience = input('Enter target audience: ')

    generate_ad_content(product_name, target_audience)