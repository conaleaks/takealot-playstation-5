import os, re

index_path = "/Users/green/Downloads/Takealot PlayStation 5/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace carousel
carousel_pattern = r'<div class="carousel" id="carousel">.*?</div>\s*<div class="dots-row"'
new_carousel = """<div class="carousel" id="carousel">
            <div class="carousel-slide"><img src="imagens/ps5_gta6_1_hero.jpg" alt="Sony PlayStation 5 Slim 1TB Console + GTA 6 Hero Bundle" /></div>
            <div class="carousel-slide"><img src="imagens/ps5_gta6_2_controller.jpg" alt="PlayStation 5 DualSense Wireless Controller Detail" /></div>
            <div class="carousel-slide"><img src="imagens/ps5_gta6_3_bundle_box.jpg" alt="PlayStation 5 Slim 1TB Console Stand Profile" /></div>
            <div class="carousel-slide"><img src="imagens/ps5_gta6_4_gameplay.jpg" alt="Grand Theft Auto VI Official PS5 Physical Game Case" /></div>
        </div>\n\n        <div class="dots-row" """

html = re.sub(carousel_pattern, new_carousel, html, flags=re.DOTALL)

# 2. Replace variation pills row
pills_pattern = r'<div class="variation-pills-row">.*?</div>\s*</div>\s*<!-- 6\. TakealotMORE Banner'
new_pills = """<div class="variation-pills-row">
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
    </div>\n\n    <!-- 6. TakealotMORE Banner"""

html = re.sub(pills_pattern, new_pills, html, flags=re.DOTALL)

# 3. Replace What's Hot
hot_pattern = r'<div class="category-hot-sec">.*?</div>\s*</div>\s*<!-- 8\. Divider -->'
new_hot = """<div class="category-hot-sec">
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
    </div>\n\n    <!-- 8. Divider -->"""

html = re.sub(hot_pattern, new_hot, html, flags=re.DOTALL)

# 4. Global replacements for any leftover paths or strings
html = html.replace('imagens/samsung_fridge_1_hero.jpg', 'imagens/ps5_gta6_1_hero.jpg')
html = html.replace('imagens/samsung_fridge_2_open.jpg', 'imagens/ps5_gta6_2_controller.jpg')
html = html.replace('imagens/samsung_fridge_3_dispenser.jpg', 'imagens/ps5_gta6_3_bundle_box.jpg')
html = html.replace('imagens/samsung_fridge_4_interior.jpg', 'imagens/ps5_gta6_4_gameplay.jpg')

html = html.replace('300L Inox (RB30)', 'PS5 Slim Disc + GTA 6')
html = html.replace('300 Litres (Fridge: 202L, Freezer: 98L)', '1TB Custom NVMe SSD (5.5 GB/s)')
html = html.replace('300L', '1TB')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html cleanly!")
