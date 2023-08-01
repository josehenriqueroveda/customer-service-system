# Customer Service System
This is a **customer service system** that acts as a customer service representative for a seed company. It provides answers to customer service queries based on the products and its characteristics.
It also contains a **NPS analyzer** that calculates the NPS based on customer feedback and generates an NPS chart. It uses OpenAI's GPT-3 model to summarize the feedback and calculate the NPS.

## Installation
1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Create a `.env` file and add your OpenAI API key as `OPENAI_API_KEY`
4. Run `poetry install` to install the required packages
5. Run `poetry shell` to activate the virtual environment


## Customer Service System Usage
1. Run `python main.py`
2. Choose option **1** to talk with customer service
3. Enter your questions regarding the products
4. The system will provide answers based on the product characteristics
5. Choose option **2** to end the service
6. Enter your feedback and rating


### Code Information
- `CustomerServiceSys`: A class that represents a customer service system. It contains the following methods:

    `get_system_message()`: Returns the system message.
  
    `add_user_message(message: str)`: Adds a user message to the messages attribute.
  
    `get_completion(model: str, temperature: int, max_tokens: int)`: Uses OpenAI's GPT-3 model to generate a response based on the user message and the previous messages in the messages attribute. It returns the generated response.
  
    `answer(message: str)`: Adds the user message to the messages attribute and uses the get_completion() method to generate a response. It returns the generated response.


## NPS Analyzer Usage
1. Run `python nps.py`
2. Input the feedback grades and comments
3. The system will summarize the feedback and calculate the NPS
4. The system will generate a NPS chart based on the calculated NPS


### Code Information
The `nps.py` file contains the following classes and functions:

- `Feedback`: A dataclass that represents a feedback with a grade and a comment.
- `FeedbackAnalyzer`: A class that contains a function to calculate the NPS based on a list of grades.
- `ChartGenerator`: A class that contains a function to generate an NPS chart based on a calculated NPS.
- `analyze_feelings`: A function that uses OpenAI's GPT-3 model to summarize the feedback and calculate the NPS. It takes a list of Feedback objects as input and returns a summary of the feedback as a JSON object with the key **"summary"** and the value being the summary.


## License
This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
If you find a bug or have a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository and submit a pull request.

Before submitting a pull request, please make sure that your code adheres to the following guidelines:
 - Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
 - Write docstrings for all functions and classes.
 - Write unit tests for all functions and classes.
 - Make sure that all tests pass by running pytest.
 - Keep the code simple and easy to understand.
