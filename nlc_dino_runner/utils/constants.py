import pygame
import os
from pygame import mixer

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

DARK_MODE = "dark"
LIGHT_MODE = "light"

RUNNING = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Dark.png")),
    ]
}

RUNNING_SHIELD = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1ShieldDark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Dark.png")),
    ]
}

RUNNING_HAMMER = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1HammerDark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2HammerDark.png")),
    ]
}

JUMPING = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png")),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpDark.png"))
}

JUMPING_SHIELD = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png")),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShieldDark.png"))
}

JUMPING_HAMMER = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png")),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammerDark.png"))
}

DUCKING = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Dark.png")),
    ]
}

DUCKING_SHIELD = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1ShieldDark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Dark.png")),
    ]
}
DUCKING_HAMMER = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1HammerDark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2HammerDark.png")),
    ]
}

DEAD = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png")),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDeadDark.png"))
}

SMALL_CACTUS = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3Dark.png")),
    ]
}

LARGE_CACTUS = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3Dark.png")),
    ]
}

BIRD = {
    LIGHT_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
    ],
    DARK_MODE: [
        pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1Dark.png")),
        pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2Dark.png")),
    ]
}

CLOUD = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/CloudDark.png'))
}

SHIELD = dict.fromkeys([LIGHT_MODE, DARK_MODE], pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')))

HAMMER = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/hammerDark.png'))
}

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png')),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeartDark.png'))
}

GAME_OVER = {
    LIGHT_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png')),
    DARK_MODE: pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOverDark.png'))
}

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

pygame.mixer.init()

SOUND_SHIELD = mixer.Sound("SoundEffects/Efecto de sonido Shield.mp3")
SOUND_HAMMER = mixer.Sound("SoundEffects/Efecto de sonido Hammer.mp3")
SOUND_GAME_LOOP = mixer.Sound("SoundEffects/Efecto de sonido Game_Loop.mp3")
SOUND_COLLISION = mixer.Sound("SoundEffects/Efecto de sonido Collision.mp3")
SOUND_HAMMER_COLLISION = mixer.Sound("SoundEffects/Efecto de sonido Hammer_Collision.mp3")
SOUND_GAME_OVER = mixer.Sound("SoundEffects/Efecto de sonido Game_over.mp3")

