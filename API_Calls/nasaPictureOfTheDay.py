from datetime import date
import requests
import os
from dotenv import load_dotenv
load_dotenv()


def nasa_web_api_call(photo_date):
    """A method to call the NASA Web API
    Used to acquire a photo of the day from NASA

    :param
    photo_date: The date of the photo from NASA
    Has to be formatted as YYYY-MM-DD

    :return:
    A JSON Object from the NASA Web API
    By default, this method will return photo from the current day
    """

    url = "https://api.nasa.gov/planetary/apod" # A link for the nasa photo of the day
    api_key = os.getenv("NASA_API_KEY")
    params = {
        "api_key" : api_key,
         "date" : photo_date
    }
    response = requests.get(url, params = params)
    response.raise_for_status()
    data = response.json()
    return data
# print(data) This API returns a dict object,so I cannot iterate over it like in weatherAPI cause there was a list inside of dict
# Gotta watch out for the data that the API returns



def main():
    while True:
        user_action = input("Use \"ENTER\" for default value specify the date with (D): ")
        if user_action.upper() == "D":
            day = input("Enter a day for nasa picture of the day: (DD) ")
            month = input("Enter a month for nasa picture of the day: (MM) ")
            year = input("Enter a year for nasa picture of the day: (YYYY) ")

            if day and month and year:
                # Just adds a zero at the beginning of a number if the number of digits is less than 2, helps with formatting
                formatted_Date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
                data = nasa_web_api_call(formatted_Date) # Assigning the method call to variable data in order to use it as a dictionary
                for key, value in data.items(): # The JSON object is a dictionary so we can iterate over it
                    print(f"{key.upper():15} : {value}")

        # Clicking ENTER for a default value of a current day
        elif user_action == "":
            today = date.today()
            formatted_Date = today.strftime("%Y-%m-%d")
            data = nasa_web_api_call(formatted_Date)
            for key, value in data.items():
                print(f"{key.upper():15} : {value}")

        # Quitting the program
        elif user_action.upper() == "Q":
            print("Thank you for using NASA Picture of The Day")
            break
        else:
            print("Invalid Input")
if __name__ == "__main__":
    main()