# Falling marigold petals -> heart (Day 14 of 100)

1500 marigold petals fall from the sky and land as a heart, drawn in Python with matplotlib.
Day 14 of the #100DaysDailyReelChallenge by @hack.n.code.

```
pip install numpy matplotlib
python petals.py     # needs ffmpeg; writes petals.mp4 (1080x1920, 17 s)
```

The heart is the implicit curve (x^2 + y^2 - 1)^3 - x^2 y^3 < 0; each petal gets a random landing spot inside it,
a random delay, a swaying fall with ease-out, and the whole heart beats once it has settled.
