// 단어 목록이 담긴 파일 불러오기
async function fetchData() {
    const response = await fetch("voca.json");
    const data = await response.json();
    return data;
  }
  
// 단어 업데이트 함수
async function loadData(count) {
    const vocaData = await fetchData();
  
    const eng = Object.keys(vocaData);
    const kor = Object.values(vocaData);
  
    let originalText = eng[count];
    //let newText = kor[count];
  
    // 업데이트만 진행
    document.getElementById("word").innerHTML = originalText;
  }
  
const wordElement = document.getElementById("word");
wordElement.addEventListener("click", async function () { // async 키워드 추가
    const currentEng = Object.keys(await fetchData())[count]; // await 키워드 추가
    const currentKor = Object.values(await fetchData())[count]; // await 키워드 추가
    if (this.innerHTML === currentEng) {
      this.innerHTML = currentKor;
    } else {
      this.innerHTML = currentEng;
    }
  });
  
const nextButton = document.getElementById("next");
const previousButton = document.getElementById("previous");

// 버튼 활성 & 비활성화 함수
async function updateButtonVisibility() {
    const vocaData = await fetchData();
    const totalVocaCount = Object.keys(vocaData).length;
  
    if (count <= 0) {
      previousButton.style.visibility = 'hidden';
    } else {
      previousButton.style.visibility = 'visible';
    }
  
    if (count >= totalVocaCount - 1) {
      nextButton.style.visibility = 'hidden';
    } else {
      nextButton.style.visibility = 'visible';
    }
  }
  
let count = 0;
  
nextButton.addEventListener("click", async () => {
    const vocaData = await fetchData();
    const totalVocaCount = Object.keys(vocaData).length;
    if (count < totalVocaCount - 1) { // count가 엘리먼트 수보다 작을 때만 작동하도록 수정
      count++;
      loadData(count);
      await updateButtonVisibility();
    }
  });
  
previousButton.addEventListener("click", () => {
    if (count > 0) { // count가 양수일 때만 작동하도록 수정
        count--;
        loadData(count);
        updateButtonVisibility();
      }
  });

loadData(0);
updateButtonVisibility();