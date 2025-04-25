
import os
from openai import AzureOpenAI  
from azure.identity import DefaultAzureCredential, get_bearer_token_provider  
  
endpoint = os.getenv("ENDPOINT_URL", "https://fantu-m9vz17l7-eastus2.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o")
  
# Initialize Azure OpenAI client with Entra ID authentication  
cognitiveServicesResource = os.getenv('AZURE_COGNITIVE_SERVICES_RESOURCE', 'YOUR_COGNITIVE_SERVICES_RESOURCE')  
token_provider = get_bearer_token_provider(  
    DefaultAzureCredential(),  
    f'{cognitiveServicesResource}.default'  
)  
        
client = AzureOpenAI(  
    azure_endpoint=endpoint,  
    azure_ad_token_provider=token_provider,  
    api_version='2024-05-01-preview',  
)  
       
completion = client.chat.completions.create(  
    model=deployment,  
    messages=[
    {
        "role": "system",
        "content": "você e um especialista em sna que ira me ajudar com duvidas sobre o tema ."
    },
    {
        "role": "user",
        "content": "o que é python"
    },
    {
        "role": "assistant",
        "content": "Python é uma linguagem de programação de propósito geral, orientada a objetos e com tipagem dinâmica, que permite expressar e materializar ideias com agilidade [doc5]. Ela é utilizada por uma ampla variedade de profissionais, como desenvolvedores de websites, cientistas, matemáticos, músicos e jornalistas, formando uma comunidade diversificada, acolhedora e produtiva [doc5].\n\nAlém disso, Python refere-se tanto à linguagem de programação quanto ao software interpretador que lê o código-fonte e executa suas instruções. O interpretador Python é gratuito e pode ser baixado do site oficial, com versões para Linux, OS X e Windows [doc1][doc5]. \n\nO nome Python foi inspirado no grupo de comédia britânico Monty Python, e não na cobra. Referências ao Monty Python e a serpentes são comuns em tutoriais e documentações da linguagem [doc1][doc2]."
    }
],  
    past_messages=10,
    max_tokens=800,  
    temperature=0.7,  
    top_p=0.95,  
    frequency_penalty=0,  
    presence_penalty=0,  
    stop=None,  
    extra_body={  
        "data_sources": [  
            {  
                "type": "azure_search",  
                "parameters": {  
                    "endpoint": os.environ["AZURE_AI_SEARCH_ENDPOINT"],  
                    "index_name": os.environ["AZURE_AI_SEARCH_INDEX"],  
                    "authentication": {  
                        "type": "system_assigned_managed_identity"  
                    }  
                }  
            }  
        ]  
    }  
)

print(completion.model_dump_json(indent=2))  