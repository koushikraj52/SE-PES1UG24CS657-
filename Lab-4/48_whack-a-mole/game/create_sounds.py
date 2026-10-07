import wave
import math
import struct
import os

SAMPLE_RATE = 44100
AMPLITUDE = 16000

os.makedirs("game/sounds", exist_ok=True)


def create_sound(filename, frequency, duration):
    path = os.path.join("game", "sounds", filename)

    with wave.open(path, "w") as sound:
        sound.setnchannels(1)
        sound.setsampwidth(2)
        sound.setframerate(SAMPLE_RATE)

        frames = []

        for i in range(int(SAMPLE_RATE * duration)):
            value = int(
                AMPLITUDE
                * math.sin(
                    2 * math.pi * frequency * i / SAMPLE_RATE
                )
            )

            frames.append(struct.pack("<h", value))

        sound.writeframes(b"".join(frames))


create_sound("whack.wav", 700, 0.12)
create_sound("miss.wav", 180, 0.15)
create_sound("game_over.wav", 300, 0.45)

print("Sound files created successfully.")