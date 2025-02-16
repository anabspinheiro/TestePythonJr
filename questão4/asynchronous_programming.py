import asyncio
import time

# função assíncrona com simulação de chamada de rede
async def simular_chamada_rede(nome, tempo):
    print(f"{nome} iniciada. Aguardando {tempo} segundos...")
    # o await vai simular uma operação de rede
    await asyncio.sleep(tempo)
    print(f"{nome} concluída após {tempo} segundos.")

# função principal e inicio do cronômetro
async def main():
    inicio = time.time()
    
    # a função asyncio.gather irá executar as 5 chamadas de rede simultaneamente
    await asyncio.gather(
        simular_chamada_rede("Chamada 1", 5),
        simular_chamada_rede("Chamada 2", 4),
        simular_chamada_rede("Chamada 3", 3),
        simular_chamada_rede("Chamada 4", 2),
        simular_chamada_rede("Chamada 5", 1)
    )    
    
    # aqui será executado o calculo de tempo total
    fim = time.time()
    tempo_total = fim - inicio
    print(f"Tempo total de execução: {tempo_total:.2f} segundos.")

# execução da função assíncrona principal
if __name__ == "__main__":
    asyncio.run(main())