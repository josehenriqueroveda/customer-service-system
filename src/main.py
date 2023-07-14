import os

import openai
from openai.openai_object import OpenAIObject
from dotenv import load_dotenv, find_dotenv

from utils import PRODUCTS, TITLE


load_dotenv(find_dotenv())
openai.api_key = os.environ["OPENAI_API_KEY"]


class CustomerServiceSys:
    delimiter = "####"
    products = PRODUCTS

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": self.get_system_message(),
            }
        ]

    def get_system_message(self) -> str:
        return f"""
        Act as a customer service representative for a seed company. \
        You will be provided with customer service queries. \
        The customer service query will be delimited with \
        {self.delimiter} characters.

        Output answers to the customer service queries \
        based on the following products and its characteristics:
        {self.products}

        Be sure to answer the customer service queries \
        based on the product characteristics in a clear and concise manner. \
        
        If you are not sure of the answer, \
        you can respond with "I am not sure, can you provide more details?". \
        """
    

    def add_user_message(self, message: str) -> None:
        self.messages.append({
            "role": "user",
            "content": f"{self.delimiter}{message}{self.delimiter}",
        })

    
    def get_completion(self, model="gpt-3.5-turbo", temperature=0, max_tokens=500) -> str | None:
        response = openai.ChatCompletion.create(
            model=model,
            messages=self.messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        if isinstance(response, OpenAIObject):
            return response.choices[0].message["content"]
        return None
    

    def answer(self, message: str) -> str | None:
        self.add_user_message(message)
        return self.get_completion()
    

def main():
    print(TITLE)
    print("1- Talk with customer service")
    print("2- End service")
    customer_service_sys = CustomerServiceSys()

    while True:
        option = input("Choose an option: ")
        if option == "1":
            message = input("Enter your questions regarding our products here: ")
            if message == "exit":
                break
            answer = customer_service_sys.answer(message)
            print(answer)
            print("Select an option:")
            print("1- Talk with customer service")
            print("2- End service")
        elif option == "2":
            score = input("Please rate our service (1-10): ")
            feedback = input("Enter your feedback: ")
            with open("../database/nps_answers.csv", "a") as f:
                f.write(f"{score},\"{feedback}\"\n")
            print("Thank you for your feedback!")
            f.close()
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
    