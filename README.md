# dev process
1. Create main window
2. Create the game class
3. Creating the player
    - show an image of the player
    - move the player
    - constrain player to the window
    - shoot a laser + recharge
4. create laser
    - sprite with a position and speed
    - removing lasers
5. placing objects
    - obstacles
    - aliens
6. make aliens:
    - move
    - shoot laser
7. add extra alien
8. implementing the collisions
    - plaer lasers -> obstacle + aliens
    - alien lasers -> obstacle + player
9. adding a health system
10. adding a score system
11. adding a CRT styling overlay
    - logic: draw some stuff on the screen and lower the opacity
12. adding the audio files
    - game music
    - laser and explosion sounds
13. showing a victory message

# IDEAS
- add falling perks that give additiona live or laser that penetrates all obstacles
- DONE blit surface with volume UP/DOWN old school ||||||
- add game over message
- DONE fewer aliens -> they move faster
- top score table
- add game menu
- add pause

# TODO
1. dev-0.2 need one place to read keys input and pass it to game control, menu, sound. 
    - now keys are read in Player class, all keys handle are done also in Player class
2. dev-sound: create separate Sound class
3. dev-0.3 
    - add keys to volume up/down music
    - add KeysControl class to decouple keys managment
    - use KEYUP event for change volume
    - make events global var
    - dislay volume on screen with timeout when up/down
    - sepeed up alien movement each time if less than 45,35,25,5
    - fix: enable alien speed by less than 1 
    CLOSE v0.3
4. dev-0.4
    - TODO:
        - add pause



# TAKEAWAY
- Rect class and how to find out its definition
- .pyi files ???
- mock shoot laser during dev
- yEd graph editor
- pygame: calling method on Group of sprites will call requseted method on all of them ONLY works with update name 
- create multiple dev branches OR keep only one dev -> create dev,merge,delete,repeat