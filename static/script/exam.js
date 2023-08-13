const inputField = document.getElementById("input-word");
const displayWord = document.getElementById("word");
let count = 0;

class currentWord {
    static async fetchData(path) {
        const response = await fetch(path);
        const text = await response.text();
        const data = JSON.parse(text);
    
        return data;
    }

    static async loadData() {
        const destinationWord = await currentWord.getDestination();
        displayWord.innerHTML = destinationWord[0];
    }

    static async getDeparture() {
        this.vocaData = await this.fetchData(pathData);
        this.departureWord = Object.keys(this.vocaData);

        return this.departureWord;
    }

    static async getDestination() {
        this.vocaData = await this.fetchData(pathData);
        this.destinationWord = Object.values(this.vocaData);

        return this.destinationWord;
    } 
}

class cssAnimation {
    static startShakeAnimation() {
        inputField.classList.add("shake");
        inputField.addEventListener("animationend", () => this.resetShakeAnimation(inputField), { once: true });
    }
      
    static resetShakeAnimation(inputField) {
        inputField.classList.remove("shake");
    }

    static changeBorderColor(temporaryColor, duration) {
        const originalBorderColor = "#2D2F3E";
        inputField.style.borderColor = temporaryColor;
      
        setTimeout(() => {
          inputField.style.borderColor = originalBorderColor;
        }, duration);
    }
}

async function isCorrectWord() {
    const departureWord = await currentWord.getDeparture();
    const destinationWord = await currentWord.getDestination();

    if (inputField.value === departureWord[count]) {
        cssAnimation.changeBorderColor("#28886D", 1000);
        count++;
        inputField.value = "";

        if (departureWord[count] === undefined) {
            displayWord.innerHTML = "모든 단어를 학습했습니다!";
        } else {
            displayWord.innerHTML = `${destinationWord[count]}`;
        }
    } else {
        cssAnimation.startShakeAnimation();
        cssAnimation.changeBorderColor("#E01A4F", 1000);
    }
}

async function help() {
    const departureWord = await currentWord.getDeparture();

    if (!(departureWord[count] === undefined)) {
        inputField.value = departureWord[count];
    } 
}

function receiveInput() {
    if (event.key === 'Enter') {
        isCorrectWord();
    }
}

currentWord.loadData();
inputField.addEventListener("keydown", receiveInput);
