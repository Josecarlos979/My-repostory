temperatura = int(input("DIigite o clima:"))
estado_do_tempo = str(input("Digite o Clima:"))
                
if temperatura <0 and estado_do_tempo =="nublado":
    print("Clima extremo e nubluado")

elif temperatura >= 0 and temperatura <15 and (estado_do_tempo =="chuvoso"):
    print("Muito frio e úmido")

elif temperatura >=15 and temperatura <20 and (estado_do_tempo =="nublado"):
    print("Frio com nuvens")

elif temperatura >=20 and temperatura < 25 and (estado_do_tempo =="ensolarado"):
    print("Clima agradável e ensolarado")
 
elif temperatura >25 and temperatura <30 and estado_do_tempo !="chuvoso":
    print("Quente e seco")

elif temperatura >=30  and (estado_do_tempo  == "ensolarado"):
    print("Muito quente e ensolarado cuidade com o calor")

else:
    print("Clima indefinido")
    # codigo do clima