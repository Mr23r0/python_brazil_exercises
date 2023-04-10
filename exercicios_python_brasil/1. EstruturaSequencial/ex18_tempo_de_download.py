''' Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_arquivo_megabytes = input('Informe o tamanho do arquivo em MB: ')
velocidade_internet_mbps = input('Informe a velocidade da internet em Mbps: ')
tempo_download_seg = (float(tamanho_arquivo_megabytes) * 8) / float(velocidade_internet_mbps)
tempo_download_min = tempo_download_seg / 60

print(f'O tempo de download desse arquivo será: {round(tempo_download_min)} minutos aproximadamente')