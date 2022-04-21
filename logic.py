import dice

# Function that calculates the damage taken
def calculate_damage(attacker, defender, combat_result):
    #Pasamos la calidad de anima a valores que nos sirvan
    if attacker.quality == 0:
        attacker.quality=0
    elif attacker.quality == 5:
        attacker.quality=1
    elif attacker.quality == 10:
        attacker.quality=2
    elif attacker.quality == 15:
        attacker.quality=3

    if attacker.quality >= defender.armor :
        final_armor=0
    else:
        final_armor =(defender.armor-attacker.quality)*10

    combat_percentage=(combat_result-final_armor)/100
    if combat_percentage <= 0:
        return("Absorción. \n No hay daño.")
    else:
        final_damage= int(attacker.damage*combat_percentage)
        return("El defensor pierde " + str(final_damage) + " de vida")



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

    def attack(self, defender):
        attack_dice=dice.roll(100)
        defense_dice=dice.roll(100)
    
        final_attack=self.ha+self.bonus_ha-self.penalizer_ha+attack_dice
        final_defense=defender.hd+defender.bonus_hd-defender.penalizer_hd+defense_dice
        if final_attack < 0:
            final_attack=0
        if final_defense < 0:
            final_defense=0
        combat_result=final_attack-final_defense
        
        if self.ha==0:
            return("ERROR\n\n Introduce el ataque")
        else:
            if combat_result > 0:        
                life_result=calculate_damage(self, defender, combat_result)
                return(f"""\n ATAQUE EXITOSO: \n Ganas de {(combat_result)}
                    \n {(life_result)}
                    \n\n Dado del atacante: {(attack_dice)}
                    \n Dado del defensor: {(defense_dice)}""")
            elif combat_result <= 0:
                return(f"""ATAQUE FALLIDO: \n Pierdes de {(abs(combat_result))}
                    \n\n Dado del atacante: {(attack_dice)}
                    \n Dado del defensor: {(defense_dice)}""")

    def defend(self, attacker):
        attack_dice=dice.roll(100)
        defense_dice=dice.roll(100)

        final_defense=self.hd+self.bonus_hd-self.penalizer_hd+defense_dice
        final_attack=attacker.ha+attacker.bonus_ha-attacker.penalizer_ha+attack_dice
        if final_attack < 0:
            final_attack=0
        if final_defense < 0:
            final_defense=0
        combat_result=final_attack-final_defense

        if self.hd==0:
            return("ERROR\n\n Introduce la defensa")
        else:
            if combat_result > 0:        
                life_result=calculate_damage(attacker, self, combat_result)
                return(f"""DEFENSA FALLIDA: \n Pierdes de {(combat_result)}
                    \n {(life_result)}
                    \n\n Dado del atacante: {(attack_dice)}
                    \n Dado del defensor: {(defense_dice)}""")
            elif combat_result <= 0:
                return(f"""\n DEFENSA EXITOSA: \n Ganas de {(abs(combat_result))}
                    \n\n Dado del atacante: {(attack_dice)}
                    \n Dado del defensor: {(defense_dice)}""")


# Personajes a utilizar en la calculadora de combate
pj_1=Character(0, 0, 0, 0, 0, 0, 0, 0, 0)
pj_2=Character(0, 0, 0, 0, 0, 0, 0, 0, 0)








# HACER UNA FUNCIÓN QUE LLAME AL OBJETO CON SU ACCIÓN. FIN Y PSARLO AL COMANDO 

# ¿ESTÁ BIEN EL CÓMO LE PASO EL RESTULADO DE COMBATE DE attack()?

# (esto no es 100% necesario) ¿Cómo hago para redondear el resultado de habilidad final en grupos de 10? es decir: 90, 100, 110, etc. 

# FILTRAR ERRORES !!

# añadir dropmenu para la calidad del arma 

# LE PONGO UN TRY EXCEPT A LAS FUNCIONES PRINCIPALES DE ATACAR Y DEFENDER POR SI NO HAY NINGÚN VALOR EN ALGUNA CASILLA PERO NO DEVUELVE EL RETURN, SIGUE DANDO ERROR
