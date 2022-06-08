'''
Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. 
Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria, 
secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
'''
total_censado = 0
prim_incomp = 0 # 1
prim_comp = 0 # 2
sec_incomp = 0 # 3
sec_comp = 0 # 4
tecnico_incomp = 0 # 5
tecnico_comp = 0 # 6
univ_incomp = 0 # 7
univ_comp = 0 # 8
posg_incomp = 0 # 9 
posg_comp = 0 # 10
mensaje_error = "\nEl valor ingresado es incorrecto, intente nuevamente.\n"


while True:
    print("\n________CENSAR 2022________")
    cc = input("'Enter' - Cargar encuesta.\
            \n'Fin' - Salir del programa.\n").lower()
    
    if cc == "fin":
            break
    elif cc != "":
        print(mensaje_error)
        continue


    nivel_de_estudio = int(input("Nivel de estudio del encuestado:\
                            \n1. Primario.\
                            \n2. Secundario.\
                            \n3. Terciario.\
                            \n4. Universitario.\
                            \n5. Posgrado.\n"))
   
    if nivel_de_estudio > 0 and nivel_de_estudio <= 5:
        comp_incomp = input("Completo o incompleto (C/I): ").lower()
        if comp_incomp == "c" or comp_incomp == "i":
            total_censado += 1
            if nivel_de_estudio == 1:
                if comp_incomp == "c":
                    prim_comp += 1
                else: prim_incomp += 1
            elif nivel_de_estudio == 2:
                if comp_incomp == "c":
                    sec_comp += 1
                else: sec_incomp += 1
            elif nivel_de_estudio == 3:
                if comp_incomp == "c":
                    tecnico_comp += 1
                else: tecnico_incomp += 1
            elif nivel_de_estudio == 4:
                if comp_incomp == "c":
                    univ_comp += 1
                else: univ_incomp += 1
            elif nivel_de_estudio == 5:
                if comp_incomp == "c":
                    posg_comp += 1
                else: posg_incomp += 1
        else:
            print(mensaje_error)
            continue
    else:
        print(mensaje_error)
        continue
    

print(f"\nResultados de la encuesta:\
    \nTamaño de la muestra: {total_censado}.\
    \n1. Personas con nivel de educacion PRIMARIO:\
    \n\tCompleto: {(prim_comp / total_censado * 100):.2f}%.\
    \n\tIncompleto: {(prim_incomp / total_censado * 100):.2f}%.\
    \n1. Personas con nivel de educacion SECUNDARIO:\
    \n\tCompleto: {(sec_comp / total_censado * 100):.2f}%.\
    \n\tIncompleto: {(sec_incomp / total_censado * 100):.2f}%.\
    \n1. Personas con nivel de educacion TERCIARIO:\
    \n\tCompleto: {(tecnico_comp / total_censado * 100):.2f}%.\
    \n\tIncompleto: {(tecnico_incomp / total_censado * 100):.2f}%.\
    \n1. Personas con nivel de educacion UNIVERSITARIO:\
    \n\tCompleto: {(univ_comp / total_censado * 100):.2f}%.\
    \n\tIncompleto: {(univ_incomp / total_censado * 100):.2f}%.\
    \n1. Personas con nivel de educacion POSGRADO:\
    \n\tCompleto: {(posg_comp / total_censado * 100):.2f}%.\
    \n\tIncompleto: {(posg_incomp / total_censado * 100):.2f}%.\n")
