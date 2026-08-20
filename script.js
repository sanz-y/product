// Teachable Machine 모델 URL
const MODEL_URL = "https://teachablemachine.withgoogle.com/models/p74Y4s7yv/";
let model = null;

// 동물상별 상세 데이터
const ANIMAL_INFO = {
    dog: {
        badge: '🐶 강아지상',
        badgeClass: 'dog',
        title: '다정하고 사랑스러운 강아지상',
        desc: '보는 사람을 기분 좋게 만들어주는 따뜻하고 순한 매력의 소유자! 동글동글 선한 눈매와 밝은 미소로 누구에게나 호감을 주는 친근한 에너지를 뿜어냅니다. 주변 사람들에게 사랑을 듬뿍 받는 스타일이에요.',
        tags: ['#멍뭉미', '#다정다감', '#애교만점', '#친근함', '#순둥이', '#호감형']
    },
    cat: {
        badge: '🐱 고양이상',
        badgeClass: 'cat',
        title: '도도하고 매혹적인 고양이상',
        desc: '또렷하고 매력적인 눈매와 시크한 분위기로 시선을 사로잡는 신비로운 매력의 소유자! 첫인상은 도도하고 쿨해보이지만, 알면 알수록 깊이 빠져드는 츤데레 매력이 가득합니다. 세련된 카리스마가 돋보여요.',
        tags: ['#냥이상', '#도도함', '#시크매력', '#츤데레', '#신비로움', '#카리스마']
    }
};

// AI 모델 로드
async function loadModel() {
    if (model) return model;
    try {
        const modelURL = MODEL_URL + "model.json";
        const metadataURL = MODEL_URL + "metadata.json";
        model = await tmImage.load(modelURL, metadataURL);
        return model;
    } catch (error) {
        console.error("모델 로딩 실패:", error);
        alert("AI 모델을 불러오는 중 오류가 발생했습니다. 네트워크 연결을 확인해 주세요.");
        return null;
    }
}

// DOM 요소들
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
const toast = document.getElementById('toast');

// 파일 선택 버튼 트리거
if (selectFileBtn) {
    selectFileBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        imageInput.click();
    });
}

if (uploadArea) {
    uploadArea.addEventListener('click', () => {
        imageInput.click();
    });

    // 드래그 앤 드롭 이벤트
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

// 파일 인풋 변경 이벤트
imageInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files.length > 0) {
        handleImageFile(e.target.files[0]);
    }
});

// 이미지 파일 처리 및 예측 실행
function handleImageFile(file) {
    if (!file.type.startsWith('image/')) {
        alert('이미지 파일(JPG, PNG 등)만 업로드 가능합니다.');
        return;
    }

    const reader = new FileReader();
    reader.onload = async (e) => {
        faceImage.src = e.target.result;
        
        // 화면 전환: 업로드 영역 숨기고 미리보기/로딩 표시
        uploadArea.style.display = 'none';
        previewArea.style.display = 'block';
        loadingSpinner.style.display = 'block';
        resultArea.style.display = 'none';

        // 이미지가 로드된 후 예측 수행
        faceImage.onload = async () => {
            await predict();
        };
    };
    reader.readAsDataURL(file);
}

// 인공지능 동물상 예측 함수
async function predict() {
    const aiModel = await loadModel();
    if (!aiModel) {
        loadingSpinner.style.display = 'none';
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

        // 합이 1이 되도록 정규화
        const total = dogProbability + catProbability;
        const dogRate = total > 0 ? (dogProbability / total) * 100 : 50;
        const catRate = total > 0 ? (catProbability / total) * 100 : 50;

        const dogRounded = Math.round(dogRate);
        const catRounded = 100 - dogRounded;

        // 주 동물상 판정
        const primaryAnimal = dogRounded >= catRounded ? 'dog' : 'cat';
        const info = ANIMAL_INFO[primaryAnimal];

        // 결과 UI 렌더링
        resultBadge.textContent = info.badge;
        resultBadge.className = `result-badge ${info.badgeClass}`;
        resultTitle.textContent = info.title;
        resultDesc.textContent = info.desc;

        // 태그 렌더링
        resultTags.innerHTML = '';
        info.tags.forEach(tag => {
            const span = document.createElement('span');
            span.className = 'tag-badge';
            span.textContent = tag;
            resultTags.appendChild(span);
        });

        // 퍼센트 수치 및 게이지 바 업데이트
        dogPercent.textContent = `${dogRounded}%`;
        catPercent.textContent = `${catRounded}%`;

        loadingSpinner.style.display = 'none';
        resultArea.style.display = 'block';

        // 프로그레스 바 애니메이션 적용
        setTimeout(() => {
            dogBar.style.width = `${dogRounded}%`;
            catBar.style.width = `${catRounded}%`;
        }, 100);

    } catch (error) {
        console.error("예측 오류:", error);
        alert("사진 분석 중 오류가 발생했습니다. 다른 사진으로 시도해 주세요.");
        resetUpload();
    }
}

// 다시하기 기능
function resetUpload() {
    imageInput.value = '';
    faceImage.src = '';
    dogBar.style.width = '0%';
    catBar.style.width = '0%';
    previewArea.style.display = 'none';
    resultArea.style.display = 'none';
    loadingSpinner.style.display = 'none';
    uploadArea.style.display = 'block';
}

if (retryBtn) {
    retryBtn.addEventListener('click', resetUpload);
}

// 공유하기 기능
if (shareBtn) {
    shareBtn.addEventListener('click', async () => {
        const shareData = {
            title: 'AI 동물상 테스트',
            text: '내가 강아지상일까, 고양이상일까? 인공지능으로 나의 동물상을 확인해보세요!',
            url: window.location.href
        };

        if (navigator.share) {
            try {
                await navigator.share(shareData);
            } catch (err) {
                // 사용자가 취소한 경우는 무시
            }
        } else {
            // 클립보드 복사 폴백
            try {
                await navigator.clipboard.writeText(window.location.href);
                showToast('링크가 클립보드에 복사되었습니다! 🎉');
            } catch (err) {
                showToast('링크 복사에 실패했습니다.');
            }
        }
    });
}

function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 2500);
}

// 테마 관리 (다크모드 / 라이트모드)
const themeToggleBtn = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const themeText = document.getElementById('theme-text');

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    
    if (theme === 'dark') {
        themeIcon.textContent = '☀️';
        themeText.textContent = '라이트모드';
    } else {
        themeIcon.textContent = '🌙';
        themeText.textContent = '다크모드';
    }

    if (typeof DISQUS !== 'undefined') {
        DISQUS.reset({ reload: true });
    }
}

// 초기 테마 설정 (로컬 스토리지 또는 OS 기본 테마)
const savedTheme = localStorage.getItem('theme');
const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
const initialTheme = savedTheme || (systemPrefersDark ? 'dark' : 'light');
applyTheme(initialTheme);

// 테마 토글 이벤트
if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    });
}

// 페이지 로드 시 AI 모델 미리 로드 (선택적 최적화)
window.addEventListener('DOMContentLoaded', () => {
    loadModel();
});

// 제휴 및 문의 폼 (Formspree AJAX 전송)
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
                formStatus.textContent = '✅ 문의가 성공적으로 접수되었습니다! 곧 답변드리겠습니다.';
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


