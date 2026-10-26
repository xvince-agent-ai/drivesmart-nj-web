# Kokoro narration for the DriveSmart NJ demo

This is the voice setup used for `public/video/DriveSmartNJ-Demo.mp4`. The script lives in `narrate.py` as `LINES`. Edit that dict, regenerate the WAVs, then remux the video.

Models are about 337 MB and are **not** in git. Copy them from a previous machine or download them:

```bash
brew install espeak-ng
python3 -m venv tools/kokoro/venv
tools/kokoro/venv/bin/pip install -r tools/kokoro/requirements.txt
bash tools/kokoro/download-models.sh
tools/kokoro/venv/bin/python tools/kokoro/narrate.py
```

Optional mix and speed: `narrate.py 0.6 1.08` (heart/bella mix, speaking rate).

Needs Homebrew `espeak-ng` so Kokoro can find `/opt/homebrew/lib/libespeak-ng.dylib`.
