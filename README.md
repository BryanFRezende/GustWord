# GustWord
## Truly Random and Memorizable Password Generator

OK, at least that's the hope. Here's my try at a password generator that's actually random. How you ask? By using the wind. And why is this generator special? Because you'll actually be able to memorize the password...at least as well as you can memorize any other phrase. How you ask, again? By using real words to generate a password and making a story that helps you remember it.

Why am I making this if there are already so many password generators out there? Because I didn't get a research internship this summer and I have to fill my time with something now don't I? No...it's not to make your life more convenient, though that might be a beneficial consequence.

I have just started this project recently (5/17ish/2021) so there is just a bit of work done but I will try to update regularly.

### How is GustWord supposed to work?

The idea is that the direction and intensity of wind is random over time. There might be preavailing winds in any given location but my assumption is that the specific combination of the angle with North and magnitude of the wind speed are two values that together are never predicatable and truly random.

OpenWeather (openweathermap.org) is an open source initiative providing local weather data from locations across the globe. They provide an API to retrieve data from a given location and this is the database GustWord will tap into to get live data about wind speed and direction.

Two locations are chosen using a pseudo-random number generator. Then, the weather data from those locations are processed to return unique values computed from the wind speed and direction. The resulting values are used as an index number to retrieve a word from the dictionary. This process is repeated multiple times to retrieve enough words to generate a truly random password.

Voila! That constitutes a truly random password which should be relatively easy to remember. The generator will have settings to constrain the minimum and maximum amount of characters and the ability to add numbers and special characters.  


Given that I will have the competency/help to finish it...The last stage will use natural language processing to weave a story together that helps the user remember the password even better.


### Please comment!

I am by no means an expert coder, so please take a look at my scripts and see if you can offer any suggestions. As of now it takes about 10 seconds on average to generate a password—that could certainly be improved. Also, if you know how to run a test to check randomness other than the Runs Test found from GeeksForGeeks, please share the link or info.

#### Please include sources if applicable.

The interesting stuff is in the "Modules.ipynb" Jupyter Notebook. "GenerateIndex.py" is outdated at this point, I will probably toss it soon. "UpdateCityIds.py" creates and updates a list of all the city ids used to randomly get wind speed and direction. "LOG.md" is a log of work by date.

### More about the method

To get a truly random word, I'm generating truly random numbers, creating an index from them, then looking up that index in a dictionary. I saw this idea in [an article online where you roll the dice to provide the truly random digits](https://theintercept.com/2015/03/26/passphrases-can-memorize-attackers-cant-guess/) and generate your password. I'm just substituting wind vectors for dice rolls and using a longer dictionary (which may have to change—we'll see). The wind to digit process is as follows:
1. Get wind vectors from two pseudo-randomly chosen cities
2. Take their dot products and cross products
3. Take the sum of the two products
4. If the number is below 10 the first digit is the number, if not it's divided by a pseudo-random number until it is below 10.
5. The numbers, even before dividing, demonstrate an exponential distribution so I added a block to pseudo-randomly either leave the digit as is or make it 10 minus itself.
