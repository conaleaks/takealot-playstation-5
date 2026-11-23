import urllib.request, io, os
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter

dest_dir = '/Users/green/Downloads/Takealot PlayStation 5/imagens'
os.makedirs(dest_dir, exist_ok=True)

headers = {'User-Agent': 'TakealotResearch/1.0 (https://takealot.co.za; dev@takealot.co.za) Python-urllib'}

# 1. Fetch PS5 + Controller
ps5_url = 'https://upload.wikimedia.org/wikipedia/commons/1/1b/PlayStation_5_and_DualSense_with_transparent_background.png'
req = urllib.request.Request(ps5_url, headers=headers)
with urllib.request.urlopen(req, timeout=25) as resp:
    ps5_raw = Image.open(io.BytesIO(resp.read())).convert('RGBA')

# 2. Fetch GTA 6 Artwork
gta6_url = 'https://upload.wikimedia.org/wikipedia/en/4/46/Grand_Theft_Auto_VI.png'
req = urllib.request.Request(gta6_url, headers=headers)
with urllib.request.urlopen(req, timeout=15) as resp:
    gta6_raw = Image.open(io.BytesIO(resp.read())).convert('RGBA')

# Crop PS5
bbox = ps5_raw.split()[3].getbbox()
ps5_cropped = ps5_raw.crop(bbox) # 1545 x 3602

# =========================================================================
# HELPER: Make 3D GTA 6 PS5 Game Case
# =========================================================================
def make_ps5_game_case(width=340, height=480):
    case = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(case)
    
    # Outer rounded rectangle (dark border/case)
    draw.rounded_rectangle([0, 0, width-1, height-1], radius=14, fill=(245, 245, 248, 255), outline=(210, 215, 225, 255), width=2)
    
    # PS5 white header bar
    header_h = int(height * 0.14)
    draw.rounded_rectangle([2, 2, width-3, header_h], radius=10, fill=(255, 255, 255, 255))
    draw.rectangle([2, header_h-10, width-3, header_h], fill=(255, 255, 255, 255))
    
    # Draw "PlayStation 5" blue logo text or stylish bar
    draw.rectangle([16, header_h//2 - 4, 38, header_h//2 + 4], fill=(0, 55, 145, 255))
    draw.text((46, header_h//2 - 8), "PlayStation 5", fill=(0, 55, 145, 255))
    
    # GTA 6 artwork cover
    art_w = width - 8
    art_h = height - header_h - 6
    gta_resized = gta6_raw.resize((art_w, art_h), Image.Resampling.LANCZOS)
    case.paste(gta_resized, (4, header_h + 2), mask=gta_resized.split()[3] if gta_resized.mode=='RGBA' else None)
    
    # Add spine highlight and subtle gloss overlay
    draw.line([(6, header_h), (6, height-6)], fill=(255, 255, 255, 120), width=3)
    draw.line([(width-4, header_h), (width-4, height-6)], fill=(0, 0, 0, 60), width=2)
    
    return case

game_case = make_ps5_game_case(320, 460)

# =========================================================================
# IMAGE 1: HERO COMBO (PS5 Console + Controller + GTA 6 Case)
# =========================================================================
canvas1 = Image.new('RGB', (1000, 1000), (255, 255, 255))

# Scale PS5 so it fits nicely
ps5_hero = ps5_cropped.copy()
ps5_hero.thumbnail((540, 880), Image.Resampling.LANCZOS)

# Position PS5 on the left-center
canvas1.paste(ps5_hero, (80, 1000 - ps5_hero.height - 70), mask=ps5_hero.split()[3])

# Position GTA 6 Case on the right side next to console
case_hero = game_case.copy()
case_hero.thumbnail((420, 580), Image.Resampling.LANCZOS)
canvas1.paste(case_hero, (550, 360), mask=case_hero.split()[3])

# Add subtle drop shadow under game case
canvas1.save(os.path.join(dest_dir, 'ps5_gta6_1_hero.jpg'), 'JPEG', quality=95)
print('Saved ps5_gta6_1_hero.jpg')

# =========================================================================
# IMAGE 2: DUALSENSE CONTROLLER CLOSEUP
# =========================================================================
# Crop controller from bottom of ps5_cropped
# Controller is in lower 45% of ps5_cropped
ctrl_box = (0, int(ps5_cropped.height * 0.58), ps5_cropped.width, ps5_cropped.height)
controller_img = ps5_cropped.crop(ctrl_box)
# Get tighter bbox
ctrl_bbox = controller_img.split()[3].getbbox()
if ctrl_bbox:
    controller_img = controller_img.crop(ctrl_bbox)

canvas2 = Image.new('RGB', (1000, 1000), (255, 255, 255))
ctrl_scaled = controller_img.copy()
ctrl_scaled.thumbnail((860, 860), Image.Resampling.LANCZOS)
offset2 = ((1000 - ctrl_scaled.width) // 2, (1000 - ctrl_scaled.height) // 2)
canvas2.paste(ctrl_scaled, offset2, mask=ctrl_scaled.split()[3])
canvas2.save(os.path.join(dest_dir, 'ps5_gta6_2_controller.jpg'), 'JPEG', quality=95)
print('Saved ps5_gta6_2_controller.jpg')

# =========================================================================
# IMAGE 3: PS5 CONSOLE ALONE (Full Profile View)
# =========================================================================
canvas3 = Image.new('RGB', (1000, 1000), (255, 255, 255))
ps5_alone = ps5_cropped.copy()
ps5_alone.thumbnail((800, 900), Image.Resampling.LANCZOS)
offset3 = ((1000 - ps5_alone.width) // 2, (1000 - ps5_alone.height) // 2)
canvas3.paste(ps5_alone, offset3, mask=ps5_alone.split()[3])
canvas3.save(os.path.join(dest_dir, 'ps5_gta6_3_bundle_box.jpg'), 'JPEG', quality=95)
print('Saved ps5_gta6_3_bundle_box.jpg')

# =========================================================================
# IMAGE 4: GTA 6 OFFICIAL KEY ART / PACKSHOT
# =========================================================================
canvas4 = Image.new('RGB', (1000, 1000), (255, 255, 255))
gta_full_case = make_ps5_game_case(520, 740)
offset4 = ((1000 - gta_full_case.width) // 2, (1000 - gta_full_case.height) // 2)
canvas4.paste(gta_full_case, offset4, mask=gta_full_case.split()[3])
canvas4.save(os.path.join(dest_dir, 'ps5_gta6_4_gameplay.jpg'), 'JPEG', quality=95)
print('Saved ps5_gta6_4_gameplay.jpg')

print('ALL 4 PS5 + GTA 6 IMAGES CREATED IN HIGH RESOLUTION ON PURE WHITE BACKGROUND!')
