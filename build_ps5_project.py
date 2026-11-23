import os, re, json

BASE_DIR = "/Users/green/Downloads/Takealot PlayStation 5"

HERO_CDN = "https://iili.io/oKDz7M7.jpg"
CONTROLLER_CDN = "https://iili.io/oKDz08b.jpg"
CONSOLE_CDN = "https://iili.io/oKDzVtV.jpg"
CASE_CDN = "https://iili.io/oKDzhMP.jpg"

HERO_TITLE = "Sony PlayStation 5 Slim 1TB Console + Grand Theft Auto VI Bundle"
HERO_MODEL = "CFI-2000A01-GTA6"
HERO_PRICE = "3,299"
HERO_PRICE_NUM = 3299
HERO_OLD_PRICE = "R 14,999"
STEP3_PRICE = 349

# 1. Update package.json
pkg_path = os.path.join(BASE_DIR, "package.json")
if os.path.exists(pkg_path):
    with open(pkg_path, "r") as f:
        pkg = json.load(f)
    pkg["name"] = "takealot-playstation-5"
    pkg["description"] = "Takealot South Africa PlayStation 5 + GTA 6 Storefront & Automated Order Engine"
    with open(pkg_path, "w") as f:
        json.dump(pkg, f, indent=2)
    print("Updated package.json")

# 2. Update .env and .env.example
for env_name in [".env", ".env.example"]:
    epath = os.path.join(BASE_DIR, env_name)
    content = f"""PORT=3025
NODE_ENV=production
STORE_NAME=Takealot PlayStation 5
GREENSEND_API_KEY=greensend_live_9b4a1f68e2
GREENSEND_SENDER_EMAIL=orders@takealot.co.za
DEFAULT_PRODUCT_TITLE=Sony PlayStation 5 Slim 1TB Console + Grand Theft Auto VI Bundle
DEFAULT_PRODUCT_PRICE=3299
DEFAULT_PRODUCT_IMAGE={HERO_CDN}
"""
    with open(epath, "w") as f:
        f.write(content)
    print(f"Updated {env_name}")

# 3. Clean and initialize data/
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)
with open(os.path.join(data_dir, "orders.json"), "w") as f:
    f.write("{}")
with open(os.path.join(data_dir, "abandoned_checkouts.json"), "w") as f:
    f.write("{}")
print("Initialized data/ storage files")

# 4. Update server.js
server_path = os.path.join(BASE_DIR, "server.js")
with open(server_path, "r", encoding="utf-8") as f:
    s = f.read()

# Port replacement
s = re.sub(r'const PORT = process\.env\.PORT \|\| \d+;', 'const PORT = process.env.PORT || 3025;', s)
s = re.sub(r'http://localhost:\d+', 'http://localhost:3025', s)

# Titles and products
s = s.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
s = s.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
s = s.replace("Samsung 300L Bottom Freezer Refrigerator", HERO_TITLE)
s = s.replace("Samsung 300L Refrigerator", HERO_TITLE)
s = s.replace("Bottom Freezer Refrigerator", "PlayStation 5 Console + GTA 6")
s = s.replace("Refrigerator", "PlayStation 5")
s = s.replace("refrigerator", "PlayStation 5")

# Prices
s = s.replace("2199", "3299")
s = s.replace("2,199", "3,299")
s = s.replace("9999", "14999")
s = s.replace("9,999", "14,999")
s = s.replace("7800", "11700")
s = s.replace("7,800", "11,700")
s = s.replace("297", "349")

# Image URLs
s = re.sub(r'https://iili\.io/[a-zA-Z0-9_\-]+\.(?:jpg|png)', HERO_CDN, s)
s = s.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
s = s.replace("imagens/samsung_fridge_2_open.jpg", "imagens/ps5_gta6_2_controller.jpg")
s = s.replace("imagens/samsung_fridge_3_dispenser.jpg", "imagens/ps5_gta6_3_bundle_box.jpg")
s = s.replace("imagens/samsung_fridge_4_interior.jpg", "imagens/ps5_gta6_4_gameplay.jpg")

# Capacity logic in track-order
s = s.replace("code.includes('43') ? '432L' : (code.includes('25') ? '254L' : '300L')", "code.includes('PRO') ? '2TB (PS5 Pro)' : '1TB (PS5 Slim)'")
s = s.replace("'300L'", "'1TB SSD'")

with open(server_path, "w", encoding="utf-8") as f:
    f.write(s)
print("Updated server.js")

# 5. Update index.html
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# Title
html = re.sub(r'<title>.*?</title>', f'<title>{HERO_TITLE} ({HERO_MODEL}) | Takealot</title>', html)

# Breadcrumbs
html = re.sub(
    r'<div class="breadcrumb-bar".*?</div>',
    '<div class="breadcrumb-bar" style="padding: 10px 16px; font-size: 11.5px; color: #666; background: #fff; border-bottom: 1px solid #f0f0f0; display: flex; align-items: center; gap: 6px; overflow-x: auto; white-space: nowrap;">'
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Home</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Gaming</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<a href="#" style="color: #0b79bf; text-decoration: none;">Consoles</a> <i class="fas fa-chevron-right" style="font-size: 8px; color: #999;"></i> '
    '<span style="color: #333; font-weight: 500;">PlayStation 5 Consoles &amp; Bundles</span></div>',
    html,
    flags=re.DOTALL
)

# Product title & brand
html = re.sub(
    r'<h1 class="product-title" id="main-product-title">.*?</h1>',
    f'<h1 class="product-title" id="main-product-title">{HERO_TITLE} ({HERO_MODEL})</h1>',
    html
)
html = html.replace('<a href="#" class="brand-link">Samsung</a>', '<a href="#" class="brand-link">Sony PlayStation</a>')

# Carousel slides
carousel_replacement = """        <div class="carousel-slide"><img src="imagens/ps5_gta6_1_hero.jpg" alt="Sony PlayStation 5 Slim Console + GTA 6 Full Game Hero Pack" /></div>
        <div class="carousel-slide"><img src="imagens/ps5_gta6_2_controller.jpg" alt="PlayStation 5 DualSense Wireless Controller Detail" /></div>
        <div class="carousel-slide"><img src="imagens/ps5_gta6_3_bundle_box.jpg" alt="PlayStation 5 Slim 1TB Console Stand Profile" /></div>
        <div class="carousel-slide"><img src="imagens/ps5_gta6_4_gameplay.jpg" alt="Grand Theft Auto VI Official PS5 Physical Game Case" /></div>"""

html = re.sub(
    r'<div class="carousel-track" id="carousel-track">.*?</div>\s*<div class="dots-row"',
    f'<div class="carousel-track" id="carousel-track">\n{carousel_replacement}\n    </div>\n    <div class="dots-row"',
    html,
    flags=re.DOTALL
)

# Prices display
html = re.sub(
    r'<span class="price-val" id="main-price-display">.*?</span>',
    f'<span class="price-val" id="main-price-display">R {HERO_PRICE}</span>',
    html
)
html = re.sub(
    r'<span class="price-old" id="main-old-price">.*?</span>',
    f'<span class="price-old" id="main-old-price">{HERO_OLD_PRICE}</span>',
    html
)
html = re.sub(
    r'<span class="bar-price" id="footer-price-display">.*?</span>',
    f'<span class="bar-price" id="footer-price-display">R {HERO_PRICE}</span>',
    html
)

# Variation pills
pills_replacement = """    <div class="variation-selector-sec">
        <div class="variation-header-row">
            <span>Edition / Bundle: <strong id="selected-size-label">PS5 Slim Disc + GTA 6 (Hero)</strong></span>
            <span style="font-size: 11.5px; color: var(--takealot-blue); font-weight: 600;"><i class="fas fa-sliders" style="margin-right: 3px;"></i> Choose edition</span>
        </div>
        <div class="variation-pills-row">
            <button class="var-pill" data-var-key="digital" onclick="selectProductVariation('digital')">
                PS5 Digital + GTA 6 <span class="pill-badge">R 2,899</span>
            </button>
            <button class="var-pill active" data-var-key="slim-disc" onclick="selectProductVariation('slim-disc')">
                PS5 Slim Disc + GTA 6 <span class="pill-badge" style="background: #007a3d;">Hot R 3,299</span>
            </button>
            <button class="var-pill" data-var-key="dual-ctrl" onclick="selectProductVariation('dual-ctrl')">
                + Extra DualSense <span class="pill-badge">R 3,599</span>
            </button>
            <button class="var-pill" data-var-key="pro" onclick="selectProductVariation('pro')">
                PS5 Pro 2TB + GTA 6 <span class="pill-badge">R 3,799</span>
            </button>
            <button class="var-pill" data-var-key="headset-bundle" onclick="selectProductVariation('headset-bundle')">
                + Pulse 3D Headset <span class="pill-badge">R 3,699</span>
            </button>
        </div>
    </div>"""

html = re.sub(
    r'<div class="variation-selector-sec">.*?</div>\s*</div>\s*<!-- 6\. TakealotMORE Banner',
    f'{pills_replacement}\n\n    <!-- 6. TakealotMORE Banner',
    html,
    flags=re.DOTALL
)

# What's Hot carousel
hot_replacement = """    <div class="category-hot-sec">
        <div class="sec-title" style="margin-bottom: 12px;">What's Hot in Gaming Consoles</div>
        <div class="hot-carousel">
            <!-- Variation 1: Digital -->
            <div class="hot-card" data-var-key="digital" onclick="selectProductVariation('digital', true)">
                <div class="hot-badges">
                    <div class="badge-black">Black<br>November.</div>
                    <div class="badge-blue">76%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/ps5_gta6_3_bundle_box.jpg" alt="PS5 Digital Edition + GTA 6" />
                </div>
                <div class="hot-title">Sony PlayStation 5 Digital Edition 1TB + GTA 6 Digital Key</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 2,899</span>
                    <span class="hot-old-price">R 11,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.8 (1,150)</div>
            </div>

            <!-- Variation 2: Slim Disc Hero -->
            <div class="hot-card active-selection" data-var-key="slim-disc" onclick="selectProductVariation('slim-disc', true)">
                <div class="hot-badges">
                    <div class="badge-black">Top<br>Seller.</div>
                    <div class="badge-blue">78%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/ps5_gta6_1_hero.jpg" alt="PS5 Slim Disc + GTA 6 Physical Disc" />
                </div>
                <div class="hot-title">Sony PlayStation 5 Slim 1TB + Grand Theft Auto VI Bundle</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 3,299</span>
                    <span class="hot-old-price">R 14,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (3,840)</div>
            </div>

            <!-- Variation 3: Dual Controller -->
            <div class="hot-card" data-var-key="dual-ctrl" onclick="selectProductVariation('dual-ctrl', true)">
                <div class="hot-badges">
                    <div class="badge-black">2x Pads</div>
                    <div class="badge-blue">79%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/ps5_gta6_2_controller.jpg" alt="PS5 Slim + GTA 6 + Extra Midnight Black DualSense" />
                </div>
                <div class="hot-title">PS5 Slim 1TB + GTA 6 + Extra Midnight Black DualSense</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 3,599</span>
                    <span class="hot-old-price">R 16,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (920)</div>
            </div>

            <!-- Variation 4: PS5 Pro -->
            <div class="hot-card" data-var-key="pro" onclick="selectProductVariation('pro', true)">
                <div class="hot-badges">
                    <div class="badge-black">PRO 2TB</div>
                    <div class="badge-blue">81%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/ps5_gta6_1_hero.jpg" alt="PlayStation 5 Pro 2TB + GTA 6" />
                </div>
                <div class="hot-title">Sony PlayStation 5 Pro 2TB Enhanced Edition + GTA 6</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 3,799</span>
                    <span class="hot-old-price">R 19,999</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 5.0 (610)</div>
            </div>

            <!-- Variation 5: Headset Bundle -->
            <div class="hot-card" data-var-key="headset-bundle" onclick="selectProductVariation('headset-bundle', true)">
                <div class="hot-badges">
                    <div class="badge-black">Pulse 3D</div>
                    <div class="badge-blue">80%<br>OFF</div>
                </div>
                <button class="hot-wishlist-btn" title="Wishlist" onclick="event.stopPropagation();"><i class="far fa-heart"></i></button>
                <div class="hot-img-wrap">
                    <img src="imagens/ps5_gta6_4_gameplay.jpg" alt="PS5 Slim GTA 6 + Pulse 3D Headset Bundle" />
                </div>
                <div class="hot-title">PS5 Slim 1TB + GTA 6 + Pulse 3D Wireless Headset Bundle</div>
                <div class="hot-price-row">
                    <span class="hot-price">R 3,699</span>
                    <span class="hot-old-price">R 18,499</span>
                </div>
                <div class="hot-rating"><i class="fas fa-star star-gold"></i> 4.9 (480)</div>
            </div>
        </div>
    </div>"""

html = re.sub(
    r'<div class="category-hot-sec">.*?</div>\s*</div>\s*<!-- 8\. Divider -->',
    f'{hot_replacement}\n\n    <!-- 8. Divider -->',
    html,
    flags=re.DOTALL
)

# Alternate seller
html = re.sub(
    r'<div class="offer-seller-name">.*?</div>',
    '<div class="offer-seller-name">Apex Gaming &amp; Electronics SA</div>',
    html
)
html = re.sub(
    r'<div class="offer-price">R \d+[\d,]*</div>',
    '<div class="offer-price">R 3,399</div>',
    html
)

# Specs table
specs_replacement = """        <div class="spec-row">
            <span class="spec-label">Brand</span>
            <span class="spec-val">Sony Interactive Entertainment</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Model Number</span>
            <span class="spec-val" id="spec-model-number">CFI-2000A01-GTA6 (PlayStation 5 Slim)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Storage Capacity</span>
            <span class="spec-val" id="spec-screen-size">1TB Ultra-High Speed Custom NVMe SSD (5.5 GB/s)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Included Game</span>
            <span class="spec-val">Grand Theft Auto VI (GTA 6) Full Game + Bonus Pre-Order DLC</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Graphics Architecture</span>
            <span class="spec-val">AMD Radeon RDNA 2 GPU with Hardware Ray Tracing (10.28 TFLOPs)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Processor</span>
            <span class="spec-val">Custom 8-Core / 16-Thread AMD Zen 2 (up to 3.5 GHz)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Video Output &amp; VRR</span>
            <span class="spec-val">4K 120Hz / 8K HDR with HDMI 2.1 Variable Refresh Rate (VRR)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Wireless Controller</span>
            <span class="spec-val">DualSense Wireless Controller (Dynamic Haptics &amp; Adaptive Triggers)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Audio System</span>
            <span class="spec-val">Tempest 3D AudioTech (Immersive 3D Spatial Surround Sound)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Optical Drive</span>
            <span class="spec-val">Ultra HD Blu-ray Disc Drive (supports 4K UHD Blu-ray Movies)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Power &amp; Protection</span>
            <span class="spec-val">220-240V AC 50/60Hz (ICASA Certified South African Plug &amp; Surge Guard)</span>
        </div>
        <div class="spec-row">
            <span class="spec-label">Warranty</span>
            <span class="spec-val">12 Months Official Sony Interactive Entertainment South Africa Warranty</span>
        </div>"""

html = re.sub(
    r'<div class="spec-table">.*?</div>\s*</div>\s*<!-- Description Tab Content -->',
    f'<div class="spec-table">\n{specs_replacement}\n        </div>\n    </div>\n    <!-- Description Tab Content -->',
    html,
    flags=re.DOTALL
)

# Highlights ul
highlights_replacement = """<ul style="padding-left: 18px; margin-bottom: 8px; line-height: 1.5;">
                <li><strong>Grand Theft Auto VI (GTA 6) Included:</strong> Explore the sprawling, neon-soaked state of Leonida, home to Vice City and beyond, in the biggest, most immersive open-world evolution in entertainment history.</li>
                <li><strong>Ultra-High Speed 1TB Custom SSD:</strong> Maximise your play sessions with lightning-fast, near-instant load times for GTA 6 and all installed PS5 games.</li>
                <li><strong>Ray Tracing &amp; 4K 120Hz Visuals:</strong> Immerse yourself in worlds with a new level of realism as rays of light are individually simulated, creating true-to-life shadows and reflections across Vice City.</li>
                <li><strong>DualSense Haptic Feedback &amp; Adaptive Triggers:</strong> Feel the rumble of high-powered muscle car engines, dynamic Florida rainstorms, and tactile weapon recoil straight through your hands.</li>
                <li><strong>Tempest 3D AudioTech:</strong> Immerse yourself in soundscapes where it feels as if the sound comes from every direction across Vice City nightclubs, traffic, and coastal waves.</li>
                <li><strong>Slim &amp; Sleek Form Factor:</strong> With PS5 Slim, players get powerful gaming technology packed inside a sleek and compact console design with 1TB SSD storage.</li>
                <li><strong>ICASA Approved South African Model:</strong> Certified for local power grids with integrated surge protection, complete with 12 months official Sony South Africa warranty.</li>
            </ul>"""

html = re.sub(
    r'<ul style="padding-left: 18px; margin-bottom: 8px; line-height: 1.5;">.*?</ul>',
    highlights_replacement,
    html,
    flags=re.DOTALL
)

# Description tab content
desc_replacement = """    <div id="desc-tab-content" class="tab-content">
        <h3 style="font-size: 15px; margin-bottom: 10px; color: #222;">Experience Grand Theft Auto VI in Next-Gen 4K with PlayStation 5 Slim</h3>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            The <strong>PlayStation 5 Slim 1TB Console + Grand Theft Auto VI Bundle</strong> is the ultimate next-generation gaming package. Return to the neon-drenched streets of Vice City and explore the vast state of Leonida with unprecedented graphical fidelity, near-instant loading times, and revolutionary tactile feedback.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Feel the Action with DualSense™:</strong> From the tactile sensation of acceleration in supercars tearing down Ocean Drive to the resistance of firearm triggers and tropical Florida thunderstorms, the DualSense wireless controller's haptic feedback and adaptive triggers put you directly into the shoes of Lucia and Jason.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555; margin-bottom: 12px;">
            <strong>Breathtaking Visuals &amp; Lightning Speeds:</strong> Powered by an ultra-fast 1TB custom NVMe SSD and custom AMD RDNA 2 GPU with dedicated hardware Ray Tracing, Vice City renders with photo-realistic water reflections, dynamic global illumination, and silky-smooth 60 FPS gameplay on 4K HDR displays.
        </p>
        <p style="font-size: 13.5px; line-height: 1.6; color: #555;">
            <strong>Complete South African Retail Pack:</strong> Includes the PlayStation 5 Slim Disc Edition console (1TB), official DualSense wireless controller, HDMI 2.1 cable, South African AC power cord, horizontal stand feet, and Grand Theft Auto VI (GTA 6) Full Game with exclusive pre-order digital bonus pack.
        </p>
    </div>"""

html = re.sub(
    r'<div id="desc-tab-content" class="tab-content">.*?</div>\s*</div>\s*<!-- 14\. Customer Reviews',
    f'{desc_replacement}\n    </div>\n    <!-- 14. Customer Reviews',
    html,
    flags=re.DOTALL
)

# 14 Customer Reviews
reviews_replacement = """        <div class="reviews-list-container">
            <!-- Review 1 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Keagan van Zyl - 20 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">62</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The GTA 6 bundle of the century. Vice City in 4K 60fps with Ray Tracing is mind-blowing...</span>
                    <span class="review-full" style="display: none;">The GTA 6 bundle of the century. Vice City in 4K 60fps with Ray Tracing is mind-blowing. The haptic feedback on the DualSense when driving sports cars across Ocean Beach feels unreal. Takealot delivered in 24 hours to Fourways!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 2 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Lerato Mokoena - 18 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">48</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Bought this for R 3,299 during the promotion and I still cannot believe the price...</span>
                    <span class="review-full" style="display: none;">Bought this for R 3,299 during the promotion and I still cannot believe the price. 1TB SSD loads Vice City in literally 2 seconds. No more loading screens ever. Soweto delivery was fast and secure with courier OTP!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 3 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Dylan Pillay - 15 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">39</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Grand Theft Auto VI looks next-gen in every sense. The tropical thunderstorms will give you goosebumps...</span>
                    <span class="review-full" style="display: none;">Grand Theft Auto VI looks next-gen in every sense. The lighting during Florida sunsets and dynamic tropical thunderstorms will give you goosebumps. DualSense triggers push back when braking or firing weapons. Outstanding product!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 4 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Andre Botha - 12 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">31</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Console is much slimmer than the original fat PS5 and whisper quiet. Doesn't overheat during 6-hour sessions...</span>
                    <span class="review-full" style="display: none;">Console is much slimmer than the original fat PS5 and whisper quiet. Doesn't overheat during 6-hour weekend GTA 6 gaming sessions in Centurion. A massive upgrade in every way.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 5 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Thulani Ndlovu - 09 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">44</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Takealot courier handed it over safely with PIN verification. Box was pristine with bubble wrap...</span>
                    <span class="review-full" style="display: none;">Takealot courier handed it over safely with PIN verification. Box was pristine with bubble wrap. Disc drive works smoothly and South African warranty is fully registered with Sony SA. Highly recommended.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 6 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Jacques Marais - 06 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">27</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Tempest 3D audio makes Vice City feel alive. You can hear police sirens in the distance with pinpoint precision...</span>
                    <span class="review-full" style="display: none;">Tempest 3D audio makes Vice City feel alive. You can hear police sirens in the distance and ambient street noise around every corner with pinpoint directional precision in Stellenbosch. Incredible atmosphere.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 7 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Brandon Smith - 03 Nov 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">33</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Upgraded from PS4 and the difference is night and day. 60 FPS performance mode is buttery smooth...</span>
                    <span class="review-full" style="display: none;">Upgraded from PS4 and the difference is night and day. 60 FPS performance mode is buttery smooth. Best purchase I've made on Takealot. The graphics on GTA 6 are unlike anything ever created.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 8 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Sibongile Dube - 30 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">38</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Got this for my son and the whole family is hooked. Vice City looks like a playable Hollywood movie...</span>
                    <span class="review-full" style="display: none;">Got this for my son and the whole family is hooked. Vice City looks like a playable Hollywood movie in Pretoria East. The extra controller from the bundle is essential for split-screen gaming.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 9 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Gareth Evans - 26 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">29</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Load times are non-existent. Fast travelling across the entire Leonida map happens in under 3 seconds...</span>
                    <span class="review-full" style="display: none;">Load times are non-existent. Fast travelling across the entire Leonida map happens in under 3 seconds here in Sea Point. Unbelievable deal at R 3,299 for a brand new PS5 Slim and GTA 6!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 10 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Francois de Villiers - 22 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">24</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Surge protection on this console works great with our backup inverter in Bloemfontein...</span>
                    <span class="review-full" style="display: none;">Surge protection on this console works great with our backup inverter in Bloemfontein. Tested during power switchovers and didn't even cause a glitch. Sony build quality at its finest.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 11 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Nkosana Zulu - 18 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">35</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">Original Sony ICASA approved unit. Packaging includes the physical GTA 6 game case and DualSense...</span>
                    <span class="review-full" style="display: none;">Original Sony ICASA approved unit. Packaging includes the physical GTA 6 game case and DualSense controller. 100% genuine with official hologram seal. Delivered in 48 hours to Kempton Park.</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 12 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Matthew Adams - 14 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">21</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The Ray Tracing reflections on neon puddle-soaked streets in Vice City at night are breathtaking...</span>
                    <span class="review-full" style="display: none;">The Ray Tracing reflections on neon puddle-soaked streets in Vice City at night are breathtaking. The slim design fits perfectly under our TV cabinet in Gqeberha. 10/10 purchase!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 13 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Wayne Cloete - 10 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">41</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">R 3,299 for a PS5 Slim AND GTA 6 is the deal of the year. Delivered right to my door in 2 business days...</span>
                    <span class="review-full" style="display: none;">R 3,299 for a PS5 Slim AND GTA 6 is the deal of the year. Delivered right to my door in 2 business days in Bellville. Excellent tracking notifications with driver location. Thank you Takealot!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>

            <!-- Review 14 -->
            <div class="review-single-card">
                <div class="review-card-top">
                    <div>
                        <strong>Tariq Moosa - 05 Oct 2026</strong>
                        <span class="verified-buyer-pill"><i class="fas fa-circle-check"></i> Verified Purchase</span>
                    </div>
                    <span class="review-likes" onclick="toggleHelpful(this)" style="cursor: pointer;"><i class="fas fa-star" style="color: #f5a623;"></i> 5 ( <i class="fas fa-thumbs-up" style="font-size: 11px;"></i> <span class="like-count">36</span> )</span>
                </div>
                <div class="review-card-text">
                    <span class="review-short">The adaptive triggers give unique resistance for every vehicle and weapon in Vice City...</span>
                    <span class="review-full" style="display: none;">The adaptive triggers give unique resistance for every vehicle and weapon in Vice City. From shooting pistols to driving helicopters, the immersion is unbelievable. Absolute masterpiece bundle!</span>
                    <a href="javascript:void(0)" class="read-more-link" onclick="toggleReviewText(this)">Read More</a>
                </div>
            </div>
        </div>"""

html = re.sub(
    r'<div class="reviews-list-container">.*?</div>\s*</div>\s*<!-- Write a Review Button',
    f'{reviews_replacement}\n    </div>\n    <!-- Write a Review Button',
    html,
    flags=re.DOTALL
)

# Javascript productVariations dictionary in index.html
js_variations = """    const productVariations = {
        "digital": {
            id: "digital",
            size: "PS5 Digital + GTA 6",
            title: "Sony PlayStation 5 Digital Edition 1TB + GTA 6 Digital Key",
            price: "2899",
            oldPrice: "R 11,999",
            discount: "76%<br>OFF",
            credit: "R 241 p/m x 12 months",
            ebucks: "eB28,990",
            miles: "28,990",
            image: "imagens/ps5_gta6_3_bundle_box.jpg",
            images: [
                "imagens/ps5_gta6_3_bundle_box.jpg",
                "imagens/ps5_gta6_1_hero.jpg",
                "imagens/ps5_gta6_2_controller.jpg",
                "imagens/ps5_gta6_4_gameplay.jpg"
            ],
            screenSizeSpec: "1TB Custom NVMe SSD (Digital)",
            modelSpec: "CFI-2000B01-GTA6"
        },
        "slim-disc": {
            id: "slim-disc",
            size: "PS5 Slim Disc + GTA 6",
            title: "Sony PlayStation 5 Slim 1TB Console + Grand Theft Auto VI Bundle",
            price: "3299",
            oldPrice: "R 14,999",
            discount: "78%<br>OFF",
            credit: "R 274 p/m x 12 months",
            ebucks: "eB32,990",
            miles: "32,990",
            image: "imagens/ps5_gta6_1_hero.jpg",
            images: [
                "imagens/ps5_gta6_1_hero.jpg",
                "imagens/ps5_gta6_2_controller.jpg",
                "imagens/ps5_gta6_3_bundle_box.jpg",
                "imagens/ps5_gta6_4_gameplay.jpg"
            ],
            screenSizeSpec: "1TB NVMe SSD + Ultra HD Blu-ray",
            modelSpec: "CFI-2000A01-GTA6"
        },
        "dual-ctrl": {
            id: "dual-ctrl",
            size: "+ Extra DualSense",
            title: "Sony PlayStation 5 Slim 1TB + GTA 6 + Extra Midnight Black DualSense",
            price: "3599",
            oldPrice: "R 16,999",
            discount: "79%<br>OFF",
            credit: "R 299 p/m x 12 months",
            ebucks: "eB35,990",
            miles: "35,990",
            image: "imagens/ps5_gta6_2_controller.jpg",
            images: [
                "imagens/ps5_gta6_2_controller.jpg",
                "imagens/ps5_gta6_1_hero.jpg",
                "imagens/ps5_gta6_3_bundle_box.jpg",
                "imagens/ps5_gta6_4_gameplay.jpg"
            ],
            screenSizeSpec: "1TB SSD + 2x DualSense Controllers",
            modelSpec: "CFI-2000A-DUALPAD"
        },
        "pro": {
            id: "pro",
            size: "PS5 Pro 2TB + GTA 6",
            title: "Sony PlayStation 5 Pro 2TB Enhanced Edition + Grand Theft Auto VI",
            price: "3799",
            oldPrice: "R 19,999",
            discount: "81%<br>OFF",
            credit: "R 316 p/m x 12 months",
            ebucks: "eB37,990",
            miles: "37,990",
            image: "imagens/ps5_gta6_1_hero.jpg",
            images: [
                "imagens/ps5_gta6_1_hero.jpg",
                "imagens/ps5_gta6_2_controller.jpg",
                "imagens/ps5_gta6_3_bundle_box.jpg",
                "imagens/ps5_gta6_4_gameplay.jpg"
            ],
            screenSizeSpec: "2TB Pro NVMe SSD (PSSR AI Upscaling)",
            modelSpec: "CFI-7000-PRO-GTA6"
        },
        "headset-bundle": {
            id: "headset-bundle",
            size: "+ Pulse 3D Headset",
            title: "Sony PlayStation 5 Slim 1TB + GTA 6 + Pulse 3D Wireless Headset Bundle",
            price: "3699",
            oldPrice: "R 18,499",
            discount: "80%<br>OFF",
            credit: "R 308 p/m x 12 months",
            ebucks: "eB36,990",
            miles: "36,990",
            image: "imagens/ps5_gta6_4_gameplay.jpg",
            images: [
                "imagens/ps5_gta6_4_gameplay.jpg",
                "imagens/ps5_gta6_1_hero.jpg",
                "imagens/ps5_gta6_2_controller.jpg",
                "imagens/ps5_gta6_3_bundle_box.jpg"
            ],
            screenSizeSpec: "1TB SSD + Pulse 3D Surround Headset",
            modelSpec: "CFI-2000A-PULSE3D"
        }
    };"""

html = re.sub(
    r'const productVariations = \{.*?\n\s*\};\s*let selectedVariationKey =',
    f'{js_variations}\n\n    let selectedVariationKey = "slim-disc";',
    html,
    flags=re.DOTALL
)

html = html.replace('let selectedVariationKey = "300l";', 'let selectedVariationKey = "slim-disc";')
html = html.replace('selectedPrice = "2199"', 'selectedPrice = "3299"')
html = html.replace('selectedTitle = "Samsung 300L', 'selectedTitle = "Sony PlayStation 5')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html")

# 6. Update checkout.html
checkout_path = os.path.join(BASE_DIR, "checkout.html")
with open(checkout_path, "r", encoding="utf-8") as f:
    chk = f.read()

chk = re.sub(r'<title>.*?</title>', f'<title>Checkout - {HERO_TITLE} | Takealot</title>', chk)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
chk = chk.replace("Samsung 300L Bottom Freezer Refrigerator", HERO_TITLE)
chk = chk.replace("Samsung 300L Refrigerator", HERO_TITLE)
chk = chk.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
chk = chk.replace("2199", "3299")
chk = chk.replace("2,199", "3,299")
chk = chk.replace("9,999", "14,999")
chk = chk.replace("Large Appliance White Glove Delivery (To Your Kitchen)", "Express Fragile Tech Delivery (PIN Verification Required)")

with open(checkout_path, "w", encoding="utf-8") as f:
    f.write(chk)
print("Updated checkout.html")

# 7. Update cart.html
cart_path = os.path.join(BASE_DIR, "cart.html")
with open(cart_path, "r", encoding="utf-8") as f:
    crt = f.read()

crt = re.sub(r'<title>.*?</title>', f'<title>Shopping Cart - {HERO_TITLE} | Takealot</title>', crt)
crt = crt.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
crt = crt.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
crt = crt.replace("Samsung 300L Refrigerator", HERO_TITLE)
crt = crt.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
crt = crt.replace("2199", "3299")
crt = crt.replace("2,199", "3,299")
crt = crt.replace("9,999", "14,999")

with open(cart_path, "w", encoding="utf-8") as f:
    f.write(crt)
print("Updated cart.html")

# 8. Update track.html
track_path = os.path.join(BASE_DIR, "track.html")
with open(track_path, "r", encoding="utf-8") as f:
    trk = f.read()

trk = re.sub(r'<title>.*?</title>', f'<title>Track Your Order - {HERO_TITLE} | Takealot</title>', trk)
trk = trk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
trk = trk.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
trk = trk.replace("Samsung 300L Refrigerator", HERO_TITLE)
trk = trk.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
trk = trk.replace("2199", "3299")
trk = trk.replace("2,199", "3,299")
trk = trk.replace("9,999", "14,999")
trk = trk.replace("Capacity: 300L", "Edition: 1TB Slim Disc + GTA 6")
trk = trk.replace("300L", "1TB Slim")
trk = trk.replace("TAK-30-994812", "TAK-55-994812")
trk = trk.replace("TAK-43-189210", "TAK-70-189210")
trk = trk.replace("TAK-25-883910", "TAK-20-883910")

with open(track_path, "w", encoding="utf-8") as f:
    f.write(trk)
print("Updated track.html")

# 9. Update obrigado.html
obrigado_path = os.path.join(BASE_DIR, "obrigado.html")
with open(obrigado_path, "r", encoding="utf-8") as f:
    obr = f.read()

obr = re.sub(r'<title>.*?</title>', f'<title>Order Confirmed - {HERO_TITLE} | Takealot</title>', obr)
obr = obr.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
obr = obr.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
obr = obr.replace("Samsung 300L Refrigerator", HERO_TITLE)
obr = obr.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
obr = obr.replace("2199", "3299")
obr = obr.replace("2,199", "3,299")
obr = obr.replace("9,999", "14,999")

with open(obrigado_path, "w", encoding="utf-8") as f:
    f.write(obr)
print("Updated obrigado.html")

# 10. Update upgrade-shipping.html
upg_path = os.path.join(BASE_DIR, "upgrade-shipping.html")
with open(upg_path, "r", encoding="utf-8") as f:
    upg = f.read()

upg = re.sub(r'<title>.*?</title>', f'<title>Priority Delivery Upgrade - {HERO_TITLE} | Takealot</title>', upg)
upg = upg.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
upg = upg.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
upg = upg.replace("Samsung 300L Refrigerator", HERO_TITLE)
upg = upg.replace("imagens/samsung_fridge_1_hero.jpg", "imagens/ps5_gta6_1_hero.jpg")
upg = upg.replace("kitchen", "gaming setup")
upg = upg.replace("Kitchen", "Gaming Setup")

with open(upg_path, "w", encoding="utf-8") as f:
    f.write(upg)
print("Updated upgrade-shipping.html")

# 11. Update api/ directory
api_dir = os.path.join(BASE_DIR, "api")
for root, dirs, files in os.walk(api_dir):
    for fn in files:
        fp = os.path.join(root, fn)
        with open(fp, "r", encoding="utf-8", errors="ignore") as f:
            c = f.read()
        orig = c
        c = c.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox (RB30J3611S9)", HERO_TITLE)
        c = c.replace("Samsung 300L Bottom Freezer Refrigerator with Water Dispenser - Inox", HERO_TITLE)
        c = c.replace("Samsung 300L Refrigerator", HERO_TITLE)
        c = c.replace("Bottom Freezer Refrigerator", "PlayStation 5 Console + GTA 6")
        c = c.replace("Refrigerator", "PlayStation 5")
        c = c.replace("refrigerator", "PlayStation 5")
        c = c.replace("3020", "3025")
        c = c.replace("2199", "3299")
        c = c.replace("2,199", "3,299")
        c = c.replace("9999", "14999")
        c = c.replace("9,999", "14,999")
        c = c.replace("297", "349")
        c = re.sub(r'https://iili\.io/[a-zA-Z0-9_\-]+\.(?:jpg|png)', HERO_CDN, c)
        if c != orig:
            with open(fp, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"Updated api/{fn}")

print("\n--- ALL PLAYSTATION 5 + GTA 6 FILES UPDATED SUCCESSFULLY ---")
