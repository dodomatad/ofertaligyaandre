import subprocess
from mutagen.mp3 import MP3
import soundfile as sf
import numpy as np

final_mp3 = "assets/audio-lygia.mp3"
raw_mp3 = "assets/test_V3.mp3"

cmd = [
    "ffmpeg", "-y", "-i", raw_mp3,
    "-af", "loudnorm=I=-14:LRA=7:TP=-1.0",
    "-ar", "44100",
    "-b:a", "192k",
    final_mp3
]
subprocess.run(cmd, check=True)

data, sr = sf.read(final_mp3)
length = MP3(final_mp3).info.length
print(f"Final audio saved to {final_mp3}")
print(f"Duration: {length:.2f}s (Round: {round(length)}s)")
print(f"Sample rate: {sr} Hz")
print(f"Max peak: {np.max(np.abs(data)):.3f}")
print(f"RMS: {np.sqrt(np.mean(data**2)):.3f}")
