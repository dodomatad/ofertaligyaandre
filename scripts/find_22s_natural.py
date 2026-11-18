import asyncio
import edge_tts
from mutagen.mp3 import MP3

variants = [
    # V1: 
    ("V1", "¡Hola mi corazón! Qué felicidad me da saludarte. Ya preparé tu plan personalizado con todo el kit navideño de las mini muñequitas. Vas a aprender a tejerlas en menos de dos horas, paso a pasito y sin enredarte. Échale un ojito aquí abajo a tu kit, ¡y empezamos juntas hoy!"),
    # V2:
    ("V2", "¡Hola mi cielo! Ay, qué felicidad me da saludarte. Mira, ya preparé con muchísimo cariño tu plan personalizado de las mini muñequitas. Te va a encantar porque las tejes en menos de dos horas, sin enredarte. Échale un ojito aquí abajo a todo lo que incluye tu kit, ¡y empezamos hoy mismo!"),
    # V3:
    ("V3", "¡Hola mi corazón! Ay, qué emoción saludarte. Ya preparé con mucho cariño tu plan personalizado con el kit navideño de las mini muñequitas. Vas a aprender a tejerlas en menos de dos horas, paso a pasito y sin enredarte. Revisa aquí abajo todo lo que incluye tu kit, ¡y empezamos juntas hoy mismo!")
]

async def test():
    for name, t in variants:
        out = f"assets/test_{name}.mp3"
        comm = edge_tts.Communicate(t, "es-CO-SalomeNeural", rate="+0%")
        await comm.save(out)
        d = MP3(out).info.length
        print(f"{name}: {d:.2f}s (Round: {round(d)}s)")

if __name__ == '__main__':
    asyncio.run(test())
