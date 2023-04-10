import datetime
import time

def countdown(tempo_em_segundos):
    try:
        tempo_em_segundos = int(tempo_em_segundos)
    except ValueError:
        print("Por favor, insira um valor numérico para o tempo em segundos.")
        return

    tempo_restante = datetime.timedelta(seconds=tempo_em_segundos)

    while tempo_restante:
        print(f"Tempo restante: {tempo_restante}", end="\r")
        tempo_restante -= datetime.timedelta(seconds=1)
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            break

    print('Contagem regressiva concluída!')

tempo = input('Insira o tempo em segundos: ')

countdown(tempo)
