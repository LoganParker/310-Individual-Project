# 310-Group-Project

## Project Description 

Our project is going to be an interactive chatbot that takes on the role of a would-be Atlantis explorer. The chatbot will only talk about things regarding Atlantis and will excitedly talk to the user about his upcoming adventure. The link to our GitHub repo is as follows https://github.com/LoganParker/310-Individual-Project. 

## How to Run the Chat Bot 

1. Download our GitHub repo 
2. Open the repo using VSCode or Terminal 
3. update your environment path on line 7 of `run_me_first.sh` to point to the json credentials file. Then run `run_me_first.sh` (If you are uncomfortable running a bash script refer to dependencies.) 
4. Run gui.py 

## Dependencies
This bot requires nltk, pyspechecker, and stanza in order to run properly. If you do not run first-time-setup.sh you will have to do the following
    
    pip install nltk
    pip install pyspellchecker
    pip install stanza
    pip install --upgrade google-cloud-translate
    pip install requests

This bot also requires an environment variable pointing to the credentials for the translation api. For instructions on 
how to do this, please refer to line 7 of `run_me_first.sh`.
    
Once the previous steps are completed, you must run `py_lib_install.py` so python can install the additional libraries. 

## Dataset 
This bot pulls from a json file with specifically designed responses for who, what, where, when, why style responses. Essentially, this bot smartly translates user text into queries to generate aproprait responses. 

## Classes and Functions 

### aBot.py 
This directory includes all the files for the bot. 

#### get_response
This function recieves the keyword dictionary, asks for user input, and returns chat bot responses. User input is processed using `get_query_objects()`, which extracts nouns and proper nouns. A for-loop iterates through each processed noun in a list and detects if the word exists in entity_dict.json. If there is a match, that means there is a chat bot response for the keyword. If there is no keyword detected in the user response, then the bot returns "Sorry can't help provide any information that relates to [*whatever related noun the user entered*]". 

Parameters:
- response: a string input by the user acting as the key for keywords

  
Returns:
- output: a string containing the bots response

#### spell_check
Takes a string and returns a string with closest related permutation that is part of the english language.

 Parameter:
 - input: a string input  

 Returns:
 - correct: a corrected string output 
    
### gui.py

### BotGUI(tk.Tk)
The class which handles window switching and displays the alternate screens

#### HomeScreen (class)
The main title screen that shows when loading the application. 

#### ChatSreen (class)
The class that manages the chatscreen. 

##### retrieve_user_message(inputField)
gets user input, and then passes the input to the bot for processing. Recieves the updated bot response, and updates the GUI with the new response.

Parameters:
- inputField: a string which determins what field to be inputed

#### show_help_popup
Just passes a string along to the responseLablel in order to display the basic welcome prompt

### data_load.py
For managing data and searching

#### data_load
Loads text from a file.

 Parameters:
 - filepath: file to path to retrieve text from 

 Returns:
  - contents: string of raw text
  

#### preproc
Extracts the nouns and proper pouns from the user query. Takes a user query and runs string 
through Stanza's Dependency Parser. More information about this library is found here: 
https://stanfordnlp.github.io/stanza/depparse.html

Parameters:
 - query: a string 

 Returns:
- obj_list: a list nouns and proper nouns from the user query 


#### dependencyParser
Helper utility used to extract the depencies from a sentence. Runs the dp pipeline object 
in order to run depparse, lemma, and pos tagginig.

Parameters: 
 - sentence: a string 

### syn_detection.py

#### detect_syn
This function takes a word and uses wordnet in order to return a list of asociated synonyms with our word,.

Parameters
- input : word to get inputs from 

Returns
- synonyms: list of synonyms associated with said words. 

### search_json.py

#### search_noun_quest
takes a noun and searches for related question style keywords. 

Parameters
- noun, question: noun and question. Question is mostly used as an adverb in this case.

Returns
- data[noun][quest]: returns a string associated with indexed value

#### get_nouns
returns a list of all nouns within json file

Returns
 - nounList: list of nouns 

#### get_verbs
Parameters
- noun: a string 
 
Returns
 - questList: list of adverbs associated with said noun
 
### unitTest.py

#### test_spell_check
Tests functionality of `spell_check()` function in bot.py

#### test_get_response
Tests functionality of `get_response(query)` function in bot.py

#### test_load_data
Tests functionality of `load_data()` 

### api_controller.py

For retrieving visualizations regarding the ongoing conversation.

#### update_image(search_tag)

Updates the image that will be shown when the visualization button is clicked.

Parameters
- search_tag: the topic regarding the most recent question asked

Returns: URL retrieved from `url_builder`


#### url_builder(response)

Constructs the image url from the Flickr API response

**Parameters**
- _response_: a json object retrieved from `update_image` which contains all necessary information to build the image URL

**Returns**: An image URL string obtained from the Flickr API

### translator.py

For translating input back into the Chatbots native language

#### translate_text(text, lang_code, project_id)

Translates the users input from the detected language back to english

**Parameters**:
- _text_: The text to be translated
- _lang_code_: the language code of the language the text to be translated is in
- _project_id_: the Google project ID

**Returns**: The english equivalent of the text string inputted

#### detect_language(in_string, project_id)

Determines the language the inputted string is written in

**Parameters**:
- _in_string_: The text to be translated
- _project_id_: the Google project ID

**Returns**: The language code of the language that was inputted


#### get_translation(in_string)

Reads the user input, detects the language input using `detect_language` and then translates it using `translate_text`

**Parameters**:
- _in_string_: The text to be translated

**Returns**: The english equivalent of the input


## New Features

### Google Translation API

In order to enhance the agents conversational abilities, I have added the ability for it to understand questions asked in
several languages. Our agent can translate questions asked in any language, and then reply in its native language 
of english. This is done within the `translator.py` class which makes use of the Advanced Google Translate API to detect
the language which is input, translate it, and then generate its standard reply. 


### Flickr API

To further enhance the conversation had with our agent, I have implemented a way to better visualize what our agent is discussing.
This is done using the Flickr API, which pulls images from Flickr that are related to the most recently asked question. 
These images are opened up in your systems default browser. This was implemented within `api_controller.py`. Due to the 
nature of Flickr, some images that are shown may not be as related as desired, because people may upload photos and tag 
them incorrectly.


