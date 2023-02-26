var fullJson = ""
async function getText() {
    fullJson = await get()
    document.getElementById("context").innerText=fullJson['context'];

    const olDefs = document.getElementById("defs");
    for(let i = 0; i < fullJson["definitions"].length; i++) {
        const liDef = document.createElement('li');
        liDef.innerHTML = fullJson["definitions"][i]["def"];

        olDefs.appendChild(liDef);
      }
}


async function setWord() {
    word = await document.getElementById("inputword").value;

    const formHandle = document.getElementById("formWord");
    formHandle.setAttribute("action", "./annotation.html?word=" + word)
}

