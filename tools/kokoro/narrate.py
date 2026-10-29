"""Render the DriveSmart NJ demo narration with Kokoro.

Default mix is af_heart + af_bella (0.6 / 0.4) at speed 1.08.
Edit LINES, then:

    python3 -m venv tools/kokoro/venv
    tools/kokoro/venv/bin/pip install -r tools/kokoro/requirements.txt
    bash tools/kokoro/download-models.sh
    tools/kokoro/venv/bin/python tools/kokoro/narrate.py

WAVs land in tools/kokoro/out/.
"""
import os
import sys

import soundfile as sf
from kokoro_onnx import EspeakConfig, Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

LINES = {
    "intro": "Hey! Meet DriveSmart NJ. Your new study buddy for the New Jersey knowledge test!",
    "stakes": "The real test? Fifty questions. And you need eighty percent to pass.",
    "s1": "Everything's right on your home screen. Practice topics, study guides, and full mock tests.",
    "s2": "Practice by topic, like road signs. Tap an answer, and boom! Instant feedback, plus why every wrong answer is wrong.",
    "s3": "Feeling ready? Take a full, timed, fifty-question mock test. Flag the tricky ones, skip ahead, and review it all before you submit.",
    "s4": "Stuck on a rule? Just ask the AI tutor. It's built around the New Jersey Driver Manual.",
    "s5": "And study the whole manual, chapter by chapter. Even offline!",
    "outro": "DriveSmart NJ. Your permit test is the next exit. Available now on the App Store!",
}

cfg = EspeakConfig(
    lib_path="/opt/homebrew/lib/libespeak-ng.dylib",
    data_path="/opt/homebrew/share/espeak-ng-data",
)
k = Kokoro(
    os.path.join(HERE, "models/kokoro-v1.0.onnx"),
    os.path.join(HERE, "models/voices-v1.0.bin"),
    espeak_config=cfg,
)
mix = float(sys.argv[1]) if len(sys.argv) > 1 else 0.6
voice = mix * k.get_voice_style("af_heart") + (1 - mix) * k.get_voice_style("af_bella")
speed = float(sys.argv[2]) if len(sys.argv) > 2 else 1.08

for name, text in LINES.items():
    samples, sr = k.create(text, voice=voice, speed=speed, lang="en-us")
    path = os.path.join(OUT, f"{name}.wav")
    sf.write(path, samples, sr)
    print(f"{name:7} {len(samples) / sr:5.2f}s  {path}")
