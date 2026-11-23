import os, re

index_path = "/Users/green/Downloads/Takealot PlayStation 5/index.html"
with open(index_path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace category-hot-sec
idx1 = text.find('<div class="category-hot-sec">')
idx2 = text.find('<div class="divider"></div>\n\n    <!-- 8. Sold By Section', idx1)

new_hot_section = """<div class="category-hot-sec">
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
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
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
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
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
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
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
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
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
                <div class="hot-selected-badge"><i class="fas fa-check"></i> Selected</div>
            </div>
        </div>
    </div>\n\n    """

if idx1 != -1 and idx2 != -1:
    text = text[:idx1] + new_hot_section + text[idx2:]
    print("Replaced category-hot-sec successfully!")

# 2. Replace intro paragraph
text = text.replace(
    'Enjoy even cooling throughout the entire compartment and icy refreshment on demand with Samsung\'s innovative All-Around Cooling™ technology and non-plumbed water dispenser.',
    'Experience the vast, sun-soaked state of Leonida and the neon streets of Vice City in stunning 4K 60FPS with the Sony PlayStation 5 Slim Console and Grand Theft Auto VI Bundle.'
)

# 3. Replace extra spec rows
old_rows_match = re.search(r'<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>\s*<tr class="extra-spec-row".*?</tr>', text, re.DOTALL)
if old_rows_match:
    new_rows = """<tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Graphics Architecture</td>
                <td class="col-val">Custom AMD RDNA 2 GPU with Hardware Ray Tracing</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">SSD Performance</td>
                <td class="col-val">Custom 1TB NVMe SSD (5.5 GB/s Read Raw)</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Included Game</td>
                <td class="col-val">Grand Theft Auto VI (GTA 6) Full Game</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Wireless Connectivity</td>
                <td class="col-val">Wi-Fi 6 (802.11ax) + Bluetooth 5.1</td>
            </tr>
            <tr class="extra-spec-row" style="display: none;">
                <td class="col-label">Regional Compliance</td>
                <td class="col-val">ICASA Certified South African Plug (AC 220-240V)</td>
            </tr>"""
    text = text[:old_rows_match.start()] + new_rows + text[old_rows_match.end():]
    print("Replaced extra spec rows!")

# 4. Clean JS selectedTitle
text = re.sub(r'let selectedTitle = ".*?";', 'let selectedTitle = "Sony PlayStation 5 Slim 1TB Console + Grand Theft Auto VI Bundle";', text)

with open(index_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Finished index.html deep update!")
