import pygame
import numpy as np
import random

# Configuration

WIDTH = 800
HEIGHT = 800

BOWL_CENTER = np.array([WIDTH / 2, HEIGHT / 2], dtype=float)
BOWL_RADIUS = 300

NUM_PARTICLES = 50
PARTICLE_RADIUS = 6
PARTICLE_SPEED = 150.0

FPS = 60

# Particle

class Particle:
    def __init__(self, position, velocity, radius=PARTICLE_RADIUS):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.radius = radius

    def update(self, dt):
        self.position += self.velocity * dt

        # TODO (GRAVITY TASK):
        # Apply gravitational acceleration to the particle.
        #
        # Hint:
        # Try to think about the physical relation,
        # how you would define acceleration, what would it affect in the particles.

        # Keep the particle inside the circular bowl.
        offset = self.position - BOWL_CENTER
        distance = np.linalg.norm(offset)

        max_distance = BOWL_RADIUS - self.radius

        if distance > max_distance:
            # Move the particle back onto the valid boundary.
            normal = offset / distance
            self.position = BOWL_CENTER + normal * max_distance

            # Reflect the velocity across the boundary normal.
            # v' = v - 2(v · n)n
            self.velocity = (
                self.velocity
                - 2 * np.dot(self.velocity, normal) * normal
            )

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