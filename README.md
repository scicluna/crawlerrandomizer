A simple python program for generating plausbile DCC characters within the context of a modern-day isekai scenario.

## Setup
Setup is simple. Just make sure you have python installed, and then install the dependancies using pip:
```
    pip install openai names
```
If it warns you that you are missing any other packages, just install them with pip.

Get an openai API key from their website and put in a few bucks to your account. This program doesn't charge you much, but it does add up over extensive use.

Rename .example.env to .env and place your openai key inside. **(Make sure to never leak this by saving it to your github repo!!!!)**

If you want to change the core prompt, head over to ai/get_ai_json.py to edit the prompt up to suit your campaign setting. Just be sure not to mess with the JSON structure!

## Use
Just run ```python main.py``` in the root of the repo, and you're good to go. Follow the prompts and get your fresh crawler in markdown format.

(MIT License) - Feel free to use this for whatever you want!

Enjoy!
