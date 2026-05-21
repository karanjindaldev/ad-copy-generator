from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='openai/gpt-oss-20b',
    provider='novita',
    temperature=0
)

model = ChatHuggingFace(
    llm=llm
)

class AdContent(BaseModel):
    social_media_caption: str = Field(description='An engaging caption for the social media posts promoting the product')
    ad_headline: str = Field(description='A short and catchy advertisement headline for the product')
    call_to_action: str = Field(description='Motivating call to action')

parser = PydanticOutputParser(pydantic_object=AdContent)

template = '''You are a marketing expert.
Based on the provided product name and target audience,
generate a social media caption, ad headline, and Call to action,
in the specified format.        
product name = {product_name}
target audience = {target_audience}
format instructions = {format_instructions}'''

prompt = PromptTemplate.from_template(template=template,
                                      partial_variables={'format_instructions':parser.get_format_instructions()})

chain = prompt | model | parser

product_name = input('Enter product name: ')
target_audience = input('Enter target audience: ')

try:
    result = chain.invoke(input={'product_name': product_name, 'target_audience': target_audience})

    print(result.model_dump_json())

    with open('sample_output.json', 'w', encoding='utf-8') as f:
        f.write(result.model_dump_json())

except Exception as e:
    print(f'The following error occured: {e}')