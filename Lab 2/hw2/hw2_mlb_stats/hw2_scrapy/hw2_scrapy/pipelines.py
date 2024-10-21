# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from bs4 import BeautifulSoup


class Hw2ScrapyPipeline:
    def process_item(self, item, spider):
        item["PLAYER"] = self.process_player(item["PLAYER"])
        return item
    
    def process_player(self, player_name):
        # Parse the player name using BeautifulSoup if player_name is an HTML string
        soup = BeautifulSoup(player_name, "html.parser")

        player_name = soup.get_text()

        first_name = ''
        last_name = ''
        uppercase_count = 0  # To track uppercase letters

        # Extract the first name (retrieve until second uppercase letter)
        for i in range(len(player_name)):
            if player_name[i].isupper():
                uppercase_count += 1
            # Retrieve characters for the first name until the second uppercase letter
            if uppercase_count == 1:
                first_name += player_name[i]
            # Stop retrieving for the first name at the second uppercase letter
            if uppercase_count == 2:
                break

        # Extract the last name (after the second uppercase and a space)
        # Look for the first space after the second uppercase letter
        space_found = False
        first_upper = False
        for j in range(i + 1, len(player_name)):
            if player_name[j] == ' ' and not space_found:
                space_found = True  # Start retrieving after the space
            elif space_found and player_name[j].isalpha():
                if player_name[j].isupper() and not first_upper:
                    first_upper = True
                elif player_name[j].isupper() and first_upper:  # Stop retrieving the last name when encountering the next uppercase letter
                    break
                last_name += player_name[j]
            # Stop retrieving the last name when encountering the next space 
            elif space_found and player_name[j] == ' ':
                break

        # Return the cleaned first and last name
        return f"{first_name.strip()} {last_name.strip()}"
