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
