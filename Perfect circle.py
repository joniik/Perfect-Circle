import pyautogui
import math
import time

# piirrettävän ympyrän säde 
radius = 300

# Näytön koko pikseleissä
width, height = pyautogui.size()
centerpoint = (width // 2, height // 2)

# Hiiren liikutus keskelle näyttöä
pyautogui.moveTo(centerpoint, duration=2)

time.sleep(1)

Aloitusaika = time.time()
KestoLimit = 7.0
Tarkkuus = 100

while time.time() - Aloitusaika < KestoLimit:
    angle = (time.time() - Aloitusaika) * 450 / KestoLimit

    # Coordinaattejen laskeminen
    x = centerpoint[0] + int(radius * math.cos(math.radians(angle)))
    y = centerpoint[1] + int(radius * math.sin(math.radians(angle)))

    # Hiiren liikutus
    pyautogui.moveTo(x, y, duration=0.0005/Tarkkuus)

# Hiiren palautus keskelle ruutua ympyrän jälkeen
pyautogui.moveTo(centerpoint, duration=1)

print(width, height)
print(centerpoint)
