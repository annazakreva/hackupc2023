import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt


USER_INDEX = 1
users_key = {1: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzEiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMiwiZXhwIjoxNjg0MjI4ODAyLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.KXAL8YvSKCwqfKgG4X5fg4BaH9LDimxvLpWosGe0h2j0MLGX6hmZSeNSKl732ijEu57CwSGK5XkLN-Eru-lg3lI2ZmRZl3CD1zY3B6eHPPr8-FYQ6_hEy1gCUwO69jT7RM8qSvoedmXbySHXdlYoBXuySihlIui0tpbIeVc7Hvn7JE0pIEeBvUCQP88OSe02ytwSv9GjDrbNwm86CtArIa2Zrf6PscwjEABt8g_cWMLXnGIEPC70-dNU6FywN4JcFpw2UxdWCFdo0G4SXQ4PL0rbh-Fh-1HcUxAppQRDECqp_F0D9rbdJjzAhFDXb9VijcEngGf1BIW20KEiMiF0kQ',
             2: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzIiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMywiZXhwIjoxNjg0MjI4ODAzLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.ODUxOMrWv8KpHgR9Rzid9D3n2cl4rcWqkWZhY7iEBgcEi48z40uOImcWXiKAL3CFY4I1oci3B3G1JxLfif7DiqJEuNPzerFQOpIJbHwPLUUln4NYKoRo4N9jcGLEC8YFZP3ntzxSpHYfNK9WWI-19HRGRnzevMO1V9B8xW3lmi-7bYRacPVJ61vBXcdWeWpj_GICoeAdeaKS9lCiIQeNVqT0OTlfnyfg7QHn7_QrYd0qUpuxhQ1TkJDrMcC9WNx9-oqZl76uNiTe5AskXr1BHzh3Eb8zuQenwXC-dfMXNw6nDrmyEccy3OE49Z6_WmKpdqZsx9lIAoimB2MGAMkAYw',
             3: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzMiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMywiZXhwIjoxNjg0MjI4ODAzLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.feYz7nzuMN8AFrpsTCXE2sR0dfXVydoYKsl8JEWnEtprCRSzxeZYTE5bUCMa4_K27cvdFdeNAwUsfaWB13MVGwJozBJA1LU252go5vkJe-9cJNPNd77njb9tWA6Vwr-4lxXgo1P0UfVuQhFXe1JCtWdxm0PvRAoANkInQIzjlDNdohzSpGbnojZqO3OJWNeaez-yZvkKdDfULfNAjPcDoJMtUZGm6zE2m_0oaRpCwq63YG4AjIKMm4jUxZSqFy62Yr-ZsH6TIw1gL1qJHLyHdsoLtl_f7ajp9inZj-74yad4PvBIX2KcgUyjczH03s2E_80hYljOiIQLkweVWubsEg',
             4: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzQiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMywiZXhwIjoxNjg0MjI4ODAzLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.JaCb34JyUgcKV39SAlpGTWYStVVnRjAv64Xngleh3HQ6ziTPpHC58ZTPxohuTmk1F_ySWjhAWYbtyISB6wFDyLrL8QJq6CyhkwyeBob288_EYV0pTse2v_hiHWGoYLZSKGs8SaqVAf7B60yF-18_lmCN0RyEEyhQciIIWbs160XczmrmHv54pi_-2BiuGbjogTsJyFCPCreNGr9L-oVUVVKiJrA7OAPmrHu7qsr2oPGc3wORwI0c485_8e5nsFA-Dp-m8upx4NzcYgaeBX8A8Z_Fs-TPL2upVSy-m_x-YHLOA35al7LXMwToS9i_mQQLaQduHDH0VcWST4xLdnzmuQ',
             5: 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzUiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwNCwiZXhwIjoxNjg0MjI4ODA0LCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.Mt3zSslrgXEhY-vhMAc312TbNsFwJnZB4Y0SneI9i1xzsPdBrXiJMlmflr3djeCiAUq3CBVl9Lj5xnLUsYtALsGAwiEHS1k3F-o5Uo0SEzLaLZISqoD03KXUlaHD4kCii9ovEjpVuiGqKZClEnAQxwaykXI1DzyElfd9BK3dxa3fMReBVJphbpH7QN1x3EgFlmTM6yBPR1EjDzT7aXZDznxSkRLy0KQLpFUAaT9loqpP389HpUHyzc34ZFoKfDRXZXrj9xRvk4acsl5jv9vPUrHYJzPo4KENTzmrwxKv0_eD1o8VQDEEQ-ifh2Lyo3pG8HdLb734Cr6DCJmSLjW2zA'}

def get_slides(user = 3, month = 5, year = 2023):
    
    # Auxiliar functions
    def get_day_most_spent(current_month, current_year, user_index):
        transactions_url = "https://int.strandscloud.com/fs-api/transactions"

        headers_user = {
            "accept": "application/json",
            "x-api-key": "0glKTRIQX060kORY94Rx6a3nT7q6wxc271eqo35I",
            "Authorization": f"bearer {users_key[user_index]}"
        }

        transactions_req = requests.get(transactions_url, headers=headers_user)
        transactions = transactions_req.json()
        
        amount_per_day = {}
        for transaction in transactions['transactions']:
            date = transaction['date']
            date_object = datetime.fromisoformat(date[:-1])

            year = date_object.year
            month = date_object.month
            day = date_object.day

            if month == current_month and year == current_year:

                amount = -transaction['amount']['amount'] 

                # Get category url
                category_id = transaction['category']['id']
                category_url = f"https://int.strandscloud.com/fs-api/categories/{category_id}"

                category = requests.get(category_url, headers=headers_user).json()['name']

                if day in amount_per_day: 
                    amount_per_day[day]['amount'] += amount
                    amount_per_day[day]['category'] += [category]
                else:
                    amount_per_day[day] = {'amount':amount, 'category': [category]}
            
        max_date = max(amount_per_day, key=lambda k: amount_per_day[k]["amount"])

        amount_per_day[max_date]['date'] = max_date

        return amount_per_day[max_date]

    def get_day_most_spent_all(month, year):
        data = {}
        for key in users_key:
            data[key] = get_day_most_spent(month, year, key)
        return data

    def to_ordinal(n):
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        suffix = 'th' if 11 <= n <= 13 else suffixes.get(n % 10, 'th')
        return f"{n}{suffix}"
    
    def data_to_slide_day_most_spent(data, user = None):
        slide = {}
        if user != None:
            slide['id'] = 3
            slide['title'] = '''Let's have a look at the craziest day of your month!'''
            if len(data['category']) == 1: 
                slide['content'] = f'''On the {to_ordinal(data['date'])} you spent {data['amount']}$ on {data['category'][0]}'''
            else:
                # Join the elements with commas
                joined_elements = ", ".join(data['category'])
                # Replace the last comma with 'and'
                last_comma_index = joined_elements.rfind(",")
                if last_comma_index != -1:
                    joined_elements = f"{joined_elements[:last_comma_index]} and{joined_elements[last_comma_index+1:]}"
                slide['content'] = f'''On the {to_ordinal(data['date'])} you spent {data['amount']}$ on {joined_elements}'''
        else:
            for key in data:
                slide[key] = {}
                slide[key]['id'] = 3
                slide[key] = {'title' : '''Let's have a look at the craziest day of your month!'''}
                if len(data[key]['category']) == 1: 
                    slide[key]['content'] = f'''On the {to_ordinal(data[key]['date'])} you spent {data[key]['amount']}$ on {data[key]['category'][0]}'''
                else:
                    # Join the elements with commas
                    joined_elements = ", ".join(data[key]['category'])
                    # Replace the last comma with 'and'
                    last_comma_index = joined_elements.rfind(",")
                    if last_comma_index != -1:
                        joined_elements = f"{joined_elements[:last_comma_index]} and{joined_elements[last_comma_index+1:]}"
                    slide[key]['content'] = f'''On the {to_ordinal(data[key]['date'])} you spent {data[key]['amount']}$ on {joined_elements}'''
        return slide
    
    def other_slides():
        headers_user1 = {
            "accept": "application/json",
            "x-api-key": "0glKTRIQX060kORY94Rx6a3nT7q6wxc271eqo35I",
            "Authorization": "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzEiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMiwiZXhwIjoxNjg0MjI4ODAyLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.KXAL8YvSKCwqfKgG4X5fg4BaH9LDimxvLpWosGe0h2j0MLGX6hmZSeNSKl732ijEu57CwSGK5XkLN-Eru-lg3lI2ZmRZl3CD1zY3B6eHPPr8-FYQ6_hEy1gCUwO69jT7RM8qSvoedmXbySHXdlYoBXuySihlIui0tpbIeVc7Hvn7JE0pIEeBvUCQP88OSe02ytwSv9GjDrbNwm86CtArIa2Zrf6PscwjEABt8g_cWMLXnGIEPC70-dNU6FywN4JcFpw2UxdWCFdo0G4SXQ4PL0rbh-Fh-1HcUxAppQRDECqp_F0D9rbdJjzAhFDXb9VijcEngGf1BIW20KEiMiF0kQ"
        }

        may_stats1_url = "https://int.strandscloud.com/fs-api/transactions/stats?fromDate=2023-05-01&toDate=2023-05-31&timeInterval=MONTH&page=0&size=50&sort=FROM_DATE_DESC"
        stats_may1_req = requests.get(may_stats1_url, headers=headers_user1)
        user1_may_stats = stats_may1_req.json()
        for data in user1_may_stats['stats']: #mirem tots els comptes en general, més endavant mirar de fer separació
            expenses = (data['expense']['amount'], data['expense']['currency'])
            income = (data['income']['amount'], data['income']['currency'])

        may_transactions1_url = "https://int.strandscloud.com/fs-api/transactions?fromDate=2023-05-01&toDate=2023-05-31&recoverHeatLevel=false&page=0&size=50&sort=DATE_DESC&applyToSplits=false"
        transactions_may1_req = requests.get(may_transactions1_url, headers=headers_user1)
        user1_may_transactions = transactions_may1_req.json()
        categories_id =[]
        for data in user1_may_transactions['transactions']: 
            categories_id.append((data['category']['id'],abs(data['amount']['amount'])))

        categories = []
        for category in range(len(categories_id)):
            categories_url = "https://int.strandscloud.com/fs-api/categories/" + str(categories_id[category][0])
            category_req = requests.get(categories_url, headers=headers_user1)
            actual_categories = category_req.json()
            categories.append((actual_categories['name'],categories_id[category][1]))

        wrapped = [{'id':i} for i in range(1,3)]
        for i in range(len(wrapped)):
            if i == 0:
                wrapped[i]['title'] = "This month you have spent " + str(abs(expenses[0])) + ' ' + str(expenses [1])
                wrapped[i]['content'] = "This represents a " + str(abs(expenses[0]*100/income[0])) + "% of your income"
            if i == 1:
                wrapped[i]['title'] = "What did you mainly spend it on?"
                wrapped[i]['content'] = " "
        return wrapped
    
    def footprints():
        transactions1_url = "https://int.strandscloud.com/fs-api/transactions"

        headers_user1 = {
            "accept": "application/json",
            "x-api-key": "0glKTRIQX060kORY94Rx6a3nT7q6wxc271eqo35I",
            "Authorization": "bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InhMQVRvOWM2T3VQci1jWEdqMEc3UiJ9.eyJpc3MiOiJodHRwczovL3N0cmFuZHMtZGVtby1iYW5rLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHx1c2VyUEZNMzEiLCJhdWQiOiJodHRwOi8vc2FuZGJveC5zdHJhbmRzY2xvdWQuY29tLyIsImlhdCI6MTY4Mzc5NjgwMiwiZXhwIjoxNjg0MjI4ODAyLCJhenAiOiJtRG5YajB0TDNZWEVOVldtQ2NOQ2xKUG5lV2loenlIbCIsImd0eSI6InBhc3N3b3JkIn0.KXAL8YvSKCwqfKgG4X5fg4BaH9LDimxvLpWosGe0h2j0MLGX6hmZSeNSKl732ijEu57CwSGK5XkLN-Eru-lg3lI2ZmRZl3CD1zY3B6eHPPr8-FYQ6_hEy1gCUwO69jT7RM8qSvoedmXbySHXdlYoBXuySihlIui0tpbIeVc7Hvn7JE0pIEeBvUCQP88OSe02ytwSv9GjDrbNwm86CtArIa2Zrf6PscwjEABt8g_cWMLXnGIEPC70-dNU6FywN4JcFpw2UxdWCFdo0G4SXQ4PL0rbh-Fh-1HcUxAppQRDECqp_F0D9rbdJjzAhFDXb9VijcEngGf1BIW20KEiMiF0kQ"
        }

        transactions1_req = requests.get(transactions1_url, headers=headers_user1)
        user1_transactions = transactions1_req.json()

        cf = 0
        for transaction in user1_transactions['transactions']: #hardcoding carbon footprint 
            transaction['cfEmissions'] = 10
            cf += 10

        wrapped = [{'id':i} for i in range(1,2)]
        for i in range(len(wrapped)):
            if i == 0:
                wrapped[i]['title'] = "Your carbon footprint emissions amount was " + str(cf/100) + "KgCO2e"
                wrapped[i]['content'] = "You're on the TOP 10 most sustainable users in your zone" 
        
        return wrapped

    if user != None:
        data = get_day_most_spent(5, 2023, user_index=user)
    else:
        data = get_day_most_spent_all(5, 2023)
    slides = data_to_slide_day_most_spent(data, user = user)

    def get_midnight_transactions(user_index, current_month = 5, current_year = 2023):
        transactions_url = "https://int.strandscloud.com/fs-api/transactions"

        headers_user = {
            "accept": "application/json",
            "x-api-key": "0glKTRIQX060kORY94Rx6a3nT7q6wxc271eqo35I",
            "Authorization": f"bearer {users_key[user_index]}"
        }

        transactions_req = requests.get(transactions_url, headers=headers_user)
        transactions = transactions_req.json()
        
        midnight_transaction = {'amount':0}
        for transaction in transactions['transactions']:
            date = transaction['date']
            date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%MZ')

            year = date_obj.year
            month = date_obj.month
            hour = int(date_obj.strftime('%H'))
            min = int(date_obj.strftime('%M'))

            if month == current_month and year == current_year and hour >= 0 and hour < 4:
                
                amount = -transaction['amount']['amount'] 

                if amount > midnight_transaction['amount']:
                    # Get category url
                    category_id = transaction['category']['id']
                    category_url = f"https://int.strandscloud.com/fs-api/categories/{category_id}"

                    category = requests.get(category_url, headers=headers_user).json()['name']

                    midnight_transaction['amount'] = amount
                    midnight_transaction['category'] = category
                    
                    midnight_transaction['time'] =  '{:02d}'.format(min) + ':' + '{:02d}'.format(min)
        
        if midnight_transaction['amount'] > 0:
            slides = {}
            slides['id'] = 4
            slides['title'] = '''What about your impulsive midnight purchases?'''
            slides['content'] = f'''You spent {midnight_transaction['amount']}$ on {midnight_transaction['category']} at {midnight_transaction['time']}'''
            return slides
        
    all_slides = [slides] + other_slides() + footprints() + [get_midnight_transactions(user_index=USER_INDEX)]


    # Convert the dictionary to a string with keys without double quotes
    string = "["
    for slides in all_slides:
        for key, value in slides.items():
            if key == 'id': 
                string += "{"+f"{key}: {value}"+", "
            else:
                string += f"{key}:"+'"' +f"{value}"+'"'
                if key == "title":
                    string += ", "
                else:
                    string += "},"
    string = string[:-2] + '}]'
    return string
