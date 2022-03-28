import random

# Función que lanza los dados
def roll_dice():
    atack_dice=random.randint(1,100)
    if atack_dice > 89:
        atack_dice=atack_dice+random.randint(1,100)

    defense_dice=random.randint(1,100)
    if defense_dice > 89:
        defense_dice=defense_dice+random.randint(1,100)

    return(atack_dice, defense_dice)


def calculate_damage(atacker, defender, combat_result):
    #Pasamos la calidad de anima a valores que nos sirvan
    if atacker.quality == 0:
        atacker.quality=0
    elif atacker.quality == 5:
        atacker.quality=1
    elif atacker.quality == 10:
        atacker.quality=2
    elif atacker.quality == 15:
        atacker.quality=3

    if atacker.quality >= defender.armor :
        final_armor=0
    else:
        final_armor =(defender.armor-atacker.quality)*10

    combat_percentage=(combat_result-final_armor)/100
    if combat_percentage <= 0:
        return("Absorción. \n No hay daño.")
    else:
        final_damage= int(atacker.damage*combat_percentage)
        return("El defensor pierde: \n " + str(final_damage) + " de vida")


class Character:
    def __init__(self, ha, bonus_ha, penalizer_ha, hd, bonus_hd, penalizer_hd, armor, damage, quality):
        self.ha=ha
        self.bonus_ha=bonus_ha
        self.penalizer_ha=penalizer_ha

        self.hd=hd
        self.bonus_hd=bonus_hd
        self.penalizer_hd=penalizer_hd

        self.armor=armor
        self.damage=damage
        self.quality=quality

    def atack(self, defender):
        dice=roll_dice()
        atack_dice=dice[0]
        defense_dice=dice[1]
    
        final_atack=self.ha+self.bonus_ha-self.penalizer_ha+atack_dice
        final_defense=defender.hd+defender.bonus_hd-defender.penalizer_hd+defense_dice
        if final_atack < 0:
            final_atack=0
        if final_defense < 0:
            final_defense=0
        combat_result=final_atack-final_defense
        
        if self.ha==0 & self.hd==0 & defender.ha==0 & defender.hd==0:
            return("¿Qué quieres calcular?\n Las fichas están vacías")
        else:
            if combat_result > 0:        
                life_result=calculate_damage(self, defender, combat_result)
                return(f"""Dado del atacante: {(atack_dice)}
                    \n Dado del defensor: {(defense_dice)}
                    \n ATAQUE EXITOSO: \n Ganas de {(combat_result)}
                    \n {(life_result)}""")
            elif combat_result <= 0:
                return(f"""Dado del atacante: {(atack_dice)}
                    \n Dado del defensor: {(defense_dice)}
                    \n ATAQUE FALLIDO: \n Pierdes de {(abs(combat_result))}""")

    def defend(self, atacker):
        dice=roll_dice()
        atack_dice=dice[0]
        defense_dice=dice[1]

        final_defense=self.hd+self.bonus_hd-self.penalizer_hd+defense_dice
        final_atack=atacker.ha+atacker.bonus_ha-atacker.penalizer_ha+atack_dice
        if final_atack < 0:
            final_atack=0
        if final_defense < 0:
            final_defense=0
        combat_result=final_atack-final_defense

        if self.ha==0 & self.hd==0 & atacker.ha==0 & atacker.hd==0:
            return("¿Qué quieres calcular?\n Las fichas están vacías")
        else:
            if combat_result > 0:        
                life_result=calculate_damage(atacker, self, combat_result)
                return(f"""Dado del atacante: {(atack_dice)}
                    \n Dado del defensor: {(defense_dice)}
                    \n DEFENSA FALLIDA: \n Pierdes de {(combat_result)}
                    \n {(life_result)}""")
            elif combat_result <= 0:
                return(f"""Dado del atacante: {(atack_dice)}
                    \n Dado del defensor: {(defense_dice)}
                    \n DEFENSA EXITOSA: \n Ganas de {(abs(combat_result))}""")


# Personajes a utilizar en la calculadora de combate
pj_1=Character(0, 0, 0, 0, 0, 0, 0, 0, 0)
pj_2=Character(0, 0, 0, 0, 0, 0, 0, 0, 0)







# La calculadora funciona perfectamente, pero no sé porq me sale el mensaje de ficha vacía al "DEFENDER" si les pongo HD. Debería hacerlo SOLO si los cuatro están a 0

#EN CALCULAR DAÑO, ¿ESTÁ BIEN CUANDO CALCULO LA armor FINAL EL CAMBIARLE EL NOMBRE? 
#¿DEBERÍA SEGUIR LLAMANDOLO defender.armor? no sé si es mejor arrastrarlo o usar otra variable

#¿ESTÁ BIEN EL CÓMO LE PASO EL RESTULADO DE COMBATE DE atack()?

# (esto no es 100% necesario) ¿Cómo hago para que se redondee el resultado de habilidad final en grupos de 10? es decir: 90, 100, 110, etc. 

# ¿FILTRAR ERRORES?

# añadir dropmenu para la calidad del arma 

# no consigo que muestre todo como quiero. ¿debo usar el return de todos en una sola función?

# LE PONGO UN TRY EXCEPT A LAS FUNCIONES PRINCIPALES DE ATACAR Y DEFENDER POR SI NO HAY NINGÚN VALOR EN ALGUNA CASILLA PERO NO DEVUELVE EL RETURN, SIGUE DANDO ERROR

# al aumentar el tamaño de la fuente en el label del resultado en calculadora_front, se descoloca y no me permite dejarlo en el centro