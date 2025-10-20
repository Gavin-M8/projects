import pygame
import pandas as pd
import numpy as np
from Mechanics import lvl1, lvl2, lvl3, lvl4, lvl5, monster_movement
from Entities import Hero, Monster
from Items import weapons, accessories, consumables

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# Initial states
player_position = pygame.Vector2(screen.get_width() / 2, 630)

cave_basic = False

is_jumping = False
gravity = 5
jump_height = 40
y_velocity = jump_height

font = pygame.font.Font(None,15)

surface_sideroom = 0
cave_sideroom = 0

battle_mode = False

heals = 5

# Initial creation of player instance
player = Hero(50,weapons.loc[weapons['name'] == 'Rusty Sword', 'damage'].values[0],0,8,'Rusty Sword', None, None, player_position.x, player_position.y)


# MAIN LOOP
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Surfaces/Images
    location_surface = font.render(f"X: {round(player_position.x)}   Y: {round(player_position.y)}    Surface Room: {surface_sideroom}    Cave Room: {cave_sideroom}", True, (0,0,0))
    health_surface = font.render(f"Health: {player.health}", True, (0,0,0))
    weapon_surface = font.render(f"Weapon: {player.active_weapon} ({player.power} damage)", True, (0,0,0))
    heals_surface = font.render(f"Heals available: {heals}", True, (0,0,0))

    background_cave_basic = pygame.image.load('cave_basic_2.0.png')
    background_surface_basic = pygame.image.load('surface_basic_2.0.png')
    

    # Determines if the player is in the main room with the ladder
    if surface_sideroom == 0:
        surface_main = True
    else:
        surface_main = False
    if cave_sideroom == 0:
        cave_main = True
    else:
        cave_main = False


    # Determines whether the player can climb a the ladder
    if player_position.x > 0 and player_position.x < 120:
        on_ladder = True
    else:
        on_ladder = False
    

    # Creating instances of monsters with difficulty level based on room number
    if surface_sideroom <= 5:
        s_level = np.abs(surface_sideroom)
    else:
        s_level = 5
    if cave_sideroom <= 5:
        c_level = np.abs(cave_sideroom)
    else:
        c_level = 5

    stats = {1:lvl1, 2:lvl2, 3:lvl3, 4:lvl4, 5:lvl5}

    if not cave_basic and not surface_main:
        spider = Monster('Spider', stats[s_level][1], stats[s_level][0], 0, 2, 'kin', ['Apple Pie', 'Polished Boots', 'Golden Chicken Nugget'], [0.75, 0.33, 0.5], monster_movement(battle_mode, 640, 630, dt))
        megafrog = Monster('Megafrog', stats[s_level][1], stats[s_level][0], 0, 2, 'ele', ['Crimson Cloak', 'Hands of Providence', 'Death Stick'], [0.33, 0.33, 0.33], monster_movement(battle_mode, 640, 630, dt))

        surface_monsters = [spider, megafrog]

        curr_monster = surface_monsters[(np.abs(surface_sideroom))%2]

        curr_monster_surface = font.render(f"Current Monster: {str(curr_monster)}", True, (0,0,0))
        curr_monster_health_surface = font.render(f"Health: {curr_monster.health}", True, (0,0,0))
        curr_monster_power_surface = font.render(f"Power: {curr_monster.power}", True, (0,0,0))

    if cave_basic and not cave_main:
        spider = Monster('Spider', stats[c_level][1], stats[c_level][0], 0, 2, 'ice', ['The Icicle', 'Shiny Amulet', 'Hot Coal'], [0.5, 0.33, 0.1], monster_movement(battle_mode, 640, 630, dt))
        skeleton = Monster('Skeleton', stats[c_level][1], stats[c_level][0], 0, 2, 'fir', ['Razorbeam', 'Cracked Staff', 'Broken Bow'], [0.25, 0.66, 0.5], monster_movement(battle_mode, 640, 630, dt))

        cave_monsters = [spider, skeleton]

        curr_monster = cave_monsters[(np.abs(cave_sideroom))%2]

        curr_monster_surface = font.render(f"Current Monster: {str(curr_monster)}", True, (0,0,0))
        curr_monster_health_surface = font.render(f"Health: {curr_monster.health}", True, (0,0,0))
        curr_monster_power_surface = font.render(f"Power: {curr_monster.power}", True, (0,0,0))

    

    # enters the cave biome
    if player_position[1] > 721:
        cave_basic = True
    if cave_basic:
        if cave_main:
            pygame.Surface.blit(screen, background_cave_basic, dest=(0,0))
        else:
            pygame.Surface.blit(screen, pygame.image.load('cave_side.png'), dest=(0,0))
    if player_position[1] < -100 and cave_basic:
        cave_basic = False


    # enters the surface biome
    if not cave_basic:
        if surface_main:
            pygame.Surface.blit(screen, background_surface_basic, dest=(0,0))
        else:
            pygame.Surface.blit(screen, pygame.image.load('surface_side.png'), dest=(0,0))


    # Drawing Hero sprite and info on screen
    hero_sprite = pygame.image.load('the_hero.png')
    pygame.Surface.blit(screen, hero_sprite, dest=player_position)

    if not surface_main or not cave_main:
        battle_mode = True

        if player.health <= 0:
            player_is_dead = True
        else:
            player_is_dead = False

        if curr_monster.health <= 0:
            monster_defeated = True
        else:
            monster_defeated = False

        if curr_monster.name == 'Spider' and not monster_defeated:
            pygame.Surface.blit(screen, pygame.image.load('spider.png'), dest=(curr_monster.x, curr_monster.y))
        if curr_monster.name == 'Skeleton' and not monster_defeated:
            pygame.Surface.blit(screen, pygame.image.load('skeleton.png'), dest=(curr_monster.x, curr_monster.y))
        if curr_monster.name == 'Megafrog' and not monster_defeated:
            pygame.Surface.blit(screen, pygame.image.load('megafrog.png'), dest=(curr_monster.x, curr_monster.y))

        if player.x in range(curr_monster.x - 20, curr_monster.x + 20) and player.y == 630:
            outcome = np.random.randint(0, 100)
            if outcome < 20:
                curr_monster.attack(player)
        
        
        if player.x in range(curr_monster.x - 20, curr_monster.x + 20) and player.y < 610:
            outcome = np.random.randint(0, 100)
            if outcome > 20:   
                curr_monster.health -= 2000


        if monster_defeated:
            battle_mode = False
    

    screen.blit(location_surface, (20, 20))
    screen.blit(health_surface, (20, 40))
    screen.blit(weapon_surface, (20, 60))
    screen.blit(heals_surface, (20, 80))

    if not surface_main or not cave_main:
        screen.blit(curr_monster_surface, (1100, 20))
        screen.blit(curr_monster_health_surface, (1100, 40))
        screen.blit(curr_monster_power_surface, (1100, 60))
    

    # Ladder mechanics
    keys = pygame.key.get_pressed()
    if cave_basic and on_ladder:
        if keys[pygame.K_w]:
            player_position.y -= 200 * dt
        if keys[pygame.K_s]:
            player_position.y += 200 * dt

    if not cave_basic and on_ladder:
        if keys[pygame.K_s]:
            player_position.y += 100 * dt

    if keys[pygame.K_SPACE]:
        is_jumping = True

    if not cave_basic:
        if not is_jumping and not on_ladder:
            while player_position.y < 630:
                player_position.y += 1
            if player_position.y > 630:
                player_position.y = 630

    if cave_basic:
        if not is_jumping and not on_ladder:
            while player_position.y < 630:
                player_position.y += 1
            if player_position.y > 630:
                player_position.y = 630


    if keys[pygame.K_h]:
        if heals > 0:
            player.heal()
            heals -= 1


    # Jumping mechanic
    if is_jumping:
        player_position.y -= y_velocity
        y_velocity -= gravity
        if y_velocity < -jump_height:
            is_jumping = False
            y_velocity = jump_height

    # Moving left and right
    if keys[pygame.K_a]:
        player_position.x -= 300 * dt
    if keys[pygame.K_d]:
        player_position.x += 300 * dt


    # Teleport to opposite side when going off-screen
    if player_position[1] > 740:
        player_position[1] = -99
    if player_position[1] < -120:
        player_position[1] = 630


    if player_position[0] > 1280:
        player_position[0] = -99
        if not cave_basic:
            surface_sideroom += 1
        if cave_basic:
            cave_sideroom += 1
    if player_position[0] < -99:
        player_position[0] = 1280
        if not cave_basic:
            surface_sideroom -= 1
        if cave_basic:
            cave_sideroom -= 1



    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
