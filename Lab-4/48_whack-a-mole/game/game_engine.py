import pygame
import random
import os
from .hole import Hole

# Game Engine

DARK_BROWN = (60, 40, 20)
MOLE_BROWN = (140, 95, 55)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class GameEngine:
    def __init__(self, width, height, rows=3, cols=3):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols

        # Initialize sound system
        pygame.mixer.init()

        # Load sound effects
        sounds_folder = os.path.join(
            os.path.dirname(__file__),
            "sounds"
        )

        self.whack_sound = pygame.mixer.Sound(
            os.path.join(sounds_folder, "whack.wav")
        )

        self.miss_sound = pygame.mixer.Sound(
            os.path.join(sounds_folder, "miss.wav")
        )

        self.game_over_sound = pygame.mixer.Sound(
            os.path.join(sounds_folder, "game_over.wav")
        )

        self.holes = []
        self._create_holes()

        self.round_seconds = 30
        self.time_left_frames = self.round_seconds * 60

        self.score = 0
        self.misses = 0

        self.font = pygame.font.SysFont("Arial", 28)

        self.game_over = False
        self.exit_requested = False
        self.game_over_sound_played = False

        # Default difficulty
        self.difficulty = "Medium"
        self.set_difficulty("Medium")

    def _create_holes(self):
        self.holes = []

        spacing_x = self.width // (self.cols + 1)
        spacing_y = (self.height - 80) // (self.rows + 1)

        for r in range(self.rows):
            for c in range(self.cols):
                cx = spacing_x * (c + 1)
                cy = 80 + spacing_y * (r + 1)
                self.holes.append(Hole(cx, cy))

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

        if difficulty == "Easy":
            self.spawn_chance = 0.012
            self.mole_up_frames = 60

        elif difficulty == "Medium":
            self.spawn_chance = 0.02
            self.mole_up_frames = 45

        elif difficulty == "Hard":
            self.spawn_chance = 0.035
            self.mole_up_frames = 30

    def reset_game(self, difficulty):
        self.set_difficulty(difficulty)

        self.score = 0
        self.misses = 0
        self.time_left_frames = self.round_seconds * 60
        self.game_over = False
        self.exit_requested = False
        self.game_over_sound_played = False

        self._create_holes()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.exit_requested = True
            return

        # Task 3: Difficulty selection after Game Over
        if self.game_over and event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                self.reset_game("Easy")

            elif event.key == pygame.K_2:
                self.reset_game("Medium")

            elif event.key == pygame.K_3:
                self.reset_game("Hard")

            elif event.key == pygame.K_4:
                self.exit_requested = True

            return

        if not self.game_over and event.type == pygame.MOUSEBUTTONDOWN:
            self._handle_click(event.pos)

    def _handle_click(self, pos):
        hit_something = False

        # Task 1: Stop after the first successful whack.
        for hole in self.holes:
            if hole.rect().collidepoint(pos):
                if hole.whack():
                    self.score += 1
                    hit_something = True

                    # Task 4: Successful whack sound
                    self.whack_sound.play()

                    break

        if not hit_something:
            self.misses += 1

            # Task 4: Missed click sound
            self.miss_sound.play()

    def handle_input(self):
        pass

    def update(self):
        if self.game_over:
            return

        self.time_left_frames -= 1

        if self.time_left_frames <= 0:
            self.game_over = True

            # Task 4: Play game-over sound once
            if not self.game_over_sound_played:
                self.game_over_sound.play()
                self.game_over_sound_played = True

            return

        for hole in self.holes:
            hole.update()

            if not hole.active and random.random() < self.spawn_chance:
                hole.pop_up(self.mole_up_frames)

    def render(self, screen):
        # Draw holes and moles
        for hole in self.holes:
            pygame.draw.circle(
                screen,
                DARK_BROWN,
                (hole.center_x, hole.center_y),
                40
            )

            if hole.active:
                pygame.draw.circle(
                    screen,
                    MOLE_BROWN,
                    (hole.center_x, hole.center_y),
                    32
                )

        # Score
        score_text = self.font.render(
            f"Score: {self.score}",
            True,
            BLACK
        )
        screen.blit(score_text, (10, 10))

        # Timer
        seconds_left = max(0, self.time_left_frames // 60)

        timer_text = self.font.render(
            f"Time: {seconds_left}s",
            True,
            BLACK
        )

        screen.blit(
            timer_text,
            (self.width - 140, 10)
        )

        # Task 2 + Task 3: Game Over screen
        if self.game_over:

            overlay = pygame.Surface(
                (self.width, self.height)
            )
            overlay.set_alpha(190)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            game_over_font = pygame.font.SysFont(
                "Arial",
                48,
                bold=True
            )

            score_font = pygame.font.SysFont(
                "Arial",
                30
            )

            option_font = pygame.font.SysFont(
                "Arial",
                23
            )

            game_over_text = game_over_font.render(
                "GAME OVER",
                True,
                WHITE
            )

            final_score_text = score_font.render(
                f"Final Score: {self.score}",
                True,
                WHITE
            )

            difficulty_text = score_font.render(
                "Choose Difficulty",
                True,
                WHITE
            )

            easy_text = option_font.render(
                "1 - Easy",
                True,
                WHITE
            )

            medium_text = option_font.render(
                "2 - Medium",
                True,
                WHITE
            )

            hard_text = option_font.render(
                "3 - Hard",
                True,
                WHITE
            )

            exit_text = option_font.render(
                "4 - Exit",
                True,
                WHITE
            )

            screen.blit(
                game_over_text,
                game_over_text.get_rect(
                    center=(
                        self.width // 2,
                        100
                    )
                )
            )

            screen.blit(
                final_score_text,
                final_score_text.get_rect(
                    center=(
                        self.width // 2,
                        170
                    )
                )
            )

            screen.blit(
                difficulty_text,
                difficulty_text.get_rect(
                    center=(
                        self.width // 2,
                        240
                    )
                )
            )

            screen.blit(
                easy_text,
                easy_text.get_rect(
                    center=(
                        self.width // 2,
                        290
                    )
                )
            )

            screen.blit(
                medium_text,
                medium_text.get_rect(
                    center=(
                        self.width // 2,
                        330
                    )
                )
            )

            screen.blit(
                hard_text,
                hard_text.get_rect(
                    center=(
                        self.width // 2,
                        370
                    )
                )
            )

            screen.blit(
                exit_text,
                exit_text.get_rect(
                    center=(
                        self.width // 2,
                        410
                    )
                )
            )