"""make.fun bounty: Sum up 23 November's world news in one image.
Renders one image summarizing the day's top world headlines. Runs offline with Pillow only.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 1200
NAVY = (18, 24, 43); RED = (227, 52, 47); WHITE = (245, 246, 250)
GREY = (150, 158, 178); AMBER = (240, 180, 60)

def font(size, bold=False):
    path = "/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf" % ("-Bold" if bold else "")
    return ImageFont.truetype(path, size)

NEWS = [
    ("UKRAINE", "Ukraine naval drones sink Russian warship Merkury in Benghazi, Libya", RED),
    ("SAUDI ARABIA", "Houthis attack Rabigh oil refinery as conflict widens", AMBER),
    ("IRAN / US", "Iran vows 'every means' to counter US blockade of Hormuz", AMBER),
    ("EUROPEAN UNION", "EU rolls out new sanctions package to starve Russia's war funding", RED),
    ("KOREA", "Russian aircraft intrude into South Korean air defense zone", GREY),
    ("SUDAN", "Drone strikes kill four in Khartoum; UN building damaged", GREY),
]

img = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 150], fill=(10, 14, 28))
d.rectangle([0, 148, W, 156], fill=RED)
d.text((70, 42), "THE WORLD IN ONE IMAGE", font=font(64, True), fill=WHITE)
d.text((70, 108), "Monday, 23 November 2026  -  six stories that moved the world", font=font(28), fill=GREY)

y = 220
for tag, headline, color in NEWS:
    d.rounded_rectangle([70, y, 330, y + 52], 12, fill=color)
    tw = d.textlength(tag, font=font(24, True))
    d.text((200 - tw/2, y + 12), tag, font=font(24, True), fill=(12, 12, 12))
    # wrap headline
    words = headline.split(); lines = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font(40)) > 1150: lines.append(cur); cur = w_
        else: cur = t
    lines.append(cur)
    ly = y
    for ln in lines:
        d.text((370, ly), ln, font=font(40), fill=WHITE); ly += 54
    d.line([70, ly + 22, 1530, ly + 22], fill=(60, 68, 92), width=2)
    y = ly + 52

d.rectangle([0, H - 110, W, H], fill=(10, 14, 28))
d.text((70, H - 78), "War at sea - Oil under fire - Sanctions tighten", font=font(32, True), fill=AMBER)
d.text((1130, H - 72), "make.fun bounty entry", font=font(24), fill=GREY)
img.save("news-image-20261123.png")
print("saved", img.size)
