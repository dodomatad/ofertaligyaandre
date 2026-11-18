import asyncio
import edge_tts
import subprocess
import os
from mutagen.mp3 import MP3

text = (
    "¡Hola mi corazón! Ay, qué felicidad me da saludarte. "
    "Mira, ya preparé con muchísimo cariño tu plan personalizado con todo el kit navideño de las mini muñequitas. "
    "Te va a encantar porque vas a aprender a tejerlas en menos de dos horas, paso a pasito y sin enredarte. "
    "Échale un ojito aquí abajo a todo lo que incluye tu kit, ¡y empezamos juntas hoy mismo!"
)

async def create_audio():
    raw_mp3 = "assets/raw_salome.mp3"
    final_mp3 = "assets/audio-lygia.mp3"
    
    # +11% produz exatamente 22.0 segundos de duração
    communicate = edge_tts.Communicate(text, "es-CO-SalomeNeural", rate="+11%", pitch="+0Hz")
    await communicate.save(raw_mp3)
    
    cmd = [
        "ffmpeg", "-y", "-i", raw_mp3,
        "-af", "highpass=f=120,lowpass=f=11000,acompressor=threshold=-18dB:ratio=2.5:attack=10:release=100",
        "-b:a", "64k",
        final_mp3
    ]
    subprocess.run(cmd, check=True)
    
    info = MP3(final_mp3).info
    print(f"Áudio final gerado com sucesso!")
    print(f"Duração exata: {info.length:.2f}s (arredondado para exibição: {round(info.length)}s)")

if __name__ == '__main__':
    asyncio.run(create_audio())
