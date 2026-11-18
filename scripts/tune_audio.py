import asyncio
import edge_tts
from mutagen.mp3 import MP3

text = "¡Hola mi cielo! Ay, qué emoción me da saludarte. Mira, ya preparé con muchísimo cariño tu plan personalizado con el kit de las mini muñequitas. Te va a encantar porque las vas a tejer en menos de dos horas, paso a pasito y sin enredarte. Échale un ojito aquí abajo a todo lo que te preparé, ¡y empezamos juntas hoy mismo!"

async def test_tuning():
    rates = ["+0%", "+3%", "+5%"]
    voices = ["es-CO-SalomeNeural", "es-MX-DaliaNeural", "es-PE-CamilaNeural"]
    for v in voices:
        for r in rates:
            out = f"assets/tune_{v.split('-')[1]}_{r.replace('+', '').replace('%', '')}.mp3"
            comm = edge_tts.Communicate(text, v, rate=r)
            await comm.save(out)
            d = MP3(out).info.length
            print(f"Voice: {v} | Rate: {r} -> {d:.2f}s ({round(d)}s)")

if __name__ == '__main__':
    asyncio.run(test_tuning())
