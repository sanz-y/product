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
themeToggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
});

// 로또 번호 추첨 로직
document.getElementById('draw-btn').addEventListener('click', () => {
    const container = document.getElementById('lotto-container');
    const numbers = generateLottoNumbers();
    
    // 기존 공 제거
    container.innerHTML = '';
    
    // 새로운 공 생성
    numbers.forEach((num, index) => {
        setTimeout(() => {
            const ball = document.createElement('div');
            ball.classList.add('ball');
            ball.classList.add(getBallColorClass(num));
            ball.textContent = num;
            container.appendChild(ball);
        }, index * 100); // 0.1초 간격으로 순차 등장
    });
});

function generateLottoNumbers() {
    const numbers = [];
    while (numbers.length < 6) {
        const rand = Math.floor(Math.random() * 45) + 1;
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


