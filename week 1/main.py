import pygame
import numpy as np
import random

# Configuration

WIDTH = 800
HEIGHT = 800

BOWL_CENTER = np.array([WIDTH / 2, HEIGHT / 2], dtype=float)
BOWL_RADIUS = 300

# Start with 1 ball (Part A/B), then 2 (Section II). Many balls is the bonus.
NUM_PARTICLES = 1
PARTICLE_RADIUS = 12
PARTICLE_SPEED = 150.0

# Pixels per second squared, not m/s^2: the arena is 300 px wide, so a literal
# 9.8 would be far too slow to see. Note that +y points DOWN on screen.
GRAVITY = 900.0

# e_w, the wall restitution coefficient.
# 1.0 = no energy lost on a bounce, < 1.0 = each bounce comes back lower.
WALL_RESTITUTION = 1.0

FPS = 60

# Particle

class Particle:
    def __init__(self, position, velocity, radius=PARTICLE_RADIUS):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius

    def update(self, dt):
        # TODO (GRAVITY TASK):
        # Apply gravitational acceleration to the particle.
        # Do it HERE, before the position step below, so that the position is
        # moved using the already-updated velocity.
        #
        # Hint:
        # Try to think about the physical relation,
        # how you would define acceleration, what would it affect in the particles.

        self.position += self.velocity * dt

        # Keep the particle inside the circular bowl.
        offset = self.position - BOWL_CENTER
        distance = np.linalg.norm(offset)

        max_distance = BOWL_RADIUS - self.radius

        if distance > max_distance:
            # TODO (WALL COLLISION TASK):
            # The particle has left the bowl. Two things need fixing here.
            #
            # Hint:
            # First, where should the particle actually be? It has strayed past
            # the wall, so put it back on the boundary it should have stopped at.
            # `offset` points from the centre of the bowl out to the particle,
            # so what does it become once you strip its length away?
            #
            # Second, what happens to the velocity? Only the part of it pointing
            # along that outward direction should change, the part sliding along
            # the wall carries on untouched. WALL_RESTITUTION decides how much of
            # the incoming speed survives the bounce.
            pass

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (220, 220, 220),
            self.position.astype(int),
            self.radius
        )

# Collision Handling

def handle_collisions(particles):
    """
    Detect and resolve collisions between particles.

    TODO:
    Implement particle-particle collision handling here.
    Assume a perfectly elastic collison.

    Hint:
    First plan out a collision, what are the required conditions for a collision,
    what parameters of a particle does it affect?
    what happens to a particle after a collision?
    how would one make it happen for every particle?

    """
    pass

# Utility Functions


def random_position_in_bowl():
    """
    Generate a random position such that the entire particle
    starts inside the circular bowl.
    """

    max_distance = BOWL_RADIUS - PARTICLE_RADIUS

    while True:
        x = random.uniform(-max_distance, max_distance)
        y = random.uniform(-max_distance, max_distance)

        position = BOWL_CENTER + np.array([x, y])

        if np.linalg.norm(position - BOWL_CENTER) <= max_distance:
            return position


def random_velocity():
    """
    Generate a random velocity with approximately
    PARTICLE_SPEED magnitude.
    """

    angle = random.uniform(0, 2 * np.pi)

    return np.array([
        np.cos(angle),
        np.sin(angle)
    ]) * PARTICLE_SPEED

# Create Particles

particles = []

for _ in range(NUM_PARTICLES):
    particle = Particle(
        random_position_in_bowl(),
        # Random starting velocity. Replace with [0.0, 0.0] to drop the ball
        # from rest, which is what you want for the e_w checks in Part B.
        random_velocity()
    )

    particles.append(particle)

# Pygame Setup

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Particle Simulation")

clock = pygame.time.Clock()

running = True

# Main Simulation Loop

while running:

    # Events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Time

    dt = clock.tick(FPS) / 1000.0

    # Update

    for particle in particles:
        particle.update(dt)

    # TODO:
    # This is the crux of your simulation loop,
    # use the function you wrote earlier to handle interactions between particles.

    # Render
    screen.fill((20, 20, 25))

    pygame.draw.circle(
        screen,
        (180, 180, 180),
        BOWL_CENTER.astype(int),
        BOWL_RADIUS,
        width=3
    )

    # Particles
    for particle in particles:
        particle.draw(screen)

    pygame.display.flip()

# Cleanup

pygame.quit()