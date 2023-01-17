# Automatic code generator API

This is a simple ML based API with [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework that uses [openAI model](https://beta.openai.com/docs/guides/code/introduction) Codex: code-cushman-001 - to generate code for your queries through an autoregressive language model that uses deep learning to produce text.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

3. Navigate into the project directory

   ```bash
   $ cd openai-quickstart-python
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file

8. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! Enjoy your coding tutor for now on :) 

And in case you have any doubt you can contact me via email anytime; happy coding!
