import asyncio
import edge_tts
import subprocess
from mutagen.mp3 import MP3
import soundfile as sf
import numpy as np

text = (
    "¡Hola mi corazón! Ay, qué felicidad me da saludarte. "
    "Mira, ya preparé con muchísimo cariño tu plan personalizado con todo el kit navideño de las mini muñequitas. "
    "Te va a encantar porque vas a aprender a tejerlas en menos de dos horas, paso a pasito y sin enredarte. "
    "Échale un ojito aquí abajo a todo lo que incluye tu kit, ¡y empezamos juntas hoy mismo!"
)

async def generate_clean_audio():
    raw_mp3 = "assets/raw_voice.mp3"
    final_mp3 = "assets/audio-lygia.mp3"
    
    # 1. Gerar com SalomeNeural em velocidade 100% natural humana (+0% ou +2%)
    comm = edge_tts.Communicate(text, "es-CO-SalomeNeural", rate="+2%", pitch="+0Hz")
    await comm.save(raw_mp3)
    
    # 2. Normalização EBU R128 profissional com loudness ideal para celular (-14 LUFS)
    # Sem corte abafado em 11kHz, a 44100Hz e 192k de bitrate
    cmd = [
        "ffmpeg", "-y", "-i", raw_mp3,
        "-af", "loudnorm=I=-14:LRA=7:TP=-1.0",
        "-ar", "44100",
        "-b:a", "192k",
        final_mp3
    ]
    subprocess.run(cmd, check=True)
    
    # Inspecionar áudio final
    data, sr = sf.read(final_mp3)
    length = MP3(final_mp3).info.length
    print(f"Duração: {length:.2f}s (exibição: {round(length)}s)")
    print(f"Taxa de amostragem: {sr} Hz")
    print(f"Max peak: {np.max(np.abs(data)):.3f}")
    print(f"RMS: {np.sqrt(np.mean(data**2)):.3f}")

if __name__ == '__main__':
    asyncio.run(generate_clean_audio())
