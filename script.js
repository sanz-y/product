// ==========================================
// 1. 테마 관리 (다크모드 / 라이트모드)
// ==========================================
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const themeText = document.getElementById('theme-text');

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    if (theme === 'dark') {
        if (themeIcon) themeIcon.textContent = '☀️';
        if (themeText) themeText.textContent = '라이트';
    } else {
        if (themeIcon) themeIcon.textContent = '🌙';
        if (themeText) themeText.textContent = '다크';
    }

    if (typeof DISQUS !== 'undefined') {
        try {
            DISQUS.reset({ reload: true });
        } catch (e) {}
    }
}

const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
applyTheme(initialTheme);

if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    });
}

// ==========================================
// 2. 토스트 알림 유틸리티
// ==========================================
const toast = document.getElementById('toast');

function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2500);
}

// ==========================================
// 3. 로또 번호 추첨 로직 (Crypto-safe RNG)
// ==========================================
const drawBtn = document.getElementById('draw-btn');
const lottoContainer = document.getElementById('lotto-container');

if (drawBtn && lottoContainer) {
    drawBtn.addEventListener('click', () => {
        const numbers = generateLottoNumbers();
        lottoContainer.innerHTML = '';
        
        numbers.forEach((num, index) => {
            setTimeout(() => {
                const ball = document.createElement('div');
                ball.classList.add('ball');
                ball.classList.add(getBallColorClass(num));
                ball.textContent = num;
                lottoContainer.appendChild(ball);
            }, index * 100);
        });
    });
}

function generateLottoNumbers() {
    const numbers = [];
    const array = new Uint32Array(1);
    while (numbers.length < 6) {
        window.crypto.getRandomValues(array);
        const rand = (array[0] % 45) + 1;
        if (!numbers.includes(rand)) {
            numbers.push(rand);
        }
    }
    return numbers.sort((a, b) => a - b);
}

function getBallColorClass(num) {
    if (num <= 10) return 'ball-yellow';
    if (num <= 20) return 'ball-blue';
    if (num <= 30) return 'ball-red';
    if (num <= 40) return 'ball-gray';
    return 'ball-green';
}

// ==========================================
// 4. AI 동물상 테스트 (Teachable Machine)
// ==========================================
const MODEL_URL = "https://teachablemachine.withgoogle.com/models/p74Y4s7yv/";
let model = null;

const ANIMAL_INFO = {
    dog: {
        badge: '🐶 강아지상 (Dog Face)',
        badgeClass: 'dog',
        title: '다정하고 사랑스러운 강아지상',
        desc: '보는 사람을 무장해제시키는 선하고 다정한 매력의 소유자! 동글동글 맑은 눈망울과 부드러운 볼선, 기분 좋은 미소로 누구에게나 호감을 주는 친근한 에너지를 뿜어냅니다. 주변 사람들에게 사랑을 듬뿍 받는 힐링형 스타일이에요.',
        tags: ['#멍뭉미', '#다정다감', '#애교만점', '#친근함', '#순둥이', '#호감형', '#보호본능']
    },
    cat: {
        badge: '🐱 고양이상 (Cat Face)',
        badgeClass: 'cat',
        title: '도도하고 매혹적인 고양이상',
        desc: '또렷하고 세련된 눈매와 시크한 분위기로 첫눈에 시선을 사로잡는 신비로운 매력의 소유자! 첫인상은 도도하고 차가워 보이지만, 알면 알수록 깊이 빠져드는 츤데레 매력이 가득합니다. 도회적인 카리스마가 돋보여요.',
        tags: ['#냥이상', '#도도함', '#시크매력', '#츤데레', '#신비로움', '#카리스마', '#세련미']
    }
};

async function loadModel() {
    if (model) return model;
    if (typeof tmImage === 'undefined') return null;
    try {
        const modelURL = MODEL_URL + "model.json";
        const metadataURL = MODEL_URL + "metadata.json";
        model = await tmImage.load(modelURL, metadataURL);
        return model;
    } catch (error) {
        console.error("AI 모델 로드 실패:", error);
        return null;
    }
}

const uploadArea = document.getElementById('upload-area');
const imageInput = document.getElementById('image-input');
const selectFileBtn = document.getElementById('select-file-btn');
const previewArea = document.getElementById('preview-area');
const faceImage = document.getElementById('face-image');
const loadingSpinner = document.getElementById('loading-spinner');
const resultArea = document.getElementById('result-area');

const resultBadge = document.getElementById('result-badge');
const resultTitle = document.getElementById('result-title');
const resultDesc = document.getElementById('result-desc');
const resultTags = document.getElementById('result-tags');
const dogPercent = document.getElementById('dog-percent');
const dogBar = document.getElementById('dog-bar');
const catPercent = document.getElementById('cat-percent');
const catBar = document.getElementById('cat-bar');

const retryBtn = document.getElementById('retry-btn');
const shareBtn = document.getElementById('share-btn');

if (selectFileBtn && imageInput) {
    selectFileBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        imageInput.click();
    });
}

if (uploadArea && imageInput) {
    uploadArea.addEventListener('click', () => {
        imageInput.click();
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadArea.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            uploadArea.classList.remove('dragover');
        });
    });

    uploadArea.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files && files.length > 0) {
            handleImageFile(files[0]);
        }
    });
}

if (imageInput) {
    imageInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files.length > 0) {
            handleImageFile(e.target.files[0]);
        }
    });
}

function handleImageFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('이미지 파일(JPG, PNG 등)만 업로드 가능합니다.');
        return;
    }

    const reader = new FileReader();
    reader.onload = (e) => {
        if (!faceImage) return;
        faceImage.src = e.target.result;
        
        if (uploadArea) uploadArea.style.display = 'none';
        if (previewArea) previewArea.style.display = 'block';
        if (loadingSpinner) loadingSpinner.style.display = 'block';
        if (resultArea) resultArea.style.display = 'none';

        faceImage.onload = async () => {
            await predict();
        };
    };
    reader.readAsDataURL(file);
}

async function predict() {
    const aiModel = await loadModel();
    if (!aiModel) {
        if (loadingSpinner) loadingSpinner.style.display = 'none';
        alert("AI 모델을 불러오지 못했습니다. 잠시 후 다시 시도해 주세요.");
        resetUpload();
        return;
    }

    try {
        const predictions = await aiModel.predict(faceImage, false);
        
        let dogProbability = 0;
        let catProbability = 0;

        predictions.forEach(p => {
            const label = p.className.toLowerCase();
            if (label.includes('dog')) {
                dogProbability = p.probability;
            } else if (label.includes('cat')) {
                catProbability = p.probability;
            }
        });

        const total = dogProbability + catProbability;
        const dogRate = total > 0 ? (dogProbability / total) * 100 : 50;
        const catRate = total > 0 ? (catProbability / total) * 100 : 50;

        const dogRounded = Math.round(dogRate);
        const catRounded = 100 - dogRounded;

        const primaryAnimal = dogRounded >= catRounded ? 'dog' : 'cat';
        const info = ANIMAL_INFO[primaryAnimal];

        if (resultBadge) {
            resultBadge.textContent = info.badge;
            resultBadge.className = `result-badge ${info.badgeClass}`;
        }
        if (resultTitle) resultTitle.textContent = info.title;
        if (resultDesc) resultDesc.textContent = info.desc;

        if (resultTags) {
            resultTags.innerHTML = '';
            info.tags.forEach(tag => {
                const span = document.createElement('span');
                span.className = 'tag-badge';
                span.textContent = tag;
                resultTags.appendChild(span);
            });
        }

        if (dogPercent) dogPercent.textContent = `${dogRounded}%`;
        if (catPercent) catPercent.textContent = `${catRounded}%`;

        if (loadingSpinner) loadingSpinner.style.display = 'none';
        if (resultArea) resultArea.style.display = 'block';

        setTimeout(() => {
            if (dogBar) dogBar.style.width = `${dogRounded}%`;
            if (catBar) catBar.style.width = `${catRounded}%`;
        }, 100);

    } catch (error) {
        console.error("예측 오류:", error);
        alert("사진 분석 중 오류가 발생했습니다. 다른 사진으로 시도해 주세요.");
        resetUpload();
    }
}

function resetUpload() {
    if (imageInput) imageInput.value = '';
    if (faceImage) faceImage.src = '';
    if (dogBar) dogBar.style.width = '0%';
    if (catBar) catBar.style.width = '0%';
    if (previewArea) previewArea.style.display = 'none';
    if (resultArea) resultArea.style.display = 'none';
    if (loadingSpinner) loadingSpinner.style.display = 'none';
    if (uploadArea) uploadArea.style.display = 'block';
}

if (retryBtn) {
    retryBtn.addEventListener('click', resetUpload);
}

if (shareBtn) {
    shareBtn.addEventListener('click', async () => {
        const shareData = {
            title: 'AI 동물상 얼굴 테스트 | 럭키앤뷰티 랩',
            text: '인공지능으로 나의 동물상도 분석하고 행운의 로또 번호도 뽑아보세요!',
            url: window.location.href
        };

        if (navigator.share) {
            try {
                await navigator.share(shareData);
            } catch (err) {}
        } else {
            try {
                await navigator.clipboard.writeText(window.location.href);
                showToast('링크가 클립보드에 복사되었습니다! 🎉');
            } catch (err) {
                showToast('링크 복사에 실패했습니다.');
            }
        }
    });
}

// ==========================================
// 5. 제휴 및 문의 폼 (Formspree AJAX)
// ==========================================
const contactForm = document.getElementById('contact-form');
const submitBtn = document.getElementById('submit-btn');
const formStatus = document.getElementById('form-status');

if (contactForm) {
    contactForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const originalBtnText = submitBtn.textContent;
        submitBtn.disabled = true;
        submitBtn.textContent = '전송 중...';
        formStatus.textContent = '';
        formStatus.className = 'form-status';

        try {
            const formData = new FormData(contactForm);
            const response = await fetch(contactForm.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            if (response.ok) {
                formStatus.textContent = '✅ 문의가 성공적으로 접수되었습니다! 빠른 시일 내에 답변드리겠습니다.';
                formStatus.className = 'form-status success';
                contactForm.reset();
            } else {
                const data = await response.json();
                if (data && data.errors) {
                    formStatus.textContent = '❌ ' + data.errors.map(err => err.message).join(', ');
                } else {
                    formStatus.textContent = '❌ 전송에 실패했습니다. 잠시 후 다시 시도해 주세요.';
                }
                formStatus.className = 'form-status error';
            }
        } catch (error) {
            formStatus.textContent = '❌ 네트워크 오류가 발생했습니다. 다시 시도해 주세요.';
            formStatus.className = 'form-status error';
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalBtnText;
        }
    });
}

window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('upload-area')) {
        loadModel();
    }
});
