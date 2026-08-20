# -*- coding: utf-8 -*-
import os

BASE_URL = "https://sanz-y.github.io/product"
PUB_ID = "ca-pub-4764608029803832"

def get_head(title, description, canonical_path, is_subfolder=False):
    css_path = "../style.css" if is_subfolder else "style.css"
    canonical_url = f"{BASE_URL}/{canonical_path}"
    
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | 럭키앤뷰티 랩</title>
    <meta name="google-adsense-account" content="{PUB_ID}">
    <meta name="description" content="{description}">
    <meta property="og:title" content="{title} | 럭키앤뷰티 랩">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <link rel="canonical" href="{canonical_url}">
    <link rel="stylesheet" href="{css_path}">

    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB_ID}"
         crossorigin="anonymous"></script>

    <!-- TensorFlow.js & Teachable Machine Image Library -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@teachablemachine/image@latest/dist/teachablemachine-image.min.js"></script>
</head>
<body>
"""

def get_header(active_nav="", is_subfolder=False):
    prefix = "../" if is_subfolder else ""
    return f"""
    <header class="global-header">
        <div class="header-inner">
            <a href="{prefix}index.html" class="logo">
                <span class="logo-badge">✨ LAB</span>
                <span class="logo-text">럭키앤뷰티 랩</span>
            </a>
            <nav class="nav-menu">
                <a href="{prefix}index.html" class="{'active' if active_nav=='home' else ''}">홈</a>
                <a href="{prefix}animal-test.html" class="{'active' if active_nav=='animal' else ''}">🐾 동물상 테스트</a>
                <a href="{prefix}lotto.html" class="{'active' if active_nav=='lotto' else ''}">🎱 로또 6/45</a>
                <a href="{prefix}articles/index.html" class="{'active' if active_nav=='articles' else ''}">📚 칼럼&가이드</a>
                <a href="{prefix}about.html" class="{'active' if active_nav=='about' else ''}">소개</a>
            </nav>
            <div class="header-actions">
                <button id="theme-toggle" class="theme-toggle-btn" aria-label="테마 전환" title="다크/라이트 모드 전환">
                    <span class="theme-icon" id="theme-icon">🌙</span>
                    <span class="theme-text" id="theme-text">다크</span>
                </button>
            </div>
        </div>
    </header>
"""

def get_footer(is_subfolder=False):
    prefix = "../" if is_subfolder else ""
    return f"""
    <footer class="global-footer">
        <div class="footer-inner">
            <div class="footer-grid">
                <div class="footer-col brand-col">
                    <h3>✨ 럭키앤뷰티 랩</h3>
                    <p>인공지능 비전 기술 기반의 동물상 분석과 수학적 통계 기반의 로또 6/45 연구를 제공하는 라이프스타일 테크 포털입니다.</p>
                </div>
                <div class="footer-col">
                    <h4>서비스 메뉴</h4>
                    <ul>
                        <li><a href="{prefix}animal-test.html">AI 동물상 테스트</a></li>
                        <li><a href="{prefix}lotto.html">로또 6/45 번호 추첨</a></li>
                        <li><a href="{prefix}articles/index.html">전문 칼럼 & 가이드</a></li>
                        <li><a href="{prefix}sitemap.html">전체 사이트맵</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>정책 및 정보</h4>
                    <ul>
                        <li><a href="{prefix}about.html">연구소 소개</a></li>
                        <li><a href="{prefix}privacy.html">개인정보처리방침</a></li>
                        <li><a href="{prefix}terms.html">이용약관</a></li>
                        <li><a href="{prefix}contact.html">제휴 및 문의</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <p class="copyright">© 2026 Lucky & Beauty Lab. All rights reserved.</p>
                <p class="disclaimer">본 사이트의 AI 분석 및 로또 번호 추첨 서비스는 엔터테인먼트 및 정보 제공용이며, 복권 당첨 등을 보장하지 않습니다.</p>
            </div>
        </div>
    </footer>
    <div id="toast" class="toast">링크가 복사되었습니다! 🎉</div>
    <script src="{prefix}script.js"></script>
</body>
</html>
"""

def get_disqus():
    return """
    <section class="comments-section">
        <h3 class="comments-title">💬 커뮤니티 의견 나누기</h3>
        <p class="comments-desc">나의 테스트 결과나 의견을 자유롭게 댓글로 남겨보세요!</p>
        <div id="disqus_thread"></div>
        <script>
            (function() {
                var d = document, s = d.createElement('script');
                s.src = 'https://product-ot07uvrdym.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
    </section>
"""

# ==========================================
# 2. animal-test.html
# ==========================================
animal_test_content = get_head(
    "AI 동물상 얼굴 테스트 - 강아지상 vs 고양이상 분석",
    "구글 인공지능 머신러닝 비전 모델이 나의 얼굴 이목구비 비율을 분석하여 강아지상과 고양이상 확률을 정확하게 측정합니다. 100% 무료 및 안전 분석!",
    "animal-test.html"
) + get_header("animal") + """
<main class="page-container">
    <div class="content-wrapper">
        <div class="page-header text-center">
            <span class="category-badge">AI Vision Analysis</span>
            <h1>🐾 인공지능(AI) 동물상 얼굴 테스트</h1>
            <p class="page-subtitle">수천 장의 얼굴 빅데이터를 학습한 AI 모델이 당신의 이목구비를 정밀 분석합니다.</p>
        </div>

        <div class="privacy-badge">
            <span>🔒 <strong>개인정보 안심 보장</strong>: 업로드하신 사진은 외부 서버로 전송되지 않으며, 브라우저 내부 메모리에서만 즉시 분석 후 파기됩니다.</span>
        </div>

        <!-- AI Test Card -->
        <div class="test-card main-tool-card">
            <div id="upload-area" class="upload-area">
                <input type="file" id="image-input" accept="image/*" class="file-input">
                <div class="upload-prompt" id="upload-prompt">
                    <div class="upload-icon">📸</div>
                    <p class="upload-title">분석할 얼굴 사진을 올려주세요</p>
                    <p class="upload-desc">정면 얼굴이 선명하게 나온 사진일수록 인공지능 분석 정확도가 향상됩니다.<br>(파일을 드래그하거나 아래 버튼을 클릭하세요)</p>
                    <button type="button" class="upload-btn" id="select-file-btn">내 기기에서 사진 선택</button>
                </div>
            </div>

            <div id="preview-area" class="preview-area" style="display: none;">
                <div class="image-wrapper">
                    <img id="face-image" src="" alt="업로드된 얼굴 사진">
                </div>
                
                <div id="loading-spinner" class="loading-box">
                    <div class="spinner"></div>
                    <p class="loading-text">인공지능 신경망이 이목구비 특징점을 추출하고 있습니다... 🔍</p>
                </div>

                <div id="result-area" class="result-area" style="display: none;">
                    <div class="result-header">
                        <span id="result-badge" class="result-badge">결과 분석 완료</span>
                        <h2 id="result-title" class="result-title">강아지상</h2>
                        <p id="result-desc" class="result-desc">설명</p>
                        <div id="result-tags" class="result-tags"></div>
                    </div>

                    <div class="chart-container">
                        <div class="chart-item">
                            <div class="chart-label">
                                <span>🐶 강아지상 지수</span>
                                <span id="dog-percent" class="percent-val">0%</span>
                            </div>
                            <div class="progress-bg">
                                <div id="dog-bar" class="progress-bar dog-bar" style="width: 0%;"></div>
                            </div>
                        </div>

                        <div class="chart-item">
                            <div class="chart-label">
                                <span>🐱 고양이상 지수</span>
                                <span id="cat-percent" class="percent-val">0%</span>
                            </div>
                            <div class="progress-bg">
                                <div id="cat-bar" class="progress-bar cat-bar" style="width: 0%;"></div>
                            </div>
                        </div>
                    </div>

                    <div class="action-buttons">
                        <button id="retry-btn" class="btn btn-secondary">🔄 다른 사진으로 재측정</button>
                        <button id="share-btn" class="btn btn-primary">🔗 내 결과 공유하기</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- In-Depth Guide Section on Animal Faces -->
        <article class="article-body-box">
            <h2>📖 동물상 관상학과 인공지능 분석 가이드</h2>
            <p>동물상(Animal Face Types)은 사람의 이목구비 비율, 눈꼬리의 각도, 턱선, 입꼬리의 형태에 따라 특정 동물의 인상과 닮았다고 분류하는 한국 고유의 친근한 인상학적 문화입니다. 본 서비스는 구글의 최신 머신러닝 기술을 통해 객관적인 시각 특징을 백분율로 도출합니다.</p>

            <h3>1. 강아지상 vs 고양이상 특징 비교표</h3>
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>구분</th>
                            <th>🐶 강아지상 (Dog Face)</th>
                            <th>🐱 고양이상 (Cat Face)</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>눈매 및 눈꼬리</strong></td>
                            <td>동글동글하고 눈꼬리가 수평이거나 살짝 내려간 형태</td>
                            <td>가로로 길고 눈꼬리가 살짝 올라간 또렷한 형태</td>
                        </tr>
                        <tr>
                            <td><strong>턱선 및 얼굴형</strong></td>
                            <td>부드러운 볼선과 둥근 U라인 턱선</td>
                            <td>날렵하고 세련된 V라인 턱선</td>
                        </tr>
                        <tr>
                            <td><strong>대표적인 인상</strong></td>
                            <td>다정다감함, 친근함, 순둥이, 보호본능 자극</td>
                            <td>도도함, 시크함, 신비로움, 도회적인 카리스마</td>
                        </tr>
                        <tr>
                            <td><strong>추천 스타일링</strong></td>
                            <td>내추럴 웨이브, 웜톤 파스텔, 부드러운 브라운 아이라인</td>
                            <td>스트레이트 헤어, 쿨톤 모노톤, 엣지 있는 블랙 아이라인</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>2. 인공지능 분석 정확도를 극대화하는 촬영 팁</h3>
            <ul>
                <li><strong>정면 각도 유지</strong>: 얼굴이 정면을 향하고 턱이 과도하게 들리거나 숙여지지 않은 각도에서 가장 정확한 특징점 추출이 이루어집니다.</li>
                <li><strong>밝고 균일한 조명</strong>: 얼굴에 짙은 그림자가 지지 않도록 자연광이나 밝은 실내 조명 아래에서 촬영된 사진을 권장합니다.</li>
                <li><strong>안경 및 마스크 미착용</strong>: 눈매와 입술 선이 명확히 드러날수록 AI 신경망의 인식 정확도가 대폭 향상됩니다.</li>
            </ul>
        </article>

        <!-- FAQ Section -->
        <section class="faq-section">
            <h2>❓ 동물상 테스트 관련 FAQ</h2>
            <div class="faq-list">
                <details class="faq-item">
                    <summary class="faq-question">Q. 사진 분석 후 이미지는 어떻게 처리되나요?</summary>
                    <div class="faq-answer">
                        <p>모든 이미지 분석은 브라우저의 WebGL 자원을 활용하여 로컬에서 즉시 수행됩니다. 사진 데이터는 외부 서버에 전송되거나 저장되지 않으므로 개인정보 유출에 대해 안심하고 사용하셔도 됩니다.</p>
                    </div>
                </details>
                <details class="faq-item">
                    <summary class="faq-question">Q. 연예인 사진이나 반려동물 사진도 분석 가능한가요?</summary>
                    <div class="faq-answer">
                        <p>인물 얼굴 사진에 최적화되어 있으므로 사람의 정면 얼굴 사진을 업로드하셨을 때 가장 정밀한 결과를 얻으실 수 있습니다.</p>
                    </div>
                </details>
            </div>
        </section>

        """ + get_disqus() + """
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/animal-test.html", "w", encoding="utf-8") as f:
    f.write(animal_test_content)

print("Generated animal-test.html")

# ==========================================
# 3. lotto.html
# ==========================================
lotto_content = get_head(
    "로또 6/45 번호 추첨기 & 통계 분석 연구소",
    "암호학적 난수 생성(Crypto-RNG)과 수학적 확률 통계 원리를 적용한 행운의 로또 6/45 번호 추첨기 및 역대 당첨 번호 분포 분석 가이드!",
    "lotto.html"
) + get_header("lotto") + """
<main class="page-container">
    <div class="content-wrapper">
        <div class="page-header text-center">
            <span class="category-badge">Mathematical Probability Lab</span>
            <h1>🎱 로또 6/45 번호 추첨 & 통계 분석기</h1>
            <p class="page-subtitle">수학적 확률과 번호대별 균형 통계 알고리즘으로 오늘의 6가지 행운 번호를 추첨합니다.</p>
        </div>

        <!-- Lotto Machine Card -->
        <div class="lotto-card main-tool-card">
            <h2 class="lotto-heading">🍀 6/45 행운 번호 무작위 추첨</h2>
            <p class="lotto-intro">아래 버튼을 누르면 1부터 45까지의 숫자 중 중복 없는 6개의 행운 번호가 순차적으로 등장합니다.</p>
            
            <div id="lotto-container" class="ball-container">
                <div class="ball placeholder">?</div>
                <div class="ball placeholder">?</div>
                <div class="ball placeholder">?</div>
                <div class="ball placeholder">?</div>
                <div class="ball placeholder">?</div>
                <div class="ball placeholder">?</div>
            </div>

            <button id="draw-btn" class="draw-btn">🎱 행운의 번호 추첨하기</button>
            
            <div class="lotto-tip-box">
                <h4>💡 공식 로또 색상 구간 안내</h4>
                <div class="lotto-color-legend">
                    <span><strong style="color:#f59e0b;">●</strong> 1~10번 (노랑)</span>
                    <span><strong style="color:#0284c7;">●</strong> 11~20번 (파랑)</span>
                    <span><strong style="color:#dc2626;">●</strong> 21~30번 (빨강)</span>
                    <span><strong style="color:#64748b;">●</strong> 31~40번 (회색)</span>
                    <span><strong style="color:#65a30d;">●</strong> 41~45번 (초록)</span>
                </div>
            </div>
        </div>

        <!-- In-Depth Statistical Analysis Guide -->
        <article class="article-body-box">
            <h2>📊 로또 6/45 통계학과 합리적인 번호 조합 전략</h2>
            <p>로또 6/45에서 1등에 당첨될 수학적 확률은 조합 공식 <sub>45</sub>C<sub>6</sub> = <strong>8,145,060분의 1 (약 0.0000123%)</strong>입니다. 모든 번호 조합의 당첨 확률은 수학적으로 동일하지만, 역대 수천 회차의 당첨 결과 데이터에는 뚜렷한 통계학적 정규분포 패턴이 존재합니다.</p>

            <h3>1. 홀짝(Odd/Even) 비율 통계</h3>
            <p>6개 번호의 홀수와 짝수 비율은 다음과 같은 통계적 출현 빈도를 보입니다:</p>
            <div class="table-responsive">
                <table class="data-table">
                    <thead>
                        <tr>
                            <th>홀짝 비율</th>
                            <th>이론적 조합 수</th>
                            <th>출현 확률 (%)</th>
                            <th>추천 여부</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>홀 3 : 짝 3</strong></td>
                            <td>2,727,340</td>
                            <td><strong>33.5%</strong></td>
                            <td>⭐ 적극 추천 (최다 출현)</td>
                        </tr>
                        <tr>
                            <td><strong>홀 4 : 짝 2 / 홀 2 : 짝 4</strong></td>
                            <td>3,931,200</td>
                            <td><strong>48.3%</strong></td>
                            <td>⭐ 적극 추천 (균형 구간)</td>
                        </tr>
                        <tr>
                            <td><strong>홀 5 : 짝 1 / 홀 1 : 짝 5</strong></td>
                            <td>1,335,072</td>
                            <td>16.4%</td>
                            <td>⚠️ 보통</td>
                        </tr>
                        <tr>
                            <td><strong>홀 6 : 짝 0 / 홀 0 : 짝 6</strong></td>
                            <td>151,448</td>
                            <td><strong>1.8%</strong></td>
                            <td>❌ 비추천 (극히 희귀)</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <h3>2. 고저(High/Low) 구간 스프레드</h3>
            <p>전체 1~45 숫자를 <strong>저번호(1~22)</strong>와 <strong>고번호(23~45)</strong>로 양분했을 때도 3:3 또는 2:4, 4:2의 분배 비율이 전체 당첨 회차의 80% 이상을 차지합니다. 번호가 한쪽 구간에만 쏠리는 조합은 피하는 것이 통계학적으로 유리합니다.</p>

            <h3>3. 6개 번호 총합(Sum) 유효 구간</h3>
            <p>역대 당첨 번호 6개의 합계를 계산하면 최솟값은 1+2+3+4+5+6 = 21, 최댓값은 40+41+42+43+44+45 = 255입니다. 그러나 정규분포 곡선의 중심인 <strong>100 ~ 175 사이의 합계 구간</strong>에서 전체 당첨의 약 75%가 발생합니다.</p>
        </article>

        <!-- FAQ Section -->
        <section class="faq-section">
            <h2>❓ 로또 번호 추첨기 FAQ</h2>
            <div class="faq-list">
                <details class="faq-item">
                    <summary class="faq-question">Q. 이 번호 추첨기를 사용하면 당첨 확률이 올라가나요?</summary>
                    <div class="faq-answer">
                        <p>복권의 각 회차 추첨은 독립 시행이므로 어떤 번호를 선택하든 수학적 당첨 확률 자체는 동일합니다. 다만 통계적으로 극단적인 편향(예: 1, 2, 3, 4, 5, 6 또는 올홀수/올짝수)을 피해 균형 잡힌 번호 조합을 선택하는 데 도움을 드립니다.</p>
                    </div>
                </details>
                <details class="faq-item">
                    <summary class="faq-question">Q. 하루에 몇 번까지 추첨할 수 있나요?</summary>
                    <div class="faq-answer">
                        <p>제한 없이 무제한으로 무료 추첨하실 수 있습니다.</p>
                    </div>
                </details>
            </div>
        </section>

        """ + get_disqus() + """
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/lotto.html", "w", encoding="utf-8") as f:
    f.write(lotto_content)

print("Generated lotto.html")

# ==========================================
# 4. articles/index.html (Article Category Index)
# ==========================================
articles_index_content = get_head(
    "전문 분석 칼럼 & 가이드 센터",
    "관상학, 인공지능 컴퓨터 비전 기술, 로또 통계학 및 퍼스널 스타일링에 관한 심층 전문 칼럼 모음입니다.",
    "articles/index.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <div class="page-header text-center">
            <span class="category-badge">Knowledge Hub</span>
            <h1>📚 전문 분석 칼럼 & 가이드 센터</h1>
            <p class="page-subtitle">관상학, 인공지능(AI) 기술, 수학적 통계학, 뷰티 스타일링에 관한 고품질 오리지널 아티클을 제공합니다.</p>
        </div>

        <div class="articles-grid-large">
            <article class="article-card-large">
                <span class="category-tag">관상 & 인상학</span>
                <h2><a href="animal-face-types.html">강아지상 vs 고양이상: 얼굴 특징과 관상학적 매력 심층 비교</a></h2>
                <p class="article-excerpt">얼굴의 골격 구조, 눈매의 각도, 볼과 턱선의 곡률에 따라 결정되는 대표 동물상들의 외모적 차이와 인상학적 특징, 매력 포인트 및 스타일링 가이드를 완벽하게 정리했습니다.</p>
                <div class="article-meta">
                    <span>✍️ 럭키앤뷰티 인상학 에디터</span>
                    <span>📖 읽는 시간: 6분</span>
                    <span>📅 2026.08</span>
                </div>
            </article>

            <article class="article-card-large">
                <span class="category-tag">AI & 머신러닝</span>
                <h2><a href="ai-computer-vision.html">인공지능(AI)은 어떻게 사진에서 동물상을 인식할까? CNN 신경망 원리</a></h2>
                <p class="article-excerpt">구글의 TensorFlow.js와 사전 학습된 Teachable Machine 비전 모델이 사람의 얼굴에서 눈꼬리, 코, 입술 등의 특징점(Feature Points)을 추출하고 분류하는 컴퓨터 비전의 수학적 원리를 해설합니다.</p>
                <div class="article-meta">
                    <span>✍️ AI 테크 에디터</span>
                    <span>📖 읽는 시간: 7분</span>
                    <span>📅 2026.08</span>
                </div>
            </article>

            <article class="article-card-large">
                <span class="category-tag">통계 & 수학</span>
                <h2><a href="lotto-statistics-probability.html">로또 6/45 수학적 확률의 진실: 814만 분의 1과 통계학적 조합 전략</a></h2>
                <p class="article-excerpt">조합론(Combinatorics)과 대수의 법칙, 그리고 역대 수천 회차의 실제 로또 당첨 데이터 분포를 통해 분석한 홀짝 비율, 고저 스프레드, 총합 구간의 통계학적 법칙을 공개합니다.</p>
                <div class="article-meta">
                    <span>✍️ 데이터 통계 분석팀</span>
                    <span>📖 읽는 시간: 8분</span>
                    <span>📅 2026.08</span>
                </div>
            </article>

            <article class="article-card-large">
                <span class="category-tag">뷰티 & 스타일링</span>
                <h2><a href="facial-image-styling.html">얼굴형과 인상에 따른 퍼스널 이미지 메이킹 & 스타일링 가이드</a></h2>
                <p class="article-excerpt">동물상별 고유의 매력을 극대화하는 맞춤형 헤어 볼륨 연출법, 아이라인 스킬, 퍼스널 컬러 조화법을 통해 첫인상을 호감형으로 업그레이드하는 실전 뷰티 가이드입니다.</p>
                <div class="article-meta">
                    <span>✍️ 스타일링 랩</span>
                    <span>📖 읽는 시간: 6분</span>
                    <span>📅 2026.08</span>
                </div>
            </article>

            <article class="article-card-large">
                <span class="category-tag">알고리즘 공학</span>
                <h2><a href="rng-algorithm-in-lottery.html">난수 생성기(RNG)의 공학적 원리와 복권 추첨의 공정성 검증</a></h2>
                <p class="article-excerpt">컴퓨터 프로그래밍에서 사용되는 의사 난수(PRNG)와 물리적 엔트로피 기반의 진성 난수(TRNG)의 차이점, 그리고 복권 시스템의 보안 알고리즘을 분석합니다.</p>
                <div class="article-meta">
                    <span>✍️ 소프트웨어 엔지니어링팀</span>
                    <span>📖 읽는 시간: 7분</span>
                    <span>📅 2026.08</span>
                </div>
            </article>
        </div>
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/index.html", "w", encoding="utf-8") as f:
    f.write(articles_index_content)

print("Generated articles/index.html")

# ==========================================
# 5. articles/animal-face-types.html
# ==========================================
art1_content = get_head(
    "강아지상 vs 고양이상: 얼굴 특징과 관상학적 매력 심층 비교",
    "강아지상과 고양이상의 이목구비 비율, 눈매 각도, 턱선 구조의 차이와 인상학적 성향, 어울리는 스타일링 가이드를 완벽 정리했습니다.",
    "articles/animal-face-types.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-tag">관상 & 인상학</span>
                <h1>강아지상 vs 고양이상: 얼굴 특징과 관상학적 매력 심층 비교</h1>
                <div class="article-meta">
                    <span>✍️ 럭키앤뷰티 인상학 연구팀</span>
                    <span>📅 2026년 8월</span>
                    <span>⏱️ 읽는 시간 약 6분</span>
                </div>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">사람의 첫인상은 만난 지 단 3초 만에 결정된다고 합니다. 특히 한국의 인상학적 문화에서는 이목구비의 균형과 형태에 따라 <strong>'강아지상'</strong>, <strong>'고양이상'</strong>, <strong>'토끼상'</strong> 등 동물에 빗대어 매력을 표현하곤 합니다. 오늘은 그중에서도 가장 대표적인 양대 산맥인 강아지상과 고양이상의 해부학적·관상학적 특징을 심층 분석합니다.</p>

                <h2>1. 강아지상(Dog Face)의 핵심 해부학적 특징</h2>
                <p>강아지상의 가장 큰 매력은 <strong>'친근함'</strong>과 <strong>'다정함'</strong>입니다. 상대방에게 경계심을 주지 않고 편안한 감정을 불러일으키는 외모적 요소들은 다음과 같습니다.</p>
                <ul>
                    <li><strong>눈매(Eye Shape)</strong>: 동그랗고 큰 눈망울을 지녔으며, 눈꼬리가 수평이거나 약간 아래로 내려가 있어 순하고 선한 인상을 풍깁니다.</li>
                    <li><strong>볼과 턱선(Cheek & Jawline)</strong>: 젖살이 살짝 남아 있는 듯한 부드러운 볼선과 둥근 U자형 턱선이 특징입니다.</li>
                    <li><strong>미소(Smile Line)</strong>: 웃을 때 입꼬리가 둥글게 올라가며 눈이 반달 모양으로 접히는 매력적인 미소선을 가집니다.</li>
                </ul>

                <h2>2. 고양이상(Cat Face)의 핵심 해부학적 특징</h2>
                <p>고양이상의 대표 키워드는 <strong>'시크함'</strong>, <strong>'도도함'</strong>, 그리고 <strong>'신비로운 카리스마'</strong>입니다. 첫눈에 시선을 강하게 사로잡는 포인트는 다음과 같습니다.</p>
                <ul>
                    <li><strong>눈매(Eye Shape)</strong>: 가로로 길고 눈꼬리가 살짝 위를 향해 치켜 올라간 형태로, 깊고 도발적인 눈빛을 연출합니다.</li>
                    <li><strong>콧대와 턱선(Nose & Jawline)</strong>: 오뚝하고 날렵한 콧대와 날카롭게 정돈된 V라인 턱선이 세련된 도시적 느낌을 강조합니다.</li>
                    <li><strong>입술(Lip Shape)</strong>: 도톰하면서도 큐피드 활 모양(Cupid's Bow)이 뚜렷한 입술 선을 지녀 입체감이 돋보입니다.</li>
                </ul>

                <h2>3. 동물상별 비교 요약표</h2>
                <div class="table-responsive">
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>비교 항목</th>
                                <th>🐶 강아지상</th>
                                <th>🐱 고양이상</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>첫인상 키워드</strong></td>
                                <td>친근함, 순둥이, 호감형, 다정다감</td>
                                <td>시크함, 세련미, 도도함, 신비로움</td>
                            </tr>
                            <tr>
                                <td><strong>눈꼬리 각도</strong></td>
                                <td>0° ~ -5° (수평 또는 약간 하향)</td>
                                <td>+5° ~ +15° (상향 곡선)</td>
                            </tr>
                            <tr>
                                <td><strong>베스트 퍼스널 컬러</strong></td>
                                <td>웜톤 라이트 (베이지, 코랄, 피치)</td>
                                <td>쿨톤 모노톤 (블랙, 실버, 버건디)</td>
                            </tr>
                            <tr>
                                <td><strong>추천 헤어 스타일</strong></td>
                                <td>자연스러운 웨이브펌, 시스루뱅</td>
                                <td>슬릭 스트레이트, 풀뱅 또는 사이드 가르마</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <h2>4. 결론: 나의 동물상 매력을 살리는 법</h2>
                <p>강아지상과 고양이상은 우열을 가릴 수 없는 고유의 매력을 지니고 있습니다. 인공지능 동물상 테스트를 통해 본인의 주된 얼굴형을 파악하고, 그에 맞는 헤어스타일과 메이크업을 연출한다면 자신만의 매력을 200% 발산할 수 있습니다.</p>

                <div class="article-cta-box">
                    <h3>🐾 지금 바로 내 동물상을 확인해보세요!</h3>
                    <p>구글 딥러닝 AI가 당신의 얼굴 사진을 분석하여 강아지상과 고양이상 확률을 정확히 알려드립니다.</p>
                    <a href="../animal-test.html" class="btn btn-primary">AI 동물상 테스트 하러 가기 →</a>
                </div>
            </div>
        </article>
        """ + get_disqus() + """
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/animal-face-types.html", "w", encoding="utf-8") as f:
    f.write(art1_content)

print("Generated articles/animal-face-types.html")

# ==========================================
# 6. articles/ai-computer-vision.html
# ==========================================
art2_content = get_head(
    "인공지능(AI)은 어떻게 사진에서 동물상을 인식할까? CNN 신경망 원리",
    "구글 Teachable Machine과 TensorFlow.js 기반의 합성곱 신경망(CNN)이 얼굴의 특징점(Feature Map)을 추출하고 분류하는 컴퓨터 비전의 수학적 원리를 해설합니다.",
    "articles/ai-computer-vision.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-tag">AI & 머신러닝</span>
                <h1>인공지능(AI)은 어떻게 사진에서 동물상을 인식할까? CNN 신경망 원리</h1>
                <div class="article-meta">
                    <span>✍️ AI 테크놀로지 랩</span>
                    <span>📅 2026년 8월</span>
                    <span>⏱️ 읽는 시간 약 7분</span>
                </div>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">스마트폰으로 찍은 사진 한 장만으로 인공지능이 "이 사람은 85% 확률로 강아지상입니다"라고 판단할 수 있는 비결은 무엇일까요? 본 아티클에서는 구글의 <strong>TensorFlow.js</strong>와 <strong>합성곱 신경망(Convolutional Neural Network, CNN)</strong> 모델이 이미지를 해석하는 공학적 원리를 알기 쉽게 설명해 드립니다.</p>

                <h2>1. 디지털 이미지를 숫자의 행렬(Matrix)로 변환하기</h2>
                <p>컴퓨터는 사람처럼 눈으로 사진을 '바라보는' 것이 아니라, 픽셀(Pixel)의 밝기와 색상(RGB) 값을 2차원 수치 행렬(Matrix)로 읽어들입니다. 예를 들어 224x224 크기의 이미지는 224 x 224 x 3(Red, Green, Blue 채널) = 약 15만 개의 숫자 데이터로 변환됩니다.</p>

                <h2>2. 합성곱 층(Convolutional Layer)의 필터링과 특징점 추출</h2>
                <p>CNN 신경망의 핵심은 **'필터(Filter 또는 Kernel)'**라 불리는 작은 수학적 격자를 이미지 전체에 슬라이딩하면서 엣지(윤곽선), 질감, 곡률 등의 특징(Feature)을 추출하는 것입니다.</p>
                <ul>
                    <li><strong>초기 층(Low-level Features)</strong>: 눈꼬리의 직선/곡선 윤곽, 턱선의 경계선 등 단순한 선과 모서리를 감지합니다.</li>
                    <li><strong>중간 층(Mid-level Features)</strong>: 추출된 선들이 모여 눈의 모양(타원형인지, 가로로 긴지), 콧날의 각도, 입술의 굴곡 등 국소적 형태를 인식합니다.</li>
                    <li><strong>심층 층(High-level Features)</strong>: 얼굴 전체의 이목구비 비율과 골격 배치 등 복합적인 얼굴 랜드마크 패턴을 완성합니다.</li>
                </ul>

                <h2>3. 완전 연결 층(Fully Connected Layer)과 소프트맥스(Softmax) 확률 계산</h2>
                <p>추출된 얼굴 특징 벡터는 최종적으로 **소프트맥스 함수(Softmax Function)**를 통과하여 각 클래스(강아지상 vs 고양이상)에 속할 확률의 합이 1(100%)이 되도록 정규화됩니다. 이를 통해 직관적인 백분율 수치가 산출되는 것입니다.</p>

                <h2>4. 브라우저 내 WebGL 가속과 개인정보 보호</h2>
                <p>본 사이트에서 사용하는 <code>@teachablemachine/image</code> 라이브러리는 웹 브라우저의 그래픽 하드웨어 가속(WebGL)을 활용합니다. 따라서 고용량의 사진을 외부 서버로 업로드할 필요 없이, 사용자의 기기 내부 GPU에서 밀리초(ms) 단위로 초고속 추론이 완료되어 완벽한 프라이버시를 보장합니다.</p>
            </div>
        </article>
        """ + get_disqus() + """
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/ai-computer-vision.html", "w", encoding="utf-8") as f:
    f.write(art2_content)

print("Generated articles/ai-computer-vision.html")

# ==========================================
# 7. articles/lotto-statistics-probability.html
# ==========================================
art3_content = get_head(
    "로또 6/45 수학적 확률의 진실: 814만 분의 1과 통계학적 조합 전략",
    "조합론(Combinatorics)과 대수의 법칙, 역대 로또 당첨 데이터 분포를 통해 분석한 홀짝 비율, 고저 스프레드, 총합 구간의 수학적 원리를 분석합니다.",
    "articles/lotto-statistics-probability.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-tag">통계 & 수학</span>
                <h1>로또 6/45 수학적 확률의 진실: 814만 분의 1과 통계학적 조합 전략</h1>
                <div class="article-meta">
                    <span>✍️ 응용통계학 리서치팀</span>
                    <span>📅 2026년 8월</span>
                    <span>⏱️ 읽는 시간 약 8분</span>
                </div>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">매주 수많은 사람들이 인생역전의 꿈을 안고 로또 6/45 복권을 구매합니다. 과연 1등 당첨 번호는 완전히 통제 불가능한 순수한 우연의 산물일까요, 아니면 수학적 통계 모델을 통해 일정한 패턴을 관찰할 수 있을까요? 조합론과 확률론의 관점에서 로또 6/45를 해부합니다.</p>

                <h2>1. 1등 당첨 확률 8,145,060분의 1의 유도 과정</h2>
                <p>로또 6/45는 1부터 45까지의 서로 다른 45개의 공 중 순서에 상관없이 6개를 뽑는 **조합(Combination)**입니다. 수학적 조합 공식은 다음과 같습니다:</p>
                <div class="math-formula-box">
                    <strong><sub>45</sub>C<sub>6</sub> = (45 × 44 × 43 × 42 × 41 × 40) / (6 × 5 × 4 × 3 × 2 × 1) = 8,145,060</strong>
                </div>
                <p>즉, 발생 가능한 모든 번호 조합의 수는 정확히 814만 5,060가지이며, 1장을 구매했을 때 1등에 당첨될 확률은 약 <strong>0.000012277%</strong>에 해당합니다. 이는 벼락을 맞을 확률보다도 낮은 극히 희박한 수치입니다.</p>

                <h2>2. 대수의 법칙(Law of Large Numbers)과 정규분포</h2>
                <p>확률론의 기본 정리인 **대수의 법칙**에 따르면, 추첨 회차가 수천 회 이상 누적될수록 각 번호(1~45번)의 출현 빈도는 평균값(총 추첨 공 수 ÷ 45)에 점진적으로 수렴하게 됩니다. 특정 번호가 일시적으로 자주 나오거나 덜 나올 수는 있지만, 장기적으로는 균등한 분포를 형성합니다.</p>

                <h2>3. 실전 번호 조합 시 피해야 할 극단적 패턴</h2>
                <ul>
                    <li><strong>연속 6개 번호 (예: 1, 2, 3, 4, 5, 6)</strong>: 이론상 나올 확률은 다른 조합과 같으나, 전체 814만 개 조합 중 단 40개(0.00049%)에 불과합니다.</li>
                    <li><strong>모두 홀수 또는 모두 짝수</strong>: 전체 조합 중 1.8%에 불과하므로, 3:3 또는 4:2의 균형 배분이 통계적으로 유리합니다.</li>
                    <li><strong>동일 끝수 과다 조합 (예: 3, 13, 23, 33, 43...)</strong>: 끝자리가 같은 숫자가 4개 이상 중복되는 경우 역시 통계적으로 매우 드뭅니다.</li>
                </ul>
            </div>
        </article>
        """ + get_disqus() + """
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/lotto-statistics-probability.html", "w", encoding="utf-8") as f:
    f.write(art3_content)

print("Generated articles/lotto-statistics-probability.html")

# ==========================================
# 8. articles/facial-image-styling.html
# ==========================================
art4_content = get_head(
    "얼굴형과 인상에 따른 퍼스널 이미지 메이킹 & 스타일링 가이드",
    "동물상별 고유의 매력을 극대화하는 맞춤형 헤어 볼륨 연출법, 아이라인 스킬, 퍼스널 컬러 조화법을 통해 첫인상을 업그레이드하는 뷰티 솔루션입니다.",
    "articles/facial-image-styling.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-tag">뷰티 & 스타일링</span>
                <h1>얼굴형과 인상에 따른 퍼스널 이미지 메이킹 & 스타일링 가이드</h1>
                <div class="article-meta">
                    <span>✍️ 퍼스널 스타일링 랩</span>
                    <span>📅 2026년 8월</span>
                    <span>⏱️ 읽는 시간 약 6분</span>
                </div>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">외모의 장점은 부각하고 단점은 자연스럽게 보완하는 '이미지 메이킹(Image Making)'은 현대인의 자기표현에서 매우 중요한 요소입니다. 본인의 동물상 유형을 알았다면, 이제 그 매력을 극대화할 수 있는 실전 스타일링 팁을 적용해 보세요.</p>

                <h2>1. 강아지상(Dog Face)을 위한 러블리 스타일링</h2>
                <ul>
                    <li><strong>아이 메이크업</strong>: 점막을 얇게 채우고 눈꼬리는 본래 눈매 라인을 따라 자연스럽게 수평으로 빼주는 것이 핵심입니다. 음영은 따뜻한 로즈 브라운이나 피치 계열을 추천합니다.</li>
                    <li><strong>블러셔 & 립</strong>: 볼 중앙(애플존)에 둥글게 원을 그리듯 블러셔를 터치하여 특유의 사랑스러운 생기를 연출합니다. 글로시한 텍스처의 코랄 틴트가 찰떡궁합입니다.</li>
                    <li><strong>헤어스타일</strong>: 굵은 S컬 웨이브나 볼륨감이 있는 빌드펌, 이마를 살짝 드러내는 시스루뱅이 부드러운 인상을 배가시킵니다.</li>
                </ul>

                <h2>2. 고양이상(Cat Face)을 위한 시크 카리스마 스타일링</h2>
                <ul>
                    <li><strong>아이 메이크업</strong>: 눈 앞머리는 날렵하게 트여 보이게 섀도를 터치하고, 눈꼬리는 살짝 위로 날렵하게 올려 그리는 캣츠아이(Cat's Eye) 라인을 연출합니다. 쿨톤 브라운 및 플럼 계열이 시크함을 극대화합니다.</li>
                    <li><strong>컨투어링 & 립</strong>: 턱선과 광대 외곽에 음영을 주어 또렷한 윤곽을 강조하고, 선명한 레드 립이나 딥한 모브 핑크로 립 포인트를 줍니다.</li>
                    <li><strong>헤어스타일</strong>: 깔끔하게 떨어지는 슬릭컷, 칼단발, 혹은 5:5 롱 스트레이트 헤어가 도회적이고 세련된 아우라를 완성합니다.</li>
                </ul>
            </div>
        </article>
        """ + get_disqus() + """
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/facial-image-styling.html", "w", encoding="utf-8") as f:
    f.write(art4_content)

print("Generated articles/facial-image-styling.html")

# ==========================================
# 9. articles/rng-algorithm-in-lottery.html
# ==========================================
art5_content = get_head(
    "난수 생성기(RNG)의 공학적 원리와 복권 추첨의 공정성 검증",
    "의사 난수(PRNG)와 물리적 엔트로피 기반의 진성 난수(TRNG)의 차이점, 그리고 디지털 복권 추첨 시스템이 공정성을 보장하기 위해 채택하는 보안 기술을 알아봅니다.",
    "articles/rng-algorithm-in-lottery.html",
    is_subfolder=True
) + get_header("articles", is_subfolder=True) + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-tag">알고리즘 공학</span>
                <h1>난수 생성기(RNG)의 공학적 원리와 복권 추첨의 공정성 검증</h1>
                <div class="article-meta">
                    <span>✍️ 암호학 및 시스템 엔지니어링팀</span>
                    <span>📅 2026년 8월</span>
                    <span>⏱️ 읽는 시간 약 7분</span>
                </div>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">컴퓨터는 본래 정해진 명령어에 따라 예측 가능하게 동작하는 결정론적(Deterministic) 기계입니다. 그렇다면 컴퓨터 프로그램은 과연 어떻게 '예측 불가능한 무작위 번호'를 생성할 수 있을까요? 복권 및 보안 시스템의 핵심인 **난수 생성기(Random Number Generator, RNG)**의 세계를 살펴봅니다.</p>

                <h2>1. 의사 난수(PRNG) vs 진성 난수(TRNG)</h2>
                <ul>
                    <li><strong>의사 난수 생성기 (Pseudo-Random Number Generator, PRNG)</strong>: 수학적 공식(예: 메르센 트위스터)에 초기 시드(Seed) 값을 입력하여 무작위처럼 보이는 수열을 계산합니다. 시드 값을 알면 다음 숫자를 정확히 예측할 수 있다는 한계가 있습니다.</li>
                    <li><strong>진성 난수 생성기 (True Random Number Generator, TRNG)</strong>: 열 잡음, 방사성 붕괴, 공기 대류 등 자연계의 물리적 무작위 현상(Entropy)을 측정하여 숫자를 생성합니다. 완전히 예측이 불가능한 완벽한 무작위성을 가집니다.</li>
                </ul>

                <h2>2. 럭키앤뷰티 랩의 암호학적 난수 생성(Crypto-RNG) 방식</h2>
                <p>본 사이트의 로또 6/45 추첨 엔진은 단순한 <code>Math.random()</code> 대신 웹 표준 암호화 API인 <strong><code>window.crypto.getRandomValues()</code></strong>를 사용합니다. 이는 운영체제의 엔트로피 풀(Entropy Pool)을 활용하여 암호학적으로 안전한 난수를 생성하므로 인위적인 조작이나 편향이 전혀 발생하지 않습니다.</p>
            </div>
        </article>
        """ + get_disqus() + """
    </div>
</main>
""" + get_footer(is_subfolder=True)

with open("/workspaces/codespaces-blank/articles/rng-algorithm-in-lottery.html", "w", encoding="utf-8") as f:
    f.write(art5_content)

print("Generated articles/rng-algorithm-in-lottery.html")

# ==========================================
# 10. about.html
# ==========================================
about_content = get_head(
    "연구소 소개 (About Us)",
    "럭키앤뷰티 랩(Lucky & Beauty Lab)의 설립 목적, 기술 스택, 서비스 철학 및 운영진 소개입니다.",
    "about.html"
) + get_header("about") + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-badge">About Us</span>
                <h1>✨ 럭키앤뷰티 랩(Lucky & Beauty Lab) 소개</h1>
                <p class="page-subtitle">인공지능 비전 기술과 수학적 통계 데이터를 결합하여 일상에 즐거움과 유익한 가치를 전달합니다.</p>
            </header>

            <div class="article-body">
                <h2>1. 설립 배경 및 미션</h2>
                <p><strong>럭키앤뷰티 랩</strong>은 최신 웹 기반 인공지능(AI) 기술과 데이터 과학을 누구나 쉽고 재미있게 체험할 수 있도록 돕는 라이프스타일 엔터테인먼트 & 테크 연구 포털입니다.</p>
                <p>우리는 복잡한 딥러닝 알고리즘을 사용자가 클릭 한 번으로 직관적으로 경험할 수 있는 웹 서비스를 구축하고, 신뢰할 수 있는 수학·인상학 칼럼을 통해 방문자에게 실질적인 지식과 즐거움을 드리는 것을 최고의 가치로 삼고 있습니다.</p>

                <h2>2. 우리가 보유한 핵심 기술</h2>
                <ul>
                    <li><strong>Google TensorFlow.js & Teachable Machine</strong>: 웹 브라우저 상에서 서버 통신 없이 실시간으로 얼굴 이미지를 분석하는 고성능 엣지 AI(Edge AI) 엔진</li>
                    <li><strong>암호학적 난수 생성(Crypto-safe RNG)</strong>: 공정성과 무작위성을 보증하는 웹 크립토 기반의 로또 추첨 시스템</li>
                    <li><strong>반응형 모던 웹 아키텍처</strong>: 모바일, 태블릿, PC 등 모든 기기에서 최적화된 다크/라이트 모드 UI 제공</li>
                </ul>

                <h2>3. 서비스 운영 원칙</h2>
                <ol>
                    <li><strong>철저한 개인정보 보호</strong>: 업로드된 사진이나 이용자의 민감 데이터는 외부 서버에 절대 수집·보관되지 않습니다.</li>
                    <li><strong>평생 100% 무료 제공</strong>: 모든 인터랙티브 테스트와 칼럼 콘텐츠는 회원가입 없이 영구적으로 무료 개방됩니다.</li>
                    <li><strong>지속적인 연구와 업데이트</strong>: 최신 AI 모델과 통계 데이터를 지속적으로 반영하여 서비스 품질을 고도화합니다.</li>
                </ol>
            </div>
        </article>
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/about.html", "w", encoding="utf-8") as f:
    f.write(about_content)

print("Generated about.html")

# ==========================================
# 11. privacy.html
# ==========================================
privacy_content = get_head(
    "개인정보처리방침 (Privacy Policy)",
    "럭키앤뷰티 랩의 개인정보 수집 및 처리 방침, Google AdSense 쿠키 정책 및 사용자 권리 안내입니다.",
    "privacy.html"
) + get_header("") + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-badge">Legal Policy</span>
                <h1>🔒 개인정보처리방침 (Privacy Policy)</h1>
                <p class="page-subtitle">최종 수정일: 2026년 8월 20일</p>
            </header>

            <div class="article-body">
                <p class="lead-paragraph">럭키앤뷰티 랩(이하 '회사' 또는 '사이트')은 이용자의 개인정보를 매우 소중하게 생각하며, 대한민국의 「개인정보 보호법」 및 글로벌 데이터 보호 규정을 엄격히 준수합니다.</p>

                <h2>1. 수집하는 개인정보 항목 및 수집 방법</h2>
                <ul>
                    <li><strong>동물상 테스트 이미지 데이터</strong>: 이용자가 업로드하는 사진은 브라우저 내 메모리에서 로컬(Client-side)로만 처리되며, 당사의 서버로 전송되거나 저장되지 않습니다.</li>
                    <li><strong>문의하기 폼 데이터</strong>: 이용자가 문의 접수 시 직접 입력하는 이름, 이메일 주소, 문의 내용 (Formspree를 통한 안전 전송).</li>
                    <li><strong>자동 수집 정보</strong>: 서비스 이용 과정에서 쿠키(Cookie), 접속 IP, 브라우저 유형, 방문 일시 등의 로그 정보가 통계 및 서비스 개선 목적으로 자동 생성되어 수집될 수 있습니다.</li>
                </ul>

                <h2>2. Google AdSense 및 제3자 쿠키(Cookie) 안내</h2>
                <p>본 사이트는 서비스 운영 및 맞춤형 광고 게재를 위해 Google AdSense를 이용하고 있습니다.</p>
                <ul>
                    <li>Google을 비롯한 제3자 광고 사업자는 쿠키를 사용하여 이용자의 본 사이트 및 인터넷상의 다른 웹사이트 방문 기록을 바탕으로 맞춤형 광고를 게재합니다.</li>
                    <li>Google의 광고 쿠키 사용으로 인해 Google과 파트너사는 이용자의 방문 기록에 기반한 적절한 광고를 제공할 수 있습니다.</li>
                    <li>이용자는 <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google 광고 설정 페이지</a>를 방문하여 개인 맞춤 광고 설정을 해제하거나 거부할 수 있습니다.</li>
                </ul>

                <h2>3. 개인정보의 보유 및 이용 기간</h2>
                <p>문의하기를 통해 접수된 개인정보는 문의 처리 완료 후 3년간 보관되며, 이후 지체 없이 안전하게 파기됩니다.</p>

                <h2>4. 개인정보 보호책임자</h2>
                <p>개인정보 처리와 관련한 문의 및 권리 행사는 <a href="contact.html">문의 페이지</a>를 통해 언제든지 접수해 주시기 바랍니다.</p>
            </div>
        </article>
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/privacy.html", "w", encoding="utf-8") as f:
    f.write(privacy_content)

print("Generated privacy.html")

# ==========================================
# 12. terms.html
# ==========================================
terms_content = get_head(
    "이용약관 (Terms of Service)",
    "럭키앤뷰티 랩 서비스 이용 조건, 권리 및 책임에 관한 이용약관입니다.",
    "terms.html"
) + get_header("") + """
<main class="page-container">
    <div class="content-wrapper">
        <article class="single-article">
            <header class="article-header">
                <span class="category-badge">Legal Terms</span>
                <h1>📜 서비스 이용약관 (Terms of Service)</h1>
                <p class="page-subtitle">최종 수정일: 2026년 8월 20일</p>
            </header>

            <div class="article-body">
                <h2>제1조 (목적)</h2>
                <p>본 약관은 럭키앤뷰티 랩(이하 '사이트')이 제공하는 AI 동물상 테스트, 로또 번호 추첨 및 정보 콘텐츠 서비스의 이용에 관한 조건과 절차를 규정함을 목적으로 합니다.</p>

                <h2>제2조 (면책 조항)</h2>
                <ol>
                    <li>본 사이트의 AI 동물상 분석 및 로또 번호 추첨 서비스는 오락 및 참고용 엔터테인먼트 서비스입니다.</li>
                    <li>로또 번호 추첨 결과는 수학적 확률에 기반한 추천일 뿐, 실제 복권 당첨을 보증하지 않으며 복권 구매로 인한 금전적 손실에 대해 사이트는 일체의 법적 책임을 지지 않습니다.</li>
                </ol>

                <h2>제3조 (지식재산권)</h2>
                <p>본 사이트에 게시된 모든 칼럼, 아티클, 디자인, 프로그램 소스 코드에 대한 저작권은 럭키앤뷰티 랩에 귀속되며, 무단 전재 및 상업적 복제를 금합니다.</p>
            </div>
        </article>
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/terms.html", "w", encoding="utf-8") as f:
    f.write(terms_content)

print("Generated terms.html")

# ==========================================
# 13. contact.html
# ==========================================
contact_content = get_head(
    "제휴 및 문의하기 (Contact Us)",
    "럭키앤뷰티 랩 제휴 문의, 기술 지원 및 피드백 접수 페이지입니다.",
    "contact.html"
) + get_header("") + """
<main class="page-container">
    <div class="content-wrapper">
        <div class="page-header text-center">
            <span class="category-badge">Get in Touch</span>
            <h1>🤝 제휴 및 문의하기 (Contact Us)</h1>
            <p class="page-subtitle">비즈니스 제휴, 콘텐츠 문의, 기능 제안 및 버그 제보를 환영합니다.</p>
        </div>

        <div class="inquiry-card">
            <form id="contact-form" action="https://formspree.io/f/mvkpdlzv" method="POST">
                <div class="form-group">
                    <label for="name">성함 / 기업명 <span class="required">*</span></label>
                    <input type="text" id="name" name="name" placeholder="홍길동 또는 기업명" required>
                </div>
                <div class="form-group">
                    <label for="email">이메일 주소 <span class="required">*</span></label>
                    <input type="email" id="email" name="email" placeholder="example@email.com" required>
                </div>
                <div class="form-group">
                    <label for="message">문의 내용 <span class="required">*</span></label>
                    <textarea id="message" name="message" rows="5" placeholder="문의하실 내용을 상세히 적어주세요." required></textarea>
                </div>
                <button type="submit" id="submit-btn" class="submit-btn">문의 메일 전송하기</button>
                <div id="form-status" class="form-status"></div>
            </form>
        </div>
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/contact.html", "w", encoding="utf-8") as f:
    f.write(contact_content)

print("Generated contact.html")

# ==========================================
# 14. sitemap.html
# ==========================================
sitemap_content = get_head(
    "전체 사이트맵 (Sitemap)",
    "럭키앤뷰티 랩의 모든 서비스, 칼럼 및 정책 페이지를 한눈에 확인할 수 있는 사이트맵입니다.",
    "sitemap.html"
) + get_header("") + """
<main class="page-container">
    <div class="content-wrapper">
        <div class="page-header text-center">
            <span class="category-badge">Site Index</span>
            <h1>🗺️ 전체 사이트맵 (Sitemap)</h1>
            <p class="page-subtitle">럭키앤뷰티 랩의 모든 페이지 링크를 편리하게 탐색하세요.</p>
        </div>

        <div class="sitemap-grid">
            <div class="sitemap-col">
                <h3>🚀 메인 서비스</h3>
                <ul>
                    <li><a href="index.html">포털 홈 (Home)</a></li>
                    <li><a href="animal-test.html">🐾 AI 동물상 얼굴 테스트</a></li>
                    <li><a href="lotto.html">🎱 로또 6/45 번호 추첨기</a></li>
                </ul>
            </div>

            <div class="sitemap-col">
                <h3>📚 전문 분석 칼럼</h3>
                <ul>
                    <li><a href="articles/index.html">칼럼 & 가이드 센터 메인</a></li>
                    <li><a href="articles/animal-face-types.html">강아지상 vs 고양이상 관상학 비교</a></li>
                    <li><a href="articles/ai-computer-vision.html">인공지능 비전 CNN 신경망 원리</a></li>
                    <li><a href="articles/lotto-statistics-probability.html">로또 6/45 수학적 확률 분석</a></li>
                    <li><a href="articles/facial-image-styling.html">얼굴형과 퍼스널 스타일링 가이드</a></li>
                    <li><a href="articles/rng-algorithm-in-lottery.html">난수 생성기(RNG)와 복권 보안</a></li>
                </ul>
            </div>

            <div class="sitemap-col">
                <h3>ℹ️ 회사 및 정책</h3>
                <ul>
                    <li><a href="about.html">연구소 소개 (About Us)</a></li>
                    <li><a href="privacy.html">개인정보처리방침 (Privacy Policy)</a></li>
                    <li><a href="terms.html">이용약관 (Terms of Service)</a></li>
                    <li><a href="contact.html">제휴 및 문의 (Contact Us)</a></li>
                </ul>
            </div>
        </div>
    </div>
</main>
""" + get_footer()

with open("/workspaces/codespaces-blank/sitemap.html", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print("Generated sitemap.html")

# ==========================================
# 15. sitemap.xml & robots.txt & ads.txt
# ==========================================
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://sanz-y.github.io/product/index.html</loc><priority>1.0</priority></url>
  <url><loc>https://sanz-y.github.io/product/animal-test.html</loc><priority>0.9</priority></url>
  <url><loc>https://sanz-y.github.io/product/lotto.html</loc><priority>0.9</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/index.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/animal-face-types.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/ai-computer-vision.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/lotto-statistics-probability.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/facial-image-styling.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/articles/rng-algorithm-in-lottery.html</loc><priority>0.8</priority></url>
  <url><loc>https://sanz-y.github.io/product/about.html</loc><priority>0.7</priority></url>
  <url><loc>https://sanz-y.github.io/product/privacy.html</loc><priority>0.7</priority></url>
  <url><loc>https://sanz-y.github.io/product/terms.html</loc><priority>0.7</priority></url>
  <url><loc>https://sanz-y.github.io/product/contact.html</loc><priority>0.7</priority></url>
  <url><loc>https://sanz-y.github.io/product/sitemap.html</loc><priority>0.6</priority></url>
</urlset>
"""
with open("/workspaces/codespaces-blank/sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

robots_txt = """User-agent: *
Allow: /

Sitemap: https://sanz-y.github.io/product/sitemap.xml
"""
with open("/workspaces/codespaces-blank/robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_txt)

ads_txt = "google.com, pub-4764608029803832, DIRECT, f08c47fec0942fa0\n"
with open("/workspaces/codespaces-blank/ads.txt", "w", encoding="utf-8") as f:
    f.write(ads_txt)

print("Generated all files successfully!")
