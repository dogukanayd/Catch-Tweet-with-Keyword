# CATCH TWEET WITH KEYWORD 

This project allows you to extract data from the API with the entered word and date using the Twitter API.

## Example of the outputs

![](/outputs/outputsexample.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Python 2.7 and Pip

### Installing


```
git clone https://github.com/dogukanayd/Catch-Tweet-with-Keyword.git
cd Catch-Tweet-with-Keyword
pip install -r requirements.txt
```

Enter your own keys into the settings.py 
```
    YOUR_CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
    YOUR_CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET_KEY'
    YOUR_KEY = 'YOUR_KEY'
    YOUR_SECRET = 'YOUR_SECRET_KEY'
```

## Running

The main function is called at the bottom of the catch_tweet.py file. Go there and enter the values you want.

The first parameter is the word you want to search for

The second parameter is how many days you want to go back

The third parameter is language choice for your keyword: Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.

Example:


```
main('btc', 7, 'tr')
```

Go to the folder where the project is located from the terminal

```
cd Catch-Tweet-with-Keyword
python catch-tweet.py
```

Keyword Analysis

Go to the keyword-analysis.py than

Change the inside of this array you want to search for

```
keywords = ["dump", "pump"]
```


## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
