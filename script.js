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
