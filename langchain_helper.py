from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Load API key from .env file
load_dotenv()
api_token = os.getenv("GOOGLE_API_KEY")  # Ensure this is set in your .env file

# Initialize Gemini Model (Fixed model name)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",  # Fixed incorrect model name
    google_api_key=api_token,
    temperature=0.7
)


#defining function for llm
def generate_baby_name(personality_type, gender_type, religion_type,country_type):
    prompt_template_name = PromptTemplate(
        input_variables=['personality_type', 'gender_type', 'religion_type','country_type'],
        template=(
            "You are 15+ years in experience deciding names, more sort of a linguist and history enthusiast.You suggest cooler names appropriate for the future of the child as well as the parents.I want a baby name inspired by the personality trait '{personality_type}'. "
            "The baby is {gender_type}, and I prefer names influenced by {religion_type} culture. "
            "Suggest 10 unique and meaningful names that reflect {personality_type} characteristics.The names should be unique and can be the synonyms of deities or famous personalities of my {religion_type}.The names can be of famous personalities of history and country where my {religion_type} is from and  a good name associated with my country{country_type}. 4 of the names must be cool, you don't have to mention cool explictly while answering.First thank me for caring about my child and validate me about my  parenting. You can describe names a little bit."
        )
    )

    # Create LLM Chain
    chain = LLMChain(llm=llm, prompt=prompt_template_name)

    # Invoke LLM with input parameters
    response = chain.invoke({
        "personality_type": personality_type,
        "gender_type": gender_type,
        "religion_type": religion_type,
        "country_type": country_type
    })

    return response.get('text', "No response generated.")  # Handle potential missing 'text' key

# **Test Function**
if __name__ == "__main__":
    print(generate_baby_name("brave", "boy", "hinduism"))
