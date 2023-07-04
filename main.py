import pygame
import os
import moviepy.editor as mp
from itertools import cycle

# Window
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Star Rail Matching Game")
FPS = 60

# Video BG
video_path = os.path.join("assets/background", "bg.mp4")
video = mp.VideoFileClip(video_path)
video = video.resize((WIDTH, HEIGHT))

# Create an iterable to cycle through video frames
frames = cycle(video.iter_frames())

# Drawing to the window


def draw_window():
    # Get the next frame from the cycle
    frame = next(frames)

    # Convert frame to Pygame surface
    pygame_frame = pygame.surfarray.make_surface(
        frame)

    # Resize to match screen dimensions
    pygame_frame = pygame.transform.scale(pygame_frame, (WIDTH, HEIGHT))

    # Blit to screen
    WIN.blit(pygame_frame, (0, 0))

    # update display
    pygame.display.update()

# Main loop


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
