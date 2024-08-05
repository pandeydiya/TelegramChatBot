
import re
# re is a sequence of characters that forms a search pattern.
# allows us to find symbols within a string just to extract that and put it into a list.

def process_message(message, response_array, response):
    # Splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())
    # extract words without symbols so that it is easy to read.
    # create a scoring system i.e going to check each word in the user message and check how many words are in response message.

    # Scores the amount of words in the message
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    # Returns the response and the score of the response
    # print(score, response) # bot response will be paired with score.
    return [score, response]  # A message with higher score will give a better response. This is a helper function.


# function that contains the messages!
def get_response(message):  # will take message as an argument.
    # we add our custom responses here.
    response_list = [
        process_message(message, ['hello', 'hi', 'hey'], 'Hey there!'),
        process_message(message, ['bye', 'goodbye'], 'Goodbye!'),
        process_message(message, ['how', 'are', 'you'], 'I\'m doing fine thanks!'),
        process_message(message, ['your', 'name'], 'My name is DIYA\'s bot, nice to meet you!'),
        process_message(message, ['help', 'me'], 'I will do my best to assist you!')
    ]

    # Checks all of the response scores and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    # Get the max value for the best response and store it into a variable
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    # Return the matching response to the user
    if winning_response == 0:
        bot_response = 'I didn\'t understand what you wrote.'
    else:
        bot_response = matching_response[1]

    print('Bot response:', bot_response)
    return bot_response