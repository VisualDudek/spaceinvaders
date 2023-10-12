
# GOALS
After one year since I last worked on this code will revisit the code with following goals:
1. assess how well code is documented and does `README` or other resources (e.g. graphml) provide you a quick way to get along with code
2. document code logic with marmaid in VS Code
3. enhance code with type annotations

# DIARY
## 12/10/23
- IDEA: create your own Color class based on `Colour` lib. which already have decent `RGB_TO_COLOR_NAMES` dict
- NOTE: lack of src. of code, I beleve that this is based on some YT tutorial
- NOTE: `pygame` have interesting internal events system, simillar to `Textual`
- TODO: need to know more about event system, is it reseted every game tick?
  - `pygame.event.get()` will get all the messages and removes them feom the queue. See docs.
  - `pygame.time.set_timer(event, millis, loops=0)` repeatedly create an event on the envent queue
  - `pygame.sprite.Group` a container class to hold and manage multiple Sprite obj. e.g. `.update()`
- IDEA: refactor `ALIENLASER` type int into `pygame.event.Event` obj.
- TODO: need to decouple the code!
- NOTE: how to test pypame code?
- ADD GAME FEATURE: show cooldown bar

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
- DONE blit surface with volume UP/DOWN old school ||||||
- DONE add pause
- DONE fewer aliens -> they move faster
- add game over message
- top score table
- add game menu
- add recharge indicator
- add falling perks that give additiona live or laser that penetrates all obstacles
- ask "Do You want to surender? Y/N" on quite

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
    - add pause; NEED to introduce GameState 
        NEED to move alien_shoot out of event_loop
            STOPGAP: remove alienlaser form event loop, DISADVANTAGE: after
                alienlaser is restored laser timer is reseted
    - add Game State
    - add SFX click
    CLOSE v0.4
5. dev-0.5
    - fix display lives and score during pause DONE
    - constrain volume display to [0,1] DONE
    - decouple magic number in alienlaser time event DONE
    - speed up last atanding alien DONE
    - speed up laser shoot: DONE
        - remove and add new alienlaser event only once
    - add super laser for player mode DONE
    - add invincible mode DONE
    - rewrite game.check_speed if-conditions


# TAKEAWAY
- Rect class and how to find out its definition
- .pyi files ???
- mock shoot laser during dev
- yEd graph editor
- pygame: calling method on Group of sprites will call requseted method on all of them ONLY works with update name 
- create multiple dev branches OR keep only one dev -> create dev,merge,delete,repeat