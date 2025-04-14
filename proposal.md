# Motorcycle **Rev Up**

## Repository
<https://github.com/Nyx1325/FinalProject_LE.git>

## Description
1-2 sentence description of what it will do and how it relevant to media and digital arts.

## Features
- Particle trail
	- Same as we've learn but make it follow the motorcyles by adding the start point on both individualy & connecting it to the grid layout in order to keep them within a clear path. Also, avoid the dead function to keep the particles in place without fading them or deleting before the end of the game.
- Collision
	- Creating a way to signal the code when there's been an attempt/overlap of characters (not obstacles) and/or particle trails thus signalling a game over/winner title.
- Randomized obstacles' location 
	- Each restart or new window, the obstacles will be in different locations following the grid layout by having random function based on x & y points on specific collumns.

## Challenges
- Add some sort of collision aspect when player hits opposing smoke trail and bounce when hitting an obstacle
- See how to alter the randomization for CPU movement & obstacle placement.
- See how to keep the particle trail within the grid patterns to show clear path of both characters
- Adding a Game Over/Winner title based off a collision
- Adding a restart button in Game over/ Winner title

## Outcomes
Ideal Outcome:
- Player/CPU moves motorcycles that leaves a smoke trail based on direction & if either one collides with the trail, it will lead to a Game Over/Winner title with a restart button. With each restart/new window, obstacles will change locations and player/cpu will bounce if hitting them.

Minimal Viable Outcome:
- Player/CPU moves motorcycles that leaves a smoke trail based on direction & if either collides with the trail, the game will stop & restart itself. Obstacles will be in fixed locations & if the player/cpu hits them, they will not be able to move over or under the obstacle making them go around it.

## Milestones

- Week 1
  1. Motorcycle & Background design
  2. Grid layout

- Week 2
  1. Randomize the motion of CPU motorcyle
  2. Particle trails & Collisions

- Week N (Final)
  1. Randomize obstcales & Game Over/Winner & Restart
  2. Fix any bugs & Optimize
