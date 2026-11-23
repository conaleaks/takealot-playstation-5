with open("/Users/green/Downloads/Takealot PlayStation 5/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 1570 replacement
for idx, l in enumerate(lines):
    if "Variations of Refrigerators" in l:
        lines[idx] = "        <!-- 7. What's Hot in Gaming Consoles -->\n"

# Locate start and end of reviews container
start_idx = -1
end_idx = -1
for idx, l in enumerate(lines):
    if 'id="reviews-list-container"' in l:
        start_idx = idx
    if start_idx != -1 and 'id="load-more-reviews-btn"' in l:
        end_idx = idx
        break

print(f"Reviews container starts at line {start_idx+1} and ends before line {end_idx+1}")

reviews_block = """        <div id="reviews-list-container">
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
        </div>\n\n        """

lines[start_idx:end_idx] = [reviews_block]

with open("/Users/green/Downloads/Takealot PlayStation 5/index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Replaced all 14 reviews cleanly!")
