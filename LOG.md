# Log

## Entries by date with information on updates

*5/24/2021*  
##### Updates
Started GustWord repo. Added README and UpdateCityIds files.

##### To-do
* Upload a more specific description of how this generator will work
  * OpenWeather API calls
  * Pseudo VS True Random
* Upload more files
---

*5/27/2021*
##### Updates
* Updated README with more information on OpenWeather and how the passwords are supposed to be generated.
* Uploaded GenerateIndex.py a file which generates an index integer of 6 figures from API calls to OpenWeather and mathematical operations for each integer.

##### To-do
* Find a suitable dictionary to pull words from.
* Add some technical information about the mathematical operations that generate each random integer
---

*6/16/2021*
##### Updates
* Found a dictionary from [matthewreagan's WebstersEnglishDictionary repository](https://github.com/matthewreagan/WebstersEnglishDictionary) at `https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json`
  * Note that the URL is the RAW link. I found out that if you want to use `curl` for a file on GitHub that you have to use the RAW link not the one found simply by navigating to the file from the repository.

##### To-do
* Add the technical info. Maybe just comment the lines in the code instead of putting in the README.
---

*6/29/2021*
##### Updates
* Modified the GenerateIndex script to only return indices within the bounds of the dictionary
  * This was kind of "hard-coded", it would be nice to update this so that any updates to the number of dictionary entries are automatically accounted for in the index range.
* Discovered the results from chosen method don't follow a uniform distribution!
  * I decided to run the script 1000 times in a slightly modified way. I constrained the possible resulting numbers to 1-9 and populated a list with results, then plotted a histogram.
  * It seems like the distribution is exponential, or maybe it follows Benford's rule, I'm not sure.
  * The partial fix was to use the built-in random function to choose whether the number would be itself or 10 minus the number generated. This resulted in a more uniform distribution but with two clear peaks.
  * After running a couple of Runs Tests I found from two different sources, it seems like the numbers are still random. There is probably room for improvement but I'm not exactly sure at this moment.

##### To-do
* Find more reliable ways of testing the "randomness" of the generated numbers.
* Push the updates to GitHub
