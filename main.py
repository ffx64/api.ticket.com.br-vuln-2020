import requests
import random
import json
import csv

def make_api_request():
    url = f"https://api.ticket.com.br/ticketshop/v1/simulacao/{random.randrange(1, 9999)}/cliente"
    response = requests.get(url)
    
    if response.status_code == 500:
        return 500
    
    return json.loads(response.text)

def save_to_csv(data):
    with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("[INFO] Data saved to 'output.csv'")

def print_separator(title):
    print("~~" * 10, title, "~" * 10)

def process_data_and_save():
    count = 0
    data_to_save = []

    while True:
        count += 1

        response_json = make_api_request()

        if response_json != 500:
            if response_json['pessoaJuridica'] is False:
                account_data = {}

                # Extracting required fields
                account_data['cpf'] = response_json.get('cpfCnpj', 'N/A')
                account_data['social_reason'] = response_json.get('razaoSocial', 'N/A')
                account_data['birth_date'] = response_json.get('dataNascimento', 'N/A')
                account_data['phone_commercial'] = response_json.get('telefoneComercial', 'N/A')
                account_data['phone_cell'] = response_json.get('telefoneCelular', 'N/A')

                # Extract user info
                user_info = response_json.get('usuario', [{}])[0]
                account_data['user_name'] = user_info.get('nome', 'N/A')
                account_data['user_phone_commercial'] = user_info.get('telefoneComercial', 'N/A')
                account_data['user_phone_cell'] = user_info.get('telefoneCelular', 'N/A')
                account_data['user_email'] = user_info.get('email', 'N/A')
                account_data['user_password'] = user_info.get('senha', 'N/A')

                # Extract address info
                address_info = response_json.get('endereco', {})
                account_data['address_cep'] = address_info.get('cep', 'N/A')
                account_data['address_logradouro'] = address_info.get('logradouro', 'N/A')
                account_data['address_number'] = address_info.get('numero', 'N/A')
                account_data['address_complement'] = address_info.get('complemento', 'N/A')
                account_data['address_neighborhood'] = address_info.get('bairro', 'N/A')
                account_data['address_state'] = address_info.get('estado', 'N/A')
                account_data['address_municipality'] = address_info.get('municipio', 'N/A')
                account_data['address_type'] = address_info.get('tipoLogradouro', 'N/A')

                # Extract last update info
                account_data['last_update'] = response_json.get('ultimaAtualizacao', 'N/A')

                # Adding data to the list for saving
                data_to_save.append(account_data)

                # Print the summary
                print_separator("Information Summary")
                for key, value in account_data.items():
                    print(f"{key.replace('_', ' ').title()}: {value}")

                print_separator("Final")
                print(f"Total Accounts Checked: {count}")
                print_separator("End of Data")

                # Save data to CSV and exit the loop
                save_to_csv(data_to_save)
                break

if __name__ == "__main__":
    process_data_and_save()
