# Pokémon Card Data Scraper
This Python script automates the process of collecting Pokémon card data from the website pokellector.com. It retrieves information such as card names, sets, and prices based on user-inputted Pokémon names and saves the data into a CSV file for further analysis.

This script essentially automates gathering Pokémon card data from the specified website for a given Pokémon name and saves it in a CSV file.

## Layout

1. **Importing Libraries:** The script starts by importing necessary libraries such as BeautifulSoup (for parsing HTML), Selenium (for web automation), time (for time-related operations), and pandas (for data manipulation).

2. **Input Pokemon Name:** It prompts the user to input the name of a Pokémon.

3. **Web Scraping Initialization:** It initializes a WebDriver (for Chrome in this case) using Selenium. Then, it navigates to the search page of pokellector.com with the provided Pokémon name.

4. **Scraping Page Data:**

- It scrapes the HTML content of the page using BeautifulSoup.
- It finds out the number of pages available for the search results.
- It constructs URLs for English and Japanese versions of the website.
- It loops over each page and retrieves data like card name, set, and price.

5.  **Data Collection:** It collects the card data (name, set, price) from each page and stores it in lists (cards_name, cards_set, cards_price).

6. **Data Storage:** After scraping, it creates a dictionary from the collected data and then converts it into a pandas DataFrame. Finally, it saves the DataFrame as a CSV file in the specified directory.

7. **End Message:** It prints a message indicating the completion of the data pull and saving process.

## Return

Here is an example return after searching "Slowpoke".

![image](https://github.com/jvick1/PokeScraper/assets/32043066/44eb8683-76da-49b0-8238-7813d1e2bf95)
