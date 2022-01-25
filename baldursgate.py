print('''
                     __..---..-''_.............,_..`>
           _..-'':::_:-'_..-'_.-':::::::::,''//||                      _./
         ,':::::::,'_.-':','.-':.:.::::,','.//:||           _..---.._,','
       ,':::::::,',':'',',:':'`:.:::,',':`:/'.:::         ,'  ,'    _`/
      /::.::.::/,':'  ',':' . ' ::,',':'  '   `:\\       /     .,' _`:)
     /:.::.::://'   .          ',','         .   \\    ,/    .:;  (::
    :.::.::._//             .  /'   .     .       `:,./)    (:/ `. \`:)/
    |.:._.-'::     _..--.._                  __    (:.)      )    `'  `
    |.,'    ||  _.'     ,',`.  _.-''``.   ,''  )   /`'      :
    |/      ||,'    _.-','  |,'        ),'   ,:   (         ; __
            |/   _,':     / `         '      `:.            |',.
              _,':'    : :.                     '    ,'     /'`''
            ,':'        \::  /:..        .        .:' (:   `.      _
          ,':'            \:::::.    .`.  )   _..:.:,::`.._  ``--'',`
         /:'      _..-''```::(:.      ::\/:::.::::.'_:::'  ``----''`'
        /:     ,-'          `\:.       `::_::-''
       ::'    ,               \:.        |::|
       |:    :          ,.     `:.       |::|
       ::.   :        ,'/        `.      ;::;
        \:.   `..__.-','           )  .:/:,'
         `.:.       ,'         _..' _.-::/
           ``-----''          `:. .'<:::<
                                `. `._>::`-..__
                                ,',`-._)_).---'`-._
                               ,`-`:::`'`\::'      |
                           ___/::::::::,' `:\      (_
                       __,'::::`--.._:/     \`._   (:::._
                     ,:`._`----..._:::`-._   \:::.  `-.---:.                 
''')
print("Welcome to Baldur's Gate.")
print("Your mission is to defeat the dragon guarding the gate to undead city.")
# Write your code below this line 👇

question1 = input('What is your weapon? Type "Sword" or "Wand":').lower()

if question1 == "sword":
    print("You excel with your strength, and brandish a regal longsword. The dragon awaits your first move.")
    choice2 = input('The dragon reaches her head down towards you,tempting you to strike it. Type "Strike" to hit it or "Wait": ').lower()
    if choice2 == "strike":
        print('You\'re just a bothersome ant to the dragon, her claw slashes your chest before you can land your hit. GAME OVER.')
    else:
        print('She senses your courage, and flies away from the gate. "That\'s a brave one" She mutters annoyedly. Congrats! You win!')
elif question1 == "wand":
    print("Magic flows through your body like blood, the wand is your conduit.The dragon awaits your first move.")
    choice3 = input('The dragon reaches her head down towards you,tempting you to cast a spell. Type "Magic Missle" to cast or "Wait": ').lower()
    if choice3 == "magic missile":
        print('The dragon has seen this party trick before, she casts a shield and deflects the missiles right back at you. GAME OVER.')
    else:
        print('She senses your intelligence, and steps aside from the gate. "You are a smart one" She comments. Congrats! You win!')
else:
    print("You were too slow, the dragon's breath caught you. Game Over")