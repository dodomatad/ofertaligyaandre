import asyncio
import edge_tts
from mutagen.mp3 import MP3

text = "¡Hola, mi corazón! ¡Ay, qué felicidad me da saludarte! Mira, ya preparé con muchísimo cariño tu plan personalizado para estas navidades. Te va a encantar porque vas a aprender a tejer tus primeras mini muñequitas en menos de dos horas, paso a pasito, sin enredarte con términos difíciles. Échale un ojito aquí abajo a todo lo que incluye tu kit, ¡y empezamos juntas hoy mismo!"

voices = [
    ("es-CO-SalomeNeural", "assets/test-salome.mp3"),
    ("es-MX-DaliaNeural", "assets/test-dalia.mp3"),
    ("es-PE-CamilaNeural", "assets/test-camila.mp3"),
    ("es-US-PalomaNeural", "assets/test-paloma.mp3")
]

async def generate():
    for voice, out_path in voices:
        communicate = edge_tts.Communicate(text, voice, rate="+0%", pitch="+0Hz")
        await communicate.save(out_path)
        audio = MP3(out_path)
        print(f"Voice: {voice} -> Duration: {audio.info.length:.2f}s -> Saved to {out_path}")

if __name__ == '__main__':
    asyncio.run(generate())
