import os 
import requests
from tqdm import tqdm

def consulta_cpf(cpf):
    url = f'https://passionesearch.000webhostapp.com/api/consultacpf?chave=WmLKsGJNiUoI&cpf={cpf}'

    try: 

        response = requests.get(url)
        data = response.json()


        if data.get('cpf'):
            script_dir = os.path.dirname(os.path.realpath(__file__))

            with open(os.path.join(script_dir, 'resultados_consulta.txt'), 'a') as file:
                file.write(f"CPF: {data['cpf']}, Nome: {data['nome']}, Data de Nascimento: {data['data_nascimento']}\n")

    except Exception as e:
        pass


if __name__ ==  '__main__':
    total_cpf = 100000000000

    with tqdm(total=total_cpf, desc='Consultando CPFs', unit='CPF', unit_scale=True) as pbar:

        for i in range(1, total_cpf + 1):

            cpf_consulta = f'{i:011d}'

            consulta_cpf(cpf_consulta)

            pbar.update(1)