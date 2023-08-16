  // 단어 목록이 담긴 파일 불러오기
  async function fetchData(path) {
    const response = await fetch(path);
    const text = await response.text();
    const data = JSON.parse(text);
    return data;
  }
  
  // 단어 업데이트 함수
  async function loadData(newCount, path) {
    const vocaData = await fetchData(path);
  
    const eng = Object.keys(vocaData);
    const kor = Object.values(vocaData);
    const progress = document.getElementById("progress");

    // Wrap around the index if it goes out of bounds
    newCount = ((newCount % eng.length) + eng.length) % eng.length;
    count = newCount;
  
    let originalText = eng[count];
    //let newText = kor[count];
  
    // 업데이트만 진행
    progress.innerHTML = `${count + 1} / ${eng.length}`
    document.getElementById("word").innerHTML = originalText;
  }
  
  const wordElement = document.getElementById("word");
  wordElement.addEventListener("click", async function () {
    const currentEng = Object.keys(await fetchData(pathData))[count];
    const currentKor = Object.values(await fetchData(pathData))[count];
    if (this.innerHTML === currentEng) {
      this.innerHTML = currentKor;
    } else {
      this.innerHTML = currentEng;
    }
  });
  
  const nextButton = document.getElementById("next");
  const previousButton = document.getElementById("previous");
  
  let count = 0;
  
  nextButton.addEventListener("click", () => {
    loadData(count + 1, pathData);
  });
  
  previousButton.addEventListener("click", () => {
    loadData(count - 1, pathData);
  });
  
  loadData(0, pathData);