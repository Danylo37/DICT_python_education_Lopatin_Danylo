"""Zoo project"""

# 1-st stage: Printing 4 strings
print("I love animals! \n"
      "Let's check out the animals... \n"
      "The deer looks fine. \n"
      "The lion looks healthy.")

# 2-nd stage: Printing camel
camel = r"""
The camel habitat...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Look at that!"""
# print(camel)

# 3-rd stage: Adding new animals
rabbit = r"""
The rabbit habitat...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y  
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It looks fine!"""

lion = r"""
The lion habitat...
   \|\||
  -' ||||/
 /7   |||||/
/    |||||||/`-.____________
\-' |||||||||               `-._
 -|||||||||||               |` -`.
   ||||||               \   |   `\\
    |||||\  \______...---\_  \    \\
       |  \  \           | \  |    ``-.__--.
       |  |\  \         / / | |       ``---'
     _/  /_/  /      __/ / _| |
    (,__/(,__/      (,__/ (,__/
The lion is roaring!"""

deer = r"""
The deer habitat...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Pretty good!"""

goose = r"""
The goose habitat...
                                                        _...--.
                                        _____......----'     .'
                                  _..-''                   .'
                                .'                       ./
                        _.--._.'                       .' |
                     .-'                           .-.'  /
                   .'   _.-.                     .  \   '
                 .'  .'   .'    _    .-.        / `./  :
               .'  .'   .'  .--' `.  |  \  |`. |     .'
            _.'  .'   .' `.'       `-'   \ / |.'   .'
         _.'  .-'   .'     `-.            `      .'
       .'   .'    .'          `-.._ _ _ _ .-.    :
      /    /o _.-'               .--'   .'   \   |
    .'-.__..-'                  /..    .`    / .'
  .'   . '                       /.'/.'     /  |
 `---'                                   _.'   '
                                       /.'    .'
                                        /.'/.'
Beautiful!"""

bat = r"""
The bat habitat...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It's doing fine."""

animals = [camel, lion, deer, goose, bat, rabbit]

print("1. camel \n"
      "2. lion \n"
      "3. deer \n"
      "4. goose \n"
      "5. bat \n"
      "6. rabbit")
# answer = int(input("Please enter the number of the habitat you would like to view: > "))
# print(animals[answer-1])


# 4-th stage: Looping animals output
while True:
    answer = input("Please enter the number of the habitat you would like to view: > ")
    if answer.isdigit():
        if 0 < int(answer) <= 6:
            print(animals[int(answer)-1])
        else:
            print("Please enter the correct value: > ")
    else:
        if answer == "exit":
            print("---\n"
                  "You've reached the end of the program.")
            print("See you later!")
            break
        else:
            print("Please enter the correct value: > ")
